#! /bin/python3
#print("Hello World")
import os

os.system('clear')
print(50 * "-")
print("Hello lets set up your frida server....")
print(50 * "-")
os.system('adb devices -l')
print(50 * "-")
os.system('adb root') # Might be required
print(50 * "-")
input("Press any key to continue...")
os.system('clear')
print(50 * "-")
print("Lets send the files to the device...")
print(50 * "-")
print("Select the file you wish to send:")
print(50 * "-")
os.system('ls')
print(50 * "-")
selection = input("Select the file: " + "")
#print(selection)
dir = "/data/local/tmp/"
command = "adb push" + " " + selection + " " + dir
#print(command)
command1 = 'adb shell' + " " + '"chmod 755' + " " + dir + selection + '"'
#print(command1) 
command2 = "adb shell" + " " + '"' + dir + selection + " " + '&' + '"'
#print(command2)
print("Lets send the files!")
print(50 * "-")
os.system(command)
os.system(command1)
os.system(command2)
input("Done! lets make a test to see if frida is running on the device!")
os.system("clear")
print(50 * "-")
os.system("frida-ps -U")
print(50 * "-")
input("is it working properly?")
exit()
