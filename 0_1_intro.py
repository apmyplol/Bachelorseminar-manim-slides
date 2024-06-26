from manim import *
from manim_slides import Slide

class Intro(Slide):
    def construct(self):
        # Load the SVG file
        svg_file = SVGMobject("intro.svg", use_svg_cache=False, width=14+2/9)

        inds = [0, 366, 1031, 1129, 1641, 2375, 3001, 3114, 4229, 4581, 4959, 5601, 5944, 6284, 6922, 7389, 7887, 8207, 8822, 9314, 9603, 9951, 10484, 10875, 11234, 11732, 12227, 12509, 12783, 13401, 15703, 17269, 17979, 18596]

        parts = [svg_file[inds[i] : inds[i+1]] for i in range(len(inds)-1)]


        for i in range(len(parts)):
            self.play(FadeIn(parts[i]))
            self.next_slide()

