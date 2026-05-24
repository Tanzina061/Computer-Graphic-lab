import turtle
import random

# ---------------- SCREEN ----------------
screen = turtle.Screen()
screen.setup(1000, 650)
screen.bgcolor("lightblue")
screen.title("Ball Sort Puzzle - Simple Levels")

screen.tracer(0, 0)

drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed(0)

tube_x = [-350, -170, 10, 190, 370]

tubes = []
selected_tube = None

level = 1
max_level = 10

# ---------------- COLORS ----------------
color_pool = ["red", "blue", "green", "yellow", "purple", "orange"]

# ---------------- LEVEL GENERATOR (ALL SAME STYLE) ----------------
def generate_level(lv):
    global tubes, selected_tube

    selected_tube = None

    # same structure every level
    colors = color_pool[:4]   # FIXED SAME EVERY LEVEL

    balls = []
    for c in colors:
        balls += [c] * 4   # each color = 4 balls

    random.shuffle(balls)

    tubes = [[] for _ in range(5)]

    idx = 0
    for b in balls:
        tubes[idx].append(b)
        idx = (idx + 1) % 4

    tubes[4] = []

# ---------------- DRAW ----------------
def draw_game():

    drawer.clear()

    drawer.penup()
    drawer.goto(0, 270)
    drawer.color("darkblue")
    drawer.write(
        f"BALL SORT PUZZLE - LEVEL {level}",
        align="center",
        font=("Arial", 26, "bold")
    )

    for i in range(5):

        x = tube_x[i]

        drawer.color("yellow" if selected_tube == i else "white")

        drawer.pensize(6)
        drawer.penup()
        drawer.goto(x, -180)
        drawer.setheading(90)
        drawer.pendown()
        drawer.forward(260)
        drawer.right(90)
        drawer.forward(70)
        drawer.right(90)
        drawer.forward(260)

        y = -150
        for c in tubes[i]:
            drawer.penup()
            drawer.goto(x + 35, y)
            drawer.dot(50, c)
            y += 55

    if check_win():
        drawer.penup()
        drawer.goto(0, -280)
        drawer.color("darkgreen")

        if level < max_level:
            drawer.write(
                "CLICK TO NEXT LEVEL",
                align="center",
                font=("Arial", 20, "bold")
            )
        else:
            drawer.write(
                "YOU WIN ALL 10 LEVELS 🎉",
                align="center",
                font=("Arial", 24, "bold")
            )

    screen.update()

# ---------------- MOVE RULE ----------------
def can_move(from_tube, to_tube):

    if len(tubes[from_tube]) == 0:
        return False

    if len(tubes[to_tube]) >= 4:
        return False

    return True

# ---------------- WIN CHECK ----------------
def check_win():

    for t in tubes:

        if len(t) == 0:
            continue

        if len(t) != 4:
            return False

        if len(set(t)) != 1:
            return False

    return True

# ---------------- CLICK ----------------
def click_handler(x, y):
    global selected_tube, level

    clicked = None

    for i in range(5):
        if tube_x[i] < x < tube_x[i] + 80:
            clicked = i
            break

    if clicked is None:
        return

    # NEXT LEVEL
    if check_win():
        if level < max_level:
            level += 1
            generate_level(level)
            draw_game()
        return

    # SELECT FIRST
    if selected_tube is None:
        if len(tubes[clicked]) > 0:
            selected_tube = clicked
        draw_game()
        return

    # CANCEL
    if selected_tube == clicked:
        selected_tube = None
        draw_game()
        return

    # MOVE
    if can_move(selected_tube, clicked):

        ball = tubes[selected_tube].pop()
        tubes[clicked].append(ball)

    selected_tube = None
    draw_game()

# ---------------- START ----------------
generate_level(level)
draw_game()

screen.onclick(click_handler)
screen.mainloop()