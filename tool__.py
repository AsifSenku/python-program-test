
import os
import sys
usern = "Ghoul"
pwd = "ghouleye"

print("Login To Use The Tool")

inpusr = str(input("Enter Username: "))
inppwd = str(input("Enter Password: "))

if inpusr == usern and inppwd == pwd:
	print("Trying To login.....")
	os.system("clear")
	
	pass
	
else:
	print("Login fail")
	sys.exit()
	
print("Login Success")

red="\033[0;31m" 
color_off="\033[0m"

print(red+"Thanks For using"+color_off)






	
print("[>]Enter Your Option:\n\n")

print("[1]Addition\n")
print("[2]Subtract\n")
print("[3]Multiplication\n")
print("[4]division")

a = int(input("\nEnter Your Option: "))
	
def add():
	a = int(input("Enter First Num: "))
	b = int(input("Enter Second Num: "))
	r = a + b
	print("The Result is : ",r)
def sub():
	a = int(input("Enter First Num: "))
	b = int(input("Enter Second Num: "))
	r = a -  b
	print("The Result is : ",r)
	
def mul():
	a = int(input("Enter First Num: "))
	b = int(input("Enter Second Num: "))
	r = a *  b
	print("The Result is : ",r)
	
def divi():
	a = int(input("Enter First Num: "))
	b = int(input("Enter Second Num: "))
	r = a / b
	print("The Result is : ",r)
	
if a == 1:
	add()
	
elif a == 2:
	sub()
	
elif a == 3:
	mul()
	
elif a == 4:
	divi()
	

	
