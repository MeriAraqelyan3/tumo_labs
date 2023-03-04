
import random

dice_1 = random.randrange(1, 7)
dice_2 = random.randrange(1, 7)
dice_sum = dice_1 + dice_2
won_numbers = [7, 11]
lost_numbers = [2, 3, 12]
goal_numbers = [4, 5, 6, 8, 9, 10]

if dice_sum in won_numbers:
    print(f'{dice_1} + {dice_2} = {dice_sum}')
    print("congratulations you won")
elif dice_sum in lost_numbers:
    print(f'{dice_1} + {dice_2} = {dice_sum}')
    print("you lost, try again next time")
else:
    print(f'{dice_1} + {dice_2} = {dice_sum}')
    print("goal number")
    while True:
        goal_dice_1 = random.randrange(1, 7)
        goal_dice_2 = random.randrange(1, 7)
        goal_dice_sum = goal_dice_1 + goal_dice_2
        print(f'{goal_dice_1} + {goal_dice_2} = {goal_dice_sum}')
        if goal_dice_sum == 7:
            print("you lost, try again next time")
            break
        elif goal_dice_sum == dice_sum:
            print('you won')
            break
