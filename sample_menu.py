################################################################################
# sample_menu.py
# A. Hornof - Sept 2015
#
# A sample program to show how to move through a list of sound objects with
# single keystrokes.
#
################################################################################
__author__ = 'hornof'

# Package imports
import readchar

# Local imports
from sound import Sound

################################################################################
# Create the sound objects for the auditory menus and display.

# Create ten sound objects in a list.
menu_sound_objects = [
    Sound( "wav_files/hours_f/1AM_f.wav" ),
    Sound( "wav_files/hours_f/2AM_f.wav" ),
    Sound( "wav_files/hours_f/3AM_f.wav" ),
    Sound( "wav_files/hours_f/4AM_f.wav" ),
    Sound( "wav_files/hours_f/5AM_f.wav" ),
    Sound( "wav_files/hours_f/6AM_f.wav" ),
    Sound( "wav_files/hours_f/7AM_f.wav" ),
    Sound( "wav_files/hours_f/8AM_f.wav" ),
    Sound( "wav_files/hours_f/9AM_f.wav" ),
    Sound( "wav_files/hours_f/10AM_f.wav" )
]

# Create some sounds to assist with navigation.
PRESS_AGAIN_TO_QUIT = Sound \
    ( "wav_files/menus_modes_navigation_f/Press_again_to_quit_f.wav")
EXITING_PROGRAM = Sound \
    ( "wav_files/menus_modes_navigation_f/Exiting_program_f.wav")

################################################################################
# Set some global variables.

# Keystrokes for the keyboard interaction.
PLAY_AND_ADVANCE_MENU_KEY = 'j'
QUIT_MENU_KEY = 'k'

# A minimal amount of text to display to guide the user.
MINIMAL_HELP_STRING = "Press '" + PLAY_AND_ADVANCE_MENU_KEY + "' to hear a menu item or '" + \
                QUIT_MENU_KEY + "' to quit."

################################################################################
# Permit the user to move through the list of sound objects with the 'j' key.
# The 'k' key quits the program.

# Keep track of what is the current menu item.
current_menu_position = 0

# Provide a minimal indication that the program has started.
print(MINIMAL_HELP_STRING)

# Get the first keystroke.
c = readchar.readchar()

# Endless loop responding to the user's last keystroke.
# The loop breaks when the user hits the QUIT_MENU_KEY.
while True:

    # Respond to the user's input.

    # User plays a menu item and advances to the next.
    if c == PLAY_AND_ADVANCE_MENU_KEY:

        # Play the sound
        menu_sound_objects[current_menu_position].play()

        # If you have not reached the end of the menu, advance to the next item.
        if current_menu_position < len(menu_sound_objects) - 1:
            current_menu_position += 1

        # Get the user's next keystroke.
        c = readchar.readchar()

    # User quits.
    elif c == QUIT_MENU_KEY:

        # Notify the user that another QUIT_MENU_KEY will quit the program.
        PRESS_AGAIN_TO_QUIT.play()

        # Get the user's next keystroke.
        c = readchar.readchar()

        # If the user pressed QUIT_MENU_KEY, quit the program.
        # Note how replacing the call to play_to_end() with a call to play()
        #   will cause the sound to not get played.  This is because only
        #   play_to_end() locks up the main thread while it is playing.
        #   play() can be interrupted by other sounds or by quitting.
        if c == QUIT_MENU_KEY:
            EXITING_PROGRAM.play_to_end()
            # Quit the program
            break
        # Else do nothing.

        # Get the user's next keystroke.
        c = readchar.readchar()

    # The user presses a key that will have no effect.
    else:

        print("Press '", PLAY_AND_ADVANCE_MENU_KEY, "' to hear a menu item or '",
                QUIT_MENU_KEY, "' to quit.", sep = '')

        # Get the user's next keystroke.
        c = readchar.readchar()


