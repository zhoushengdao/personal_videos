# 我的个人视频

这是我的用于存放基于 Manim 的、具有统一视觉样式的视频项目的仓库。

## 视频项目列表

以下是当前包含的视频项目：

### 1. A11yAttr

对 WAI-ARIA 1.2 中全部 48 个属性的介绍。

## 功能特性

- 🛠️ **项目管理**：创建、组织和管理多个视频项目
- 🎥 **预览渲染**：快速预览动画效果
- 🎬 **高清渲染**：生成高质量的视频输出
- 📦 **依赖管理**：自动化安装和更新 Python 依赖
- 📁 **模板系统**：提供标准化的视频项目模板
- 🔄 **在线渲染**：支持 Github Actions 在线渲染

## 快速开始

### 克隆仓库

```bash
git clone https://gitcode.com/zhoushengdao/personal_videos.git
cd personal_videos
```

### 安装依赖

```bash
# 安装依赖
python main.py install

# 安装其他 pip 包
python main.py install package1 package2
```

### 创建新项目

```bash
python main.py new MyVideoProject
```

### 预览视频

```bash
python main.py pre MyVideoProject
```

### 渲染高质量视频

```bash
python main.py prod MyVideoProject
```

## 项目结构

```
personal_videos/
├── main.py              # 主管理脚本
├── requirements.in      # 依赖包列表
├── requirements.txt     # 编译后的依赖
├── template.py          # 视频模板库
├── assets/              # 全局资源目录
└── [项目目录]/           # 各视频项目
    └── main.py          # 项目主文件
```

## 现有全局资源

- avatar.jpg：个人头像
- fonts/：HarmonyOS Sans SC 和 JetBrains Mono 字体

## 许可证

本项目采用 [署名—非商业性使用—禁止演绎 4.0 协议国际版](LICENSE)。
