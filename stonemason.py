def repair_column():
    turn_left()
    while front_is_clear():
        put_stone()
        move()
    if front_is_blocked():
        put_stone()
    original_column()

def original_column():
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()

def next_column():
    for i in range(4):
        move()
def put_stone():
    if beepers_present():
        pass
    else:
        put_beeper()

def main():
    repair_column()
    while front_is_clear():
        next_column()
        repair_column()

if __name__ == ' __main__':
    run_karel_program('SampleQuad1.w')
