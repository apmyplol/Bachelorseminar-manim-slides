from manim import *
from manim.utils.color.BS381 import MIDDLE_BUFF
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


class LpSegAdditive(Slide):
    def construct(self):

        lp = MathTex(r"\delta(a, b) = \left[\sum_{i=1}^{n} |a_i - b_i|^p\right]^{1/p}").to_corner(UL)
        self.play(Write(lp))
        self.next_slide()

        segment = MathTex(r"y = (1-t) x + t z").next_to(lp, RIGHT)
        self.play(Write(segment))
        self.next_slide()

        step1 = MathTex(
            "d(x, y) + d(y, z)"
        ).scale(0.8)
        self.play(Write(step1), VGroup(lp, segment).animate.scale(0.6).to_corner(UL))
        self.next_slide()


        step2 = MathTex(
            "d(x, y) + d(y, z)", "=", "\\left[ \\sum_{i=1}^{n} \\left|", "x_i - (1 - t) x_i - t z_i", "\\right|^p \\right]^{1/p}", 
            "+", "\\left[ \\sum_{i=1}^{n} \\left|", "(1 - t) x_i + t z_i - z_i", "\\right|^p \\right]^{1/p}"
        ).scale(0.8)
        self.play(ReplacementTransform(step1, step2))
        self.next_slide()


        step3 = MathTex(
            "d(x, y) + d(y, z)", "=", "\\left[ \\sum_{i=1}^{n} \\left|", "t \cdot (x_i -  z_i)", "\\right|^p \\right]^{1/p}", 
            "+", "\\left[ \\sum_{i=1}^{n} \\left|", "(1 - t)( x_i - z_i)", "\\right|^p \\right]^{1/p}"
        ).scale(0.8)

        self.play(ReplacementTransform(step2, step3))
        self.next_slide()

        step4 = MathTex(
            "d(x, y) + d(y, z)", "=", "t", "\\left[ \\sum_{i=1}^{n} \\left|", "(x_i -  z_i)", "\\right|^p \\right]^{1/p}", 
            "+", "(1-t)", "\\left[ \\sum_{i=1}^{n} \\left|", "( x_i - z_i)", "\\right|^p \\right]^{1/p}"
        ).scale(0.8)

        self.play(ReplacementTransform(step3, step4))
        self.next_slide()

        step5 = MathTex(
            "d(x, y) + d(y, z)", "=", "\\left[ \\sum_{i=1}^{n} \\left|", "(x_i -  z_i)", "\\right|^p \\right]^{1/p}",
        ).scale(0.8)

        self.play(ReplacementTransform(step4, step5))
        self.next_slide()

        end = MathTex(
            "d(x, y) + d(y, z)", "=", "d(x, z)"
        ).scale(0.8)

        self.play(ReplacementTransform(step5, end))

class AddDiffModel(Slide):
    def construct(self):
        # self.next_section(skip_animations=True)

        lp = MathTex(r"\left[", r"\sum_{i=1}^{n}", "|", "a", r"_i", "-", "b", r"_i", "|", r"^p", r"\right]", r"^{1/p}").to_edge(UP)
        self.play(Write(lp))
        self.next_slide()

        lp.generate_target()
        lp.target[4].set_color(GREEN)
        lp.target[7].set_color(GREEN)
        lp.target.scale(0.6).to_edge(UP)
        self.play(MoveToTarget(lp))

        decomp = MathTex("F[\psi(a_1, b_1, \ldots , \psi(a_n, b_n))]", color=GREEN).to_corner(UL).shift(1.5*DOWN)
        self.play(Transform(lp.copy(), decomp))
        self.next_slide()

        dec_t = Tex("Decomposability").next_to(decomp, RIGHT*6)
        self.play(Write(dec_t))
        self.next_slide()
        


        lp.generate_target()
        self.play(Flash(lp.target[1], color=PINK))
        lp.target[1].set_color(PINK)
        self.play(MoveToTarget(lp))

        add = MathTex(r"G \left [ \sum_{i=1}^{n} \psi_i(a_i, b_i) \right]", color=PINK).next_to(decomp, DOWN)
        self.play(Transform(lp.copy(), add))
        self.next_slide()

        add_t = Tex("Additivity").next_to(dec_t, DOWN).set_y(add.get_y())
        self.play(Write(add_t))
        self.next_slide()



        lp.generate_target()
        self.play(Flash(lp.target[5], color=BLUE))
        lp.target[5].set_color(BLUE)
        self.play(MoveToTarget(lp))

        diff = MathTex(r"F[ |\varphi_1(a_1) - \varphi_1(b_a)| , \ldots , | \varphi_n(a_n) - \varphi_n(b_n)| ]", color=BLUE).scale(0.6).next_to(add, DOWN)
        self.play(Transform(lp.copy(), diff))
        self.next_slide()

        diff_t = Tex("Subtractivity").next_to(add_t, DOWN).set_y(diff.get_y())
        self.play(Write(diff_t))
        self.next_slide()

        models = VGroup(add, decomp, diff)
        admodel = MathTex(r"G \left \{ \sum_{i=1}^{n} F_i[ | \varphi_i(a_i) - \varphi_i(b_i)| ] \right \}")
        ad_t = Tex("Additive Difference Model").scale(0.8).next_to(admodel, RIGHT)
        # self.next_section()
        models2 = VGroup(admodel, ad_t).to_edge(DOWN).set_x(0)
        self.play(Transform(models, models2))
        self.play(Write(SurroundingRectangle(models2, color=PURPLE_A, buff=MED_LARGE_BUFF*0.6)))
