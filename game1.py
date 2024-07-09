import random

def main():
    rockList = []
    randPile = random.randint(2, 5)
    name1, name2 = get_players()

    player = name1

    get_board(rockList, randPile)
    play_again(rockList, randPile, name1, name2, player)

def get_players():
    return input("Enter player 1 name: "), input("Enter player 2 name: ")

def get_board(rockList, randPile):
    print("Let's look at the board now.")
    print("-" * 25)
    for i in range(randPile):
        redStones = random.randint(1, 8)
        blueStones = random.randint(1, 8)
        rockList.append((redStones, blueStones))
        print(f'Pile {i + 1}: {"R" * redStones} {"B" * blueStones}')
    print("-" * 25)
    nim_sum(rockList)

def get_valid_input(rockList, player):
    while True:
        stones = input(f'{player}, how many stones to remove? ')
        color = input('Which color to remove? Enter R for Red or B for Blue: ').upper()
        piles = input('Pick a pile to remove from: ')

        if stones.isdigit() and piles.isdigit() and color in ('R', 'B'):
            stones, piles = int(stones), int(piles)
            if 1 <= piles <= len(rockList):
                redStones, blueStones = rockList[piles - 1]
                if (color == 'R' and 0 < stones <= redStones) or (color == 'B' and 0 < stones <= blueStones):
                    break

        print(f"Hmmm. You entered an invalid value. Try again, {player}.")

    if color == 'R':
        rockList[piles - 1] = (redStones - stones, blueStones)
    else:
        rockList[piles - 1] = (redStones, blueStones - stones)

    continue_game(rockList, player)

def continue_game(rockList, player):
    print("Let's look at the board now.")
    print("-" * 25)
    for i, (redStones, blueStones) in enumerate(rockList):
        print(f"Pile {i + 1}: {'R' * redStones} {'B' * blueStones}")
    print("-" * 25)
    if rockList != [(0, 0)] * len(rockList):
        nim_sum(rockList)

def play_again(rockList, randPile, name1, name2, player):
    while True:
        get_valid_input(rockList, player)
        if rockList == [(0, 0)] * len(rockList):
            print(f"{player} is the winner of this round!")
            user = input("Do you want to play again? Enter y for yes, anything for no: ")
            if user.lower() == 'y':
                rockList = []
                randPile = random.randint(2, 5)
                name1, name2 = get_players()
                player = name1
                get_board(rockList, randPile)
                get_valid_input(rockList, player)
            else:
                break
        player = name2 if player == name1 else name1

def nim_sum(rockList):
    red_nim = blue_nim = 0
    for redStones, blueStones in rockList:
        red_nim ^= redStones
        blue_nim ^= blueStones
    print(f"Hint: Red nim sum is {red_nim}. Blue nim sum is {blue_nim}.")
    if red_nim > 0:
        print(f"Pick stones from the pile with {max(rockList, key=lambda x: x[0])[0]} red stones.")
    if blue_nim > 0:
        print(f"Pick stones from the pile with {max(rockList, key=lambda x: x[1])[1]} blue stones.")
    if red_nim == 0 and blue_nim == 0:
        print("Pick all stones from the pile with the most stones.")

main()