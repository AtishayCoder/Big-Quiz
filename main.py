WIDTH = 1280
HEIGHT = 720

main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

score = 0
time_left = 10

q1 = ["I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?", "An echo", "A shadow", "A ghost", "A whisper", 1]
q2 = ["I am light as a feather, yet the strongest person cannot hold me for more than a few minutes. What am I?", "A flame", "Smoke", "Breath", "A cloud", 3]
q3 = ["I am always running but never move, have a bed but never sleep, and have a mouth but never speak. What am I?", "A wheel", "A clock", "A river", "A song", 3]
q4 = ["The more of me you take, the more you leave behind. What am I?", "Time", "Shadows", "Memories", "Steps", 4]
q5 = ["What has cities, but no houses; forests, but no trees; rivers, but no water?", "A painting", "A map", "A dream", "A book", 2]

questions = [q1, q2, q3, q4, q5]
question = questions.pop(0)

def draw():
    screen.fill("dim grey")
    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.filled_rect(timer_box, "sky blue")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "orange")

    screen.draw.textbox(str(time_left), timer_box, color=("black"))
    screen.draw.textbox(question[0], main_box, color=("black"))

    index = 1
    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color=("black"))
        index += 1

def game_over():
    global question, time_left
    message = "Game over. You got %s questions correct" % str(score)
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0

def correct_answer():
    global question, score, time_left

    score += 1
    if questions:
        question = questions.pop(0)
        time_left = 10
    else:
        print("End of questions")
        game_over()

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print(f"Clicked on answer {index}")
            if index == question[5]:
                print("Correct.")
                correct_answer()
            else:
                game_over()
        index += 1

def update_time_left():
    global time_left

    if time_left:
        time_left -= 1
    else:
        game_over()

clock.schedule_interval(update_time_left, 1.0)

# Use pgzrun main.py in the terminal to play! Have fun!
