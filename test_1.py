from manim import *


class MovingFrame(Scene):
    def construct(self):
        text1 = MathTex(r"\frac{xy}{x+y}", "=", "1", font_size=33)
        text2 = MathTex(r"\frac{yz}{y+z}", "=", "2", font_size=33).next_to(text1, DOWN)
        text3 = MathTex(r"\frac{xz}{x+z}", "=", "3", font_size=33).next_to(text2, DOWN)
        xyz = MathTex(r"x, y, z", r"\neq", "0", font_size=35).next_to(text1, RIGHT)
        group1 = VGroup(text1, text2, text3)
        brace = Brace(group1, LEFT)

        text4 = MathTex(r"\frac{0*0}{x+y}", "=", "1", font_size=33)
        text5 = MathTex(r"\frac{0*0}{y+z}", "=", "2", font_size=33).next_to(text4, DOWN)
        text6 = MathTex(r"\frac{0*0}{x+z}", "=", "3", font_size=33).next_to(text5, DOWN)

        text7 = MathTex(r"\frac{0}{x+y}", "=", "1", font_size=33)
        text8 = MathTex(r"\frac{0}{y+z}", "=", "2", font_size=33).next_to(text7, DOWN)
        text9 = MathTex(r"\frac{0}{x+z}", "=", "3", font_size=33).next_to(text8, DOWN)

        text10 = MathTex(r"0", r"\neq", "1", font_size=33)
        text11 = MathTex(r"0", r"\neq", "2", font_size=33).next_to(text10, DOWN)
        text12 = MathTex(r"0", r"\neq", "3", font_size=33).next_to(text11, DOWN)

        text13 = MathTex(r"\frac{xy}{x+y}", "=", "1", font_size=33)
        text14 = MathTex(r"\frac{yz}{y+z}", "=", "2", font_size=33).next_to(text13, DOWN)
        text15 = MathTex(r"\frac{xz}{x+z}", "=", "3", font_size=33).next_to(text14, DOWN)

        text16 = MathTex(r"xy", "=", "x+y", font_size=33)
        text17 = MathTex(r"yz", "=", r"2(y+z)", font_size=33).next_to(text16, DOWN)
        text18 = MathTex(r"xz", "=", r"3(x+z)", font_size=33).next_to(text17, DOWN)

        text19 = MathTex(r"\frac{x+y}{xy}", "=", "1", font_size=33)
        text20 = MathTex(r"\frac{y+z}{yz}", "=", r"\frac{1}{3}", font_size=33).next_to(text19, DOWN)
        text21 = MathTex(r"\frac{x+z}{xz}", "=", r"\frac{1}{3}", font_size=33).next_to(text20, DOWN)

        self.play(Write(text1), Write(text2), Write(text3), FadeIn(brace), run_time=2)
        self.wait(0.5)
        self.play(Write(xyz))
        self.wait(0.5)
        self.play(Transform(text1, text4), Transform(text2, text5), Transform(text3, text6), run_time=1)
        self.wait(0.5)
        self.play(Transform(text4, text7), Transform(text5, text8), Transform(text6, text9),
                  FadeOut(text1, text2, text3), run_time=1)
        self.wait(0.5)
        self.play(Transform(text7, text10), Transform(text8, text11), Transform(text9, text12),
                  xyz.animate.set_fill(RED_B),
                  FadeOut(text4, text5, text6), run_time=1)
        self.wait(1)
        self.play(Transform(text10, text13), Transform(text11, text14), Transform(text12, text15),
                  FadeOut(text7, text8, text9), xyz.animate.scale(0.9).next_to(text7, UP),
                  run_time=1)
        self.wait(1)
        self.play(Transform(text13, text16), Transform(text14, text17), Transform(text15, text18),
                  FadeOut(text10, text11, text12), run_time=1.5)
        self.wait(1)
        self.play(Transform(text16, text19), Transform(text17, text20), Transform(text18, text21),
                  FadeOut(text13, text14, text15), run_time=1)
        self.wait(2)
# manim -p -ql test_1.py MovingFrame
