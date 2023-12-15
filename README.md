# GUI_to_EXE
GUI_to_Executer

As the title says Converting tkinter to exe I believe pyinstaller is worth mentioning in this case.

There are some debates on which is better pyinstaller or cx_Freeze on the Internet, but I found pyinstaller simpler and it worked for me out of the box with tkinter. A one-liner in cmd:

pyinstaller.exe --onefile --icon=myicon.ico main.py
--onefile option produces, well, one output file instead of many.

--icon will connect an icon of your choice.

main.py is your main file with the main function.
