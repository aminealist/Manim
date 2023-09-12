from manim import *


class syst(Scene):
    def construct(self):
        brace = BraceBetweenPoints([-0.5, 0.5, 0], [-0.5, -2.5, 0])
        text1 = MathTex(r"\frac{xy}{x+y}", "=", "1", font_size=33)
        text2 = MathTex(r"\frac{yz}{y+z}", "=", "2", font_size=33).next_to(text1, DOWN)
        text3 = MathTex(r"\frac{xz}{x+z}", "=", "3", font_size=33).next_to(text2, DOWN)
        self.play(FadeIn(brace), Write(text1), Write(text2), Write(text3),run_time=2)
        self.wait(2)

# manim -p -ql system.py syst
