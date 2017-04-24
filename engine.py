from os import system as sy
import sys
import threading
def help():
    print("Available Commands: ")
    print("----------------------------------")
    print("myc help      -view commands")
    print("myc ls        -see file containers")
    print("myc start     -restart stopped file container")
    print("myc stop      -stop a file container")
    print("myc attach    -attach to file container")
    print("myc run       -run new file container")
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
t = threading.Thread(target=addInp)
t.daemon
t.start()
print("Available Commands: ")
print("----------------------------------")
print("myc help      -view commands")
print("myc ls        -see file containers")
print("myc start     -restart stopped file container")
print("myc stop      -stop a file container")
print("myc attach    -attach to file container")
print("myc run       -run new file container")
