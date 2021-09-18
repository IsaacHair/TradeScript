This provides a script to automatically trade in realm of the mad god.
The program expects you to use two accounts in two different windows.
Each window is selected, then a message is typed, and trades are checked for.
If there is a trade request, the program beeps.
Four pixel locations need to be set: the location of trade requests on the first account,
location of trade requests on the second account, location of the main window on the
first account, and location of the main window on the second account.
These can be set using pixelset.py; you will have two seconds to mouse over each
location in that order, then will hear a beep.
These are stored in pixels.txt
Running script.py will use the locations in pixels.txt to automate the trades.
The first message is the first line in the file msg.txt; the second message is the second
line.
To edit the messages, just open this file and change them.
Note: to exit the script, just move the mouse.