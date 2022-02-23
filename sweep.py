import re
from board import Board

DEMO_X = 4
DEMO_Y = 4
DEMO_MINES = 4

SHIFT = True
MOVE_FORMAT = re.compile(r"|(F\d )? *\d+ +\d+")
gameOver = False
turns = 0

theBoard = Board(DEMO_X, DEMO_Y)
theBoard.placeMines()

print("\n~MINESWEEPER~\n")

while not gameOver:
    theBoard.display()

    theMove = input("Enter a row number followed by column number: ")

    if theMove.upper().strip() == "HELP":
        #do something helpful
        print("No, thank you.")

    #validMove = MOVEFORMAT.fullmatch(theMove.upper().strip())
    if not True:
        print("Invalid input. Syntax: (F#) rr cc")
    else:
        try:
            moveParts = theMove.split(" ")
            # no flag given
            if len(moveParts) == 2:
                #for use with cs-style indices (0, 1, 2...)
                #pos_x, pos_y = int(moveParts[0]), int(moveParts[1])

                #for use with counting-style indices (1, 2, 3...)
                pos_x, pos_y = int(moveParts[0])-1, int(moveParts[1])-1
                theTile = theBoard.getTile(pos_x, pos_y)
                theTile.reveal()
                gameOver = theBoard.explode(theTile)
                #print(theTile)
            #flag given
            else:
                #for use with cs-style indices (0, 1, 2...)
                #pos_x, pos_y = int(moveParts[1]), int(moveParts[2])

                #for use with counting-style indices (1, 2, 3...)
                pos_x, pos_y = int(moveParts[1])-1, int(moveParts[2])-1

                flag = moveParts[0].lstrip("Ff")
                theBoard.getTile(pos_x, pos_y).setFlagType(flag)
        except ValueError:
            print("Invalid input. Syntax: (F#) rr cc")
        except IndexError:
            print("Invalid input. Board is {0}x{1}".format(theBoard.rows(), theBoard.cols()))



print("\n\n KABOOM!!\n")
theBoard.showSolution()






