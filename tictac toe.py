theBoard={'top-L': ' ','top-M':' ','top-R': ' ','mid-L':' ','mid-M': ' ','mid-R':' ','low-L':' ','low-M':' ','low-R':' '}
def printBoard(board):
    print(board['top-L'] + '|' +board['top-M'] + '|' +board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn='X'
i=0
while(i<9):
    if i==0:
        printBoard(theBoard)
    print('Turn for '+turn+' .Move on which space?')
    move=input()
    if move not in theBoard.keys():
        print("wrong input")
    else:

        if theBoard[move] == ' ':
            theBoard[move]=turn
            printBoard(theBoard)
            i=i+1
            if turn=='X':
                turn='O'
            else:
                turn='X'
            if i>=3:
                if theBoard['top-L']==theBoard['top-M'] and theBoard['top-M']==theBoard['top-R']:
                    if theBoard['top-L']=='X':
                        print("X wins")
                        break
                    elif theBoard['top-L']=='O':
                        print("O wins")
                        break
                elif theBoard['mid-L']==theBoard['mid-M'] and theBoard['mid-M']==theBoard['mid-R']:
                    if theBoard['mid-L']=='X':
                        print("X wins")
                        break
                    elif theBoard['mid-L']=='O':
                        print("O wins")
                        break

                elif theBoard['low-L']==theBoard['low-M'] and theBoard['low-M']==theBoard['low-R']:
                    if theBoard['low-L']=='X':
                        print("X wins")
                        break
                    elif theBoard['low-L']=='O':
                        print("O wins")
                        break

                elif theBoard['top-L']==theBoard['mid-L'] and theBoard['mid-L']==theBoard['low-L']:
                    if theBoard['top-L']=='X':
                        print("X wins")
                        break
                    elif theBoard['top-L']=='O':
                        print("O wins")
                        break

                elif theBoard['top-M']==theBoard['mid-M'] and theBoard['mid-M']==theBoard['low-M']:
                    if theBoard['top-M']=='X':
                        print("X wins")
                        break
                    elif theBoard['top-M']=='O':
                        print("O wins")
                        break

                elif theBoard['top-R']==theBoard['mid-R'] and theBoard['mid-R']==theBoard['low-R']:
                    if theBoard['top-R']=='X':
                        print("X wins")
                        break
                    elif theBoard['top-R']=='O':
                        print("O wins")
                        break

                elif theBoard['top-L']==theBoard['mid-M'] and theBoard['mid-M']==theBoard['low-R']:
                    if theBoard['top-L']=='X':
                        print("X wins")
                        break
                    elif theBoard['top-L']=='O':
                        print("O wins")
                        break

                elif theBoard['top-R']==theBoard['mid-M'] and theBoard['mid-M']==theBoard['low-L']:
                    if theBoard['top-R']=='X':
                        print("X wins")
                        break
                    elif theBoard['top-R']=='O':
                        print("O wins")
                        break

        else:
            print("The position you entered is already filled")