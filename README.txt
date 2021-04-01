This is the source code of daemon program in python. 

Ref: Advanced programming in the unix environment by Richard Stevens

Requirement to run the program

1) Python 3.8
2) python libraries, standard installation should cover the program

zip folder contains
1) newcall.py
2) callee.py
3) README.txt

How to run
start the daemon
# python newcall.py start

Verify if Daemon is running
# ps -efww | grep -i newcall

stop the daemon
#python newcall.py stop
