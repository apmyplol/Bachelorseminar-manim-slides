from manim import *
from manim_slides import Slide

class RecapInhalt567(MovingCameraScene, Slide):
    def construct(self):
        # Load the SVG file
        self.camera.frame.save_state()
        svg_file = SVGMobject("2_inhalt.svg", use_svg_cache=False, height=7)

        lp_metr_ind =150+151+1538+465 - 1
        hinr_notw_ind = lp_metr_ind + 384 + 200 + 88 + 168 + 661 + 283 + 1542
        add_diff_ps_ind = hinr_notw_ind + 125 + 409 + 481 + 1214
        seg_add_metric_satz_ind = add_diff_ps_ind + 233 + 157 + 333 + 427 + 415 +105 + 103 + 809
        seg_solv_ind = seg_add_metric_satz_ind + 2334
        add_dif_model_seg_add_metr_ind = seg_solv_ind + 572 + 416 + 1379 + 100
        represent_ind = add_dif_model_seg_add_metr_ind + 1129
        prox_struct_ind = represent_ind + 1006
        intro_ind = prox_struct_ind + 2823

        inds = [intro_ind, prox_struct_ind, represent_ind, add_dif_model_seg_add_metr_ind, seg_solv_ind, seg_add_metric_satz_ind, add_diff_ps_ind, hinr_notw_ind, lp_metr_ind, 0]

        parts = [svg_file[inds[i+1] : inds[i]] for i in range(len(inds)-1)]

        self.play(FadeIn(VGroup(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])))
        self.next_slide()



        skalen = BulletedList("Nominal: $f$ bijektiv",
                              "Ordinal: $f$ steigend",
                              "Intervall.: $f(x) = ax + b, a > 0$",
                              "Verhältnis.: $f(x) = ax, a > 0$")
        skalen.set(height = parts[0].height*0.5).next_to(parts[0], LEFT, aligned_edge=UP).shift(0.3*DOWN)

        part1 = SurroundingRectangle(VGroup(parts[0], skalen))

        self.play(self.camera.frame.animate.move_to(part1).set(width = part1.width*1.2))
        self.next_slide()

        self.play(Write(skalen))
        self.next_slide()


        prox_str = MathTex(r"\langle A = \prod A_i, \succsim \rangle").set(width = parts[1].width* 0.3).next_to(parts[1], DOWN).shift(0.2*LEFT)
        part2 = SurroundingRectangle(VGroup(parts[1], prox_str))

        self.play(self.camera.frame.animate.move_to(part2).set(width = part2.width*1.4))
        self.next_slide()

        self.play(Write(prox_str))
        self.next_slide()


        reprable = MathTex(r"\delta(a, b) &\geq \delta(c, d) \\ &\iff \\ (a, b) &\succsim (c, d)").set(width=parts[2].width * 0.8).next_to(parts[2], UP)
        part3 = SurroundingRectangle(VGroup(parts[2], reprable))

        self.play(self.camera.frame.animate.move_to(part3))
        self.next_slide()

        self.play(Write(reprable))
        self.next_slide()


        add_d_model = MathTex(r"G \left \{ \sum_{i=1}^{n} F_i[ | \varphi_i(a_i) - \varphi_i(b_i)| ] \right \}").set(width=parts[3].width*0.4).next_to(parts[3], RIGHT).shift(UP*2).shift(LEFT)
        add_d_model_sp_case = MathTex(r"\rightarrow \quad F^{-1} \left \{ \sum_{i=1}^{n} F[ | \varphi_i(a_i) - \varphi_i(b_i)| ] \right \}").set(width=add_d_model.width).next_to(add_d_model, RIGHT)
        bsps = BulletedList(r"$l^p: F(x) = x^p$", 
                               r"p-exp: $F(t) = q \cdot (e^{t \cdot r} - 1)^p$").set(width=add_d_model_sp_case.width).next_to(add_d_model_sp_case, DOWN)


        self.play(self.camera.frame.animate.shift(4*RIGHT).scale(1.3))
        self.next_slide()

        self.play(Write(add_d_model))
        self.next_slide()

        self.play(Write(add_d_model_sp_case))
        self.next_slide()

        self.play(Write(bsps))
        self.next_slide()

        self.play(Restore(self.camera.frame))
        self.next_slide()

        self.play(FadeIn(VGroup(parts[6], parts[7])))
        self.next_slide()




