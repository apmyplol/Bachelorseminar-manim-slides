from manim import *
from manim_slides import Slide

class Quellen(Slide):
    def construct(self):
        quell = Tex("Quellen: ").to_corner(UL)
        self.play(Write(quell))
        self.next_slide()
        quels = BulletedList(r"Aczél, J. (Ed.). (1966). Lectures on functional equations and their applications. Academic press.",
                             r"Hardy, G. H., Littlewood, J. E., \& Pólya, G. (1952). Inequalities. Cambridge university press.",
                             r"H. P. Mulholland, On Generalizations of Minkowski’s Inequality in the Form of a Triangle Inequality, Proceedings of the London Mathematical Society, s2-51 (1949), pp. 294–307.",
                             r"Krantz, D. H., \& Tversky, A. (1975). Similarity of rectangles: An analysis of subjective dimensions. Journal of mathematical Psychology, 12(1), 4-34.",
                             r"Suppes, P. (2014). Foundations of Measurement: Volume 2 (Vol. 2). Elsevier.",
                             r"Krantz, D. H., \& Tversky, A. (1975). Similarity of rectangles: An analysis of subjective dimensions. Journal of mathematical Psychology, 12(1), 4-34.",
                             r"Breinbauer, I. (1976). Bernhard Orth: Einführung in die Theorie des Messens. Kohlhammer Verlag, Stuttgart/Berlin/Köln/Mainz 1974, 131 Seiten, 15, – DM (Kohlhammer Standards Psychologie, Basisbücher und Studientexte).. Vierteljahrsschrift für wissenschaftliche Pädagogik, 52(1), 106-107. https://doi.org/10.30965/25890581-05201016").scale(0.5).next_to(quell, DOWN, aligned_edge=LEFT)

        self.play(Write(quels))
        self.next_slide()
