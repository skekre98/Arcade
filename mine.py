import curses
import random
import subprocess
import sys


defaultDifficulty = 0.1
setDifficulty = defaultDifficulty

class BigText:

    def __init__(self, string):
        self.characters = {

          "0": ["  ***  ",
                " *   * ",
                "*   * *",
                "*  *  *",
                "* *   *",
                " *   * ",
                "  ***  "],
          
          "1": [" * ",
                "** ",
                " * ",
                " * ",
                " * ",
                " * ",
                "***"],

          "2": ["*** ",
                "   *",
                "   *",
                "  **",
                "   *",
                "   *",
                "*** "],

          
          "3": ["*** ",
                "   *",
                "   *",
                "  **",
                "   *",
                "   *",
                "*** "],

          "4": ["*   * ",
                "*   * ",
                "*   * ",
                "******",
                "    * ",
                "    * ",
                "    * "],

          "5": ["*****",
                "*    ",
                "*    ",
                "**** ",
                "    *",
                "*   *",
                " *** "],

          "6": [" **** ",
                "*     ",
                "* *** ",
                "**   *",
                "*    *",
                "*    *",
                " **** "],

          "7": ["*****",
                "    *",
                "   * ",
                "  *  ",
                "  *  ",
                "  *  ",
                "  *  "],

          "8": [" *** ",
                "*   *",
                "*   *",
                " *** ",
                "*   *",
                "*   *",
                " *** "],

          "9": [" ****",
                "*   *",
                "*   *",
                " ****",
                "    *",
                "    *",
                "    *"],

          "a": ["  **  ",
                " *  * ",
                "*    *",
                "*    *",
                "******",
                "*    *",
                "*    *"],

          "b": ["**** ",
                "*   *",
                "*   *",
                "**** ",
                "*   *",
                "*   *",
                "**** "],

          "c": [" *** ",
                "*   *",
                "*    ",
                "*    ",
                "*    ",
                "*   *",
                " *** "],

          "d": ["***  ",
                "*  * ",
                "*   *",
                "*   *",
                "*   *",
                "*  * ",
                "***  "],

          "e": ["****",
                "*   ",
                "*   ",
                "****",
                "*   ",
                "*   ",
                "****"],

          "f": ["****",
                "*   ",
                "*   ",
                "*** ",
                "*   ",
                "*   ",
                "*   "],

          "g": ["*****",
                "*   *",
                "*    ",
                "*    ",
                "*  **",
                "*   *",
                "*****"],

          "h": ["*   *",
                "*   *",
                "*   *",
                "*****",
                "*   *",
                "*   *",
                "*   *"],

          "i": ["*****",
                "  *  ",
                "  *  ",
                "  *  ",
                "  *  ",
                "  *  ",
                "*****"],

          "j": ["*****",
                "   * ",
                "   * ",
                "   * ",
                "   * ",
                "*  * ",
                " **  "],

          "k": ["*   *",
                "*  * ",
                "* *  ",
                "*    ",
                "* *  ",
                "*  * ",
                "*   *"],

          "l": ["*    ",
                "*    ",
                "*    ",
                "*    ",
                "*    ",
                "*    ",
                "*****"],

          "m": ["*         *",
                "**       **",
                "* *     * *",
                "*  *   *  *",
                "*   * *   *",
                "*    *    *",
                "*         *"],

          "n": ["*     *",
                "**    *",
                "* *   *",
                "*  *  *",
                "*   * *",
                "*    **",
                "*     *"],

          "o": ["  ***  ",
                " *   * ",
                "*     *",
                "*     *",
                "*     *",
                " *   * ",
                "  ***  "],

          "p": ["**** ",
                "*   *",
                "*   *",
                "**** ",
                "*    ",
                "*    ",
                "*    ",],

          "q": [" ****  ",
                "*    * ",
                "*    * ",
                "*  * * ",
                "*   ** ",
                "*    * ",
                " **** *"],

          "r": ["**** ",
                "*   *",
                "*   *",
                "**** ",
                "* *  ",
                "*  * ",
                "*   *"],

          "s": [" *** ",
                "*   *",
                "*    ",
                " *** ",
                "    *",
                "*   *",
                " *** ",],

          "t": ["*****",
                "  *  ",
                "  *  ",
                "  *  ",
                "  *  ", 
                "  *  ",
                "  *  "],

          "u": ["*    *",
                "*    *",
                "*    *",
                "*    *",
                "*    *",
                "*    *",
                " **** "],

          "v": ["*    *",
                "*    *",
                "*    *",
                "*    *",
                "*    *",
                " *  * ",
                "  **  "],

          "w": ["*         *",
                "*    *    *",
                "*   * *   *",
                "*  *   *  *",
                "* *     * *",
                "**       **",
                "*         *"],

          "x": ["*     *",
                " *   * ",
                "  * *  ",
                "   *   ",
                "  * *  ",
                " *   * ",
                "*     *"],

          "y": ["*    *",
                "*    *",
                "*    *",
                " *****",
                "     *",
                "*    *",
                " **** "],

          "z": ["*******",
                "     * ",
                "    *  ",
                "   *   ",
                "  *    ",
                " *     ",
                "*******"],

          " ": ["   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   "],

          "!": ["*",
                "*",
                "*",
                "*",
                "*",
                " ",
                "*"],

          ".": [" ",
                " ",
                " ",
                " ",
                " ",
                " ",
                "*"],

          ",": ["  ",
                "  ",
                "  ",
                "  ",
                "  ",
                " *",
                "* "],

          "?": [" *** ",
                "*   *",
                "*   *",
                "   * ",
                "  *  ",
                "     ",
                "  *  "]}

        string = string.lower()
        # Possible characters are numbers or lowercase letters.
        self.completeSequence = []
        for line in range(7):
            # This grabs each line of each character, and resets for each line.
            sequence = []
            try:
                for character in string:
                    #This goes through each character, adding the relevant line to "sequence".
                    sequence.append(self.characters[character][line])
                
                # This joins "sequence" to make a string which can be printed for each line.
                sequence = " ".join(sequence)

                self.width = len(sequence)

                #spareColumns = termColumns - len(sequence)
                #paddingColumns = spareColumns // 2
                #padding = [" "]*paddingColumns
                #for i in range(paddingColumns):
                #    padding[i] = str(random.randint(0,1))
                #padding = "".join(padding)
                #sequence = padding + sequence + padding

                self.completeSequence.append(sequence)
            
            except KeyError as err:
                    print("This program can't convert", err, "to ascii art.")
                    print("Contact the developer if you want it included.")
                    sys.exit()
        self.completeSequenceJoined = "\n".join(self.completeSequence)

