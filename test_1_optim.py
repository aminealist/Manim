from manim import *


class movingframe(Scene):
    def construct(self):
        txt = []
        groups = []
        braces = []
        groupss = []
        fst = []

        fst.append(MathTex(r"\frac{xy}{x+y}", "=", "1", font_size=33))
        fst.append(MathTex(r"\frac{yz}{y+z}", "=", "2", font_size=33).next_to(fst[0], DOWN))
        fst.append(MathTex(r"\frac{xz}{x+z}", "=", "3", font_size=33).next_to(fst[1], DOWN))
        fst_g = VGroup(fst[0], fst[1], fst[2])
        fst_b = Brace(fst_g, 1.1 * LEFT)
        fst_g_b = VGroup(fst[0], fst[1], fst[2], fst_b)

        txt.append(MathTex(r"\frac{xy}{x+y}", "=", "1", font_size=33))
        txt.append(MathTex(r"\frac{yz}{y+z}", "=", "2", font_size=33).next_to(txt[0], DOWN))
        txt.append(MathTex(r"\frac{xz}{x+z}", "=", "3", font_size=33).next_to(txt[1], DOWN))

        # groups.append(VGroup(txt[0]))s

        txt.append(MathTex(r"\frac{0}{x+y}", "=", "1", font_size=33))
        txt.append(MathTex(r"\frac{0}{y+z}", "=", "2", font_size=33).next_to(txt[3], DOWN))
        txt.append(MathTex(r"\frac{0}{y+z}", "=", "3", font_size=33).next_to(txt[4], DOWN))

        txt.append(MathTex("0", "=", "1", font_size=33))
        txt.append(MathTex("0", "=", "2", font_size=33).next_to(txt[6], DOWN))
        txt.append(MathTex("0", "=", "3", font_size=33).next_to(txt[7], DOWN))

        txt.append(MathTex("0", "\\neq", "1", font_size=33))
        txt[9][1].set_color(RED)
        txt.append(MathTex("0", "\\neq", "2", font_size=33).next_to(txt[9], DOWN))
        txt[10][1].set_color(RED)
        txt.append(MathTex("0", "\\neq", "3", font_size=33).next_to(txt[10], DOWN))
        txt[11][1].set_color(RED)

        rightarrow_xyz0 = MathTex("\\Rightarrow", font_size=33).next_to(txt[10], 1.1 * RIGHT)
        xyz0 = MathTex("x, y, z \\neq 0", color=RED_A, font_size=30).next_to(rightarrow_xyz0, 0.9 * RIGHT)

        txt.append(MathTex(r"\frac{xy}{x+y}", "=", "1", font_size=33).next_to(fst_g_b, 0.2 * UP))
        txt.append(MathTex(r"\frac{yz}{y+z}", "=", "2", font_size=33).next_to(txt[12], DOWN))
        txt.append(MathTex(r"\frac{xz}{x+z}", "=", "3", font_size=33).next_to(txt[13], DOWN))

        txt.append(MathTex(r"\frac{x+y}{xy}", "=", "1", font_size=33).next_to(txt[12], 0))
        txt.append(MathTex(r"\frac{y+z}{yz}", "=", r"\frac{1}{2}", font_size=33).next_to(txt[15], DOWN))
        txt.append(MathTex(r"\frac{x+z}{xz}", "=", r"\frac{1}{3}", font_size=33).next_to(txt[16], DOWN))

        txt.append(MathTex(r"\frac{1}{y} + \frac{1}{x}", "=", "1", font_size=33).next_to(txt[15], 0))
        txt.append(MathTex(r"\frac{1}{z} + \frac{1}{y}", "=", r"\frac{1}{2}", font_size=33).next_to(txt[18], DOWN))
        txt.append(MathTex(r"\frac{1}{z} + \frac{1}{x}", "=", r"\frac{1}{3}", font_size=33).next_to(txt[19], DOWN))

        txt.append(MathTex(r"B + A", "=", "1", font_size=33).next_to(txt[18], 0))
        txt.append(MathTex(r"C + B", "=", r"\frac{1}{2}", font_size=33).next_to(txt[21], 1.7 * DOWN))
        txt.append(MathTex(r"C + A", "=", r"\frac{1}{3}", font_size=33).next_to(txt[22], DOWN))
        one = MathTex("(1)", font_size=30).next_to(txt[21], 2 * LEFT)
        two = MathTex("(2)", font_size=30).next_to(txt[22], 2 * LEFT)
        three = MathTex("(3)", font_size=30).next_to(txt[23], 2 * LEFT)
        ravnosil = MathTex(r"\Leftrightarrow", font_size=33).next_to(txt[22], 1.1 * RIGHT)

        two_three = MathTex("(2)-(3)", font_size=28).next_to(ravnosil, 0.3 * RIGHT)

        txt.append(MathTex(r"B - A", " =   \\frac{1}{2}", font_size=32).next_to(two_three, 2.5 * RIGHT))
        one_two = MathTex("(1)-(2)", font_size=28).next_to(two_three, 2 * UP)
        three_one = MathTex("(3)-(1)", font_size=28).next_to(two_three, 2 * DOWN)

        txt.append(MathTex(r"A - C", " =   \\frac{1}{6}", font_size=32).next_to(one_two, 2.5 * RIGHT))
        txt.append(MathTex(r"C - B", "=-\\frac{2}{3}", font_size=32).next_to(three_one, 2.5 * RIGHT))

        k = 0
        for i in range((len(txt) + 1) // 3):
            groups.append(VGroup(txt[k], txt[k + 1], txt[k + 2]))

            braces.append(Brace(groups[i], 0.8 * LEFT))
            groupss.append(VGroup(txt[k], txt[k + 1], txt[k + 2], braces[i]))
            k += 3

        if_ = Text("If", color=RED_A).next_to(braces[0], UP)
        if_.scale(0.37)
        if_xyz0 = MathTex("x, y, z", "=", "0:", font_size=30).next_to(if_, 0.3 * RIGHT)
        if_xyz0.set_color(RED_A)
        ABC = MathTex("A = \\frac{1}{x}; B = \\frac{1}{y}; C = \\frac{1}{z} :", font_size=25).next_to(groupss[5],
                                                                                                      1.4 * UP)

        self.play(FadeIn(fst_b), Write(fst[0]), Write(fst[1]), Write(fst[2]))
        self.wait(2)
        self.add(braces[0], txt[0], txt[1], txt[2])
        self.play(fst_g_b.animate.scale(0.7).next_to(txt[0], 3 * LEFT))
        self.play(Write(if_), Write(if_xyz0))
        self.wait(1)
        for i in range(3):
            self.play(ReplacementTransform(groupss[i], groupss[i + 1]))
            self.wait(0.5)
        self.wait(0.5)
        self.play(Write(rightarrow_xyz0))
        self.play(Write(xyz0))
        self.wait(1.5)
        self.play(xyz0.animate.scale(1).next_to(fst_g_b, UP), FadeOut(if_), FadeOut(rightarrow_xyz0),
                  FadeOut(if_xyz0), ReplacementTransform(fst_g_b, groupss[4]), FadeOut(groupss[3]))
        self.wait(1)
        self.play(TransformMatchingShapes(groupss[4], groupss[5]))
        self.wait(1)
        self.play(FadeOut(xyz0), Write(ABC), TransformMatchingShapes(groupss[5], groupss[6]))
        self.wait(1)
        self.play(TransformMatchingShapes(groupss[6], groupss[7]))
        self.wait(1)
        self.play(Write(one), Write(two), Write(three))
        self.wait(1)
        self.play(Write(ravnosil))
        self.play(Write(two_three), Write(one_two), Write(three_one))
        self.play(Write(txt[24]), Write(txt[25]), Write(txt[26]), FadeIn(braces[8]))
        self.wait(2)

# manim -p -ql test_1_optim.py movingframe
# manim -p -qh test_1_optim.py movingframe
