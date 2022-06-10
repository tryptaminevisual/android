#! /bin/python3

#-------------------------
# Requirements
#-------------------------
# pip3 install os
# pip3 install asyncore
# pip3 install python-ptrace // Not necessary, we can use strace instead (local on target)
#-------------------------
from asyncore import read
import os
import sys
import sys
import subprocess
import signal
import ptrace.debugger
#------------------------
#print("Hello World") // I always start with this line to test if it works
# First we are going to download the file from '/proc/self/status'
# We are also going to create a small directory which we will delete later 
#------------------------------------------------------------------------
# Here we are going to define the documentation of this program
#------------------------------------------------------------------------
def doc():
    os.system("clear")
    print(50 * "-")
    print('Welcome to this Ptrace tool, for this tool to work you need to have an android device.')
    print('Make sure your device is recognize, you can use the following command:')
    print('-> adb devices -l')
    print('Once you have done all the necessary checks we can proceed with the tool')
    print(50 * "-")
    input('Press any key to continue: ' + '')
# here we are going to do a verification test for the folder adb_t
# If the folder exists it will delete it, if not it will go to create it and keep the flow going
def check_f():
    os.system("ls > verf.txt")
    with open('verf.txt') as file:
        if 'adb_t' in file.read():
            os.system("rm -rf adb_t")
            os.system("rm -rf verf.txt")
            os.system("rm -rf adb_t/status.txt")
            os.system("rm -rf jdwp1.txt")

def start():
    os.system("clear")
    print(50 * "-")
    print("Downloading file....")
    print(50 * "-")
    os.system("mkdir adb_t")
    #os.system("rm -rf mkdir adb_t") # We want to keep this line for testing purposes, then we just comment it out
    os.system("adb pull /proc/self/status")
    os.system("cat status > status.txt")
    os.system("mv status.txt adb_t/")
    os.system("rm -rf status")
    print(50 * "-")
    input("Press any key to continue: " + "")

def gdb_check():
    os.system("clear")
    # First we are going to read the file status and we are going to check the 'TracerPid:'
    with open('adb_t/status.txt') as file:
        if 'TracerPid:	0' in file.read():
            package = "com.example.debugtest"
            #print("true") # This is a verification test to see what the value is, in this case 0
            # For more documentation about the 'python-ptrace' check out the documentation
            # -> https://python-ptrace.readthedocs.io/en/latest/usage.html
            #debugger = ptrace.debugger.PtraceDebugger()
            print(50 * "-")
            print("Lets try and attach the debugger to the PID")
            print(50 * "-")
            print("Lets start the debug test app")
            print(50 * "-")
            os.system("adb shell monkey -p" + " " + package + " " + "-c android.intent.category.LAUNCHER 1")
            print(50 * "-")
            print("This is the PID for our APK")
            print(50 * "-")
            os.system("adb shell ps | grep debug")
            print(50 * "-")
            #print('Does it work?')
            value_in = input("Please enter the PID of the APK: " + "")
            print(50 * "-")
            command = ("adb shell su strace -p" + " " + value_in + " " + "&")
            #print(command) #-> Command looks goods
            os.system(command)
            print(50 * "-")
            print("Done! Strace running in background process!")
            print(50 * "-")
            command_2 = 'adb shell ps | grep com.example.debugtest | cut -f7 -d\ > jdwp1.txt '''
            os.system(command_2)
            print("The jdwp port is: ")
            os.system("cat jdwp1.txt")
            os.system("mv jdwp1.txt adb_t/")
            print(50 * "-")
            print("Doing some configuration... Please wait!")
            print(50 * "-")
            os.system("adb forward tcp:8888 jdwp:" + value_in)
            #process_atc = debugger.addProcess(int(value_in), False) -> This only works on local host, we need to use strace
            # Remember to kill strace session -> adb shell su -c pkill strace {NECESSARY}
            # Process_atc is a PtraceProcess instance {Have to do more research}
            # Find a way to attatch tracer to PID in target system {Done!}
            print(50 * "-")
            location = "/usr/lib/jvm/jdk-18/bin/jdb"
            #print("{ cat; } | " + location + " " + "--attach :7777")
            os.system("clear")
            os.system("{ cat; } | " + location + " " + "-attach localhost:8888")
            os.system("clear")
            exit()

        elif 'TracerPid:	-1' in file.read():
            print(50 * "-")
            print("Trace failed! GDB is present")
            print(50 * "-")
            input("Press any key to exit the problem: " + "")
            os.system("clear")
            exit()

#----------------------------------------
doc()
check_f()
start()
gdb_check()
#----------------------------------------
# // TODO 
# -> Understand the excersise better so the program is more effective
# -> step 6? What does it mean?
# -> Join? attach?
# -> jdb command? does not exist at the moment
# -> Remember to go to "Settings/Developer Options" and make sure that the value of "Wait for debugger"  
# -> Remember to change the path of your JDB to your current one because it might be in a different directory than mine :) 
#-----------------------------------------