class board:
 

    def __init__(self):
        termRows, termColumns = subprocess.check_output(['stty', 'size'], universal_newlines=True).strip().split()
        global width, height
        width = int(termColumns)
        height = int(termRows)

    def options(self):
        totalTiles = width * height

        #possible choices of tile: either "*" or " "
        self.mineNumber = int(setDifficulty * totalTiles)
        choices = list(self.mineNumber * "*")
        choices.extend(list((totalTiles-len(choices))*" "))
        return choices

    # If we use a dictionary rather than a list in the following
    # function, we will get a KeyError if we try to access a 
    # negative index, assuming we construct the dictionary such
    # that it has identical indexes to the list equivalent.
    # i.e. dictionary = {0:{0:" ", 1:" ", 2"*"}, 1:{0:"*", 1:" ", 2:" "}}
    # This will be helpful, as it will negate the need to explicitly
    # check whether a particular coordinate is legitimate. i.e. a 
    # dictionary won't match negative values for x, y, but a list will...
    ### Conversion Complete ###


    # For every x and y, check all the squares around to see if there is a mine,
    # add together the number of mines touching the original square and replace
    # the original square with the final count.
    def numberise(self, board):
        for x in range(width):
            for y in range(height):
                count = 0
                if board[x][y] != "*":
                        for i in range(-1, 2):
                            for n in range(-1, 2):
                                try:
                                    if board[x+i][y+n] == "*":
                                        count += 1
                                except KeyError:
                                    pass
                        if count != 0:
                            board[x][y] = str(count)


    def create(self):
        self.mineCoords = []
        choices = self.options()
        board = {}
        for i in range(0, width):
            board[i] = {}
            for n in range(0, height):
                board[i][n] = choices.pop(choices.index(random.choice(choices)))
                if board[i][n] == "*":
                    self.mineCoords.append([i,n])
                    
        self.numberise(board)

        return board

    def visibleScreen(self):
        board = {}
        for i in range(0, width):
            board[i] = {}
            for n in range(0, height):
                board[i][n] = " "
        return board



