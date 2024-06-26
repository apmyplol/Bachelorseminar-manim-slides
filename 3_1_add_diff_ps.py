from manim import *
from manim_slides import Slide


class HinrNotwBeds(Slide):
    def construct(self):
        
        # self.next_section(skip_animations=True)

        v1 = Tex("$\\langle A, \succsim \\rangle$", "factorial proximity structure")
        self.play(Write(v1))
        self.next_slide()

        v2 = Tex("$\\langle A, \succsim \\rangle$", " additive difference ", "factorial proximity structure")
        self.play(ReplacementTransform(v1, v2))
        self.next_slide()

        self.play(v2.animate.shift(2*UP))
        self.next_slide()

        ar = Tex("$\\Downarrow$").next_to(v2, DOWN)
        vf = BulletedList(r"$\varphi_i : A_i \rightarrow \mathbb{R}$, Intervallskalen",
                          r"$F_i: \mathbb{R} \rightarrow \mathbb{R}_+$, Intervallskalen, steigend, $F_i(0) = 0$",
                          r"""\begin{align*}
                          (a_1, \ldots, a_n, b_1, \ldots, b_n) &\succsim (c_1, \ldots, c_n, d_1, \ldots, d_n) \\
                          &\iff \\
                          \sum_{i=1}^{n} F_i(|\varphi_i(a_i) - \varphi_i(b_i)|) &\geq \sum_{i=1}^{n} F_i(|\varphi_i(c_i) - \varphi_i(d_i)|)
                          \end{align*}
                          """).scale(0.6).next_to(ar, DOWN*2)

        b1 = SurroundingRectangle(vf, color=BLUE, buff=MED_SMALL_BUFF)
        self.play(Write(ar), Write(vf), Write(b1))
        self.next_slide()

        vg1 = VGroup(vf, b1)
        self.play(vg1.animate.scale(0.9).to_edge(LEFT))
        self.play(ar.animate.scale(0.9).next_to(vg1, UP))
        self.next_slide()

        ba1 = Tex("$\\langle A$", "$\\succsim$", "$\\rangle$", " representable mit ", "$\\delta$")
        bb1 = MathTex(r"a_j = b_j &= c_j \forall j \neq i \\", r"\text{ und }", r"(a, c) &\succsim (a, b), (b,c)\\",r"&\Downarrow\\", r"\delta(a, b) + \delta(&b, c) = \delta(a, c)").next_to(ba1, DOWN)
        repV = VGroup(ba1, bb1).scale(0.7).next_to(vg1, 7*RIGHT)
        repB = SurroundingRectangle(repV, color=BLUE, buff=MED_SMALL_BUFF)

        self.play(Write(repV), Write(repB))
        self.next_slide()



        plus2 = MathTex("+").next_to(b1, 2.5*RIGHT).shift(UP)
        notw = MathTex(r"\Uparrow").next_to(plus2, UP)
        notwf = Tex("?", color=PINK).next_to(notw, UP)

        self.play(Write(plus2), Write(notw), Write(notwf))
        self.next_slide()


        plus = Tex("$+$", r"?", r"$\Rightarrow$").next_to(b1, RIGHT).shift(DOWN)
        plus[1].set_color(ORANGE)
        self.play(Write(plus))
        self.next_slide()

        self.play(Unwrite(ar), Unwrite(v2), run_time=0.5)
        al = VGroup(plus2, notw, notwf, plus, repB, repV, vg1)
        self.play(al.animate.shift(UP))
        self.next_slide()

        n1 = Tex("$F$", " stetig,", " konvex ", "$F_i(x) = F(t_i x), t_i > 0$", color=PINK).next_to(notwf, UP)
        self.play(ReplacementTransform(notwf.copy(), n1))
        self.next_slide()


        h1 = Tex("$\\bullet$", "+", "$\\log F(e^x)$ konvex").next_to(plus, DOWN*2)
        h1[0].set_color(PINK)
        h1[2].set_color(ORANGE)
        self.play(ReplacementTransform(plus.copy(), h1))
        self.next_slide()

        
        s1 = MathTex(r"\sum_{i=1}^{n} F_i(|\varphi_i(a_i) - \varphi_i(b_i)|) &\geq \sum_{i=1}^{n} F_i(|\varphi_i(c_i) - \varphi_i(d_i)|)").scale(0.5).to_corner(UL)
        s2 = MathTex("\\iff", r"(a, b) \succsim (c, d)", r"\iff").scale(0.5).next_to(s1, RIGHT)
        s3 = MathTex(r"\delta(a, b) \geq \delta(c,d)").scale(0.5).next_to(s2, RIGHT)
        s4 = MathTex(r"\text{Dim Add} \\ F \text{ steigend}").scale(0.5).next_to(s3, RIGHT*1.5)

        alle = VGroup(al, n1, h1).copy()
        pline = Line(start=LEFT*10, end=RIGHT*10, color=PINK).shift(UP*2.3)


        self.play(Unwrite(al), Unwrite(h1),ReplacementTransform(n1, pline), run_time=0.8)
        self.play(Write(VGroup(s1, s2, s3, s4).set_x(0)))
        self.next_slide()

 
        s5 = MathTex(r"\sum_{i=1}^{n} F_i(|\varphi_i(a_i) - \varphi_i(b_i)|) &\geq \sum_{i=1}^{n} F_i(|\varphi_i(c_i) - \varphi_i(d_i)|)","\\iff", r"\delta(a, b) \geq \delta(c,d)").scale(0.7)
        self.play(ReplacementTransform(VGroup(s1.copy(), s3.copy()), s5))
        self.next_slide()

        
        ar = MathTex(r"\Downarrow").next_to(s5, DOWN)
        g1 = MathTex(r"\exists G \text{ steigend}: ", r"\delta(a, b) = G \left[ \sum_{i=1}^{n} F_i(|\varphi_i(a_i) - \varphi_i(b_i)|) \right]").scale(0.8).next_to(ar, DOWN)
        self.play(Write(ar), Write(g1))
        self.next_slide()


        s6 = MathTex(r"\delta(a, b) = G \left[ \sum_{i=1}^{n} F_i(|\varphi_i(a_i) - \varphi_i(b_i)|) \right]").scale(0.6).to_corner(UL)
        self.play(ReplacementTransform(VGroup(s1, s2 ,s3), s6), Unwrite(g1), Unwrite(ar), Unwrite(s5))
        self.play(s4.animate.next_to(s6, RIGHT))
        self.next_slide()

        pf = MathTex("\\Rightarrow").next_to(s4)
        tar = BulletedList(r"$F_i(x) = F(t_i x), t_i > 0$",
                           r"$F$ stetig",
                           r"$F$ konvex", height=2).scale(0.4).next_to(pf, RIGHT)
        self.play(Write(pf), Write(tar))
        self.next_slide()



        self.play(tar[0].animate.set_color(PINK))
        self.next_slide()


        e0 = MathTex(r"\delta(a, b) + \delta(b,c) = \delta(a,c)")
        self.play(ReplacementTransform(VGroup(s4, s6).copy(), e0))
        self.next_slide()


        e1 = MathTex(r"G", r"\left(", r"F_i \left(", r"|\varphi_i(a_i) - \varphi_i(b_i)|", r"\right)", r"\right)", r"+", "G", r"\left(", r"F_i", r"\left(", r"|\varphi_i(b_i) - \varphi_i(c_i)|", r"\right) \right)",  "=", "G", r"\left(", r"F_i", r"\left(", r"|\varphi_i(a_i) - \varphi_i(c_i)|", r"\right)", r"\right)").scale(0.6)
        self.play(Write(e1), e0.animate.shift(UP))
        self.next_slide()

        # self.next_section()
        b1 = BraceLabel(e1[3], "x")
        b2 = BraceLabel(e1[11], "y")
        self.next_slide()
        
        tt1 = MathTex(r"(a,c) \succsim (a,b), (b,c)").to_edge(DOWN)
        self.play(Write(tt1))
        self.next_slide()

        tt2 = MathTex(r"\delta(a,c) \geq \delta(a, b), \delta(b,c)").move_to(tt1)
        self.play(ReplacementTransform(tt1, tt2))
        self.next_slide()

        tt3 = MathTex(r"G \left( \sum_{i=1}^{n} F_i \left( |\varphi_i(a_i) - \varphi_i(c_i)| \right) \right) \geq G \left( \sum_{i=1}^{n} F_i \left( |\varphi_i(a_i) - \varphi_i(b_i)| \right) \right)").scale(0.7).move_to(tt2)
        self.play(ReplacementTransform(tt2, tt3))
        self.next_slide()

        tt4 = MathTex(r"G \left(F_i \left( |\varphi_i(a_i) - \varphi_i(c_i)| \right) \right) \geq G \left( F_i \left( |\varphi_i(a_i) - \varphi_i(b_i)| \right) \right)").move_to(tt3)
        self.play(ReplacementTransform(tt3, tt4))
        self.next_slide()

        tt5 = MathTex(r"F_i \left( |\varphi_i(a_i) - \varphi_i(c_i)| \right) \geq  F_i \left( |\varphi_i(a_i) - \varphi_i(b_i)| \right)").move_to(tt4)
        self.play(ReplacementTransform(tt4, tt5))
        self.next_slide()

        tt6 = MathTex(r"|\varphi_i(a_i) - \varphi_i(c_i)|\geq  |\varphi_i(a_i) - \varphi_i(b_i)|").move_to(tt5)
        self.play(ReplacementTransform(tt5, tt6))
        self.next_slide()

        b3 = Brace(e1[18]) 
        b3b = MathTex(r"|\varphi_i(a_i) - \varphi_i(b_i)| + |\varphi_i(b_i) - \varphi_i(c_i)|").scale(0.7).next_to(b3, DOWN)
        self.play(Write(b1), Write(b2), Write(b3), Write(b3b))
        self.next_slide()

        e2 = MathTex(r"G", r"\left(", r"F_i \left(", "x", r"\right)", r"\right)", r"+", "G", r"\left(", r"F_i", r"\left(", "y", r"\right) \right)",  "=", "G", r"\left(", r"F_i", r"\left(", "x+y", r"\right)", r"\right)").scale(0.8)
        self.play(Unwrite(b1), Unwrite(b2), Unwrite(b3), Unwrite(b3b), Unwrite(tt6), run_time=0.7)
        self.play(ReplacementTransform(e1, e2))
        self.next_slide()

        # self.next_section(skip_animations=True)

        e3 = MathTex(r"H_i", r"\left(", "x", r"\right)", r"+", "H_i", r"\left(", "y", r"\right)", "=", "H_i", r"\left(", "x+y", r"\right)").scale(0.8)
        self.play(ReplacementTransform(e2, e3))
        self.next_slide()

        e4 = MathTex("H_i(x) = t_i x").shift(DOWN)
        self.play(Write(e4))
        self.next_slide()


        e5 = MathTex("t_i x", "=", "G(F_i(x))").shift(DOWN*2)
        self.play(Write(e5))
        self.next_slide()

        e6 = MathTex("G^{-1}(", "t_i x", ")", "=", "G^{-1}", "G(F_i(x))").shift(2*DOWN)
        self.play(TransformMatchingTex(e5, e6))
        self.next_slide()

        e7 = MathTex("G^{-1}(", "t_i x", ")", "=", "F_i(x)").shift(2*DOWN)
        self.play(TransformMatchingTex(e6, e7))
        self.next_slide()

        
        e8 = MathTex("F := F_n", "\\Rightarrow", "F_i(x) = F_n(t_i x) = F(t_i x)").shift(DOWN*3)
        self.play(Write(e8))
        self.next_slide()

        ch1 = Tex("\\checkmark").scale(0.8).next_to(tar[0]).set_color(GREEN)
        self.play(Write(ch1), tar[0].animate.set_color(WHITE), Unwrite(e7), Unwrite(e8), Unwrite(e4), Unwrite(e0), Unwrite(e3))

        self.next_slide()

        self.play(tar[1].animate.set_color(PINK))
        self.next_slide()



        lem = Tex("Lemma: ",r"$F(\alpha + \beta + \gamma) + F(\gamma) \geq F(\alpha + \gamma) + F(\beta + \gamma)$").scale(0.7).shift(UP*2)
        lem[1].set_color(PINK)
        self.play(Write(lem))
        self.next_slide()

        sag = r"\gamma"
        saa = r"\alpha"
        sab = r"\beta"
        saf = r"F"
        sas = r"\sum"
        safi = r"F^{-1}"
        gra1 = MathTex(r"\alpha_1", "=", sag)
        gra2 = MathTex(r"\alpha_2", "=", safi, "(", saf, "(", saa, "+", sag, ")", "-", saf, "(", sag, ")" , ")").next_to(gra1, DOWN)
        grb1 = MathTex(r"\beta_1" "=", sab).next_to(gra2, DOWN)
        sets = VGroup(gra1, gra2, grb1).scale(0.7).to_corner(UL).shift(2*DOWN)
        self.play(Write(sets))
        self.next_slide()


        dugl = MathTex(r"F^{-1} \left[ \sum_{i=1}^{n} F(\alpha_i) \right] + F^{-1} \left[ \sum_{i=1}^{n} F(\beta_i) \right]", r"\geq", r"F^{-1}", "\left[", r"\sum_{i=1}^{n} F(\alpha_i + \beta_i)", r"\right]").scale(0.5).to_edge(RIGHT).shift(UP*1.2)
        self.play(Write(dugl))
        self.next_slide()


        dugl2 = MathTex(r"F \left\{", r"F^{-1} \left[", r"\sum_{i=1}^{n} F(\alpha_i)i", r"\right]", "+",  r"F^{-1} \left[", r"\sum_{i=1}^{n} F(\beta_i)", r"\right]", r"\right\}", r"\geq", r"\sum_{i=1}^{n} F(\alpha_i + \beta_i)").scale(0.5).to_edge(RIGHT).shift(UP*1.2)
        self.play(ReplacementTransform(dugl, dugl2))
        self.next_slide()

        dugl3 = MathTex(r"F \left\{", r"F^{-1} \left[", "F", "(", sag, ")", "+","F", "(", safi, "(", saf, "(", saa, "+", sag, ")", "-", saf, "(", sag, ")" , ")", ")" , r"\right]", "+",  r"F^{-1} \left[", "F(", sab, ")" , r"\right]", r"\right\}").scale(0.6).to_edge(RIGHT)
        self.play(ReplacementTransform(VGroup(dugl2.copy(), sets.copy()), dugl3))
        self.next_slide()

        dugl4 = MathTex(r"F \left\{", r"F^{-1} \left[", "F", "(", sag, ")", "+", saf, "(", saa, "+", sag, ")", "-", saf, "(", sag, ")" , r"\right]", "+", sab, r"\right\}").scale(0.6).next_to(dugl3, DOWN)
        self.play(ReplacementTransform(dugl3.copy(), dugl4))
        self.next_slide()

        dugl5 = MathTex(r"F \left\{", r"F^{-1} \left[", saf, "(", saa, "+", sag, ")", r"\right]", "+", sab, r"\right\}").scale(0.6).next_to(dugl4, DOWN)
        self.play(ReplacementTransform(dugl4.copy(), dugl5))
        self.next_slide()


        dugl6 = MathTex(r"F \left\{", saa, "+", sag, "+", sab, r"\right\}").scale(0.6).next_to(dugl5, DOWN)
        self.play(ReplacementTransform(dugl5.copy(), dugl6))
        # self.play(ReplacementTransform(VGroup(dugl2.copy(), sets.copy(), )))
        self.next_slide()


        dugl6.generate_target()
        dugl6.target.set_x(0).set_y(0).shift(0.5*DOWN)
        self.play(Unwrite(VGroup(dugl3, dugl4, dugl5)), run_time=0.8)
        self.play(MoveToTarget(dugl6))
        self.next_slide()

        dugl7 = MathTex(r"F(", saa, "+", sag, "+", sab, r")", r"\geq", r"\sum_{i=1}^{n} F(\alpha_i + \beta_i)").scale(0.6).shift(0.5*DOWN)
        self.play(TransformMatchingTex(dugl6, dugl7))
        self.next_slide()

        dugl8 = MathTex(r"F(", saa, "+", sag, "+", sab, r")", r"\geq", r"F(\beta + \gamma) + F(\alpha + \gamma) - F(\gamma)").scale(0.6).shift(0.5*DOWN)
        self.play(TransformMatchingTex(dugl7, dugl8))
        self.next_slide()


        lem.generate_target()
        lem.target = lem[1].to_edge(LEFT).set_color(GREEN)


        # self.play(lem[1].animate.set_color(GREEN))
        self.play(MoveToTarget(lem), Unwrite(sets), Unwrite(dugl2), Unwrite(dugl8))
        self.next_slide()

        stet = Tex("$F$ stetig").scale(0.7)
        self.play(Write(stet))
        self.play(stet.animate.set_color(PINK).set_y(lem.get_y()).to_edge(RIGHT))
        self.next_slide()


        ann = Tex("$F(\\alpha$) Sprungstelle unten").scale(0.7)
        self.play(Write(ann))
        self.next_slide()


        b1 = MathTex(r"\exists \varepsilon > 0")
        self.play(ann.animate.shift(UP), Write(b1))
        self.next_slide()


        b2 = MathTex(r"\exists \varepsilon > 0", r": \forall \delta > 0")
        self.play(TransformMatchingTex(b1, b2))
        self.next_slide()

        b3 = MathTex(r"\exists \varepsilon > 0", r": \forall \delta > 0", r": F(\alpha + \delta) - F(\alpha) > \epsilon")
        self.play(TransformMatchingTex(b2, b3))
        self.next_slide()

        st1 = MathTex(r"F(\delta + \beta + \alpha)", "+", r"F(\alpha)", r"\geq", r"F(\alpha + \beta)", "+", r"F(\alpha + \delta)")
        self.play( Unwrite(ann), run_time=0.5)
        self.play(b3.animate.scale(0.7).shift(UP), ReplacementTransform(lem.copy(), st1))
        self.next_slide()

        st2 = MathTex(r"F(\delta + \beta + \alpha)", "-", r"F(\alpha + \beta)", r"\geq", r"F(\alpha + \delta)", "-", r"F(\alpha)")
        self.play(TransformMatchingTex(st1, st2))
        self.next_slide()

        st3 = MathTex(r"F(\delta + \beta + \alpha)", "-", r"F(\alpha + \beta)", r"\geq", r"F(\alpha + \delta)", "-", r"F(\alpha)", "> \\varepsilon")
        self.play(TransformMatchingTex(st2, st3))
        self.next_slide()

        stc = Tex("$\\Rightarrow$ unstetig in allen $\\alpha + \\beta$").next_to(st3, DOWN)
        self.play(Write(stc))
        self.next_slide()

        ch2 = Tex("\\checkmark").scale(0.8).next_to(tar[1]).set_color(GREEN)
        self.play(stet.animate.set_color(GREEN), Write(ch2), tar[1].animate.set_color(WHITE))
        self.play(Unwrite(VGroup(stc, st3, b3)), run_time=0.7)
        self.next_slide()



        self.play(tar[2].animate.set_color(PINK))
        self.next_slide()

        konv = Tex("$F$ konvex").set_color(PINK)
        self.play(ReplacementTransform(tar[2].copy(), konv))
        self.next_slide()

        self.play(konv.animate.to_edge(RIGHT).set_y(lem.get_y()), stet.animate.scale(0.7).next_to(lem, 2*RIGHT))
        self.next_slide()

        ks = Tex(r"$f$ stetig, dann konvex $\iff 2 f \left( \frac{\alpha +\beta}{2} \right) =$", "$f(\\alpha) + f(\\beta)$")
        self.play(Write(ks))
        self.next_slide()

        k1 = MathTex(r"F \left(", r"\frac{\alpha - \beta}{2} + \frac{\alpha - \beta}{2} + \beta", r"\right)", "+", r"F(\beta)").scale(0.7)
        self.play(ks.animate.scale(0.7).shift(UP*1.2), ReplacementTransform(ks[1].copy(), k1))
        self.next_slide()

        self.play(k1.animate.shift(LEFT*2))
        k2 = MathTex(r"\geq", r"F \left( \frac{\alpha - \beta}{2} + \beta \right)", "+", r"F \left( \frac{\alpha - \beta}{2} + \beta \right)").scale(0.7).next_to(k1)
        self.play(Write(k2))
        self.next_slide()

        k3 = MathTex(r"\geq","2", r"F \left( \frac{\alpha - \beta}{2} + \beta \right)").scale(0.7).next_to(k1)
        self.play(TransformMatchingTex(k2, k3))
        self.next_slide()

        k4 = MathTex(r"\geq","2", r"F \left( \frac{\alpha + \beta}{2} \right)").scale(0.7).next_to(k1)
        self.play(TransformMatchingTex(k3, k4))
        self.next_slide()


        ch3 = Tex("\\checkmark").scale(0.8).next_to(tar[2]).set_color(GREEN)
        self.play(konv.animate.set_color(GREEN).scale(0.7).next_to(stet, RIGHT*2), Write(ch3), tar[2].animate.set_color(WHITE))
        self.play(Unwrite(VGroup(k4, k1, ks)), run_time=0.7)
        self.next_slide()

        
        kor = Tex("Korollar: ").shift(UP)
        self.play(Write(kor))
        self.next_slide()

        kor1 = MathTex(r"G \left[ \sum_{i=1}^{n}", "F_i", r"(", r"|\varphi_i(a_i) - \varphi_i(b_i)|)", "\\right]").to_edge(LEFT)
        self.play(TransformMatchingTex(s1.copy(), kor1))
        self.next_slide()

        kor2 = MathTex(r"G \left[ \sum_{i=1}^{n}", "F", r"(", "t_i", r"|\varphi_i(a_i) - \varphi_i(b_i)|)", "\\right]").to_edge(LEFT)
        self.play(TransformMatchingTex(kor1, kor2))
        self.next_slide()

        kor3 = MathTex(r"G \left[ \sum_{i=1}^{n}", "F", r"(", r"|\varphi_i(a_i) - \varphi_i(b_i)|)", "\\right]").to_edge(LEFT)
        self.play(TransformMatchingTex(kor2, kor3))
        self.next_slide()


        kor4 = MathTex("G^{-1}(", "t_i", "x", ")", "=", "F_i", "(x)").next_to(kor3, DOWN*2)
        self.play(Write(kor4))
        self.next_slide()

        kor45 = MathTex("G^{-1}(", "t_n", "x", ")", "=", "F_n", "(x)").next_to(kor3, DOWN*2)
        self.play(TransformMatchingTex(kor4, kor45))
        self.next_slide()

        kor5 = MathTex("G^{-1}(", "x", ")", "=", "F", "(x)").next_to(kor3, DOWN*2)
        self.play(TransformMatchingTex(kor45, kor5))
        self.next_slide()

        kor6 = MathTex("F^{-1}(", "x", ")", "=", "G", "(x)").next_to(kor3, DOWN*2)
        self.play(TransformMatchingTex(kor5, kor6))
        self.next_slide()


        kps = VGroup(kor6, kor3)

        korr = MathTex(r"F^{-1} \left[ \sum_{i=1}^{n}", "F", r"(", r"|\varphi_i(a_i) - \varphi_i(b_i)|)", "\\right]").next_to(kps, RIGHT*2)
        rr = SurroundingRectangle(korr, color=PINK, buff=MED_SMALL_BUFF)


        self.play(ReplacementTransform(kps.copy(), korr), Write(rr))
        self.next_slide()

        hinr = korr.copy()

        self.play(Unwrite(VGroup(ch1, ch2, ch3, s4, s3, s6, pf, tar, lem, stet, konv, rr, korr, kor, kps)))

        self.play(Transform(pline, alle))
        self.next_slide()


        ch3 = Tex("\\checkmark").next_to(alle[1]).set_color(GREEN)
        self.play(Write(ch3))
        self.next_slide()

        hinr.scale(0.7).to_edge(DOWN).set_x(0)
        self.play(Write(hinr))
        self.next_slide()

        ch4 = Tex("\\checkmark").next_to(alle[2]).set_color(GREEN)
        self.play(Write(ch4))


        #TODO: KLAsse umbennennen!!!


        # l = Line(start=LEFT*10, end=RIGHT*10, color=BLUE).shift(UP*2.5)
        #
        # self.play(ReplacementTransform(b1, l), Unwrite(ar, v2), vf.animate.scale(0.5).to_corner(UL))
        #
        # v2 = Tex("$\\langle A", "$\\succ", "$\\rangle$", "representable mit", "$\\delta$")
        # v4 = Tex("a, b, c")
