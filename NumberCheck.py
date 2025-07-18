import random
n=random.randint(1,50)
def game(n):
    chance=1
    while chance<=3:
        a=int(input('enter your choice : '))
        if a==n:
            print('you won')
            break
        elif a>n:
            print('go lower')
            chance=+1
        else:
            print('go higher')
            chance=+1
    
    if chance==3 and n!=a:
        print(' sorry!! you loose')
    elif chance>3:
        print('the number was {n}')
game(n)