def fixed_addstr(screen, y, x, string, attribute=0):

    # termRows, termColumns = screen.getmaxyx()

    if y < height - 1 or x < width - 1:
        screen.addstr(y, x, string, attribute)
    else:
        screen.insstr(y, x, string, attribute)

def explore(screen, x, y):
    # This is the bit that happens when you click on a blank square
    # First it checks the squares directly around the clicked square
    # If the square it checks is a number, it will display it, and
    # if the square it checks is blank, it will add the blank square's
    # coordinates to a list or dictionary, then it will keep doing the
    # same process to all the coordinates in the list, deleting squares
    # that have been checked, and adding new squares, until the list is
    # empty. At that point, the area around the original square will be
    # revealed, as you would expect to happen in minesweeper.
    checked = [[x,y]]       # Has been checked and contains either a number or ' '
    toBeCentre = [[x, y]]   # Each point in this list will be checked on all sides for the above conditions
    centred = []            # These points have already been checked on all sides
    global cleared
    cleared = []
    
    while len(toBeCentre) > 0:
        X, Y = toBeCentre.pop(0)
        centred.append([X,Y])
        fixed_addstr(screen, Y, X, " ", curses.A_REVERSE)
        if [X,Y] not in cleared:
            cleared.append([X,Y])
        for i in range(-1, 2):
            for n in range(-1, 2):
                
        # When I was writing this section, it wouldn't work, and wouldn't work
        # and then after changing it around a million times, suddenly it started working...
        # The only problem is that I don't actually know what I did to make it work... =P
                try:
                    if ((newBoard[X+i][Y+n].isnumeric()) and ([X+i, Y+n] not in checked)):
                        fixed_addstr(screen, Y+n, X+i, newBoard[X+i][Y+n], curses.A_REVERSE)
                        checked.append([X+i, Y+n])
                        if [X+i,Y+n] not in cleared:
                            cleared.append([X+i,Y+n])
                    
                    elif newBoard[X+i][Y+n] == " ":
                        if (([X+i, Y+n] not in checked) and ([X+i, Y+n] not in toBeCentre)):
                            toBeCentre.append([X+i, Y+n])
                            checked.append([X+i, Y+n])
                except KeyError:
                    pass
    screen.move(y,x)


