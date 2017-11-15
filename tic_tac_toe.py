def init():
    print('\t\t\t\t    |   |    ')
    print('\t\t\t\t  T | I |  C ')
    print('\t\t\t\t____|___|____')
    print('\t\t\t\t    |   |    ')
    print('\t\t\t\t  T | A |  C ')
    print('\t\t\t\t____|___|____')
    print('\t\t\t\t    |   |    ')
    print('\t\t\t\t  T | O |  E ')
    print('\t\t\t\t    |   |    \n\n\n')
def printnum(l):
    print('    |   |    ')
    print(l[0]+'   | '+l[1]+' | '+l[2] )
    print('____|___|____')
    print('    |   |    ')
    print(l[3]+'   | '+l[4]+' | '+l[5] )
    print('____|___|____')
    print('    |   |    ')
    print(l[6]+'   | '+l[7]+' | '+l[8] )
    print('    |   |    ')
def side():
    p1=input('\n\nenter your choice X or O  ').upper()
    return p1
def choice():
    k=int(input('enter position :'))
    return k;
l=['0','1','2','3','4','5','6','7','8']
def printboard():
    print('\t\t\t\t    |   |    ')
    print('\t\t\t\t'+l[0]+'   | '+l[1]+' | '+l[2] )
    print('\t\t\t\t____|___|____')
    print('\t\t\t\t    |   |    ')
    print('\t\t\t\t'+l[3]+'   | '+l[4]+' | '+l[5] )
    print('\t\t\t\t____|___|____')
    print('\t\t\t\t    |   |    ')
    print('\t\t\t\t'+l[6]+'   | '+l[7]+' | '+l[8] )
    print('\t\t\t\t    |   |    \n')
def rand():
    import random
    r=random.randint(0,9)
    return r
def player(p1):
    if(p1=='X'):
        p2='O'
    else:
        p2='X'
    return p2
def win_check(board,mark):
    
    return ((board[6] == mark and board[7] == mark and board[8] == mark) or # across the top
    (board[3] == mark and board[4] == mark and board[5] == mark) or # across the middle
    (board[0] == mark and board[1] == mark and board[2] == mark) or # across the bottom
    (board[6] == mark and board[3] == mark and board[0] == mark) or # down the middle
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the right side
    (board[6] == mark and board[4] == mark and board[2] == mark) or # diagonal
    (board[8] == mark and board[4] == mark and board[0] == mark)) # diagonal
def prp():   
    printboard()
    p1=side()
    p2=player(p1)
    print('Player 1= X\n\ncomputer=O')
    global l
    l=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    tem=[0,1,2,3,4,5,6,7,8]
    num=['0','1','2','3','4','5','6','7','8']
    correctind=[0,1,2,3,4,5,6,7,8]
    while tem!=[]:
        k=choice()
        def secondchance():
            r=rand()
            ex=0
            while ex==0:
                if r in tem:
                    i=correctind.index(r)
                    tem.remove(r)
                    num[i]=' '
                    l[i]=p2
                    printboard()
                    ex=1
                else:
                    r=rand()
        if k in tem:
            i=correctind.index(k)
            tem.remove(k)
            l[i]=p1
            num[i]=' '
            printboard()
            
        else:
            print('incorrect position entered')
        
        pw1=win_check(l,p1)
        pw2=win_check(l,p2)
    
        if pw1==True:
            print('congratulations!!!\n\n     \"player 1\" is the !!__winner__!!')
            break
        if pw2==True:
            print('__you lose__\n\ncomputer is the !!__winner__!!')
            break
        secondchance()
        printnum(num)
init()
prp()
