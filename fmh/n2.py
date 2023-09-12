from manim import *


class movingframe(Scene):
    def construct(self):
        condition = MathTex("13n", "+", "m^2", " =", "11^{2023}", font_size=50)
        txttcondition = Tex("Solv equations in integers",color=YELLOW_C).move_to(UP)
        self.play(Write(txttcondition))
        self.play(Write(condition))
        self.wait(11)

# manim n2.py -pql
# manim -p -ql n1.py movingframe
# manim -p -qh n1.py movingframe