class Inhalt012(Slide):
    def construct(self):
        # Load the SVG file
        svg_file = SVGMobject("2_inhalt.svg", use_svg_cache=False, height=7)

        lp_metr_ind =150+151+1538+465 - 1
        hinr_notw_ind = lp_metr_ind + 384 + 200 + 88 + 168 + 661 + 283 + 1542
        add_diff_ps_ind = hinr_notw_ind + 125 + 409 + 481 + 1214
        seg_add_metric_satz_ind = add_diff_ps_ind + 233 + 157 + 333 + 427 + 415 +105 + 103 + 809
        seg_solv_ind = seg_add_metric_satz_ind + 2334
        add_dif_model_seg_add_metr_ind = seg_solv_ind + 572 + 416 + 1379 + 100
        represent_ind = add_dif_model_seg_add_metr_ind + 1129
        prox_struct_ind = represent_ind + 1006
        intro_ind = prox_struct_ind + 2823

        inds = [intro_ind, prox_struct_ind, represent_ind, add_dif_model_seg_add_metr_ind, seg_solv_ind, seg_add_metric_satz_ind, add_diff_ps_ind, hinr_notw_ind, lp_metr_ind, 0]

        parts = [svg_file[inds[i+1] : inds[i]] for i in range(len(inds)-1)]

        self.play(FadeIn(VGroup(parts[0])))
        self.next_slide()
        self.play(FadeIn(VGroup(parts[1], parts[2])))
        self.next_slide()



class Inhalt2345(Slide):
    def construct(self):
        # Load the SVG file
        svg_file = SVGMobject("2_inhalt.svg", use_svg_cache=False, height=7)

        lp_metr_ind =150+151+1538+465 - 1
        hinr_notw_ind = lp_metr_ind + 384 + 200 + 88 + 168 + 661 + 283 + 1542
        add_diff_ps_ind = hinr_notw_ind + 125 + 409 + 481 + 1214
        seg_add_metric_satz_ind = add_diff_ps_ind + 233 + 157 + 333 + 427 + 415 +105 + 103 + 809
        seg_solv_ind = seg_add_metric_satz_ind + 2334
        add_dif_model_seg_add_metr_ind = seg_solv_ind + 572 + 416 + 1379 + 100
        represent_ind = add_dif_model_seg_add_metr_ind + 1129
        prox_struct_ind = represent_ind + 1006
        intro_ind = prox_struct_ind + 2823

        inds = [intro_ind, prox_struct_ind, represent_ind, add_dif_model_seg_add_metr_ind, seg_solv_ind, seg_add_metric_satz_ind, add_diff_ps_ind, hinr_notw_ind, lp_metr_ind, 0]

        parts = [svg_file[inds[i+1] : inds[i]] for i in range(len(inds)-1)]

        self.play(FadeIn(VGroup(parts[0], parts[1], parts[2])))
        self.next_slide()
        self.play(FadeIn(VGroup(parts[3], parts[4], parts[5])))
        self.next_slide()

class Inhalt567(Slide):
    def construct(self):
        # Load the SVG file
        svg_file = SVGMobject("2_inhalt.svg", use_svg_cache=False, height=7)

        lp_metr_ind =150+151+1538+465 - 1
        hinr_notw_ind = lp_metr_ind + 384 + 200 + 88 + 168 + 661 + 283 + 1542
        add_diff_ps_ind = hinr_notw_ind + 125 + 409 + 481 + 1214
        seg_add_metric_satz_ind = add_diff_ps_ind + 233 + 157 + 333 + 427 + 415 +105 + 103 + 809
        seg_solv_ind = seg_add_metric_satz_ind + 2334
        add_dif_model_seg_add_metr_ind = seg_solv_ind + 572 + 416 + 1379 + 100
        represent_ind = add_dif_model_seg_add_metr_ind + 1129
        prox_struct_ind = represent_ind + 1006
        intro_ind = prox_struct_ind + 2823

        inds = [intro_ind, prox_struct_ind, represent_ind, add_dif_model_seg_add_metr_ind, seg_solv_ind, seg_add_metric_satz_ind, add_diff_ps_ind, hinr_notw_ind, lp_metr_ind, 0]

        parts = [svg_file[inds[i+1] : inds[i]] for i in range(len(inds)-1)]

        self.play(FadeIn(VGroup(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])))
        self.next_slide()
        self.play(FadeIn(VGroup(parts[6], parts[7])))
        self.next_slide()

