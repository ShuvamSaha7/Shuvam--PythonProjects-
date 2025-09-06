# shuffle deck of cards

# using RANDOM MODULE and ITERTOOLS

import random, itertools

deck = list(itertools.product(range(1,14),["Spade", "Club", "Hearts", "Diamond"]))

print(deck)


#shuffle

random.shuffle(deck)

print(deck)

for i in range(5):
    print(deck[i] [0], "of", deck[i] [1])

    