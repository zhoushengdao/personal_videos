"""模版与实用工具类"""

from json import dumps
from os import environ
from pathlib import Path
from dataclasses import dataclass
from zlib import crc32
from time import sleep
from hashlib import blake2b

from manim import (
    Scene,
    ImageMobject,
    Unwrite,
    ManimBanner,
    Animation,
    Annulus,
    config,
    FadeIn,
    PI,
    Arc,
    TAU,
    Create,
    ORIGIN,
)
from edge_tts import Communicate
from mutagen.mp3 import MP3, HeaderNotFoundError


@dataclass
class MaterialDesign:
    """Material 3 设计"""

    PRIMARY = "#E2B7F4"
    ON_PRIMARY = "#000000"
    PRIMARY_CONTAINER = "#5B396D"
    ON_PRIMARY_CONTAINER = "#F6D9FF"

    SECONDARY = "#D3C0D8"
    ON_SECONDARY = "#000000"
    SECONDARY_CONTAINER = "#504255"
    ON_SECONDARY_CONTAINER = "#F0DCF4"

    TERTIARY = "#F5B7B7"
    ON_TERTIARY = "#000000"
    TERTIARY_CONTAINER = "#663B3B"
    ON_TERTIARY_CONTAINER = "#FFDAD9"

    SURFACE = "#161217"
    ON_SURFACE = "#FFFFFF"
    SURFACE_VARIANT = "#4B444D"
    ON_SURFACE_VARIANT = "#FFFFFF"

    OUTLINE = "#F8EDF7"
    OUTLINE_VARIANT = "#CABFCA"

    ERROR = "#FFECE9"
    ON_ERROR = "#000000"
    ERROR_CONTAINER = "#FFAEA4"
    ON_ERROR_CONTAINER = "#220001"

    SURFACE_DIM = "#161217"
    SURFACE_BRIGHT = "#544E54"
    SURFACE_CONTAINER_LOWEST = "#000000"
    SURFACE_CONTAINER_LOW = "#221E24"
    SURFACE_CONTAINER = "#342F35"
    SURFACE_CONTAINER_HIGH = "#3F3A40"
    SURFACE_CONTAINER_HIGHEST = "#4A454B"

    INVERSE_SURFACE = "#E9E0E7"
    INVERSE_ON_SURFACE = "#000000"
    INVERSE_PRIMARY = "#5C3A6E"

    SHADOW = "#000000"
    SCRIM = "#000000"


class Template:
    """模版类"""

    DEFAULT_FONT = "HarmonyOS Sans SC"
    DEFAULT_VOICE = "zh-CN-YunyangNeural"

    @staticmethod
    def cached_files_num(filename: str):
        """获取缓存文件数量"""
        if environ.get("GITHUB_ACTIONS") == "true":
            return -1

        match Path(filename).resolve().parent.name:
            case "ARIAAttr":
                return 257
            case _:
                return 100

    @staticmethod
    def splash_screen(scene: Scene):
        """显示 Android 风格的启动屏动画"""
        scene.next_section("开始动画")
        avatar = ImageMobject(
            Path(__file__).resolve().parent / "assets" / "avatar.jpg"
        ).move_to(ORIGIN)
        avatar.set_height(2)
        mask = Annulus(
            inner_radius=1, outer_radius=2, color=config.background_color
        ).move_to(ORIGIN)
        progressbar = Arc(
            radius=1,
            color=MaterialDesign.PRIMARY,
            start_angle=(PI / 2),
            angle=-TAU,
            stroke_width=6,
        ).move_to(ORIGIN)
        scene.add(avatar)
        scene.add(mask)
        scene.play(FadeIn(avatar))
        scene.play(Create(progressbar))
        scene.wait(1)
        scene.play(
            mask.animate.scale(4),
            avatar.animate.scale(4).fade(1),
            progressbar.animate.scale(4).fade(1),
        )
        scene.remove(avatar, progressbar, mask)
        scene.next_section("正文", skip_animations=False)

    @staticmethod
    def end_screen(scene: Scene, *animations: Animation):
        """显示 ManimBanner 结束动画"""
        scene.next_section("结束动画")
        banner = ManimBanner()
        scene.play(banner.create())
        scene.play(banner.expand())
        scene.wait(2)
        scene.play(Unwrite(banner), *animations)
        scene.wait(0.1)

    @staticmethod
    def add_tts(
        scene: Scene,
        text: str,
        voice: str = DEFAULT_VOICE,
        *,
        # * edge_tts\communicate.py
        rate: str = "+0%",
        volume: str = "+0%",
        pitch: str = "+0Hz",
    ) -> float:
        """为视频添加 TTS 音频，并返回音频时长"""

        scene.renderer.skip_animations = False  # 确保 Scene.add_sound() 方法不被跳过

        cache_dir = Path(__file__).resolve().parent / "media" / "audios"
        cache_dir.mkdir(parents=True, exist_ok=True)

        cache_key = blake2b(
            f"?={text}&={voice}&={rate}&={volume}&={pitch}".encode(), digest_size=16
        ).hexdigest()
        audio_path = cache_dir / f"{cache_key}.mp3"
        audio_path_str = str(audio_path)

        def use_this(use_cache: bool = False) -> float:
            """使用这个"""
            duration = MP3(audio_path_str).info.length

            print(
                f"TTS {'缓存' if use_cache else '生成'}："
                f"“{text[:10] + "……" + text[-10:] if len(text) > 20 else text}” "
                f"{audio_path} ({duration}s)"
            )

            if not use_cache:
                with (cache_dir / "audios.jsonl").open("a", encoding="utf-8") as f:
                    f.write(
                        dumps(
                            {
                                "filename": audio_path.name,
                                "duration": duration,
                                "text": text,
                                "voice": voice,
                                "rate": rate,
                                "volume": volume,
                                "pitch": pitch,
                            },
                            ensure_ascii=False,
                        )
                        + "\n"
                    )

            scene.add_sound(audio_path_str)

            return duration

        if audio_path.exists():
            try:
                if MP3(audio_path_str).info.length > 0:
                    return use_this(True)
                audio_path.unlink()
            except HeaderNotFoundError:
                audio_path.unlink()

        max_attempts = 3

        for attempt in range(1, max_attempts + 1):
            try:
                communicate = Communicate(
                    text=text,
                    voice=voice,
                    rate=rate,
                    volume=volume,
                    pitch=pitch,
                )
                communicate.save_sync(audio_path_str)

                return use_this()
            except Exception:  # pylint: disable=broad-exception-caught
                if attempt < max_attempts:
                    sleep(30 ** ((attempt * 0.1) + 1))
                else:
                    raise

        raise RuntimeError("无法生成音频文件")
