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
)

from data import ARIA_ATTRIBUTES_DATA

path.append(str(Path(__file__).resolve().parent.parent))

# pylint: disable=wrong-import-position
from template import DEFAULT_FONT, MaterialColors, splash_screen, end_screen

config.background_color = MaterialColors.SURFACE


class A11yAttrScene(Scene):
    """A11yAttr 场景"""

    def construct(self):
        Text.set_default(font=DEFAULT_FONT)

        splash_screen(self)

        # 标题动画
        title = Text(
            "WAI-ARIA 1.2 属性介绍",
            font_size=72,
            color=MaterialColors.PRIMARY,
        )
        subtitle = Text(
            "全部 48 个无障碍属性简介", font_size=36, color=MaterialColors.ON_SURFACE
        )

        # 动画序列
        self.play(Write(title))
        self.wait(0.5)
        self.play(
            title.animate.to_edge(UP, buff=0).set_font_size(48),
            FadeIn(subtitle, shift=UP),
        )
        self.wait(1)

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
                gradient=(MaterialColors.PRIMARY, MaterialColors.TERTIARY),
            ),
            Text(
                "为所有用户创造包容性数字环境",
                font_size=36,
                color=MaterialColors.ON_SURFACE,
            ),
            Text(
                "https://www.w3.org/TR/wai-aria/",
                font_size=24,
                color=MaterialColors.ON_SURFACE,
            ),
        )
        final_group.arrange(DOWN, buff=0.5)
        final_group.move_to(ORIGIN)
        self.play(FadeIn(final_group, shift=UP))
        self.wait(2)

        # 渐变退出
        self.play(FadeOut(final_group))

        end_screen(self, FadeOut(title))

    def create_attribute_cards(self) -> list[VGroup]:
        """创建属性卡片网格"""
        cards = []
        for attribute in ARIA_ATTRIBUTES_DATA:
            # 创建卡片
            card = RoundedRectangle(
                height=0.6,
                width=2.6,
                corner_radius=0.2,
                fill_color=MaterialColors.SECONDARY_CONTAINER,
                fill_opacity=0.8,
                stroke_color=MaterialColors.OUTLINE,
                stroke_width=1,
            )

            # 添加属性名称
            name = Text(
                attribute["name"],
                font_size=14,
                color=MaterialColors.ON_SECONDARY_CONTAINER,
                font="JetBrains Mono",
            )
            name.move_to(card.get_center())

            # 组合元素
            card_group = VGroup(card, name)
            cards.append(card_group)

        return cards

    def arrange_in_grid(self, cards, title):
        """将属性卡片网格排列成 10 行 5 列"""
        grid = VGroup(*cards).arrange_in_grid(rows=10, cols=5, buff=(0.1, 0.1))
        grid.next_to(title, DOWN, buff=0.2)
        return grid

    def explain_attribute(self, index, attribute_card):
        """逐个详细介绍属性"""
        # 创建描述内容
        description = Text(
            ARIA_ATTRIBUTES_DATA[index]["description"],
            font_size=30,
            line_spacing=0.5,
            color=MaterialColors.ON_SURFACE,
            t2c={"[在 ARIA 1.1 中弃用]": MaterialColors.ERROR_CONTAINER},
        )
        description.next_to(attribute_card, DOWN, buff=0.5, aligned_edge=LEFT)

        # 创建值类型信息
        value_type = Text(
            ARIA_ATTRIBUTES_DATA[index]["value"],
            font_size=30,
            line_spacing=(
                0.5 if ARIA_ATTRIBUTES_DATA[index]["name"] != "aria-dropeffect" else 0.3
            ),
            color=MaterialColors.ON_SURFACE,
        )
        value_type.next_to(description, DOWN, buff=0.5, aligned_edge=LEFT)

        # 动画展示
        self.play(Write(description))
        self.play(FadeIn(value_type, scale=0.9))
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
        print(ARIA_ATTRIBUTES_DATA[index]["name"], wait_time)
        self.wait(wait_time)

        # 清理场景
        self.play(
            FadeOut(description),
            FadeOut(value_type),
        )


if __name__ == "__main__":
    scene = A11yAttrScene()
    scene.render()
