from os import system as sy
import sys
import threading

class Error(Exception):
    pass

class InputError(Error):
    pass

def hlp():
    print("Available Commands: ")
    print("-------------------------------------------")
    print("hp        -view commands")
    print("ls        -see file containers")
    print("st        -restart stopped file container")
    print("sp        -stop a file container")
    print("at        -attach to file container")
    print("rn        -run new file container")
    print("-------------------------------------------")
    return

def ls():
    sy("sudo docker ps -a")
    return

def strt():
    print("Enter name of file you wish to see")
    return

def stp():
    print("Enter name of file you don't need")
    return

def atch():
    print("Enter name of file you wish to access")
    return

def run():
    print("Enter a file you wish to containerize")
    return

def backG():
    while True:
        #print("RUNNING")
        #KEEPING TRACK OF CONTAINERS HERE
        continue
    return

def foreG():
    hlp()
    options = {'hp' : hlp,
               'ls' : ls,
               'st' : strt,
               'sp' : stp,
               'at' : atch,
               'rn' : run
    }

    while True:
        try:
            command = raw_input("\nEnter a command: ")
            if command != 'ls':
                if command != 'st':
                    if command != 'sp':
                        if command != 'at':
                            if command != 'rn':
                                if command != 'hp':
                                    raise InputError()
            else:
                print('Marker1')
                #options['hp']()
                (options[command])()
                print('MARKER2')
        except InputError:
            print("\nError in your input try again")
    return

sy("echo These are your arguments")
y = len(sys.argv)
for x in range(y - 1):
    print str(sys.argv[x+1])
#CREATING DICTIONARY


#Start threads
t1 = threading.Thread(target=backG)
t1.daemon
t1.start()
t2 = threading.Thread(target=foreG)
t2.start()

