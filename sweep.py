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

    print("\n~MINESWEEPER~\n")

    while not gameOver:
        theBoard.display()

        move_str = input("Enter a row number followed by column number: ")

        if move_str == "HELP":
            #do something helpful
            print("No, thank you.")

        theMove = Move(move_str)

        if theMove.isValid():
            try:
                theMove.parse()
                theTile = theBoard.getTile(theMove)
                theTile.setFlagType(theMove.getFlag())

                if not theTile.isFlagged():
                    theTile.reveal()
                    gameOver = theBoard.explode(theTile)

            except ValueError:
                print("Invalid input. Syntax: rr cc (F#)")
            except IndexError:
                print("Invalid input. Board is {0}x{1}".format(theBoard.rows(), theBoard.cols()))
        else:
            print("Invalid input. Syntax: rr cc (F#)")

    print("\n\n KABOOM!!\n")
    theBoard.showSolution()

    if input("Play again? (Y/N)  ").upper() == 'N':
        keepPlaying = False
