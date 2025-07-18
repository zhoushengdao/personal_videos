"""模版信息"""

from pathlib import Path
from dataclasses import dataclass

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

DEFAULT_FONT = "HarmonyOS Sans SC"


@dataclass
class MaterialColors:
    """Material 3 调色板"""

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


def splash_screen(scene: Scene):
    """显示 Android 风格的启动屏动画"""
    avatar = ImageMobject(
        Path(__file__).resolve().parent / "assets" / "avatar.jpg"
    ).move_to(ORIGIN)
    avatar.set_height(2)
    mask = Annulus(
        inner_radius=1, outer_radius=2, color=config.background_color
    ).move_to(ORIGIN)
    progressbar = Arc(
        radius=1,
        color=MaterialColors.PRIMARY,
        start_angle=(PI / 2),
        angle=-TAU,
        stroke_width=6,
    ).move_to(ORIGIN)
    scene.add(avatar)
    scene.add(mask)
    scene.play(FadeIn(avatar), run_time=1)
    scene.play(Create(progressbar, run_time=1))
    scene.wait(1)
    scene.play(
        mask.animate.scale(4),
        avatar.animate.scale(4).fade(1),
        progressbar.animate.scale(4).fade(1),
        run_time=1,
    )
    scene.remove(avatar, progressbar, mask)


def end_screen(scene: Scene, *animations: Animation):
    """显示 ManimBanner 结束动画"""
    banner = ManimBanner()
    scene.play(banner.create())
    scene.play(banner.expand())
    scene.wait(2)
    scene.play(Unwrite(banner), *animations)
