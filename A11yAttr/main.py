"""A11yAttr 视频"""

from sys import path
from pathlib import Path

from manim import (
    Scene,
    Text,
    config,
    VGroup,
    FadeIn,
    FadeOut,
    Write,
    UP,
    LEFT,
    DOWN,
    ORIGIN,
    LaggedStart,
    RoundedRectangle,
    Wait,
    AnimationGroup,
)

from data import ARIA_ATTRIBUTES_DATA

path.append(str(Path(__file__).resolve().parent.parent))

# pylint: disable=wrong-import-position
from template import MaterialDesign, Template

config.background_color = MaterialDesign.SURFACE
config.max_files_cached = Template.cached_files_num(__file__)


# edge-tts --voice zh-CN-YunyangNeural --text "W A I - A R I A 1.2 属性介绍" --write-media title.mp3
# edge-tts --voice zh-CN-YunyangNeural --text "全部 48 个无障碍属性简介" --write-media subtitle.mp3


class A11yAttrScene(Scene):
    """A11yAttr 场景"""

    def construct(self):
        Text.set_default(font=Template.DEFAULT_FONT)

        Template.splash_screen(self)

        # 标题动画
        title = Text(
            "WAI-ARIA 1.2 属性介绍",
            font_size=72,
            color=MaterialDesign.PRIMARY,
        )
        subtitle = Text(
            "全部 48 个无障碍属性简介", font_size=36, color=MaterialDesign.ON_SURFACE
        )

        # 动画序列
        self.play(
            LaggedStart(Write(title), Wait(1), lag_ratio=1),
            subcaption="WAI-ARIA 1.2 属性介绍",
        )
        self.play(
            LaggedStart(
                AnimationGroup(
                    title.animate.to_edge(UP, buff=0).set_font_size(48),
                    FadeIn(subtitle, shift=UP),
                ),
                Wait(1),
                lag_ratio=1,
            ),
            subcaption="全部 48 个无障碍属性简介",
        )

        # 创建属性卡片网格
        cards = self.create_attribute_cards()
        grid = self.arrange_in_grid(cards, title)

        # 展示所有属性
        self.play(FadeOut(subtitle))
        self.play(
            LaggedStart(
                *[FadeIn(card, scale=0.8) for card in cards],
                lag_ratio=0.1,
            ),
        )
        self.wait(1)

        # 逐个详细介绍属性
        for i, card in enumerate(cards):
            # 保存原始位置
            origin_center = card.get_center()

            # 高亮当前卡片
            self.play(
                card.animate.scale(1.5).next_to(
                    title, DOWN + LEFT, buff=1, aligned_edge=LEFT
                ),
                *[c.animate.set_opacity(0) for c in cards if c != card],
                subcaption=f"第 {i + 1} 个 {ARIA_ATTRIBUTES_DATA[i]["name"]}",
            )

            # 解释属性
            self.explain_attribute(i, card)

            # 恢复原始状态
            self.play(
                card.animate.scale(1 / 1.5).move_to(origin_center),
                *[c.animate.set_opacity(1) for c in cards if c != card],
            )

        # 结束动画
        self.play(FadeOut(grid))
        final_group = VGroup(
            Text(
                "提升 Web 无障碍体验",
                font_size=72,
                gradient=(MaterialDesign.PRIMARY, MaterialDesign.TERTIARY),
            ),
            Text(
                "为所有用户创造包容性的数字环境",
                font_size=36,
                color=MaterialDesign.ON_SURFACE,
            ),
            Text(
                "https://www.w3.org/TR/wai-aria/",
                font_size=24,
                color=MaterialDesign.ON_SURFACE,
            ),
        )
        final_group.arrange(DOWN, buff=0.5)
        final_group.move_to(ORIGIN)
        self.play(
            LaggedStart(
                FadeIn(final_group, shift=UP),
                Wait(2),
                lag_ratio=1,
            ),
            subcaption="让我们一起提升 Web 无障碍体验，为所有用户创造包容性的数字环境",
            subcaption_offset=0.5,  # type: ignore
        )
        self.play(FadeOut(final_group))

        Template.end_screen(self, FadeOut(title))

    def create_attribute_cards(self) -> list[VGroup]:
        """创建属性卡片网格"""
        cards = []
        for attribute in ARIA_ATTRIBUTES_DATA:
            # 创建卡片
            card = RoundedRectangle(
                height=0.6,
                width=2.6,
                corner_radius=0.2,
                fill_color=MaterialDesign.SECONDARY_CONTAINER,
                fill_opacity=0.8,
                stroke_color=MaterialDesign.OUTLINE_VARIANT,
                stroke_width=1,
            )

            # 添加属性名称
            name = Text(
                attribute["name"],
                font_size=14,
                color=MaterialDesign.ON_SECONDARY_CONTAINER,
                font="JetBrains Mono",
            )
            name.move_to(card.get_center())

            # 组合元素
            card_group = VGroup(card, name)
            cards.append(card_group)

        return cards

    def arrange_in_grid(self, cards: list[VGroup], title: Text):
        """将属性卡片网格排列成 10 行 5 列"""
        grid = VGroup(*cards).arrange_in_grid(rows=10, cols=5, buff=(0.1, 0.1))
        grid.next_to(title, DOWN, buff=0.2)
        return grid

    def explain_attribute(self, index: int, attribute_card: VGroup):
        """逐个详细介绍属性"""
        # 创建描述内容
        description = Text(
            ARIA_ATTRIBUTES_DATA[index]["description"],
            font_size=30,
            line_spacing=0.5,
            color=MaterialDesign.ON_SURFACE,
            t2c={"[在 ARIA 1.1 中弃用]": MaterialDesign.ERROR_CONTAINER},
        )
        description.next_to(attribute_card, DOWN, buff=0.5, aligned_edge=LEFT)

        # 创建值类型信息
        value_type = Text(
            ARIA_ATTRIBUTES_DATA[index]["value"],
            font_size=30,
            line_spacing=(
                0.5 if ARIA_ATTRIBUTES_DATA[index]["name"] != "aria-dropeffect" else 0.3
            ),
            color=MaterialDesign.ON_SURFACE,
        )
        value_type.next_to(description, DOWN, buff=0.5, aligned_edge=LEFT)

        # 动画展示
        wait_time = max(
            (
                len(
                    ARIA_ATTRIBUTES_DATA[index]["description"]
                    + ARIA_ATTRIBUTES_DATA[index]["value"]
                )
                * 0.02
            ),
            1,
        )
        self.play(
            LaggedStart(
                Write(description),
                FadeIn(value_type, scale=0.8),
                Wait(wait_time),
                lag_ratio=1,
            ),
            subcaption=self.get_description_subcaption(index),
        )

        # 清理场景
        self.play(
            FadeOut(description),
            FadeOut(value_type),
        )

    @staticmethod
    def get_description_subcaption(index: int):
        """获取属性描述的字幕"""
        description = ARIA_ATTRIBUTES_DATA[index]["description"]
        subcaption = f"它用于{description.replace("\n", "")}"
        if "[在 ARIA 1.1 中弃用]" in description:
            subcaption = (
                subcaption.replace("[在 ARIA 1.1 中弃用] ", "")
                + "它已在 ARIA 1.1 中弃用。"
            )
        return subcaption


if __name__ == "__main__":
    scene = A11yAttrScene()
    scene.render()
