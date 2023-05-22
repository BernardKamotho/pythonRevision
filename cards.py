cards = ['ace','jack','queen','king']
points = 0

for x in range(6):
    import random
    random.shuffle(cards)

print('current card is', cards[0])

random.shuffle(cards)

answer =str(input("enter card:"))

if answer == cards[0]:
    print("correct card!")
else:
    print("card not correct",cards[0])

print("game over", points)
