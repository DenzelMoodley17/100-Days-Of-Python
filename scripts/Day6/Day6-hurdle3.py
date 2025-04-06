# Reeborg Hurdle 3 code
# https://reeborg.cs20.ca/?lang=en&mode=python&menu=%2Fworlds%2Fmenus%2Fsk_menu.json&name=Hurdle%204&url=%2Fworlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

def look_up():
    turn_left()

def turn_around():
    turn_left()
    turn_left()


def hurdle():
    turn_left()

def down():
    turn_right()
    move()
    turn_right()
    move()


while not at_goal():
    if not front_is_clear():
        hurdle()
    elif right_is_clear():
        down()
    else:
        move()
