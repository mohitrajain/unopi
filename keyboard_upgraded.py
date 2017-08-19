#!/usr/bin/python
import serial
import time

# permission for generating binary output for arduino if set to false then raspberry will be controlling or if set to TRUE then output will be generated  in ard_out[]
ard_perm = False
# keystrokes value will be stored in this array
ard_out = []

try:
    ser = serial.Serial("/dev/serial0", 9600, timeout=1)
    print 'serial connection is started but will be terminated if you chose arduino mode '
except:
    print 'Serial connection on /dev/serial0 is not avaialble on this device '
    print 'May be Arduino binary output is selected'
    print 'If you want to control arduino through serial connection restart your payload and make sure /dev/serial0 is present '

# keycode understood by arduino hid

keycode = {

# code for control keys
"CONTROL_LEFT":10000,
"SHIFT_LEFT":11000,
"ALT_LEFT":12000,
"GUI_LEFT":13000,
"CONTROL_RIGHT":14000,
"SHIFT_RIGHT":15000,
"ALT_RIGHT":16000,
"GUI_RIGHT":17000,

"KEY_A":4,
"KEY_B":5,
"KEY_C":6,
"KEY_D":7,
"KEY_E":8,
"KEY_F":9,
"KEY_G":10,
"KEY_H":11,
"KEY_I":12,
"KEY_J":13,
"KEY_K":14,
"KEY_L":15,
"KEY_M":16,
"KEY_N":17,
"KEY_O":18,
"KEY_P":19,
"KEY_Q":20,
"KEY_R":21,
"KEY_S":22,
"KEY_T":23,
"KEY_U":24,
"KEY_V":25,
"KEY_W":26,
"KEY_X":27,
"KEY_Y":28,
"KEY_Z":29,
"KEY_1":30,
"KEY_2":31,
"KEY_3":32,
"KEY_4":33,
"KEY_5":34,
"KEY_6":35,
"KEY_7":36,
"KEY_8":37,
"KEY_9":38,
"KEY_0":39,

"KEY_ENTER":40,
"KEY_ESCAPE":41,
"KEY_BACKSPACE":42,
"KEY_TAB":43,
"KEY_SPACE":44,
"KEY_MINUS":45,
"KEY_EQUALS":46,
"KEY_LBRACKET":47,
"KEY_RBRACKET":48,
"KEY_BACKSLASH":49,
"KEY_NONUS_NUMBER":50,
"KEY_SEMICOLON":51,
"KEY_QUOTE":52,
"KEY_TILDE":53,
"KEY_COMMA":54,
"KEY_PERIOD":55,
"KEY_SLASH":56,
"KEY_CAPSLOCK":57,

"KEY_F1":58,
"KEY_F2":59,
"KEY_F3":60,
"KEY_F4":61,
"KEY_F5":62,
"KEY_F6":63,
"KEY_F7":64,
"KEY_F8":65,
"KEY_F9":66,
"KEY_F10":67,
"KEY_F11":68,
"KEY_F12":69,

"KEY_PRNTSCRN":70,
"KEY_SCROLLLOCK":71,
"KEY_PAUSE":72,
"KEY_INSERT":73,
"KEY_HOME":74,
"KEY_PAGEUP":75,
"KEY_DELETE":76,
"KEY_END":77,
"KEY_PAGEDOWN":78,
"KEY_RIGHTARROW":79,
"KEY_LEFTARROW":80,
"KEY_DOWNARROW":81,
"KEY_UPARROW":82,

"KEY_NUM_LOCK":83,

"KEY_NUM_DIV":84,
"KEY_NUM_MUL":85,
"KEY_NUM_SUB":86,
"KEY_NUM_ADD":87,

"KEY_NUM_ENTER":88,
"KEY_NUM_1":89,
"KEY_NUM_2":90,
"KEY_NUM_3":91,
"KEY_NUM_4":92,
"KEY_NUM_5":93,
"KEY_NUM_6":94,
"KEY_NUM_7":95,
"KEY_NUM_8":96,
"KEY_NUM_9":97,
"KEY_NUM_0":98,
"KEY_NUM_DOT":99
}

# actual ascii value table and some ways to obtain those values like :- A -> Shif_L + 'a' (KEY_A)

