from manim import *
from numpy import array as nparray
from math import sqrt


class movingframe(Scene):
    def construct(self):
        # Создание треугольника
        A, B, C = nparray([0, 0, 0]), nparray([1, 2, 0]), nparray([4, 0, 0])
        main_triangle = Polygon(A, B, C)
        AB_line = Line(A, B)
        BC_line = Line(B, C)
        AC_line = Line(A, C)

        # Квадрат на стороне AB
        LS1, LS2, LS3, LS4 = nparray([0, 0, 0]), nparray([0, sqrt(5), 0]), nparray(
            [sqrt(5), sqrt(5), 0]), nparray([sqrt(5), 0, 0])
        left_square = Polygon(LS1, LS2, LS3, LS4).rotate(angle=AB_line.get_angle(), about_point=A)

        # Квадрат на стороне BC
        RS1, RS2, RS3, RS4 = nparray([4 - sqrt(13), 0, 0]), nparray([4 - sqrt(13), sqrt(13), 0]), nparray(
            [4, sqrt(13), 0]), nparray([4, 0, 0])
        right_square = Polygon(RS1, RS2, RS3, RS4).rotate(angle=BC_line.get_angle(), about_point=C)

        # Параметры верхнего треугольника
        E = right_square.get_all_points()[4]
        F = left_square.get_all_points()[7]
        EF_line = Line(E, F, color=RED_C)
        EB_line = Line(E, B, color=RED_C)
        FB_line = Line(F, B, color=RED_C)
        EBF_angle = Angle(EB_line, FB_line, color=BLUE)

        # Создание основного рисунка
        main_construction = VGroup(main_triangle, left_square, right_square, EF_line)
        # Анимация
        
        self.play(Create(main_construction), Create(EB_line), Create(FB_line), run_time=2)
        self.play(Create(EBF_angle))
        self.wait(4)

        # manim t_s_s_perp_median.py -pql
        # manim -p -ql t_s_s_perp_median.py MovingFrame
        # manim -p -qh t_s_s_perp_median.py movingframe
