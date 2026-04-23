from manim import *
import numpy as np

class Relationship_of_suanshu_and_pingjun(Scene):
    def construct(self):
        title = Text("算术平均数与几何平均数的关系", font_size=48, color=BLUE)
        self.play(Write(title), run_time=2)
        self.wait(2)
        self.play(FadeOut(title), run_time=1)

        inequality = MathTex(r"\sqrt{ab} \leq \frac{a+b}{2}", font_size=40, color=YELLOW)
        inequality.to_edge(DOWN, buff=1.5)
        self.play(Write(inequality), run_time=2)

        half_circle = Arc(radius=3, start_angle=0, angle=PI, stroke_width=8, color=WHITE).move_arc_center_to(ORIGIN + DOWN * 1)
        A = half_circle.get_start()
        B = half_circle.get_end()
        AB = Line(A, B, stroke_width=8, color=WHITE)
        self.play(Create(AB), run_time=2)
        self.play(Create(half_circle), run_time=2)

        O = AB.get_midpoint()
        r = half_circle.radius
        M = np.array([O[0],O[1] + r,0])
        OM = Line(O, M, color=YELLOW, stroke_width=6)
        self.play(Create(OM), run_time=1)
        avg_label = MathTex(r"\frac{a+b}{2}", font_size=40, color=YELLOW)
        avg_label.next_to(OM, RIGHT, buff=0.2)
        self.play(Write(avg_label), run_time=1)

        P = Dot(B, color=RED, radius=0.1)
        self.add(P)

        a_label = MathTex("a", font_size=36, color=WHITE)
        b_label = MathTex("b", font_size=36, color=WHITE)
        a_label.add_updater(lambda m: m.move_to((A + P.get_center())/2 + DOWN*0.3))
        b_label.add_updater(lambda m: m.move_to((P.get_center() + B)/2 + DOWN*0.3))
        self.add(a_label, b_label)

        H = np.array([P.get_center()[0], 0, 0])
        PH = Line(P.get_center(), P.get_center(), color=GREEN, stroke_width=5)
        geo_label = MathTex(r"\sqrt{ab}", font_size=40, color=GREEN)
        AH_dash = DashedLine(A, H, stroke_width=3, color=WHITE ,dash_length=0.2 ,dashed_ratio=0.5)
        BH_dash = DashedLine(B, H, stroke_width=3, color=WHITE ,dash_length=0.1 ,dashed_ratio=0.7)

        def update_PH(m):
            px = P.get_center()[0]
            hx = px
            dx = px - O[0]
            val = max( r**2 - dx**2 , 1e-12)
            hy = O[1] + np.sqrt(val)
            H = np.array([hx, hy, 0])
            m.put_start_and_end_on(P.get_center(), H)
            geo_label.move_to((P.get_center() + H)/2 + RIGHT*0.3)
            AH_dash.put_start_and_end_on(A, H)
            BH_dash.put_start_and_end_on(B, H)

        PH.add_updater(update_PH)
        self.add(AH_dash, BH_dash,PH, geo_label)
        self.play(P.animate.move_to(A), run_time=8, rate_func=linear)
        self.remove(geo_label,P)
        self.wait(2)


        self.play(FadeOut(inequality), 
                  FadeOut(AB), 
                  FadeOut(half_circle), 
                  FadeOut(OM), 
                  FadeOut(avg_label), 
                  FadeOut(PH), 
                  FadeOut(AH_dash), 
                  FadeOut(BH_dash),
                  FadeOut(a_label),
                  FadeOut(b_label),
                  run_time=3
                  )
