from move import Move
from board import Board

DEMO_X = 4
DEMO_Y = 4
DEMO_MINES = 4


INPUT_TYPE = 0
gameOver = False
keepPlaying = 'Y'

while keepPlaying:

    theBoard = Board(DEMO_X, DEMO_Y)
    theBoard.placeMines()

    print("\n~MINESWEEPER~")

    while not gameOver:
        print("")
        theBoard.display()
        print("")

        move_str = input("Enter a row number followed by column number: ")

        theMove = Move(move_str)

        if move_str.upper() == "HELP":
            #do something helpful
            print("\n No, thank you.")

        elif theMove.isValid():
            try:
                theMove.parse()
                theTile = theBoard.getTile(theMove)
                theTile.setFlagType(theMove.getFlag())

                if not theTile.isFlagged():
                    theTile.reveal()
                    gameOver = theBoard.explode(theTile)

            except ValueError:
                print("\nInvalid input. Syntax: rr cc (F#)")
            except IndexError:
                print("\nInvalid input. Board is {0}x{1}.".format(theBoard.rows(), theBoard.cols()))
            except AttributeError:
                print("\nInvalid input. Board is {0}x{1}.".format(theBoard.rows(), theBoard.cols()))
                print("(Are you trying to use CS-style indexes?)")
        else:
            print("Invalid input. Syntax: rr cc (F#)")

    print("\n\n KABOOM!!\n")
    theBoard.showSolution()

    if input("Play again? (Y/N)  ").upper() == 'N':
        keepPlaying = False
