from stanfordkarel import *


def karel_infinite_move():
    """makes karel move through every corner infinitely while switching beepers
    if karel starts in top left corner facing south"""

    done = False

    while done == False:
        if no_beepers_present():
            put_beeper()
        else:
            pick_beeper()

        if front_is_clear():
            move()
        else:
            if facing_south():
                turn_left()
                if front_is_clear():
                    move()
                    turn_left()
                else:
                    done = True
            else:
                turn_left()
                turn_left()
                turn_left()
                if front_is_clear():
                    move()
                    turn_left()
                    turn_left()
                    turn_left()
                else:
                    done = True


def main():
    """does karel_infinite_move, but orients karel correctly first"""
    turn_left()
    turn_left()
    karel_infinite_move()


if __name__ == "__main__":
    run_karel_program("checkerboard_karel_end")
