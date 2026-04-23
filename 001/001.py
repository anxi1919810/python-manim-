from manim import *
import numpy as np

class gougu_law(Scene):
    def construct(self):
        title = Text("勾股定理", font="SimSun", color=YELLOW)
        self.play(Write(title), run_time=1.5)
        self.play(FadeOut(title), run_time=1)


        A = np.array([-9/5, 0, 0])
        B = np.array([16/5, 0, 0])
        C = np.array([0, 12/5, 0])

        scale = 0.5
        A = A * scale
        B = B * scale
        C = C * scale

        AB = Line(A, B)
        BC = Line(B, C)
        AC = Line(A, C)
        tri = Polygon(A, B, C, stroke_width=5, color=YELLOW, fill_opacity=0)
        self.play(Create(tri), run_time=1.5)

        def get_square_and_rotate_vec(line, color, thelt ,op):
            P1 = line.get_start()
            P2 = line.get_end()
            vec = P2 - P1
            vec1 = rotate_vector(vec, thelt * DEGREES)
            vec1 = vec1 / np.linalg.norm(vec1) * line.get_length()
            P3 = P2 + vec1
            P4 = P1 + vec1
            return (Polygon(P1, P2, P3 ,P4 , color=color, fill_opacity = op , stroke_width=5), vec1)
        
        sq_AB, AB_c= get_square_and_rotate_vec(AB,YELLOW, -90 ,0  )
        sq_BC, BC_c= get_square_and_rotate_vec(BC,PURPLE, -90 ,0.5) 
        sq_CA, CA_c= get_square_and_rotate_vec(AC,PURPLE , 90 ,0.5)
 
        self.play(Create(sq_AB), run_time=1.5)
        self.play(Create(sq_BC), run_time=1.5)
        self.play(Create(sq_CA), run_time=1.5)

        self.remove(tri)

        sq_BC_1, BC_c= get_square_and_rotate_vec(BC,PURPLE, -90 ,0) 
        sq_CA_1, CA_c= get_square_and_rotate_vec(AC,PURPLE , 90 ,0)

        A1 = A + CA_c
        B1 = B + BC_c
        C1 = C + BC_c
        C2 = C + CA_c
        
        A1C2 = Line (A1 , C2)
        B1C1 = Line (B1 , C1)
        
        def line_intersection(p1, p2, p3, p4):
            x1, y1 = p1[0], p1[1]
            x2, y2 = p2[0], p2[1]
            x3, y3 = p3[0], p3[1]
            x4, y4 = p4[0], p4[1]

            denom = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
            if denom == 0:
                return np.array([0,0,0])
            t_num = (x1 - x3)*(y3 - y4) - (y1 - y3)*(x3 - x4)
            t = t_num / denom
            x = x1 + t*(x2 - x1)
            y = y1 + t*(y2 - y1)
            return np.array([x, y, 0])

        P = line_intersection(A1, C2, B1, C1)
        C2P = Line(C2,P)
        C1P = Line(C1,P)
        self.play(Create(C2P),Create(C1P),run_time=1.5)

        trans_vec_C2=P-C2
        trans_vec_C1=P-C1

        new_A1= A1 + trans_vec_C2
        new_C2= P
        new_B1= B1 + trans_vec_C1
        new_C1= P
        
        trans_sq_AC = Polygon(A, C, new_C2, new_A1, color=PURPLE, fill_opacity=0.4, stroke_width=5)
        trans_sq_BC = Polygon(B, C, new_C1, new_B1, color=PURPLE, fill_opacity=0.4, stroke_width=5)

        self.play(Create(sq_CA_1),Create(sq_BC_1),run_time = 0.1)
        self.play(Transform(sq_CA,trans_sq_AC),Transform(sq_BC,trans_sq_BC),run_time=2)
        self.play(FadeOut(C1P),FadeOut(C2P),run_time = 0.5)

        hex = Polygon(A,new_A1,P,new_B1,B,C,color=PURPLE, stroke_width=5, fill_opacity = 0.5)
        self.add(hex)
        self.play(Uncreate(sq_CA),Uncreate(sq_BC),run_time = 1)
        
        D = sq_AB.get_vertices()[3]
        trans_vec_D = D - A
        A2 = A + trans_vec_D
        B2 = B + trans_vec_D
        C3 = C + trans_vec_D
        new_A1=new_A1 + trans_vec_D
        new_B1=new_B1 + trans_vec_D
        P = P + trans_vec_D

        hex1= Polygon(A2,new_A1,P,new_B1,B2,C3,color = PURPLE ,fill_opacity = 0.5)
        self.play(Transform(hex,hex1),run_time = 1.5)

        tri1 = Polygon(A,B,C,color = PURPLE ,fill_opacity = 0.5)
        trans_tri1 = Polygon(A2,B2,C3,color = PURPLE ,fill_opacity = 0.5)
        pent = Polygon(A2,new_A1,new_B1,B2,C3,color = PURPLE ,fill_opacity = 0.5)
        self.play(Create(tri1),Create(pent),run_time = 0.000001)
        self.play(Uncreate(hex),run_time = 1)
        self.play(Transform(tri1,trans_tri1),run_time = 1.5)
        self.wait(1)
        self.remove(pent)

        new_sq_AB = Polygon(A,B,B2,A2,color = PURPLE , fill_opacity = 0.5)
        self.add(new_sq_AB)
        self.play(Uncreate(tri1),run_time = 1)
        self.wait(1)

        self.play(FadeOut(new_sq_AB),
                  FadeOut(trans_tri1),
                  FadeOut(hex1),
                  FadeOut(sq_BC_1),
                  FadeOut(sq_CA_1),
                  FadeOut(sq_AB),
                  run_time = 2
                  )
        