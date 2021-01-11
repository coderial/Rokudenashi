init -100:

    define center = Position(xalign=0.5)
    define left = Position(xalign=0.15)
    define left_corner = Position(xalign=0.0,yalign=2.0)
    define right = Position(xalign=0.85)
    define bury = Position(xalign=0.15, yalign=8.0)
    define onHand = Position(xalign=0.5, yalign=0.35)

    transform goLeft:
        linear 0.7 xalign 0.15
    transform goCenter:
        linear 0.7 xalign 0.5

    transform LeftCorner_shake:
        yalign 2.0
        xpos 0
        linear 0.05 xpos 15
        linear 0.05 xpos 0
        linear 0.05 xpos 15
        linear 0.05 xpos 0
        linear 0.05 xpos 15
        linear 0.05 xpos 0
        linear 0.05 xpos 15
        linear 0.05 xpos 0

    transform ani_bow:
        linear 0.5 yalign 0.0
        linear 1.0 yalign 8.0


    transform left_backstep:
        linear 0.5 xalign 0.0

    transform Left_TreadOn:
        linear 0.5 xalign 0.15
        linear 0.5 xalign 0.2
        linear 0.5 xalign 0.15
        linear 0.5 xalign 0.2
        

    transform ani_harp_stand:
        yalign 8.0
        linear 1.0 yalign 4.0
            
    transform ani_stand:
        xalign 0.15
        yalign 4.0
        linear 1.0 yalign 2.0

define centered = Character(kind = centered, what_color = "#FFFFFF", what_outlines = [(1,"#000000")])

define glenn = Character('글렌',image = "ch_glenn", color="#FFFFFF")
define sistine = Character('시스티나',image = "ch_sistine", color="#FFFFFF")
define rumia = Character('루미아', image = "ch_rumia", color="#FFFFFF")
define celica = Character('세리카', image = "ch_celica", color="#FFFFFF")

define halley = Character('할리', image = "ch_halley")