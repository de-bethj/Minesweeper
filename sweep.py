from move import Move, NoSuchTileError
from board import Board

DEMO_X = 5
DEMO_Y = 5


INPUT_TYPE = 0
gameOver = False
tilesRemain = True
keepPlaying = 'Y'

while keepPlaying:

    theBoard = Board(DEMO_X, DEMO_Y)
    theBoard.placeMines()

    print("\n~MINESWEEPER~")

    while not gameOver and tilesRemain:
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

                if theMove.getFlag() is not None:
                    theTile.setFlagType(theMove.getFlag())

                elif not theTile.isFlagged():
                    theBoard.revealTile(theTile)

                    gameOver = theBoard.explode(theTile)
                    tilesRemain = theBoard.tilesLeft()

            except IndexError:
                print("\nInvalid input. Board is {0}x{1}.".format(theBoard.rows(), theBoard.cols()))
            except NoSuchTileError:
                print("\nInvalid input. Board is {0}x{1}.".format(theBoard.rows(), theBoard.cols()))
                print("(Are you trying to use CS-style indexes?)")
            except ValueError:
                print("\nInvalid input. Syntax: rr cc (F#)")
        else:
            print("Invalid input. Syntax: rr cc (F#)")

    if gameOver:
        print("\n\n KABOOM!!\n")
        theBoard.showSolution()
    if not tilesRemain:
        print("\n\nCONGRATULATIONS!!\n")

    if input("Play again? (Y/N)  ").upper() == 'N':
        keepPlaying = False
    else:
        gameOver = False
        tilesRemain = True

