"""
用于管理视频项目的 CLI 脚本。
"""

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from subprocess import run
from sys import exit as sys_exit
from pathlib import Path
from datetime import datetime
from typing import Optional


def main():
    """解析命令行参数并执行相应操作。"""
    parser = ArgumentParser(
        description="个人视频管理工具",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    subparsers = parser.add_subparsers(
        title="子命令", dest="command", help="可用的子命令"
    )

    # 安装命令
    install_parser = subparsers.add_parser(
        "install",
        help="更新并安装 pip 依赖包",
    )
    install_parser.add_argument(
        "packages",
        nargs="*",
        help="需要新安装的 pip 包",
    )

    # 预览命令
    pre_parser = subparsers.add_parser(
        "pre",
        help="预览视频",
    )
    pre_parser.add_argument(
        "project",
        nargs="?",
        help="项目名称",
    )

    # 生产命令
    prod_parser = subparsers.add_parser(
        "prod",
        help="渲染高质量视频",
    )
    prod_parser.add_argument(
        "project",
        nargs="?",
        help="项目名称",
    )

    # 新建项目命令
    new_parser = subparsers.add_parser(
        "new",
        help="新建视频项目",
    )
    new_parser.add_argument(
        "project",
        help="项目名称",
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys_exit(1)

    try:
        if args.command == "install":
            handle_install(args.packages)
        elif args.command == "pre":
            handle_preview(args.project)
        elif args.command == "prod":
            handle_production(args.project)
        elif args.command == "new":
            handle_new_project(args.project)
    except ValueError as e:
        print(f"错误：{e}")
        sys_exit(1)


def handle_install(packages: list[str]):
    """
    执行更新并安装 pip 依赖包命令。

    Args:
        packages: 要新安装的 pip 包
    """
    req_in = Path("requirements.in")
    req_txt = Path("requirements.txt")

    # 确保 requirements.in 存在
    if not req_in.exists():
        req_in.touch()

    # 添加依赖包到 requirements.in
    if packages:
        print(f"添加依赖包到 {req_in}：")
        with req_in.open("a", encoding="utf-8") as f:
            for pkg in packages:
                print(f"  - {pkg}")
                f.write(f"{pkg}\n")

    # 编译依赖包
    print("编译依赖包……")
    run(["pip-compile", str(req_in)], check=True)

    # 安装依赖包
    print("安装依赖包……")
    run(["pip", "install", "-r", str(req_txt)], check=True)


def get_valid_projects():
    """获取所有有效项目列表（按 main.py 修改时间降序排序）"""
    projects: list[tuple[datetime, str]] = []
    for item in Path(".").iterdir():
        if item.is_dir():
            main_py = item / "main.py"
            if main_py.exists():
                # 获取 main.py 的修改时间
                mod_time = datetime.fromtimestamp(main_py.stat().st_mtime)
                projects.append((mod_time, item.name))

    # 按修改时间降序排序（最新的排在最前）
    projects.sort(key=lambda x: x[0], reverse=True)
    return [name for _, name in projects]


def select_project(show_list: bool = True) -> str:
    """
    让用户从有效项目列表中选择一个项目

    Args:
        show_list: 是否显示项目列表

    Returns:
        str: 用户选择的项目名称
    """
    projects = get_valid_projects()

    if not projects:
        raise ValueError("没有找到有效项目")

    if show_list:
        print("请选择一个项目：")
        for i, project in enumerate(projects, 1):
            print(f"{i}. {project}")

    try:
        choice = input("输入项目编号 [1]：")
        if not choice:
            return projects[0]
        choice = int(choice)
        if 1 <= choice <= len(projects):
            return projects[choice - 1]
        print("无效的选择，请重新选择")
        return select_project(show_list=False)
    except ValueError:
        print("无效的选择，请重新选择")
        return select_project(show_list=False)


def handle_preview(project_name: Optional[str] = None):
    """
    预览视频

    Args:
        project_name: 项目名称
    """
    if project_name is None:
        project_name = select_project()
    validate_project(project_name)
    print(f"预览 {project_name}……")
    run(["manim", "render", "-pql", f"{project_name}/main.py"], check=True)


def handle_production(project_name: Optional[str] = None):
    """
    渲染高质量视频

    Args:
        project_name: 项目名称
    """
    if project_name is None:
        project_name = select_project()
    validate_project(project_name)
    print(f"渲染 {project_name}……")
    run(["manim", "render", "-qk", f"{project_name}/main.py"], check=True)


MAIN_TEMPLATE = """\"\"\"<PROJECT_NAME> 视频\"\"\"

from sys import path
from pathlib import Path

from manim import Scene, Text, config

path.append(str(Path(__file__).resolve().parent.parent))

# pylint: disable=wrong-import-position
from template import MaterialDesign, Template

config.background_color = MaterialDesign.SURFACE
config.max_files_cached = Template.cached_files_num(__file__)


class <PROJECT_NAME>Scene(Scene):
    \"\"\"<PROJECT_NAME> 场景\"\"\"

    def construct(self):
        Text.set_default(font=Template.DEFAULT_FONT)

        Template.splash_screen(self)

        # 自定义内容

        Template.end_screen(self)


if __name__ == "__main__":
    scene = <PROJECT_NAME>Scene()
    scene.render()
"""


def handle_new_project(project_name: str):
    """
    新建一个视频项目

    Args:
        project_name: 项目名称
    """
    # 验证为 PascalCase 格式
    if not project_name[0].isupper() or " " in project_name or "_" in project_name:
        raise ValueError("项目名称必须为 PascalCase 格式（如：“MyVideo”）")

    project_dir = Path(project_name)
    if project_dir.exists():
        raise ValueError(f'项目 "{project_name}" 已存在')

    # 创建项目文件夹
    project_dir.mkdir()
    main_py = project_dir / "main.py"

    # 写入 main.py 文件
    with main_py.open("w", encoding="utf-8") as f:
        f.write(MAIN_TEMPLATE.replace("<PROJECT_NAME>", project_name))

    print(f'项目 "{project_name}" 已创建')


def validate_project(project_name: str):
    """
    确认项目文件夹存在且包含 main.py 文件。

    Args:
        project_name: 要验证的项目文件夹名称

    Raises:
        ValueError: 如果文件夹不存在或没有 main.py 文件时
    """
    project_path = Path(project_name)
    if not project_path.is_dir():
        raise ValueError(f'项目 "{project_name}" 不存在')

    main_py = project_path / "main.py"
    if not main_py.is_file():
        raise ValueError(f'项目 "{project_name}" 中没有 main.py 文件')


if __name__ == "__main__":
    main()