ascii = { 
97:"KEY_A",
98:"KEY_B",
99:"KEY_C",
100:"KEY_D",
101:"KEY_E",
102:"KEY_F",
103:"KEY_G",
104:"KEY_H",
105:"KEY_I",
106:"KEY_J",
107:"KEY_K",
108:"KEY_L",
109:"KEY_M",
110:"KEY_N",
111:"KEY_O",
112:"KEY_P",
113:"KEY_Q",
114:"KEY_R",
115:"KEY_S",
116:"KEY_T",
117:"KEY_U",
118:"KEY_V",
119:"KEY_W",
120:"KEY_X",
121:"KEY_Y",
122:"KEY_Z",
49:"KEY_1",
50:"KEY_2",
51:"KEY_3",
52:"KEY_4",
53:"KEY_5",
54:"KEY_6",
55:"KEY_7",
56:"KEY_8",
57:"KEY_9",
48:"KEY_0",

10:"KEY_ENTER",
11:"KEY_TAB",
32:"KEY_SPACE",
45:"KEY_MINUS",
61:"KEY_EQUALS",
123:"KEY_LBRACKET",
125:"KEY_RBRACKET",
92:"KEY_BACKSLASH",
59:"KEY_SEMICOLON",
39:"KEY_QUOTE",
96:"KEY_TILDE",
44:"KEY_COMMA",
46:"KEY_PERIOD",
47:"KEY_SLASH",

95:"Shif_L_KEY_MINUS",
43:"Shif_L_KEY_EQUALS",
123:"Shif_L_KEY_LBRACKET",
125:"Shif_L_KEY_RBRACKET",
124:"Shif_L_KEY_BACKSLASH",
58:"Shif_L_KEY_SEMICOLON",
34:"Shif_L_KEY_QUOTE",
60:"Shif_L_KEY_COMMA",
62:"Shif_L_KEY_PERIOD",
63:"Shif_L_KEY_SLASH",

33:"Shif_L_KEY_1",
64:"Shif_L_KEY_2",
35:"Shif_L_KEY_3",
36:"Shif_L_KEY_4",
37:"Shif_L_KEY_5",
94:"Shif_L_KEY_6",
38:"Shif_L_KEY_7",
42:"Shif_L_KEY_8",
40:"Shif_L_KEY_9",
41:"Shif_L_KEY_0",
95:"Shif_L_KEY_MINUS",
43:"Shif_L_KEY_EQUALS",
126:"Shif_L_KEY_TILDE",

65:"Shif_L_KEY_A",
66:"Shif_L_KEY_B",
67:"Shif_L_KEY_C",
68:"Shif_L_KEY_D",
69:"Shif_L_KEY_E",
70:"Shif_L_KEY_F",
71:"Shif_L_KEY_G",
72:"Shif_L_KEY_H",
73:"Shif_L_KEY_I",
74:"Shif_L_KEY_J",
75:"Shif_L_KEY_K",
76:"Shif_L_KEY_L",
77:"Shif_L_KEY_M",
78:"Shif_L_KEY_N",
79:"Shif_L_KEY_O",
80:"Shif_L_KEY_P",
81:"Shif_L_KEY_Q",
82:"Shif_L_KEY_R",
83:"Shif_L_KEY_S",
84:"Shif_L_KEY_T",
85:"Shif_L_KEY_U",
86:"Shif_L_KEY_V",
87:"Shif_L_KEY_W",
88:"Shif_L_KEY_X",
89:"Shif_L_KEY_Y",
90:"Shif_L_KEY_Z"
}

#function for sending and recieving (feedback) data from arduino over serial communication
def tx_rx(i):
    s = str(i)
    if len(s) == 1:
        st = '0000' + s
    elif len(s) == 2:
        st = '000' + s
    elif len(s) == 3:
        st = '00' + s
    elif len(s) == 4:
        st = '0' + s         # padding extra zeros in front to make it three character string
    else:
        st = s

    #print 'sending ' + st
    ser.write(st)
    r = []                      # now reciving feedback from arduino of data sent
    k = 0
    s = 99999
    while 1:
        res = ser.read()
        if res:
            k = k + 1
            r.append(str(res))
            if k == 5 :
                p = ''.join(r)
                #print 'reading ' + p
                try:
                    s = int(p)
                except:
                    s = 99999
                    print 'using i'
                break
    return s


