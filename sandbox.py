# Python Sandbox
# Author: piyush.jadhav@nyu.edu
# Description: ...


with open("program.input") as f:
    program = f.readlines()
while(program):
	exec(program.pop(0))
