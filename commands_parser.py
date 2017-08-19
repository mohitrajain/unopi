import keyboard_upgraded
import sys

i = 0
DEFAULT_DELAY = 0
last_line = ''  # storing last line
last_args = []  # storing last arguments

def repeat(n):
    for j in range(int(n)):
        execute(last_args,last_line)

def execute(args,line):
    global i

    print i
    # checking if DEFAULT_DELAY is defined in ( first or second ) line or not . checking for arduino mode also
    if i == 0 or i == 1:

        if i == 0:
            # activating arduino mode and should be  present very first line
            if args[0] == 'ARDUINO_OUTPUT':

                print 'activated arduino mode '
                keyboard_upgraded.ard_perm = True

                # deactivating serial connection to arduino as arduino mode has been selected so keyboard_upgraded.ser has to be closed
                try:
                    keyboard_upgraded.ser.close()
                    print 'Deactivating serial connection to arduino '
                except:
                    print 'Arduino serial connection was never started '

            else:
                try:
                    keyboard_upgraded.ser
                except:
                    print 'serial connection not available '
                    print 'either chose arduino mode or connect to serial channel '
                    print 'exiting now'
                    sys.exit(-1)

            if args[0] == 'DEFAULT_DELAY':
                DEFAULT_DELAY = int(args[1])

        # checking if DEFAULT_DELAY was present on second line and ARDUINO_OUTPUT was present above
        else:
            if args[0] == 'DEFAULT_DELAY' and keyboard_upgraded.ard_perm:
                DEFAULT_DELAY = int(args[1])

    if args[0] == 'DELAY':
        print 'calling Delay for {0} milliseconds '.format(int(args[1]))
        keyboard_upgraded.delay(int(args[1]))

    elif args[0] == 'STRING':
        print 'displaying string {0} '.format(line.split('\n')[0][line.find('STRING') + 7:])
        keyboard_upgraded.string(line.split('\n')[0][line.find('STRING') + 7:])

    # APP or MENU windows feature to create
    elif args[0] == 'APP' or args[0] == 'MENU':
        print 'menu key combination of shift + f10 '
        keyboard_upgraded.menu()

    elif args[0] == 'ENTER':
        print 'Enter'
        keyboard_upgraded.string('\n')

    elif args[0] == 'WINDOWS' or args[0] == 'GUI':
        print 'windows'
        if len(args) > 1:
            keyboard_upgraded.win(args[1])
        elif len(args) == 1 :
            keyboard_upgraded.win(False)

    elif args[0] == 'SHIFT':
        print 'Shift'
        keyboard_upgraded.shift(args[1])

    elif args[0] == 'ALT':
        print 'Alt'
        keyboard_upgraded.alt(args[1])

    elif args[0] == 'CONTROL' or args[0] == 'CTRL':
        print 'control'
        keyboard_upgraded.ctrl(args[1])

    elif args[0] == 'DOWNARROW' or args[0] == 'DOWN' or args[0] == 'LEFTARROW' or args[0] == 'LEFT' or args[
        0] == 'RIGHTARROW' or args[0] == 'RIGHT' or args[0] == 'UPARROW' or args[0] == 'UP':
        print 'arrow key ' + args[0]
        keyboard_upgraded.arrow(args[0])

    # repeat last command n = args[0] times
    elif args[0] == 'REPLAY' or args[0] == 'REPEAT':
        print 'repeat ' + args[1] + 'times'
        repeat(args[1])

    # ARDUINO_OUTPUT specified on any other line than first line will be ignored
    elif args[0] == 'ARDUINO_OUTPUT' :
        if i == 0 :
            pass
        else:
            print 'ignoring ARDUINO_OUTPUT as it must be present on first line'

    # DEFAULT_DELAY should be present in first line ( or second line if ARDUINO_OUTPUT is present on first line )
    elif args[0] == 'DEFAULT_DELAY':
        if i < 1:
            pass
        else:
            print 'DEFAULT_DELAY should be present in first line ( or second line if ARDUINO_OUTPUT is present on first line )'
            print 'Ignoring DEFAULT_DELAY'

    else:
        print 'Misc command'  # misc. commands like capslock , backspace etc
        keyboard_upgraded.misc(args[0])

    # taking care of line numbers
    i = i + 1

with open('linux_mal','r') as f :
    for line in f:

        # sanitizing file front spaces
        line = line.split('\n')[0]
        args = line.split(' ')

        for j in range(args.count('')):
            args.remove('')

        print args

        # saving last argument and last line but if it is NOT first line then executing first then saving parameters
        if i == 0:
            # executing if it is not comment i.e. REM else just printing out comment
            if args[0] == 'REM':
                print 'comment ' + line.split('\n')[0][line.find('REM') + 4:]
            else:
                last_args = args  # storing current arguments so that it can repeated  if required
                last_line = line  # storing current line so that it can repeated  if required
                execute(args, line)
        else:
            # executing if it is not comment i.e. REM else just printing out comment
            if args[0] == 'REM':
                print 'comment ' + line.split('\n')[0][line.find('REM') + 4:]
            else:
                execute(args, line)
                last_args = args  # storing current arguments so that it can repeated  if required
                last_line = line  # storing current line so that it can repeated  if required


        # default delay after every command
        keyboard_upgraded.delay(DEFAULT_DELAY)

# if ard_perm is selected then calling function for generating output
if keyboard_upgraded.ard_perm:
    keyboard_upgraded.gen_ard_out()

# trying to close serial conection which may be open till now
try:
    keyboard_upgraded.ser.close()
    print 'serial connection closed successfully '
except:
    pass