def centredBigTextOrSmallText(screen, text, cursesDisplayOption):
    height, width = screen.getmaxyx()
    bigTextMaker = BigText(text)
    bigText = bigTextMaker.completeSequence
    if len(bigText[0]) <= width and 8 < height:
        lineNum = height//2-4
        for line in bigText:
            lineNum += 1
            fixed_addstr(screen, lineNum, width//2-len(bigText[0])//2, line, cursesDisplayOption)

    else:
        # This prints a small version of the text, centred on the screen.
        fixed_addstr(screen, height//2, width//2-len(text)//2, text, cursesDisplayOption)

def welcome(screen):
    centredBigTextOrSmallText(screen, "Minesweeper", curses.A_BLINK)
    fixed_addstr(screen, height-1, width//2-len("press 'h' for help")//2, "press 'h' for help")

    loop = True
    while loop:
        c = screen.getch()
        if c in [ord('q')]:
            # Quits out immediately
            sys.exit() 
        if c in [10, 32, ord('p'), ord('r'), ord('n'), ord('g')]:
            break
        if c == ord('h'):
            help(screen)

def help(screen):
    screen.clear()
    text = ["quit -  q", 
            "start - Return", 
            "move - arrow keys",
            "flag - f",
            "clear - c"]

    startLine = height//2-len(text)//2
    length = 0
    for n in text:
        if len(n) > length:
            length = len(n)

    for lineNumber in range(len(text)):
        fixed_addstr(screen, startLine+lineNumber, width//2-length//2, text[lineNumber])



def main(screen):
    height, width = screen.getmaxyx()
    loop = True
    flaggedCoords = []
    mineCoords = board.mineCoords
    flaggedMineCoords = []
    mineNumber = board.mineNumber
    for y in range(height):
       for x in range(width):
           # This bit of code's dodgy, because it relies on the 
           # creation of "visibleScreen" external to the function...
           fixed_addstr(screen, y, x, visibleScreen[x][y])

    while loop: 
        c = screen.getch()
        if c in [ord('q'), 27]:
            break
        cursorY, cursorX = curses.getsyx()
        if c == ord('c'):
            # This is 'c', for 'clear'...
            if newBoard[cursorX][cursorY] == "*":
                for y in range(height):
                    for x in range(width):
                        # This bit of code's dodgy, because it relies on the 
                        # creation of "newBoard" external to the function...
                        fixed_addstr(screen, y, x, newBoard[x][y])
            screen.move(cursorY, cursorX) 
            # This moves the cursor back to where it was before random stuff was added
 
            if newBoard[cursorX][cursorY].isnumeric():
                #visibleScreen[x][y] = newBoard[x][y]
                fixed_addstr(screen, cursorY, cursorX, newBoard[cursorX][cursorY], curses.A_REVERSE)
                screen.move(cursorY, cursorX) 
 
            if newBoard[cursorX][cursorY] == " ":
                explore(screen, cursorX, cursorY)
 
        if c == ord('f'): 
            # 'f' for 'flag'
            if [cursorX, cursorY] in cleared:
                paintOption = curses.A_REVERSE
                character = newBoard[cursorX][cursorY]
            else:
                paintOption = 0
                character = " "

            if [cursorX, cursorY] not in cleared:
                ### !!! The winning condition is broken, because I inadvertantly deleted the !!! ###
                ### !!! mineCoords stuff... FIX THIS! =P                                     !!! ###

                # If it's flagged, but not a mine, just remove the flag.
                if ([cursorX, cursorY] in flaggedCoords) and ([cursorX, cursorY] not in mineCoords):
                    fixed_addstr(screen, cursorY, cursorX, character, paintOption)
                    flaggedCoords.remove([cursorX,cursorY])
                    mineNumber += 1
                    screen.move(cursorY, cursorX)
                    continue

                # If it's flagged, and it is a mine, remove the flag and add the coords to the 
                # list of mines that haven't been flagged.
                if ([cursorX, cursorY] in flaggedCoords) and ([cursorX, cursorY] in mineCoords):
                    fixed_addstr(screen, cursorY, cursorX, character, paintOption)
                    flaggedCoords.remove([cursorX, cursorY])
                    flaggedMineCoords.remove([cursorX, cursorY])
                    mineNumber += 1
                    screen.move(cursorY, cursorX)
                    continue

                # If it's not flagged, and it's not a mine, flag it, and reduce the mine count by 1,
                # but don't actually add the coords to the list of mines that have been flagged.
                if ([cursorX, cursorY] not in flaggedCoords) and ([cursorX, cursorY] not in mineCoords):
                    fixed_addstr(screen, cursorY, cursorX, "#", paintOption)
                    flaggedCoords.append([cursorX, cursorY])
                    mineNumber -= 1
                    screen.move(cursorY, cursorX)
                    continue

                # If it's not flagged, and it is a mine, flag it, and reduce the mine count by 1,
                # and remove the coords from the list of mines that haven't been flagged.
                if ([cursorX, cursorY] not in flaggedCoords) and ([cursorX, cursorY] in mineCoords):

                    fixed_addstr(screen, cursorY, cursorX, "#", paintOption)
                    flaggedCoords.append([cursorX, cursorY])
                    flaggedMineCoords.append([cursorX, cursorY])
                    mineNumber -=1
                    screen.move(cursorY, cursorX)
                    continue


 
 
        try:
            if c in [curses.KEY_LEFT, ord('h')]:
                screen.move(cursorY, cursorX-1)
            if c in [curses.KEY_RIGHT, ord('l')]:
                screen.move(cursorY, cursorX+1)
            if c in [curses.KEY_UP, ord('k')]:
                screen.move(cursorY-1, cursorX)
            if c in [curses.KEY_DOWN, ord('j')]:
                screen.move(cursorY+1, cursorX)
        except curses.error:
            curses.flash()

        ### This is the winning condition... ###
        if (mineNumber == 0) and (len(mineCoords) == len(flaggedMineCoords)):
            screen.clear()
            #curses.curs_set(0)
            centredBigTextOrSmallText(screen, "YOU WIN!!!", curses.A_BLINK)
    

def display(screen):
    welcome(screen)
    main(screen)
            
            

board = board()
newBoard = board.create()
visibleScreen = board.visibleScreen()

curses.wrapper(display)
