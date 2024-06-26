from manim import *
from manim_slides import Slide

class lp_Defbereiche(Slide):
    def construct(self):
        # self.next_section(skip_animations=True)

        MathTex.set_default(font_size=30)
        Tex.set_default(font_size=30)
        BulletedList.set_default(buff=0.3)
        
        vor = BulletedList(r"$\langle A, \succsim \rangle$ vollständig, segmentally additive proximity structure und additive difference structure").shift(UP)

        ard = MathTex("\\Downarrow").next_to(vor, DOWN)

        folg1 = BulletedList(r"$(a, b) \succsim (c, d) \iff \delta(a, b) \geq \delta(c, d)$",
                             r"eindeutiges $r \geq 1$",
                             r"$\varphi_i$ reellwertig \& Verhältnisskala",
                             r"$\delta(a, b) = \left[\sum_{i=1}^{n} |\varphi_i(a) - \varphi_i(b)|^r\right]^{1/r}$"
                             ).next_to(ard, DOWN)
        self.play(Write(ard), Write(folg1), Write(vor), run_time=0.7)
        self.next_slide()


        vor2 = BulletedList(r"$\delta(a, b) = F^{-1} \left( \sum_{i=1}^{n} F \left( |\varphi_i(a_i) - \varphi_i(b_i)| \right) \right)$",
                           r"$\delta$ homogen: $\delta(x, x + t(z-x)) = t \delta(x,z)$, für $t > 0$"
                           ).shift(UP)
        self.play(ReplacementTransform(vor, vor2), ard.animate.next_to(vor2, DOWN))
        self.next_slide()


        folg2 = BulletedList(r"eindeutiges $r \geq 1$",
                             r"$\delta(a, b) = \left[\sum_{i=1}^{n} |\varphi_i(a) - \varphi_i(b)|^r\right]^{1/r}$"
                             ).next_to(ard, DOWN)
        self.play(TransformMatchingTex(folg1, folg2))
        self.next_slide()

        # sazz = VGroup(vor2, ard, folg2).arrange(RIGHT, buff=0.5)

        # self.play(sazz.animate.scale(0.7).to_corner(UL))
        self.play(vor2.animate.scale(0.7).to_corner(UL))
        self.play(ard.animate.rotate(PI/2).next_to(vor2))
        self.play(folg2.animate.scale(0.7).next_to(ard))
        self.play(Write(Line(start=LEFT*10, end=RIGHT*10, color=BLUE).shift(UP*2.3)))
        self.next_slide()


        steps0 = BulletedList("Definitionsbereich von $F$ erweitern",
                              "Funktionalgleichung für $F$ herleiten",
                              "Eindeutige Lösung zu dieser Gl. ist $x^r$")

        self.play(Write(steps0))
        self.next_slide()


        steps = BulletedList("$F$ erweitern", "GL Herleiten", "$x^r$ einzige Lsg").scale(0.7).to_corner(UR)
        self.play(ReplacementTransform(steps0, steps))
        self.next_slide()


        ## 1. step
        self.play(steps[0].animate.set_color(BLUE))
        self.next_slide()
        
        nl1 = UnitInterval(include_ticks=False).add_labels({0: "0", 0.3: Tex("$F_2$"), 0.5: Tex("$F_1$"), 1: Tex("$F_n$")})
        self.play(Write(nl1))
        self.next_slide()

        # nl1.
        omeg = LabeledDot(Tex("$\\omega$"), point=nl1.n2p(0.95), color=BLUE_E)
        self.play(Write(omeg))
        self.next_slide()

        self.play(VGroup(nl1, omeg).animate.shift(UP))
        self.next_slide()

        omeg_1 = LabeledDot(Tex("$\\omega_1$"), point=nl1.n2p(0.46), color=BLUE_E)
        omeg_2 = LabeledDot(Tex("$\\omega_2$"), point=nl1.n2p(0.26), color=BLUE_E)

        self.play(Write(omeg_1), Write(omeg_2))
        self.next_slide()


        f2 = MathTex(r"\omega_i = \omega / t_i")
        self.play(Write(f2))
        self.next_slide()


        f3 = MathTex(r"\omega_i = \omega/ t_i", r"\Rightarrow", r"F^{-1} \left[ \sum_{i=1}^{n} F_i(\omega_i) \right]").shift(DOWN)
        self.play(TransformMatchingTex(f2, f3))
        self.next_slide()


        f4  = MathTex(r"\omega_i =\omega / t_i", r"\Rightarrow", r"F^{-1} \left[ \sum_{i=1}^{n} F_i(\omega_i) \right]", r"= F^{-1} \left[ nF(\omega) \right]").shift(DOWN)
        self.play(TransformMatchingTex(f3, f4))
        self.next_slide()


        f5  = MathTex(r"\omega_i =\omega / t_i", r"\Rightarrow", r"F^{-1} \left[ \sum_{i=1}^{n} F_i(\omega_i) \right]", r"= F^{-1} \left[ nF(\omega) \right]", r"=:", r"\Omega").shift(DOWN)
        self.play(TransformMatchingTex(f4, f5))
        self.next_slide()


        self.play(f5.animate.shift(LEFT*2))
        f6 = Tex("F mindestens auf ", "$[0, \\Omega]$").next_to(f5, RIGHT)
        self.play(Write(f6))
        self.next_slide()

        f7 = MathTex(r"F^{-1} \left[ nF(\alpha) \right]").shift(DOWN*2)
        f8 = MathTex(r"F^{-1} \left[ nF(\alpha) \right]", "=", r"F^{-1} \left[ nF(", r"\alpha \cdot \frac{\omega}{\omega}", r") \right]").shift(DOWN*2)
        f9 = MathTex(r"F^{-1} \left[ nF(\alpha) \right]", "=", r"\frac{\alpha}{\omega}", r"F^{-1} \left[ nF(", r"\omega", r") \right]").shift(DOWN*2)
        f10 = MathTex(r"F^{-1} \left[ nF(\alpha) \right]", "=", r"\frac{\alpha}{\omega}", "\\Omega").shift(DOWN*2)


        self.play(Write(f7))
        self.next_slide()

        self.play(TransformMatchingTex(f7, f8))
        self.next_slide()
        
        self.play(TransformMatchingTex(f8, f9))
        self.next_slide()

        self.play(TransformMatchingTex(f9, f10))
        self.next_slide()

        # self.play(VGroup())

        self.play(Unwrite(VGroup(f5, omeg_1, omeg_2, omeg, nl1, f6)))
        self.next_slide()


        fa0 = MathTex(r"F^{-1} \left[ nF(", r"\alpha", r") \right]", "=",r"\alpha", r"\frac{\Omega}{\omega}").shift(UP*1.8)
        self.play(ReplacementTransform(f10, fa0))
        self.next_slide()


        fa = MathTex(r"F^{-1} \left[ nF(", r"\alpha \cdot \frac{\omega}{\Omega}", r") \right]", "=",r"\alpha", r"\cdot \frac{\omega}{\Omega}", r"\frac{\Omega}{\omega}").to_edge(LEFT)
        self.play(ReplacementTransform(fa0.copy(), fa))
        self.next_slide()

        fa1 = MathTex(r"F^{-1} \left[ nF(", r"\alpha \cdot \frac{\omega}{\Omega}", r") \right]", "=",r"\alpha").to_edge(LEFT)
        self.play(TransformMatchingTex(fa, fa1))
        self.next_slide()

        fa2 = MathTex(r" F(a) = nF(a \omega/\Omega)").next_to(fa1, DOWN)
        self.play(Write(fa2))
        self.next_slide()

        fab = MathTex(r"0 \leq \alpha \leq \Omega").next_to(fa2, DOWN)
        self.play(Write(fab))
        self.next_slide()

        
        fb1 = MathTex(r"F^{-1} \left[", r" nF( F^{-1}(\alpha/n) ) ", r"\right]=", r" F^{-1}(\alpha / n) ", r"\frac{\Omega}{\omega}").to_edge(RIGHT)
        self.play(ReplacementTransform(fa0.copy(), fb1))
        self.next_slide()

        fb2 = MathTex(r"F^{-1} \left[", r" n \alpha/n", r" \right]= ", r"F^{-1}(\alpha / n) ", r"\frac{\Omega}{\omega}").to_edge(RIGHT)
        self.play(TransformMatchingTex(fb1, fb2))
        self.next_slide()

        fb3 = MathTex(r"F^{-1} \left[", r"\alpha ", r"\right]= ", r"F^{-1}(\alpha / n) ", r"\frac{\Omega}{\omega}").to_edge(RIGHT)
        self.play(TransformMatchingTex(fb2, fb3))
        self.next_slide()

        fbb = MathTex(r"0 \leq a \leq nF(\omega)").next_to(fb3, DOWN)
        self.play(Write(fbb))
        self.next_slide()

        fbbg = VGroup(fb3, fbb)


        self.play(Unwrite(fa1), VGroup(fab, fa2).animate.shift(UP*2.5), fbbg.animate.shift(UP*1.8))
        self.play(fa2.animate.set_color(PINK), fb3.animate.set_color(ORANGE) )
        self.next_slide()


        self.play(fab.animate.scale(0.8).shift(LEFT))
        self.next_slide()


        fabb = MathTex(r"0 \leq a \leq", r"\Omega^2/\omega").scale(0.8).next_to(fab, RIGHT*2.5)
        self.play(Write(fabb))
        self.next_slide()


        self.play(fbb.animate.scale(0.8).shift(LEFT))
        self.next_slide()

        fbbb = MathTex(r"0 \leq a \leq", r"nF(\Omega)").scale(0.8).next_to(fbb, RIGHT*2)
        self.play(Write(fbbb))
        self.next_slide()

        fbbb1 = MathTex(r"0 \leq a \leq", r"n^2F(\omega)").scale(0.8).next_to(fbb, RIGHT*2)
        self.play(TransformMatchingTex(fbbb, fbbb1))
        self.next_slide()


        self.play(Unwrite(fbb), Unwrite(fab), fbbb1.animate.next_to(fb3, DOWN), fabb.animate.next_to(fa2, DOWN))
        fbbg.remove(fbb)
        self.next_slide()


        self.play(Unwrite(fa0))
        self.play(VGroup(fb3, fbbb1).animate.next_to(fab, DOWN, aligned_edge=LEFT))
        self.next_slide()



        hom0 = Tex(r"Homogenität für ", r"$t \cdot \alpha_i \leq \omega$").shift(UP*2)
        self.play(Write(hom0))
        self.next_slide()

        hom11 = MathTex(r"F^{-1} \left[ \sum_{i=1}^{n} F(t \alpha_i) \right]").scale(0.8).shift(UP*1.3)
        self.play(Write(hom11))
        self.next_slide()
        
        hom0a = Tex(r"Homogenität für ", r"$t \cdot \alpha_i \leq \omega$", r"$\rightarrow$", r"$t \cdot \alpha_i \leq \Omega$:").shift(UP*2)
        self.play(TransformMatchingTex(hom0, hom0a))
        self.play(hom0a[3].animate.set_color(YELLOW))


        hom1 = MathTex(
            r"=", r"F^{-1} \left[", r"\sum_{i=1}^{n}", r"n", r"F(t \alpha_i \omega \backslash \Omega) \right]"
        ).scale(0.8)
        hom3 = MathTex(
            r"=", r"\frac{\Omega}{\omega} F^{-1} \left[ \sum_{i=1}^{n} F(t \alpha_i \omega \backslash \Omega) \right]"
        ).scale(0.8)
        hom4 = MathTex(
            r"=", r" \frac{\Omega}{\omega} t F^{-1} \left[ \sum_{i=1}^{n} F(\alpha_i \omega \backslash \Omega) \right]"
        ).scale(0.8)
        hom5 = MathTex(
            r"=", r" t F^{-1} \left[", "n", r" \sum_{i=1}^{n}", r"F(\alpha_i \omega \backslash \Omega) \right]"
        ).scale(0.8)
        hom7 = MathTex(
            r"=", r" t F^{-1} \left[ \sum_{i=1}^{n} F(\alpha_i) \right]"
        ).scale(0.8)

        # Arrange homuations
        homeqs = VGroup(hom1, hom3, hom4, hom5, hom7).arrange(DOWN, aligned_edge=LEFT).next_to(hom11, aligned_edge=UP)
        hom2 = MathTex(
            r"=", r" F^{-1} \left[", "n", r"\sum_{i=1}^{n}", r"F(t \alpha_i \omega \backslash \Omega) \right]"
        ).scale(0.8).move_to(hom1)
        hom6 = MathTex(
            r"=", r" t F^{-1} \left[", r" \sum_{i=1}^{n}", "n", r"F(\alpha_i \omega \backslash \Omega) \right]"
        ).scale(0.8).move_to(hom5)
        hom1[0].set_color(PINK).scale(1.2)
        hom2[0].set_color(PINK).scale(1.2)
        hom3[0].set_color(ORANGE).scale(1.2)
        hom5[0].set_color(ORANGE).scale(1.2)
        hom6[0].set_color(ORANGE).scale(1.2)
        hom7[0].set_color(PINK).scale(1.2)

        self.play(Write(hom1))
        self.next_slide()

        self.play(TransformMatchingTex(hom1, hom2))
        self.next_slide()
        
        self.play(Write(hom3))
        self.next_slide()

        self.play(Write(hom4))
        self.next_slide()

        self.play(Write(hom5))
        self.next_slide()

        self.play(TransformMatchingTex(hom5, hom6))
        self.next_slide()

        self.play(Write(hom7))
        self.next_slide()
        

        verg = Tex("$\\Rightarrow$ Vergrößerung um Faktor $\\Omega \\over \\omega$").next_to(hom0a, RIGHT)
        self.play(hom0a[2].animate.set_color(GREEN), Write(verg))
        self.next_slide()


        hom0b = Tex(r"Homogenität für ", r"$0 \leq \alpha_i \leq \infty$").scale(0.8).move_to(hom0a)
        self.play(Unwrite(VGroup(hom2, hom3, hom4, hom6)), run_time=0.7)
        self.play(hom7.animate.next_to(hom11, RIGHT))
        self.next_slide()


        fabb1 = MathTex(r"0 \leq a \leq", r"\infty").scale(0.8).move_to(fabb)
        fbbb2 = MathTex(r"0 \leq a \leq", r"\infty").scale(0.8).move_to(fbbb1)
        self.play(Unwrite(verg), steps[0].animate.set_color(WHITE))
        self.next_slide()


        self.play(TransformMatchingTex(fabb, fabb1), TransformMatchingTex(fbbb1, fbbb2))
        fbbg.add(fbbb2)
        self.next_slide()


        homg = VGroup(hom11, hom7)
        self.play(TransformMatchingTex(hom0a, hom0b), homg.animate.next_to(hom0b, DOWN).scale(0.8))
        self.play(fbbg.animate.next_to(VGroup(homg, hom0b), RIGHT*2))
        self.next_slide()


        erw_check = Tex("\\checkmark", color=GREEN).next_to(steps[0], RIGHT)
        self.play(Write(erw_check))
        self.next_slide()

        ######## Nächster Teil
        self.play(steps[1].animate.set_color(BLUE))
        self.next_slide()

        homgg = MathTex(r"F^{-1} \left[ \sum_{i=1}^{n} F(t \alpha_i) \right]", "=", r"t F^{-1} \left[ \sum_{i=1}^{n} F(\alpha_i) \right]")
        self.play(Write(homgg))
        self.next_slide()


        homgg1 = MathTex(r"\Omega / \omega", r"F^{-1} \left[ \frac{1}{n} \sum_{i=1}^{n} F(t \alpha_i) \right]", "=", r"F^{-1} \left[ \sum_{i=1}^{n} F(t \alpha_i) \right]", "=", r"t F^{-1} \left[ \sum_{i=1}^{n} F(\alpha_i) \right]")
        homgg1[2].set_color(ORANGE).scale(1.4)
        self.play(TransformMatchingTex(homgg, homgg1))
        self.next_slide()


        homgg2 = MathTex(r"\Omega / \omega", r"F^{-1} \left[ \frac{1}{n} \sum_{i=1}^{n} F(t \alpha_i) \right]", "=", r"F^{-1} \left[ \sum_{i=1}^{n} F(t \alpha_i) \right]", "=", r"t F^{-1} \left[ \sum_{i=1}^{n} F(\alpha_i) \right]", "=", r"\Omega / \omega", r"tF^{-1} \left[ \frac{1}{n} \sum_{i=1}^{n} F(\alpha_i) \right]")
        homgg2[2].set_color(ORANGE).scale(1.4)
        homgg2[6].set_color(ORANGE).scale(1.4)
        self.play(TransformMatchingTex(homgg1, homgg2))
        self.next_slide()

        # self.next_section()

        homgg3 = MathTex(r"\Omega / \omega", r"F^{-1} \left[ \frac{1}{n} \sum_{i=1}^{n} F(t \alpha_i) \right]", "=",  r"\Omega / \omega", r"tF^{-1} \left[ \frac{1}{n} \sum_{i=1}^{n} F(\alpha_i) \right]")
        self.play(TransformMatchingTex(homgg2, homgg3))
        self.next_slide()

        homgg4 = MathTex(r"F^{-1} \left[ \frac{1}{n} \sum_{i=1}^{n} F(t \alpha_i) \right]", "=", r"tF^{-1} \left[ \frac{1}{n} \sum_{i=1}^{n} F(\alpha_i) \right]")
        self.play(TransformMatchingTex(homgg3, homgg4))
        self.next_slide()

        ard = MathTex(r"\Downarrow").next_to(homgg4, DOWN)
        aczel = Tex(r"Aczel: $\uparrow$ Gleichung für $\alpha_i, t \in [0, \infty)$, steigend, $F(0) = 0$. Dann einzige Lösung: $k\alpha^r$").next_to(ard, DOWN)
        bord = SurroundingRectangle(aczel, color=BLUE, buff=MED_SMALL_BUFF)
        self.play(Write(ard), Write(aczel), Write(bord))
        self.next_slide()

        arr = Tex(r"$\Rightarrow F$ mind. auf $[0, \Omega]$ gleich $k \alpha^r$").next_to(bord, DOWN, aligned_edge=LEFT)
        self.play(Write(arr))
        self.next_slide()


        gl_check = Tex("\\checkmark", color=GREEN).next_to(steps[1], RIGHT)
        self.play(Write(gl_check), steps[1].animate.set_color(WHITE))
        self.next_slide()

        self.play(Unwrite(VGroup(aczel, bord, ard, homgg4, fbbg, homg, hom0b, fabb1, fa2)))
        self.play(arr.animate.move_to(fa2, aligned_edge=LEFT))
        self.next_slide()

        ######### Letzter Teil


        self.play(steps[2].animate.set_color(BLUE))
        self.next_slide()

        vor = MathTex(r"\forall |\varphi_i(a_i) - \varphi_i(b_i)| \exists t > 0: \quad t|\varphi_i(a_i) - \varphi_i(b_i)| < \omega").next_to(arr, RIGHT)
        self.play(Write(vor))
        self.next_slide()

        part1 = MathTex(r"\delta(a, b)").to_edge(LEFT)

        part2 = MathTex("=", r"F^{-1} \left( \sum_{i=1}^{n} F \left(", r"|\varphi_i(a_i) - \varphi_i(b_i)| \right) \right)")


        part4 = MathTex("=", r"\frac{1}{t}", r"\left( \sum_{i=1}^{n}", r" \left(", "tk", r"|\varphi_i(a_i) - \varphi_i(b_i)| \right)", "^r", r"\right)", r"^{1/r}")
        part6 = MathTex("=", "k", r"\left( \sum_{i=1}^{n} |\varphi_i(a_i) - \varphi_i(b_i)|^r \right)^{1/r}")

        proof_parts = VGroup(part2, part4).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(part1, RIGHT, aligned_edge=UP).shift(0.25*UP)

        part3 = MathTex("=", r"\frac{1}{t}", r"F^{-1}", r"\left( \sum_{i=1}^{n}", "F", r"\left(", "t", r"|\varphi_i(a_i) - \varphi_i(b_i)| \right)", r"\right)").move_to(part2, aligned_edge=LEFT)
        part5 = MathTex("=", r"\frac{1}{t}", r"tk", r"\left( \sum_{i=1}^{n}", r" \left(", r"|\varphi_i(a_i) - \varphi_i(b_i)| \right)", "^r", r"\right)", r"^{1/r}").move_to(part4, aligned_edge=LEFT)
        part6 = MathTex("=", "k", r"\left( \sum_{i=1}^{n}", r" \left(", r"|\varphi_i(a_i) - \varphi_i(b_i)| \right)", "^r", r"\right)", r"^{1/r}").move_to(part5, aligned_edge=LEFT)

        self.play(Write(part1))
        self.next_slide()

        self.play(Write(part2))
        self.next_slide()

        self.play(TransformMatchingTex(part2, part3))
        self.next_slide()

        self.play(Write(part4))
        self.next_slide()

        self.play(TransformMatchingTex(part4, part5))
        self.next_slide()

        self.play(TransformMatchingTex(part5, part6))
        self.next_slide()

        fin = Tex(r"$\Rightarrow F(\alpha) = k \alpha^r$ für alle $\alpha$, also $F$ ist Verhältnisskala").next_to(proof_parts, DOWN, aligned_edge=LEFT)
        self.play(Write(fin))
        self.next_slide()

        fin_check = Tex("\\checkmark", color=GREEN).next_to(steps[2], RIGHT)
        self.play(Write(fin_check), steps[2].animate.set_color(WHITE))