# function for sending data passed in as j and checking that it is sent correctly
def send(j):
    #print 'sending j = ' + str(j)
    if not ard_perm:
        x = tx_rx(j)
        while x != j:
            while ser.read():
                print "reading extra"
            print 'not sent correctly sending again ' + str(j)
            x = tx_rx(j)
    else:
        log(j)

# function for sending info about releasing key
def release_key():
    if not ard_perm:
        x = tx_rx(0)
        while x != 0:
            while ser.read():
                print "reading extra"
            print 'not sent correctly sending agian ' + str(0)
        x = tx_rx(0)
    else:
        log(0)

# this shift function is used for capitalising characters
def shift_plus(key):
    #print 'request for shift ' +  key
    send(keycode[key] + keycode["SHIFT_LEFT"])


# function for parsing and sending string passwd to it as my_string
def string(my_string):
    for j in my_string:
        y = ascii[ord(j)]
        if 'Shif_L' in y:
            shift_plus(y[7:])
        else:
            send(keycode[y])

        release_key()

        # by default there is no delay between any two individual characters , uncomment below option and change the paramter if you want some delay between two characters
        #delay(0)

# defining delay in milli seconds using time.sleep ( delay is being implemented on pi rather than arduino in case if serial connection is set)
def delay(milli):
    # if 0 seconds delay is asked then nothing will happen doing so will save no of instructions to process
    if milli == 0:
        pass
    else:
        # restricting milli seconds to 9999 milli seconds
        if milli > 9999:
            milli = 9999

        if not ard_perm:
            time.sleep(milli / 1000)
        else:
            # code for our delay is 2**** so we can have at max of 9999 milli seconds of delay
            log(20000 + milli)

# function for windows key or gui left = 13000
def win(key):
    if key:
        try:
            send(13000 + keycode[ascii[ord(key)]])  # for sending single characters like a ,b ,c etc
        except:
            send(13000 + keycode['KEY_' + key])  # for special single characters like enter etc
        release_key()
    else:
        send(101)
        release_key()
    #delay(10)

# function for sending leftshift = 11000 + f10 = 67 key
def menu():
    send(11067)
    release_key()

#this function receives keys to be inserted in conjunction with left shift = 11000 like insert etc
def shift(key):
    key = 'KEY_' + key
    send(11000 + keycode[key])
    release_key()

# this function receives keys to be inserted in conjunction with left alt = 12000 like end ,esc etc
def alt(key):
    try:
        send(12000 + keycode[ascii[ord(key)]])  # for single character
    except:
        send(12000 + keycode['KEY_' + key])        # for keys like end ,esc , tab etc
    release_key()

# this function receives keys to be inserted in conjunction with left ctrl = 10000 like end ,esc etc
def ctrl(key):
    try:
        send(10000 + keycode[ascii[ord(key)]])  # for single character
    except:
        send(10000 + keycode['KEY_' + key])        # for keys like end ,esc , tab etc
    release_key()

# this is arrow function which presses arrow keys like up , down , right etc
def arrow(key):
    key = 'KEY_' + key
    send(keycode[key])
    release_key()

# function for miscellaneous commands like backspace ,tab etc
def misc(key):
    send(keycode['KEY_' + key])
    release_key()

# logging function :- it notes keystrokes and appends them to a array
def log(v):
    s = str(v)
    if len(s) == 1:
        st = '0000' + s
    elif len(s) == 2:
        st = '000' + s
    elif len(s) == 3:
        st = '00' + s
    elif len(s) == 4:
        st = '0' + s  # padding extra zeros in front to make it three character string
    else:
        st = s

    # appending codes to ard_out array
    ard_out.append(st)

# this function will generate output for arduino only mode and write main.cpp file which then will be flashed to arduino uno's Atmega328p
def gen_ard_out():
    s = '{'
    for k in range(len(ard_out)):
        if k != len(ard_out) - 1:
            s = s + '"' + ard_out[k] + '",'
        else:
            s = s + '"' + ard_out[k] + '"}'

    # reading sample file and making main.c file
    with open('sample.cpp', 'r') as sam:
        lines = sam.readlines()
        lines[4] = lines[4].format(len(ard_out), s)  # providing len
        lines[20] = lines[20].format(len(ard_out))
        lines[30] = lines[30].format(250)  # providing delay between two key presses to delay({0});
        with open('plat/src/main.cpp', 'w') as man:
            man.writelines(lines)
