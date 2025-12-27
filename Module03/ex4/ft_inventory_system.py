#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_inventory_system.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rmarin-n <rmarin-n@student.42barcelona.co  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/26 08:30:17 by rmarin-n          #+#    #+#              #
#    Updated: 2025/12/26 08:30:21 by rmarin-n         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import List, Dict

def create_item(name: str, category: str, rarity: str, quantity: int, value: int):
    return {'name': name, 'category': category, 'rarity': rarity, 'quantity': quantity, 'value': value}


def create_inventory():
    return dict()


def add_item(inventory: dict, item: dict):
    if item['name'] in inventory:
        inventory[item['name']]['quantity'] += item['quantity']
    else:
        inventory.update({item['name']: dict(item)})


def create_player(player: str, inventory: list):
    return {'name': player, 'inventory': inventory}


def transfer_item(sender: dict, receiver: dict, item_name: str, quantity: int):
    sender_item = sender['inventory'].get(item_name)
    if not sender_item:
        print("No item in inventory")
        return
    if sender_item['quantity'] < quantity:
        print("Not enough quantity!\n")
        return
    sender_item['quantity'] -= quantity

    receiver_item = receiver['inventory'].get(item_name)
    if receiver_item:
            receiver_item['quantity'] += quantity
    else:
        new_item = dict(sender_item)
        new_item['quantity'] = quantity
        receiver['inventory'].update({item_name: new_item})
        receiver_item = new_item

    print(f"=== Transaction: {sender['name']} gives {receiver['name']} {quantity} {item_name}s ===")
    print(f"Transaction successful!\n")
    print("=== Updated Inventories ===")
    print(f"{sender['name']} {item_name}s: {sender_item['quantity']}")
    print(f"{receiver['name']} {item_name}s: {receiver_item['quantity']}\n")


def inventory_calculator(inventory: dict):
    total_value = 0
    total_items = 0
    category_units = {}
    for item in inventory.values():
        stack_price = item['quantity'] * item['value']
        total_value += stack_price
        total_items += item['quantity']
        category = item['category']
    
        if category in category_units.keys():
            category_units.update({category: category_units.get(category) + item['quantity']})
        else:
            category_units.update({category: item['quantity']})
    return total_value, total_items, category_units


def show_inventory(inventory: dict):
    total_value, total_items, category_units = inventory_calculator(inventory)
    for item in inventory.values():
        stack_price = item['quantity'] * item['value']
        print(f"{item['name']} ({item['category']}, {item['rarity']}) {item['quantity']}x @ {item['value']} gold each = {stack_price}")

    print(f"\nInventory value: {total_value} gold")
    print(f"Item count: {total_items} items")

    categories = ""
    for category_name in category_units.keys():
        categories += f"{category_name}({category_units[category_name]}), "
    print(f"Categories: {categories[:-2]}\n")


def inventory_analytics(player1: dict, player2: dict, inventory1: dict, inventory2: dict):
    print("=== Inventory Analytics ===")

    total_value1, total_items1, _ = inventory_calculator(inventory1)
    total_value2, total_items2, _ = inventory_calculator(inventory2)
    
    if total_value1 > total_value2:
        print(f"Most valuable player: {player1['name']} ({total_value1} gold)")
    elif total_value1 < total_value2:
        print(f"Most valuable player: {player2['name']} ({total_value2} gold)")
    else:
        print(f"Both players have the same value: {total_value1} items")

    if total_items1 > total_items2:
        print(f"Most items: {player1['name']} ({total_items1} items)")
    elif total_items1 < total_items2:
        print(f"Most items: {player2['name']} ({total_items2} items)")
    else:
        print(f"Both players have the same number of items: {total_items1} items")
    rares = ""
    for inventory, player in [(inventory1, player1['name']), (inventory2, player2['name'])]:
        for item in inventory.values():
            if item['rarity'] == 'rare':
                if rares != "":
                    rares += ", "
                rares += f"{item['name']}"
    print(f"Rarest items: {rares}")


def ft_inventory_system():
    sword = create_item('sword','weapon', 'rare', 1, 500)
    potion = create_item('potion', 'consumable', 'common', 5, 50)
    shield = create_item('shield', 'armor', 'uncommon', 1, 200)
    ring = create_item('magic_ring', 'armor', 'rare', 1, 400)
    
    alice_inventory = create_inventory()
    bob_inventory = create_inventory()

    alice = create_player('Alice', alice_inventory)
    bob = create_player('Bob', bob_inventory)
   
    for item in [sword, potion, shield]:
        add_item(alice_inventory, item)
    add_item(bob_inventory, ring)

    print("=== Player Inventory System ===\n")
    
    print(f"=== {alice['name']}'s Inventory ===")
    show_inventory(alice_inventory)
    transfer_item(alice, bob, 'potion', 2)
    inventory_analytics(alice, bob, alice_inventory, bob_inventory)
    

if __name__ == '__main__':
    ft_inventory_system()
    
