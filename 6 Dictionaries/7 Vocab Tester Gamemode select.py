from easygui import *

def gamemodes():
    while 1:
        gamemode = enterbox("Enter a letter from A to E")
        if gamemode == None: return None
        try:
            gamemode = str(gamemode)
        except:
            msgbox("A-E Please", "Get it right!")

        return gamemode

gamemodes()





##from easygui import *
##
##def gamemodes():
##    while 1:
##        gamemode = enterbox("Enter a letter from A to E")
##        if gamemode == None: return None
##        try:
##            if gamemode.lower() == "a":
##                global start
##                start = 0
##                global end
##                end = 13
##            elif gamemode.lower() == "b":
##                global start
##                start = 14
##                global end
##                end = 15
##            elif gamemode.lower() == "c":
##                global start
##                start = 16
##                global end
##                end = 41
##            elif gamemode.lower() == "d":
##                global start
##                start = 42
##                global end
##                end = 54
##            elif gamemode.lower() == "e":
##                global start
##                start = 55
##                global end
##                end = 67
##        except:
##            msgbox("A-E Please", "Get it right!")
##
##            return gamemode
##
##gamemodes()
