import random
import figid
number_of_hands = 2
total_hands = number_of_hands
used_hands = 0
points_to_score = 40
score = 0
while number_of_hands != 0:
    print("\nNew hand\n\nYou have to score", points_to_score, "points.\n\nYou currently have", score, "points and", number_of_hands, "hands.\n")
    wannaknowpoints = 0
    wannaknowpoints = input("Do you want to know what\neach hand give? y/n")
    if wannaknowpoints == "y":
        print("\n\nPair gives 10 points\nThree of a kind gives 20 points\n Small Straight and Full House both give 30 points\nFour of a kind gives 35 points\nBig Straight gives 40 points\nFive of a kind gives 50 points")
    dice = []
    keep = []
    for i in range(5):
        dice.append(random.randint(1,6))
    dice.sort()
    print("\nHere are your dice\n")
    print("     ", dice)
    number_of_reroll = 2
    reroll = input("\ndo you want to reroll? (y/n)")
    if reroll == "y":
        for i in range(number_of_reroll):
            for i in range(5):
                answer = input(f"Keep die {i+1}? (y/n)")
                if answer == ("n"):
                    dice[i] = random.randint(1,6)
            dice.sort()
            print(dice)
        if i == 2:
            reroll = input("\ndo you want to reroll? (y/n)")
            if reroll == "n":
                    number_of_reroll = i
    figure=figid.figure_det(dice)
    if figure == 8:
        score += 50
    elif figure == 7:
        score += 40
    elif figure == 6:
        score += 35
    elif figure == 5:
        score += 30
    elif figure == 4:
        score += 30
    elif figure == 3:
        score += 20
    elif figure == 2:
        score += 10
    number_of_hands -=1
    used_hands += 1
    if score >= points_to_score:
        number_of_hands =  0
    if number_of_hands > 0:
        idkhahaha= input("\nContinue to next hand\n(press enter)")
if score >= points_to_score:
    print("You have", score, "points\nwith", total_hands-used_hands, "hands remaining\nYou won!")
