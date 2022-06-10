#! /bin/python3
#-------------------------
# Requirements
#-------------------------
# // TODO
import os
#------------------------------------------------------------------------
# Here we are going to define the documentation of this program
#------------------------------------------------------------------------
def setup():
    package = "com.example.debugtest"
    print(50 * "-")
    print("Setting up your enviroment...")
    print(50 * "-")
    sel1 = "/home/kali/Desktop/Training/gdb/gdb.sh"
    os.system("adb push" + " " + sel1 + " " + "/data/local/tmp")
    os.system("adb devices -l")
    print(50 * "-")
    os.system("adb shell monkey -p" + " " + package + " " + "-c android.intent.category.LAUNCHER 1")
    print(50 * "-")
    os.system("adb shell ps | grep debugtest") # -> Making sure the PID is correct
    print(50 * "-")
    in1 = input("Please enter the PID: " + " ")
    print(50 * "-")
    os.system("adb forward tcp:8888 tcp:2000")
    os.system("adb shell su -c /data/local/tmp/./gdb.sh") # Need to add some more scripts here to make it work 
    #os.system("adb shell su gdbserver64 localhost:2000 -attach" + " " + in1)
#----------------------------------------
# // TODO -> Here we input the functions
setup()
#----------------------------------------
# // TODO 
# For some reason the GDB import duplicates the output, why?
# Also, we cant use 'su' properly, for it we will change some permissions
# To make this fix we need to change the file system properties of the Android device
# -> 1) adb shell, 2) su, 3) chmod 777 /system/bin/pm
# Another fix could be the following command:
# -> adb shell su -c "your commands"
# OK, {THE BEST FIX IS TO LOCATE EXECUTABLES ON [/data/local/tmp]}
#-----------------------------------------