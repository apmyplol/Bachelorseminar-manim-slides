from manim import *
import numpy as np
from manim_slides import Slide

def expm(x, q):
    return np.exp(q*x) - 1

def expm_inv(x, q):
    return np.log(x + 1)/q

p_x = 0
p_y = 0
p = 2

def metrik(q, p, r, t):
    return q.get_value()*np.power(np.exp(r.get_value() * t), p.get_value())

def metrik_inv(q, p, r, t):
    return 1/r.get_value() * np.log(1 + ( np.power(t / q.get_value(), 1/p.get_value()) ))

def exp_metr(x, y):
    return expm_inv( expm(np.abs(x[0] - y[0]), 1) + expm(np.abs(x[1] - y[1]), 1), 1)

class expMIsoCurves(Slide):
    def construct(self):

        Tex.set_default(font_size = 30)
        self.play(Write(NumberPlane()))
        self.next_slide()

        center = Dot([0, 0, 0], color=PINK)
        
        rad1 = ImplicitFunction(
            lambda x, y: exp_metr([x,y], [0, 0]) - 1,
            color=YELLOW
        )

        p_1 = Dot([0, 1, 0])
        self.play(Write(center), Write(rad1), Write(p_1))
        self.next_slide()

        # r1lab = MathTex("r = 1").next_to(rad1, DOWN)

        rad3 = ImplicitFunction(
            lambda x, y: exp_metr([x,y], [0, 0]) - 3,
            color=YELLOW
        )

        # r3lab = MathTex("r = 3").next_to(rad3, UP)

        self.next_slide()


        p_2 = Dot([0, 3, 0])
        self.play(Write(rad3), Write(p_2))
        self.next_slide()

        brace = BraceBetweenPoints([0, 1, 0], [0, 3, 0])
        brace_label = brace.get_tex(exp_metr(p_1.get_center(), p_2.get_center()))

        self.play(Write(brace), Write(brace_label))
        self.next_slide()

        p_3 = Dot(rad1.get_all_points()[500], color=BLUE)
        self.play(Write(p_3))

        rad2 = ImplicitFunction(
            lambda x, y: exp_metr([x,y], p_3.get_center()) - 2,
            color=BLUE
        )

        self.next_slide()
        self.play(Write(rad2))
