from os import system as sy
import sys
import threading
def help():
    print("Available Commands: ")
    print("----------------------------------")
    print("help      -view commands")
    print("ls        -see file containers")
    print("start     -restart stopped file container")
    print("stop      -stop a file container")
    print("attach    -attach to file container")
    print("run       -run new file container")
    return

def ls():
    sy("docker ps -a")
    return

def start():
    print("Enter name of file you wish to see")
    return

def stop():
    print("Enter name of file you don't need")
    return

def attach():
    print("Enter name of file you wish to access")
    return

def run():
    print("Enter a file you wish to containerize")
    return

def addInp():
    while True:
        #print("RUNNING")
    return

sy("echo These are your arguments")
y = len(sys.argv)
for x in range(y - 1):
    print str(sys.argv[x+1])
t1 = threading.Thread(target=addInp)
t1.daemon
t1.start()


