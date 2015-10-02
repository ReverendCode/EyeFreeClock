#Python is different and scary and I don't like change
#I guess I probably need these
import readchar
import os
from sound import Sound

#   Picture a set of spinners with Days / Hours / Minutes on them,
#   you can move between the spinners, and spin them each direction


#first there probably should be some kind of response lists

#audio cues for menu shifts??
MENUS = "./sounds/menu_navigation/"
clock_menu = [
    Sound(MENUS + "Set_day_of_week_f.wav"),
    Sound(MENUS + "Set_hour_f.wav"),
    Sound(MENUS + "Set_minutes_f.wav")
]

exitLoop = [
    Sound(MENUS + "press_again_to_quit_f.wav"),
    Sound(MENUS + "Exiting_program_f.wav")
]

#programmatically add the sounds to the appropriate spinners (lists)
days = []
DAYS_DIR = "./sounds/days_of_week/"
for file in os.listdir(DAYS_DIR):
    if file.endswith(".wav"):
        days.insert(len(days),Sound(DAYS_DIR + file))



#hours
#This is done to keep things in the proper order without having to parse filenames
hours = []
HOURS_AM_DIR = "./sounds/hours_am_pm/hours_am/"
HOURS_PM_DIR = "./sounds/hours_am_pm/hours_pm/"
for file in os.listdir(HOURS_AM_DIR):
    if file.endswith(".wav"):
        hours.insert(len(hours),Sound(HOURS_AM_DIR + file))
for file2 in os.listdir(HOURS_PM_DIR):
    if file2.endswith(".wav"):
        hours.insert(len(hours),Sound(HOURS_PM_DIR + file2))

#minutes (maybe seperate tens and 0-9 to avoid potential 30 presses)
# If I knew python better I would generate these programmatically, but this is literally the first time I have ever seen
# this language, I do like the intelliJ based ide though (PyCharm)

# Update: turns out it wasn't that hard after all
minutes = [
]
MINUTE_DIR = "./sounds/minutes_0_59/"
for file in os.listdir(MINUTE_DIR):
    if file.endswith(".wav"):
        minutes.insert(len(minutes),Sound(MINUTE_DIR + file))

#now build inputs

MENU_UP = 'l'
MENU_DOWN = ';'
SELECTION_UP = 'j'
SELECTION_DOWN = 'k'
SPEAK_TIME = ' '
QUIT = 'q'

exit_timer = 0

# very minimal console output

INVALID_INPUT = "This version of the Eye Free Clock only supports using the jkl; and space keys"
RUNNING_CONFIRMATION = "The Eye Free Clock is now running, use jkl; and space to operate the clock"

#finally, some trackers
spinner_list = [
    days,
    hours,
    minutes
]
spinner_indices = [
    0,
    0,
    0
]
menu_index = 0

print(RUNNING_CONFIRMATION)
uInput = readchar.readchar()

while True:
    if uInput != SPEAK_TIME:
        exit_timer = 0

    if uInput == MENU_UP:
        if menu_index == len(clock_menu) - 1 :
            menu_index = 0
        else:
            menu_index += 1

        clock_menu[menu_index].play()
        uInput = readchar.readchar()

    elif uInput == MENU_DOWN:
        if menu_index == 0:
            menu_index = len(clock_menu) - 1
        else:
            menu_index -= 1
        clock_menu[menu_index].play()
        uInput = readchar.readchar()

    elif uInput == SELECTION_UP:
        if spinner_indices[menu_index] == len(spinner_list[menu_index]) - 1:
            spinner_indices[menu_index] = 0
        else:
            spinner_indices[menu_index] += 1

        spinner_list[menu_index][spinner_indices[menu_index]].play()
        uInput = readchar.readchar()

    elif uInput == SELECTION_DOWN:
        if spinner_indices[menu_index] == 0:
            spinner_indices[menu_index] = len(spinner_list[menu_index]) - 1
        else:
            spinner_indices[menu_index] -= 1

        spinner_list[menu_index][spinner_indices[menu_index]].play()
        uInput = readchar.readchar()

    elif uInput == SPEAK_TIME:
        if exit_timer == 0:
            exit_timer += 1
            menu_index = 0
            day_index = spinner_indices[0]
            hour_index = spinner_indices[1]
            minute_index = spinner_indices[2]

            days[day_index].play_to_end()
            isAM = True
            # Next construct hour/minute string and speak that
            if hour_index > 11:
                isAM = False
                minutes[hour_index - 11].play_to_end()
            else:
                minutes[hour_index+1].play_to_end()
            if (minute_index != 0):
                minutes[minute_index].play_to_end()
            if isAM:
                Sound("./sounds/hours_am_pm/AM_f.wav").play_to_end()
            else:
                Sound("./sounds/hours_am_pm/PM_f.wav").play_to_end()
            uInput = readchar.readchar()
        elif exit_timer == 1:
            exit_timer += 1
            exitLoop[0].play_to_end()
            uInput = readchar.readchar()
        elif exit_timer == 2:
            exitLoop[1].play_to_end()
            break

    else:
        print(INVALID_INPUT)
        uInput = readchar.readchar()





