from manim import *
from manim_slides import Slide


# def bez(x):
# B_{x}(t)=(1-t)^{3}c_{1}+3t(1-t)^{2}c_{2}+3t^{2}(1-t)c_{3}+t^{3}c_{4}
# B_{y}(t)=(1-t)^{3}v_{1}+3t(1-t)^{2}v_{2}+3t^{2}(1-t)v_{3}+t^{3}v_{4}

class AddSegments(Slide):
    def construct(self):

        
        start = MathTex(r"\delta(a,b)", "+", r"\delta(b,c)",  "=", r"\delta(a, c)")
        self.play(Write(start))
        self.next_slide()
        # self.play(new_p.animate.shift(1.5*UP).scale(0.7))
        newp_bed = MathTex(r"\delta(a', b') \leq \delta(a, b)", color=PINK).next_to(start, DOWN)
        newp_bed2 = MathTex(r"\delta(a, c) &\leq \delta(a', c')", color=ORANGE).next_to(newp_bed, DOWN)
        self.play(Write(newp_bed), Write(newp_bed2))
        self.next_slide()


        formulas = VGroup(start, newp_bed, newp_bed2)
        # self.play(newp_bed.animate.scale(0.7).next_to(start, DOWN))
        scopy = start.copy()
        self.play(formulas.animate.shift(UP*2).scale(0.7))
        self.next_slide()

        self.play(Write(scopy))
        self.next_slide()

        eq1 = MathTex(r"\delta(a,b)", "+", r"\delta(b,c)", "=", r"\delta(a, c)", r"\leq", r"\delta(a', c')")
        eq1[5].set_color(ORANGE)
        self.play(TransformMatchingTex(scopy, eq1))
        self.next_slide()

        eq2 = MathTex(r"\delta(a,b)", "+", r"\delta(b,c)", "=", r"\delta(a, c)", r"\leq", r"\delta(a', c')", r"\leq \delta(a', b')", "+", r"\delta(b', c')")
        eq2[5].set_color(ORANGE)
        self.play(TransformMatchingTex(eq1, eq2))
        self.next_slide()

        eq3 = MathTex(r"\delta(b,c)", r"\leq", r"\delta(b', c')")
        eq3[1].set_color(PINK)
        self.play(TransformMatchingTex(eq2, eq3))
        self.next_slide()


        ar = MathTex(r"\Downarrow").next_to(newp_bed2, DOWN)
        self.play(Succession(eq3.animate.shift(DOWN*0.7), Write(ar)))
        self.next_slide()

        formulas.add(eq3, ar)

        self.play(formulas.animate.to_edge(UL).scale(0.8))
        self.next_slide()


        tern_rel = Tex(r"ternary relation $(a b c \rangle$", color=PURPLE_A).to_edge(UP).shift(RIGHT)
        self.play(Write(tern_rel))
        self.next_slide()

        bl = BulletedList(r"$(a, b) \succsim (a', b')$ und $(a', c') \succsim (a, c)$, dann $(b', c') \succsim (b, c)$",
                        r"strikt impliziert strikt",
                        r"$\langle a b c \rangle$ wenn $(a b c \rangle$ und $(c b a \rangle$").scale(0.6).next_to(tern_rel, DOWN)

        t_def = VGroup(bl, tern_rel)
        sr = SurroundingRectangle(t_def, color=PURPLE_A, buff=MED_LARGE_BUFF*0.7)
        self.play(Write(bl), Write(sr))
        self.next_slide()

        # Draw circles
        inner_circle = Circle(radius=1.5, color=WHITE)
        middle_circle = Circle(radius=3, color=WHITE)

        # Draw points
        point_a = Dot(inner_circle.get_center(), color=WHITE)
        point_b = Dot(inner_circle.get_center() + UP*1.5, color=WHITE)
        point_c = Dot(middle_circle.get_center() + UP*3, color=WHITE)

        point_b_prime = Dot(point_a.get_center()+ UP*1 + RIGHT*0.5, color=BLUE)
        point_c_prime = Dot(point_a.get_center() + UP*3.5 + LEFT*0.3, color=BLUE)
        
        # Labels
        label_a = MathTex("a", color=WHITE).next_to(point_a, DOWN)
        label_b = MathTex("b", color=WHITE).next_to(point_b, DOWN)
        label_c = MathTex("c", color=WHITE).next_to(point_c, DOWN)

        label_b_prime = MathTex("b'", color=BLUE).next_to(point_b_prime, DOWN)
        label_c_prime = MathTex("c'", color=BLUE).next_to(point_c_prime, DOWN)

        cGroup = VGroup(inner_circle, middle_circle, point_a, point_b, point_c, label_a, label_b, label_c, point_b_prime, point_c_prime, label_b_prime, label_c_prime).scale(0.5).to_edge(DOWN)
        self.play(Write(cGroup))
        self.next_slide()

        b1 = BraceBetweenPoints(point_b.get_center(), point_c.get_center())
        b2 = BraceBetweenPoints(point_b_prime.get_center(), point_c_prime.get_center(), color=BLUE, direction=[-1, 0, 0])
        self.play(Write(b1), Write(b2))
        self.next_slide()

        b1.generate_target()
        b2.generate_target()
        b1.target.rotate(PI/2).shift(UP+RIGHT)
        kl = MathTex("\\geq").next_to(b1.target, LEFT)
        b2.target.rotate(-PI/2).next_to(kl, LEFT)

        self.play(Succession( MoveToTarget(b1), Write(kl), MoveToTarget(b2)))
        self.next_slide()

        draw1 = VGroup(cGroup, b1, b2, kl)
        self.play(draw1.animate.to_edge(LEFT))
        self.next_slide()

        idee = Tex(r"$\langle a b c \rangle \overset{\land}{=}$ additivity", color=GREEN).next_to(sr, DOWN)
        self.play(Write(idee))
        self.next_slide()

        seg_sol = Tex("Segmental solvability", color=PURPLE_A).next_to(idee, DOWN)
        self.play(Write(seg_sol))
        self.next_slide()

        s_sol_cond = Tex(r"Wenn $(a, c) \succsim (e, f)$, dann $\exists b \in A: (a, b) \sim (e, f)$ und $\langle abc \rangle$").scale(0.6).next_to(seg_sol, DOWN)
        self.play(Write(s_sol_cond))
        self.next_slide()

        also = MathTex(r"\Rightarrow").next_to(cGroup, RIGHT*1.5).shift(DOWN*0.5)
        th = Tex(r"$\langle a b c \rangle$ gdw. $\delta(a,b) + \delta(b,c) = \delta(a,c)$", color=BLUE_A).next_to(also, RIGHT*1.5)
        self.play(Write(also), Write(th), Write(SurroundingRectangle(VGroup(also, th), color=BLUE_A, buff=MED_LARGE_BUFF*0.5)))
