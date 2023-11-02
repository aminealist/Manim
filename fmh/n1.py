from manim import *


class movingframe(Scene):
    def construct(self):
        # База индукции

        condition1 = MathTex("\\frac{1}{(n+3)(n+4)}", "+", "\\frac{1}{((n+1)+3) ((n+1)+4)}",
                             "+", "...", "+",
                             "\\frac{1}{(2n+3)(2n+4)}", "=", "\\frac{n+1}{2(n+2)(n+3)}", font_size=33)

        tracing = SurroundingRectangle(condition1, stroke_width=0.8, stroke_color=WHITE)
        Proof = Text("Prove that", font_size=27).next_to(tracing, UP)

        Base_case = Text("Base case", font_size=22, color=YELLOW)
        Base_case_n = MathTex("n = 1", ":", font_size=31, color=YELLOW).next_to(Base_case)
        Base_case = VGroup(Base_case, Base_case_n).center()

        condition_n1 = []

        condition_n1.append(MathTex("\\frac{1}{(n+3)(n+4)}", "+", "\\frac{1}{(2n+3)(2n+4)}",
                                    "=", "\\frac{n+1}{2(n+2)(n+3)}",
                                    font_size=33))
        condition_n1.append(MathTex("\\frac{1}{(1+3)(1+4)}", "+", "\\frac{1}{(2+3)(2+4)}",
                                    "=", "\\frac{1+1}{2(1+2)(1+3)}",
                                    font_size=33))
        condition_n1.append(MathTex("\\frac{1}{4*5}", "+", "\\frac{1}{5*6}",
                                    "=", "\\frac{2}{2*3*4}", font_size=33))

        condition_n1.append(MathTex("\\frac{1}{20}", "+", "\\frac{1}{30}",
                                    "=", "\\frac{1}{12}", font_size=33))

        condition_n1.append(MathTex("\\frac{1}{12}",
                                    "=", "\\frac{1}{12}", font_size=33))

        self.play(FadeIn(Proof))
        self.play(Write(condition1), run_time=4.5)
        self.play(Create(tracing), run_time=2)
        condition = VGroup(condition1, tracing)

        self.play(condition.copy().animate.scale(0.6).move_to(UP * 2.6), FadeOut(Proof), FadeOut(tracing))
        Base_case.next_to(condition, UP)
        self.play(Write(Base_case), run_time=1)

        self.play(ReplacementTransform(condition1, condition_n1[0]))
        for i in range(4):
            self.play(ReplacementTransform(condition_n1[i], condition_n1[i + 1]))
            self.wait(0.3)

        Induction_hypothesis1 = Text("Induction hypothesis:",
                                     color=YELLOW, font_size=23).move_to(1.2 * UP)
        Induction_hypothesis2 = Text("Assume that denote the statement is true for some",
                                     font_size=23).next_to(Induction_hypothesis1, RIGHT * 0.35)
        Induction_hypothesis3 = MathTex("k", "\in", "\mathbb{N}",
                                        font_size=35).next_to(Induction_hypothesis2, RIGHT * 0.3)

        Induction_hypothesis = VGroup(Induction_hypothesis1, Induction_hypothesis2,
                                      Induction_hypothesis3).move_to(1.2 * UP)
        self.wait(1)
        self.play(FadeOut(condition_n1[4]), FadeOut(Base_case), Write(Induction_hypothesis), run_time=3)
        self.wait(1)

        # предположение индукции
        Let = [MathTex("\\frac{1}{(k+3)(k+4)}+", " \\frac{1}{((k+1)+3) ((k+1)+4)} + ... + \\frac{1}{(2k+3)(2k+4)}", "=",
                       "\\frac{k+1}{2(k+2)(k+3)}", font_size=25).move_to(RIGHT * 0.5)]

        Let.append(Tex("Let S =", color=RED_A, font_size=32).next_to(Let[0], 0.7 * LEFT))
        Let.append(VGroup(Let[0], Let[1]))
        Induction_step = [Tex("Induction step n = k+1:", font_size=29).move_to(1.1 * UP)]
        self.play(Write(Let[0]))
        self.wait(1)
        self.play(Write(Let[1]))
        self.wait(1)
        self.play(Let[2].animate.scale(0.9).move_to(1.8 * UP),
                  Induction_hypothesis.animate.scale(0.7).move_to(DOWN),
                  ReplacementTransform(Induction_hypothesis, Induction_step[0]))
        self.wait(1)
        n_k1 = [MathTex("\\frac{1}{(k+4)(k+5)}", "+",
                        "\\frac{1}{((k+2)+3) ((k+2)+4)}", "+", "...", "+",
                        "\\frac{1}{(2k+3)(2k+4)}", "+", "\\frac{1}{(2k+4)(2k+5)}",
                        "+ \\frac{1}{(2k+2+3)(2k+2+4)}",
                        "=", "\\frac{k+2}{2(k+3)(k+4)}",
                        font_size=21)]

        n_k1.append(MathTex("\\frac{1}{(k+4)(k+5)} + \\frac{1}{(k+5) ((k+6)} + ... +"
                            " \\frac{1}{(2k+3)(2k+4)}",
                            "+ \\frac{1}{(2k+4)(2k+5)} + \\frac{1}{(2k+5)(2k+6)} = \\frac{k+2}{2(k+3)(k+4)}",
                            font_size=25))

        framebox = [SurroundingRectangle(n_k1[1][0], buff=.1)]
        framebox.append(SurroundingRectangle(Let[0][1], buff=.1))
        framebox.append(SurroundingRectangle(Let[0][3], buff=.1))

        self.play(ReplacementTransform(Let[0].copy(), n_k1[0]))

        self.wait(1)

        for i in range(1):
            self.play(ReplacementTransform(n_k1[i], n_k1[i + 1]))
            self.wait(0.5)

        self.play(Create(framebox[0]), Create(framebox[1]))

        self.wait(1)

        S = MathTex("S",
                    "-\\frac{1}{(k+3)(k+4)}+ \\frac{1}{(2k+4)(2k+5)} + \\frac{1}{(2k+5)(2k+6)} ="
                    " \\frac{k+2}{2(k+3)(k+4)}",
                    font_size=27)

        S1 = MathTex("\\frac{k+1}{2(k+2)(k+3)}",
                     "-\\frac{1}{(k+3)(k+4)}+ \\frac{1}{2(k+2)(2k+5)} + \\frac{1}{2(2k+5)(k+3)} ="
                     " \\frac{k+2}{2(k+3)(k+4)}",
                     font_size=27)

        self.play(FadeOut(framebox[0]), FadeOut(framebox[1]),
                  ReplacementTransform(n_k1[1], S))

        self.wait(0.5)

        self.play(Create(framebox[2]))

        self.wait(1)

        self.play(ReplacementTransform(S, S1))

        self.play(FadeOut(framebox[2]))
        self.wait(1)

        sm_snol_steps = Text("A few simple steps and ...", font_size=22).next_to(Induction_hypothesis,
                                                                                 0.9 * DOWN)
        end = [MathTex("\\frac{(k+1)(k+4)(2k+5)}{2(k+2)(k+3)(k+4)(2k+5)}",
                       "-\\frac{2(k+2)(2k+5)}{2(k+2)(k+3)(k+4)(2k+5)} + "
                       "\\frac{(k+3)(k+4)}{2(k+2)(k+3)(k+4)(2k+5)} + "
                       "\\frac{(k+4)(k+2)}{2(2k+5)(k+4)(k+3)(k+2)} = "
                       "\\frac{k+2}{2(k+3)(k+4)}",
                       font_size=19)]
        self.play(ReplacementTransform(S1, end[0]), Write(sm_snol_steps))

        self.wait(0.7)

        end.append(MathTex("\\frac{2k^3+15k^2+33k+20}{2(k+2)(k+3)(k+4)(2k+5)}",
                           "-\\frac{4k^2+18k+20}{2(k+2)(k+3)(k+4)(2k+5)} + "
                           "\\frac{k^2+7k+12}{2(k+2)...(2k+5)} + "
                           "\\frac{k^2+6k+8}{2(k+2)...(2k+5)} = "
                           "\\frac{k+2}{2(k+3)(k+4)}",
                           font_size=20))

        self.play(ReplacementTransform(end[0], end[1]))

        self.wait(0.7)

        end.append(MathTex("\\frac{2k^3+13k^2+28k+20}{2(k+2)(k+3)(k+4)(2k+5)} = "
                           "\\frac{k+2}{2(k+3)(k+4)}",
                           font_size=20))

        self.play(ReplacementTransform(end[1], end[2]))

        self.wait(0.7)

        end.append(MathTex("\\frac{(k+2)^2(2k+5)}{2(k+2)(k+3)(k+4)(2k+5)} = "
                           "\\frac{k+2}{2(k+3)(k+4)}",
                           font_size=20))

        self.play(ReplacementTransform(end[2], end[3]))

        self.wait(0.7)

        end.append(MathTex("\\frac{(k+2)}{2(k+3)(k+4)} = "
                           "\\frac{k+2}{2(k+3)(k+4)}",
                           font_size=20))

        self.play(ReplacementTransform(end[3], end[4]), run_time=0.7)

        self.play(end[4].animate.scale(1.9).move_to(DOWN))

        self.wait(1.5)

        self.clear()
        end1 = VGroup((MathTex("\\frac{1}{(n+3)(n+4)}", "+",
                               "\\frac{1}{((n+1)+3) ((n+1)+4)}", "+", "...", "+",
                               "\\frac{1}{(2n+3)(2n+4)}", "=", "\\frac{n+1}{2(n+2)(n+3)}",
                               font_size=33)), (Tex("TRUE").move_to(DOWN)))
        self.play(Write(end1))

        self.wait(1)
        self.play(FadeOut(end1))
        self.wait(2)

# manim n1.py -pql
# manim -p -ql n1.py movingframe
# manim -p -qh n1.py movingframe
