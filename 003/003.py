from manim import *
import numpy as np
class cosine_law(Scene):
    def construct(self):
        title = Text("余弦定理", font_size = 48, color=BLUE)
        self.play(Write(title), run_time=2)
        self.wait(2)
        self.play(FadeOut(title), run_time=1)

        O = np.array([0, 0, 0])
        A = np.array([0, 3, 0])
        B = np.array([4, 0, 0])
        C = np.array([-2, 0, 0])

        A = A * 0.5
        B = B * 0.5
        C = C * 0.5

        tri = Polygon(A, B, C, color=WHITE)
        self.play(Create(tri), run_time=2)
        
        OA = Line(O, A, color=YELLOW, stroke_width=6)
        OA_dash = DashedLine(O, A, color=YELLOW, stroke_width=6)
        self.play(Create(OA_dash), run_time=1)

        right_angle = RightAngle(Line(O, A), Line(O, B), length=0.3, color=WHITE)
        self.play(Create(right_angle), run_time=1.5)

        def sq(line, color, thelt ,op):
            P1 = line.get_start()
            P2 = line.get_end()
            vec = P2 - P1
            vec1 = rotate_vector(vec, thelt * DEGREES)
            vec1 = vec1 / np.linalg.norm(vec1) * line.get_length()
            P3 = P2 + vec1
            P4 = P1 + vec1
            return Polygon(P1, P2, P3 ,P4 , color=color, fill_opacity = op , stroke_width=5)
        
        sq_AB = sq(Line(A, B), YELLOW, 90 ,0.5)
        sq_AC = sq(Line(A, C), RED, -90 ,0)
        sq_BC = sq(Line(B, C), GREEN, 90 ,0)
        self.play(Create(sq_AB), run_time=1.5)
        self.play(Create(sq_AC), run_time=1.5)
        self.play(Create(sq_BC), run_time=1.5)

        def get_topline(sq):
            q1 = sq.get_vertices()[2]
            q2 = sq.get_vertices()[3]
            return Line(q1, q2, color=WHITE, stroke_width=5)
        topline_AB = get_topline(sq_AB)
        topline_AC = get_topline(sq_AC)
        topline_BC = get_topline(sq_BC)

        a_label = MathTex("a", color=GREEN)
        b_label = MathTex("b", color=RED)
        c_label = MathTex("c", color=YELLOW)
        c_label.move_to(topline_AB.get_center()+ 0.25* UP)
        a_label.move_to(topline_BC.get_center() + 0.25* DOWN)
        b_label.move_to(topline_AC.get_center() + 0.25* UP)
        self.play(Write(a_label), Write(b_label), Write(c_label), run_time=1.5)

        sq_OB = sq(Line(B, O), GREEN, 90 ,0.5)
        self.play(Create(sq_OB), run_time=1.5)

        def angle_between(v1, v2):
            u1 = v1 / np.linalg.norm(v1)
            u2 = v2 / np.linalg.norm(v2)
            angle = np.arccos(np.clip(np.dot(u1, u2), -1.0, 1.0))
            return angle

        theta = angle_between(A - C, A - O)
        theta_label = MathTex(r"\theta")
        theta_label.move_to(C + 0.5 * RIGHT + 0.25 * UP)
        self.play(Write(theta_label), run_time=1.5) 

        b_cos_theta = MathTex(r"b \cos \theta", color=WHITE, font_size=22)
        b_cos_theta.move_to(Line(C, O).get_center() + 0.25 * DOWN)
        self.play(Write(b_cos_theta), run_time=1.5)



        phi = angle_between(A - O, A - C)
        AO1 = OA.animate.rotate(-phi, about_point=A)
        self.play(AO1,  run_time=1.5)

        sq_OA1 = sq(OA, RED, 90 ,0.5)
        self.play(Create(sq_OA1), run_time=1.5)

        b_sin_theta = MathTex(r"b \sin \theta", color=WHITE, font_size=22) 
        b_sin_theta.move_to(OA.get_center() + 0.15 * UP + 0.15 *LEFT)
        b_sin_theta.rotate(OA.get_angle())
        self.play(Write(b_sin_theta), run_time=1.5)

        self.play(FadeOut(sq_BC),
                  FadeOut(a_label), 
                  FadeOut(sq_AC), 
                  FadeOut(b_cos_theta), 
                  FadeOut(b_sin_theta), 
                  FadeOut(theta_label),
                  FadeOut(b_label),
                  FadeOut(c_label),
                  run_time=1.5
                  )
        self.play(FadeOut(tri),FadeOut(OA),run_time = 0.5)

        sq_OA2 = sq_OA1.animate.rotate(phi, about_point=A)
        self.play(sq_OA2,  run_time=1.5)
        self.play(FadeOut(OA_dash), run_time=0.5)

        S_OA_label = MathTex(r"(b\sin\theta)^2", color=WHITE, font_size=25)
        S_OA_label.move_to(sq_OA1.get_center() )
        S_OB_label = MathTex(r"(a - b\cos\theta)^2", color=WHITE, font_size=25)
        S_OB_label.move_to(sq_OB.get_center() )
        S_OA_label_AB_label = MathTex(r"c^2", color=WHITE, font_size=25)
        S_OA_label_AB_label.move_to(sq_AB.get_center() )
        self.play(Write(S_OA_label), Write(S_OB_label), Write(S_OA_label_AB_label), run_time=1.5)

        eq = MathTex(r"c^2 &= (b\sin\theta)^2 + (a - b\cos\theta)^2 \\",r"&= a^2 + b^2 - 2ab\cos\theta",color=WHITE,font_size=36)
        eq.move_to(2.6 * DOWN)
        self.play(Write(eq), run_time=2)
        self.wait(2)

        self.play(FadeOut(S_OA_label),
                  FadeOut(S_OB_label),
                  FadeOut(S_OA_label_AB_label),
                  FadeOut(eq),
                  FadeOut(sq_OA1),
                  FadeOut(sq_OB),
                  FadeOut(sq_AB),
                  FadeOut(right_angle),
                  run_time=1.5
                  )