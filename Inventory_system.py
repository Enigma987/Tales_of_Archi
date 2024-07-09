from pprint import pprint


def display_inventory(inventory):
    pprint(dict(inventory))


def add_item(item, inventory):
    dict(inventory).setdefault(item, 0)
    dict(inventory)[item] += 1

    return inventory


def removeItem(item, inventory):
    if dict(inventory)[item] == 1:
        del dict(inventory)[item]
    else:
        dict(inventory)[item] -= 1

    return inventory

