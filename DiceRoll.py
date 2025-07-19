import random
print('Welcome guys!! let us play a dice game')
print('1.Roll the dice')
option=int(input('enter option: '))
dice=random.randint(1,6)
while True:
    if option ==1:
        if dice==6:
            print('you won')
        else:
            print(dice)
            break
            