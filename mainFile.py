#Python is different and scary and I don't like change
#I guess I probably need these
import readchar
from sound import Sound

#first there probably should be some kind of response lists

#audio cues for menu shifts??
MENUS = "wav_files/menus_modes_navigation_f/"
clock_menu = [
    Sound(MENUS + "Set_day_of_week_f.wav"),
    Sound(MENUS + "Set_hour_f.wav"),
    Sound(MENUS + "Set_minutes_f.wav")
]

#days of the week
DAYF = "wav_files/days_of_week_f/"
days = [
    Sound(DAYF + "sunday_f.wav"),
    Sound(DAYF + "monday_f.wav"),
    Sound(DAYF + "tuesday_f.wav"),
    Sound(DAYF + "wednesday_f.wav"),
    Sound(DAYF + "thursday_f.wav"),
    Sound(DAYF + "friday_f.wav"),
    Sound(DAYF + "saturday_f.wav")
]

#hours
HOURF = "wav_files/hours_f/"
hours = [
    Sound(HOURF + "1AM_f.wav"),
    Sound(HOURF + "2AM_f.wav"),
    Sound(HOURF + "3AM_f.wav"),
    Sound(HOURF + "4AM_f.wav"),
    Sound(HOURF + "5AM_f.wav"),
    Sound(HOURF + "6AM_f.wav"),
    Sound(HOURF + "7AM_f.wav"),
    Sound(HOURF + "8AM_f.wav"),
    Sound(HOURF + "9AM_f.wav"),
    Sound(HOURF + "10AM_f.wav"),
    Sound(HOURF + "11AM_f.wav"),
    Sound(HOURF + "12AM_f.wav"),
    Sound(HOURF + "1PM_f.wav"),
    Sound(HOURF + "2PM_f.wav"),
    Sound(HOURF + "3PM_f.wav"),
    Sound(HOURF + "4PM_f.wav"),
    Sound(HOURF + "5PM_f.wav"),
    Sound(HOURF + "6PM_f.wav"),
    Sound(HOURF + "7PM_f.wav"),
    Sound(HOURF + "8PM_f.wav"),
    Sound(HOURF + "9PM_f.wav"),
    Sound(HOURF + "10PM_f.wav"),
    Sound(HOURF + "11PM_f.wav"),
    Sound(HOURF + "12PM_f.wav")
]

#minutes (maybe seperate tens and 0-9 to avoid potential 30 presses)
MINF = "wav_files/minutes_f/"
# If I knew python better I would generate these programmatically, but this is literally the first time I have ever seen
# this language, I do like the intelliJ based ide though (PyCharm)
minutes = [
    Sound(MINF + "00_f.wav"),
    Sound(MINF + "01_f.wav"),
    Sound(MINF + "02_f.wav"),
    Sound(MINF + "03_f.wav"),
    Sound(MINF + "04_f.wav"),
    Sound(MINF + "05_f.wav"),
    Sound(MINF + "06_f.wav"),
    Sound(MINF + "07_f.wav"),
    Sound(MINF + "08_f.wav"),
    Sound(MINF + "09_f.wav"),
    Sound(MINF + "10_f.wav"),
    Sound(MINF + "11_f.wav"),
    Sound(MINF + "12_f.wav"),
    Sound(MINF + "13_f.wav"),
    Sound(MINF + "14_f.wav"),
    Sound(MINF + "15_f.wav"),
    Sound(MINF + "16_f.wav"),
    Sound(MINF + "17_f.wav"),
    Sound(MINF + "18_f.wav"),
    Sound(MINF + "19_f.wav"),
    Sound(MINF + "20_f.wav"),
    Sound(MINF + "21_f.wav"),
    Sound(MINF + "22_f.wav"),
    Sound(MINF + "23_f.wav"),
    Sound(MINF + "24_f.wav"),
    Sound(MINF + "25_f.wav"),
    Sound(MINF + "26_f.wav"),
    Sound(MINF + "27_f.wav"),
    Sound(MINF + "28_f.wav"),
    Sound(MINF + "29_f.wav"),
    Sound(MINF + "30_f.wav"),
    Sound(MINF + "31_f.wav"),
    Sound(MINF + "32_f.wav"),
    Sound(MINF + "33_f.wav"),
    Sound(MINF + "34_f.wav"),
    Sound(MINF + "35_f.wav"),
    Sound(MINF + "36_f.wav"),
    Sound(MINF + "37_f.wav"),
    Sound(MINF + "38_f.wav"),
    Sound(MINF + "39_f.wav"),
    Sound(MINF + "40_f.wav"),
    Sound(MINF + "41_f.wav"),
    Sound(MINF + "42_f.wav"),
    Sound(MINF + "43_f.wav"),
    Sound(MINF + "44_f.wav"),
    Sound(MINF + "45_f.wav"),
    Sound(MINF + "46_f.wav"),
    Sound(MINF + "47_f.wav"),
    Sound(MINF + "48_f.wav"),
    Sound(MINF + "49_f.wav"),
    Sound(MINF + "50_f.wav"),
    Sound(MINF + "51_f.wav"),
    Sound(MINF + "52_f.wav"),
    Sound(MINF + "53_f.wav"),
    Sound(MINF + "54_f.wav"),
    Sound(MINF + "55_f.wav"),
    Sound(MINF + "56_f.wav"),
    Sound(MINF + "57_f.wav"),
    Sound(MINF + "58_f.wav"),
    Sound(MINF + "59_f.wav")
]

#now build inputs

MENU_UP = 'l'
MENU_DOWN = ';'
SELECTION_UP = 'j'
SELECTION_DOWN = 'k'
SPEAK_TIME = ' '
QUIT = 'q'

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
    if uInput == QUIT:
        break

    elif uInput == MENU_UP:
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
        menu_index = 0
        for index in range(len(spinner_list)):
            spinner_list[index][spinner_indices[index]].play_to_end()

        uInput = readchar.readchar()

    else:
        print(INVALID_INPUT)
        uInput = readchar.readchar()





