from manim import *
from manim_slides import Slide


class pexpMetrik(Slide):
    def construct(self):
        
        # self.next_section(skip_animations=True)
        admodel = MathTex(r"G", r"\left \{ \sum_{i=1}^{n} F[ | a_i - b_i| ] \right \}")
        self.play(Write(admodel))
        self.next_slide()

        admo = MathTex(r"F^{-1}", r"\left \{ \sum_{i=1}^{n} F[ | a_i - b_i| ] \right \}")
        self.play(ReplacementTransform(admodel, admo))
        self.next_slide()

        self.play(admo.animate.scale(0.5).to_corner(UR))
        self.next_slide()


        fam = MathTex(r"F(t) = q \cdot (e^{t \cdot r} - 1)^p", r"\qquad", "q, r > 0, p \geq 1")
        self.play(Write(fam))
        self.next_slide()

        self.play(fam.animate.scale(0.5).to_corner(UL).set_y(admo.get_y()))
        self.play(Write(Line(start=LEFT*10, end=RIGHT*10, color=BLUE).shift(UP*2.5)))
        self.next_slide()

        
        pos = Tex("Positivität: ").to_edge(LEFT).shift(UP*2)
        self.play(Write(pos))
        self.next_slide()

        p1 = MathTex(r"\delta(a,b) = 0").next_to(pos, RIGHT)
        self.play(Write(p1))
        self.next_slide()

        p2  = MathTex(r"\delta(a,b) = 0", r"\Rightarrow", r"F(|a_i - b_i|) = 0").next_to(pos, RIGHT)
        self.play(ReplacementTransform(p1, p2))
        self.next_slide()

        p3  = MathTex(r"F(|a_i - b_i|) = 0", r"\Rightarrow", r"a_i = b_i").next_to(pos, RIGHT)
        self.play(ReplacementTransform(p2, p3))
        self.next_slide()

        p4 = MathTex(r"a \neq b").next_to(p3, DOWN)
        self.play(Write(p4))
        self.next_slide()

        p5 = MathTex(r"a \neq b", r"\Rightarrow", r"a_i \neq b_i").next_to(p3, DOWN)
        self.play(ReplacementTransform(p4, p5))
        self.next_slide()

        p6 = MathTex(r"a_i \neq b_i", r"\Rightarrow", r"F(|a_i - b_i|) > 0").next_to(p3, DOWN)
        self.play(ReplacementTransform(p5,p6))
        self.next_slide()
    
        pos_check = Tex("\\checkmark", color=GREEN).next_to(pos, RIGHT)
        self.play(ReplacementTransform(VGroup(p3, p6), pos_check))
        self.next_slide()


        sy = Tex("Symmetrie: ").next_to(pos, DOWN)
        self.play(Write(sy))
        self.next_slide()

        p7 = MathTex(r"|a_i - b_i| = |b_i - a_i|").next_to(sy, RIGHT)
        self.play(Write(p7))
        self.next_slide()

        sym_check = Tex("\\checkmark", color=GREEN).next_to(sy, RIGHT)
        self.play(ReplacementTransform(p7, sym_check))
        self.next_slide()
        



        dugl = Tex("Dreiecksungl.: ", r"$\delta(a, b) + \delta(b, c) \geq \delta(a, c)$").next_to(sy, DOWN, aligned_edge=LEFT)
        self.play(Write(dugl))
        self.next_slide()

        mulh = Tex("Mulholland", color=BLUE)
        self.next_slide()

        mulh_b = BulletedList(
                            r"$f$ stetig, streng monoton steigend, und $f(0) = 0$",
                            r"$f$ konvex auf $[0, \infty)$",
                            r"$\log f(e^x)$ ist konvex für $x \in (-\infty, \infty)$"
                            ).scale(0.7).next_to(mulh, DOWN)
        ar = MathTex(r"\Downarrow").next_to(mulh_b, DOWN)
        mulh_f =  MathTex(r"f^{-1} \left[ \sum f(|x_i + y_i|) \right] \leq f^{-1}  \left[ \sum f(|x_i|) \right] + f^{-1} \left[ \sum f(|y_i|) \right]").scale(0.8).next_to(ar, DOWN)

        mul_g = VGroup(mulh, mulh_b, ar, mulh_f).scale(0.8)
        rec = SurroundingRectangle(mul_g, color=BLUE, buff=MED_SMALL_BUFF)
        self.play(Write(mul_g), Write(rec))
        self.next_slide()


        fam2 = MathTex(r"F(t) = q \cdot (e^{t \cdot r} - 1)^p", "\\\\", "q, r > 0, p \geq 1").scale(0.4).to_corner(UL)
        self.play(Unwrite(admo), Unwrite(sy), Unwrite(dugl), Unwrite(pos), Unwrite(pos_check), Unwrite(sym_check), ReplacementTransform(fam, fam2), run_time=1)
        self.play(Unwrite(mulh),Unwrite(rec), mulh_b.animate.scale(0.8).next_to(fam2, RIGHT*1.3), run_time=1)
        self.play(ar.animate.rotate(PI/2).next_to(mulh_b, RIGHT), run_time=1)
        self.play(mulh_f.animate.scale(0.7).next_to(ar, RIGHT), run_time=1)
        self.next_slide()

        c1 = Tex("\\checkmark", color=GREEN).scale(0.6).next_to(mulh_b[0], RIGHT)
        self.play(Write(c1))
        self.next_slide()

        c2 = Tex("\\checkmark", color=GREEN).scale(0.6).next_to(mulh_b[1], RIGHT)
        self.play(Write(c2))
        self.next_slide()


        e1 = MathTex(r"\log q(e^{re^x} -1)^p")
        self.play(ReplacementTransform(fam2[0].copy(), e1))
        self.next_slide()

        e2 = MathTex(r"\log q(e^{re^x} -1)^p", "=", r"\log q", r"+ p \cdot", r"\log(e^{re^x} - 1)")
        self.play(TransformMatchingTex(e1, e2))
        self.next_slide()

        e3 = MathTex(r"\log(e^{re^x} - 1)", r"\text{ konvex}")
        self.play(TransformMatchingTex(e2, e3))
        self.next_slide()

        self.play(e3.animate.next_to(fam2, 3*DOWN, aligned_edge=LEFT).set_color(YELLOW))

        e4 = MathTex("{", r"{r e^{re^x + x}", r"\left( r (-e^x) + e^{re^x} - 1 \right)}", r"\over", r"{\left( e^{re^x} - 1 \right)^2}}")
        self.play(Write(e4))
        self.next_slide()


        e5 = MathTex("{", r"{r e^{re^x + x}", r"\left( r (-e^x) + e^{re^x} - 1 \right)}", r"\over", r"{\left( e^{re^x} - 1 \right)^2}}", r"\overset{!}{>} 0")
        self.play(TransformMatchingTex(e4, e5))
        self.next_slide()

        br1 = BraceLabel(e5[4], "> 0")
        self.play(Write(br1), run_time=0.5)
        self.next_slide()

        e6 = MathTex("{", r"{r e^{re^x + x}", r"\left( r (-e^x) + e^{re^x} - 1 \right)}", r"\overset{!}{>}",  "0")
        self.play(Unwrite(br1), TransformMatchingTex(e5, e6))
        self.next_slide()

        br2 = BraceLabel(e6[1], ">0")
        self.play(Write(br2), run_time=0.5)
        self.next_slide()

        e7 = MathTex(r"\left( r (-e^x) + e^{re^x} - 1 \right)}", r"\overset{!}{>} 0")
        self.play(Unwrite(br2), TransformMatchingTex(e6, e7))
        self.next_slide()

        ar = MathTex(r"\Leftarrow").next_to(e3, RIGHT)
        e8 = MathTex(r"\left( r (-e^x) + e^{re^x} - 1 \right)}", r">", "0").set_color(YELLOW).next_to(ar, RIGHT)
        self.play(Write(ar), ReplacementTransform(e7, e8), e3.animate.set_color(WHITE))
        self.next_slide()

        e9 = MathTex(r" e^{re^x}  - r e^x" r">", "1").set_color(YELLOW).next_to(ar, RIGHT)
        self.play(ReplacementTransform(e8, e9))
        self.next_slide()

        ee2 = MathTex(r"re^x \cdot e^{re^x} - re^x")
        self.play(Write(ee2))
        self.next_slide()

        ee3 = MathTex(r"re^x \cdot e^{re^x} - re^x", "=", r"re^x",  r"\cdot", r"(e^{re^x} - 1)")
        self.play(ReplacementTransform(ee2, ee3))
        self.next_slide()

        br1 = BraceLabel(ee3[2], ">0")
        br2 = BraceLabel(ee3[4], ">0")
        self.play(Write(br1), Write(br2), run_time=0.5)
        self.next_slide()

        ee4 = MathTex(r"re^x \cdot e^{re^x} - re^x", "=", r"re^x",  r"\cdot", r"(e^{re^x} - 1)", "> 0")
        self.play(TransformMatchingTex(ee3, ee4), Unwrite(br1), Unwrite(br2))
        self.next_slide()

        self.play(ee4.animate.scale(0.7).next_to(e3, 3*DOWN, aligned_edge=LEFT))
        self.next_slide()

        em1 = MathTex(r"\lim_{x \rightarrow -\infty} e^{re^x}  - r e^x")
        self.play(Write(em1))
        self.next_slide()

        em2 = MathTex(r"\lim_{x \rightarrow -\infty} e^{re^x}  - r e^x", r" = 1")
        self.play(ReplacementTransform(em1, em2))
        self.next_slide()

        self.play(em2.animate.to_edge(RIGHT).set_y(ee4.get_y()))
        self.next_slide()

        a1 = MathTex("\\Rightarrow", r"\left( r (-e^x) + e^{re^x} - 1 \right)", r">", "0").shift(DOWN)
        self.play(Write(a1), e9.animate.set_color(GREEN))
        self.next_slide()

        a2 = MathTex("\\Rightarrow", r"\left( r (-e^x) + e^{re^x} - 1 \right)", r">", "0", r"\Rightarrow", r"\log(e^{re^x} - 1)", r"\text{ konvex}").shift(DOWN)
        self.play(ReplacementTransform(a1, a2), e3.animate.set_color(GREEN))
        self.next_slide()

        
        lkc = Tex("\\checkmark", color=GREEN).next_to(mulh_b[2], RIGHT)
        self.play(Write(lkc))
        self.next_slide()

        fin = Tex("$\\Rightarrow F(t)$", " als Additive Difference Model ist Metrik").to_edge(DOWN)
        self.play(Write(fin), Write(SurroundingRectangle(fin, color=GREEN, buff=MED_SMALL_BUFF)))
        

