from random import choice
from random import shuffle
from random import randint
from statistics import mean

print(mean([100, 90]))

coin = choice([1, 2,3,4,5,6])
print(coin)

number = randint(1, 10)
print(number)

cards = ["jack", "queen", "king"]
shuffle(cards)
for card in cards:
    print(card)
    
