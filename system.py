import random

dice_system = 12


def dice_throw():
    rand = random.randint(1, dice_system+1)
    return (1 / dice_system) * rand


def test(arg1):
    print("Argument 1: " + arg1)


def attack(weapon_attack, *mods):
    dice = dice_throw()
    real_attack = weapon_attack * dice

    return real_attack


def defence(armor_defence, *mods):
    dice = dice_throw()
    real_defence = armor_defence * dice

    return real_defence


def battle_result(weapon_attack, *weapon_mods, armor_defence, **armor_mods):
    attack_value = attack(weapon_attack, weapon_mods)
    defence_value = defence(armor_defence, armor_mods)

    if attack_value > defence_value:
        return "Victory"
    elif attack_value == defence_value:
        return "Draw"
    else:
        return "Lose"


