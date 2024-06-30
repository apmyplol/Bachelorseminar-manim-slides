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



class pexp_Bsp(Slide):
    def construct(self):
        Text.set_default(font_size = 24)
        MathTex.set_default(font_size = 24)

        plane = NumberPlane()
        rad = ValueTracker(1)
        p = ValueTracker(1)
        r = ValueTracker(1)
        q = ValueTracker(1)

        number_line = NumberLine(x_range=[0, 10], length=3).to_corner(UR).shift(DOWN).add_numbers([0, 1, 10], font_size=15)
        point_p = always_redraw(lambda: Vector(0.3*DOWN).next_to(number_line.n2p(p.get_value()), UP))
        point_r = always_redraw(lambda: Vector(0.3*DOWN).next_to(number_line.n2p(r.get_value()), UP))
        # point_q = always_redraw(lambda: Vector(0.3*UP).next_to(number_line.n2p(q.get_value()), 1.5*DOWN))
        point_rad = always_redraw(lambda: Vector(0.3*UP).next_to(number_line.n2p(rad.get_value()), 1.5*DOWN))
        label_p = MathTex("p").add_updater(lambda m: m.next_to(point_p, UP))
        label_r = MathTex("r").add_updater(lambda m: m.next_to(point_r, UP))
        # label_q = MathTex("q").add_updater(lambda m: m.next_to(point_q, DOWN))
        label_rad = MathTex("\\text{rad}").add_updater(lambda m: m.next_to(point_rad, DOWN))
        number_line_stuff = VGroup(number_line, point_p, point_r, point_rad, label_p, label_r, label_rad)


        # exp_norm = always_redraw(lambda: ImplicitFunction(
        #     lambda x, y: expm_inv( expm(np.abs(x), q.get_value()) + expm(np.abs(y), q.get_value()), q.get_value()) - rad.get_value(),
        #     color=YELLOW
        # ))

        p_norm = always_redraw(lambda: ImplicitFunction(
            lambda x, y: np.power( np.power(np.abs(x), p.get_value()) + np.power(np.abs(y), p.get_value()), 1/p.get_value() ) - rad.get_value(),
            color=BLUE
        ))

        m_norm = always_redraw(lambda: ImplicitFunction(
            lambda x, y: metrik_inv(q, p, r, metrik(q, p, r, np.abs(x)) + metrik(q, p, r, np.abs(y))) - rad.get_value(),
            color=YELLOW
        ))


        ydot = Dot(color=YELLOW).to_corner(UL)
        ydot_text = MathTex("q \cdot (e^{r \cdot t} - 1)^p").next_to(ydot, RIGHT)
        pdot = Dot(color=BLUE).next_to(ydot, 1.5*DOWN)
        pdot_text = MathTex("x^p", font_size=24).next_to(pdot, RIGHT)
        text_stuff = VGroup(ydot, ydot_text, pdot, pdot_text)
        self.play(Create(number_line_stuff), Create(plane), Create(text_stuff))
        self.next_slide()


        self.play(Create(p_norm))
        self.next_slide()
        
        # self.play(rad.animate.increment_value(5), rate_func=linear, run_time=1)
        self.play(p.animate.set_value(5), rate_func=linear, run_time=1)
        self.next_slide()
        self.play(p.animate.set_value(1), rate_func=exponential_decay, run_time=1)
        self.next_slide()
        self.play(p.animate.set_value(0), rate_func=linear, run_time=1)
        self.next_slide()
        self.play(p.animate.set_value(1), rate_func=exponential_decay, run_time=1)
        self.next_slide()

        self.play(Create(m_norm))
        self.next_slide()
        self.play(r.animate.set_value(5), rate_func=linear, run_time=1)
        self.next_slide()
        self.play(r.animate.set_value(3), rate_func=exponential_decay, run_time=1)
        self.next_slide()
        # self.play(q.animate.set_value(5), rate_func=linear, run_time=1)
        # self.play(q.animate.set_value(2), rate_func=exponential_decay, run_time=1)
        # self.wait(0.5)

        self.play(p.animate.set_value(5), rate_func=linear, run_time=1)
        self.next_slide()
        self.play(p.animate.set_value(1.5), rate_func=exponential_decay, run_time=1)
        self.next_slide()

        self.play(rad.animate.increment_value(5), rate_func=linear, run_time=5)
        self.next_slide()



# class expMIsoCurves(Slide):
#     def construct(self):
#
#         Tex.set_default(font_size = 30)
#         center = Dot([0, 0, 0], color=PINK)
#         
#         rad1 = ImplicitFunction(
#             lambda x, y: exp_metr([x,y], [0, 0]) - 1,
#             color=YELLOW
#         )
#
#         self.play(Write(NumberPlane()), Write(center), Write(rad1))
#         self.next_slide()
#
#         # r1lab = MathTex("r = 1").next_to(rad1, DOWN)
#
#         rad3 = ImplicitFunction(
#             lambda x, y: exp_metr([x,y], [0, 0]) - 3,
#             color=YELLOW
#         )
#
#         # r3lab = MathTex("r = 3").next_to(rad3, UP)
#
#         self.add(rad3)
#         self.next_slide()
#
#
#         p_1 = Dot([0, 1, 0])
#         p_2 = Dot([0, 3, 0])
#         
#
#         brace = BraceBetweenPoints([0, 1, 0], [0, 3, 0])
#         brace_label = brace.get_tex(exp_metr(p_1.get_center(), p_2.get_center()))
#
#         self.add(p_1, p_2, brace, brace_label)
#
#         p_3 = Dot(rad1.get_all_points()[500], color=BLUE)
#
#         rad2 = ImplicitFunction(
#             lambda x, y: exp_metr([x,y], p_3.get_center()) - 2,
#             color=BLUE
#         )
#
#
#         self.add(rad2, p_3)
