import random

balance = 100

class Game():
    while (True):
        print('Balance : ' + str(balance))
        einsatz = input('Wie viel möchtest du setzten : ')
        if (int(einsatz) <= int(balance)):
            balance = int(balance) - int(einsatz)
            multiplier = 0.0
            chance = 2

            while(int(chance) >= 2):
                print(str(multiplier) + 'x')
                multiplier = multiplier + round(random.uniform(1.01, 1.49), 3)
                chance = random.randrange(1, 15, 1)
                weiter = input('Möchtest du weiter spielen (J/N): ')
                if (weiter == 'n'):
                    chance = 0
            if(chance == 0):
                balance = int(balance) + int(einsatz) * int(multiplier)
                print(balance)

            if(chance == 1):
                print('Crashed!')
        else:
            print('Du kannst nicht ins Minus gehen!')