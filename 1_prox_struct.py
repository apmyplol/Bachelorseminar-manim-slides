from manim import *
from manim_slides import Slide

class FactorialProximityStructure(Slide):
    def construct(self):

        SMenge = Tex("$A$ Stimulimenge")
        self.play(Write(SMenge))
        
        self.next_slide(notes="blabla")
        # Target text

        text2 = Tex("$a, b, c, d \\in$", "$A$ Stimulimenge")
        self.play(ReplacementTransform(SMenge, text2))
        self.next_slide()


        paare = Tex("$(a,b)$",  "$(c,d)$")
        paarv = Tex("$(a,b)$",  "$\\succsim$" , "$(c,d)$")
        paarf = Tex("$(a,b)$",  "$\\succsim$" , "$(c,d)$", "\\quad a \\& b unähnlicher als c \\& d")
        self.play(text2.animate.shift(UP), Write(paare))
        self.next_slide()


        self.play(ReplacementTransform(paare, paarv))
        self.next_slide()

        self.play(ReplacementTransform(paarv, paarf))
        self.next_slide()

        group = VGroup(text2, paarf)
        self.play(group.animate.shift(2.5*UP).scale(0.7))
        # Tex.set_default(font_size = 40)
        prox_struct = BulletedList(r"$\succsim$ zusammenhängend und transitiv",
                                    r"$(a, b) \succsim (a, a)$ wenn $a \neq b$",
                                    r"$(a, a) \sim (b, b)$ (Minimalität)",
                                    r"$(a, b) \sim (b, a)$ (Symmetrie)",
                                    r"factorial, wenn $A = \prod_{i=1}^{n} A_i$",
                                    height=2).to_edge(LEFT).shift(0.5*DOWN)

        self.play(Write(prox_struct))
        self.next_slide()
        
        fac_prox_struct = Tex(r"(fact.) proximity structure $\langle A, \succsim \rangle$", font_size=35, color=PURPLE_A).next_to(prox_struct, 0.5*UP)
        self.play(prox_struct.animate.scale(0.8), Write(fac_prox_struct))
        self.next_slide()

        metr_spc = Tex(r"$\langle A, \delta \rangle, \delta$ Metrik").to_edge(RIGHT).to_edge(UP).shift(0.5*LEFT)
        arrow = Arrow(start=LEFT, end=RIGHT, color=GREEN).next_to(metr_spc, LEFT)
        self.play(group.animate.to_edge(LEFT))
        self.play( Write(arrow), Write(metr_spc))
        self.next_slide()

        repr = Tex("representable", color=PURPLE_A).next_to(metr_spc, DOWN).shift(DOWN)
        self.play(Write(repr))
        self.next_slide()

        repr_cond = MathTex(r"\delta(a, b) &\geq \delta(c, d) \\ &\iff \\ (a, b) &\succsim (c, d)").next_to(repr, DOWN)
        self.play(Write(repr_cond))

        self.wait(2)
