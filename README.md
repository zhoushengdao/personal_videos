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

## 可用的音色

| Name                           | Gender | ContentCategories     | VoicePersonalities                     |
| ------------------------------ | ------ | --------------------- | -------------------------------------- |
| en-GB-LibbyNeural              | Female | General               | Friendly, Positive                     |
| en-GB-MaisieNeural             | Female | General               | Friendly, Positive                     |
| en-GB-RyanNeural               | Male   | General               | Friendly, Positive                     |
| en-GB-SoniaNeural              | Female | General               | Friendly, Positive                     |
| en-GB-ThomasNeural             | Male   | General               | Friendly, Positive                     |
| en-US-AnaNeural                | Female | Cartoon, Conversation | Cute                                   |
| en-US-AndrewMultilingualNeural | Male   | Conversation, Copilot | Warm, Confident, Authentic, Honest     |
| en-US-AndrewNeural             | Male   | Conversation, Copilot | Warm, Confident, Authentic, Honest     |
| en-US-AriaNeural               | Female | News, Novel           | Positive, Confident                    |
| en-US-AvaMultilingualNeural    | Female | Conversation, Copilot | Expressive, Caring, Pleasant, Friendly |
| en-US-AvaNeural                | Female | Conversation, Copilot | Expressive, Caring, Pleasant, Friendly |
| en-US-BrianMultilingualNeural  | Male   | Conversation, Copilot | Approachable, Casual, Sincere          |
| en-US-BrianNeural              | Male   | Conversation, Copilot | Approachable, Casual, Sincere          |
| en-US-ChristopherNeural        | Male   | News, Novel           | Reliable, Authority                    |
| en-US-EmmaMultilingualNeural   | Female | Conversation, Copilot | Cheerful, Clear, Conversational        |
| en-US-EmmaNeural               | Female | Conversation, Copilot | Cheerful, Clear, Conversational        |
| en-US-EricNeural               | Male   | News, Novel           | Rational                               |
| en-US-GuyNeural                | Male   | News, Novel           | Passion                                |
| en-US-JennyNeural              | Female | General               | Friendly, Considerate, Comfort         |
| en-US-MichelleNeural           | Female | News, Novel           | Friendly, Pleasant                     |
| en-US-RogerNeural              | Male   | News, Novel           | Lively                                 |
| en-US-SteffanNeural            | Male   | News, Novel           | Rational                               |
| zh-CN-XiaoxiaoNeural           | Female | News, Novel           | Warm                                   |
| zh-CN-XiaoyiNeural             | Female | Cartoon, Novel        | Lively                                 |
| zh-CN-YunjianNeural            | Male   | Sports, Novel         | Passion                                |
| zh-CN-YunxiNeural              | Male   | Novel                 | Lively, Sunshine                       |
| zh-CN-YunxiaNeural             | Male   | Cartoon, Novel        | Cute                                   |
| zh-CN-YunyangNeural            | Male   | News                  | Professional, Reliable                 |
| zh-CN-liaoning-XiaobeiNeural   | Female | Dialect               | Humorous                               |
| zh-CN-shaanxi-XiaoniNeural     | Female | Dialect               | Bright                                 |
| zh-HK-HiuGaaiNeural            | Female | General               | Friendly, Positive                     |
| zh-HK-HiuMaanNeural            | Female | General               | Friendly, Positive                     |
| zh-HK-WanLungNeural            | Male   | General               | Friendly, Positive                     |
| zh-TW-HsiaoChenNeural          | Female | General               | Friendly, Positive                     |
| zh-TW-HsiaoYuNeural            | Female | General               | Friendly, Positive                     |
| zh-TW-YunJheNeural             | Male   | General               | Friendly, Positive                     |

## 许可证

本项目采用 [署名—非商业性使用—禁止演绎 4.0 协议国际版](LICENSE)。
