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

from typing import Dict

data = {
        'players': {
            'alice': {'items': {'pixel_sword': 1, 'code_bow': 1, 'health_byte': 1, 'quantum_ring': 3}, 'total_value': 1875, 'item_count': 6}, 
            'bob': {'items': {'code_bow': 3, 'pixel_sword': 2}, 'total_value': 900, 'item_count': 5}, 
            'charlie': {'items': {'pixel_sword': 1, 'code_bow': 1}, 'total_value': 350, 'item_count': 2}, 
            'diana': {'items': {'code_bow': 3, 'pixel_sword': 3, 'health_byte': 3, 'data_crystal': 3}, 'total_value': 4125, 'item_count': 12}
    }, 
        'catalog': {
            'pixel_sword': {'type': 'weapon', 'value': 150, 'rarity': 'common'}, 
            'quantum_ring': {'type': 'accessory', 'value': 500, 'rarity': 'rare'},
            'health_byte': {'type': 'consumable', 'value': 25, 'rarity': 'common'}, 
            'data_crystal': {'type': 'material', 'value': 1000, 'rarity': 'legendary'}, 
            'code_bow': {'type': 'weapon', 'value': 200, 'rarity': 'uncommon'}
    }
}

def build_inventory(player_items: Dict[str, int], catalog: Dict[str, Dict[str, object]] ) -> Dict[str, Dict[str, object]]: 
    inventory = dict()
    for item_name in player_items.keys():
        quantity = player_items.get(item_name)
        info = catalog.get(item_name)

        item = dict()
        item.update({'name': item_name})
        item.update({'category': info.get('type')})
        item.update({'rarity': info.get('rarity')})
        item.update({'value': info.get('value')})
        item.update({'quantity': quantity}) 

        inventory.update({item_name: item})
    return inventory


def transfer_item(sender: Dict[str, object], receiver: Dict[str, object], item_name: str, quantity: int) -> None:
    sender_inv = sender['inventory']
    item = sender_inv.get(item_name)

    if item is None or item['quantity'] < quantity:
        print("Not enough quantity or item not found!\n")
        return

    item['quantity'] -= quantity
    receiver_item = receiver['inventory'].get(item_name)

    if receiver_item:
        receiver_item['quantity'] += quantity
    else:
        new = dict(item)
        new['quantity'] = quantity
        receiver['inventory'].update({item_name: new})

    print(f"=== Transaction: {sender['name']} gives {receiver['name']} {quantity} {item_name}s ===")
    print("Transaction successful!\n")
    print("=== Updated Inventories ===")
    print(f"{sender['name']} {item_name}s: {sender_inv[item_name]['quantity']}")
    print(f"{receiver['name']} {item_name}s: {receiver['inventory'][item_name]['quantity']}\n")


def show_inventory(inventory: Dict[str, Dict[str, object]], player_name: str) -> None:
    total_value = 0
    total_items = 0
    categories = dict()
    
    print(f"=== {player_name}'s Inventory ===")
    for item_name in inventory.keys():
        item = inventory.get(item_name)
        stack = item.get('quantity') * item.get('value')
        total_value += stack
        total_items += item.get('quantity')
        category = item.get('category')
        current = categories.get(category)

        categories.update({category: categories.get(category, 0) + item['quantity']})
        print(f"{item['name']} ({item['category']}, {item['rarity']}) {item['quantity']}x @ {item['value']} gold each = {stack} gold")
    
    print(f"\nInventory value: {total_value} gold")
    print(f"Item count: {total_items} items")
    print("Categories: ", end="")

    first = True
    for category in categories.keys():
        if not first:
            print(", ", end="")
        print(f"{category}({categories[category]})", end="")
        first = False
    print("\n")


def ft_inventory_system() -> None:
    catalog = data['catalog']
    players_data = data['players']
    
    alice   = {'name': 'Alice', 'inventory': build_inventory(players_data['alice']['items'], catalog)}
    bob     = {'name': 'Bob', 'inventory': build_inventory(players_data['bob']['items'], catalog)}
    charlie = {'name': 'Charlie', 'inventory': build_inventory(players_data['charlie']['items'], catalog)}
    diana   = {'name': 'Diana', 'inventory': build_inventory(players_data['diana']['items'], catalog)}
    
    print("=== Player Inventory System ===\n")
    
    show_inventory(alice['inventory'], "Alice")
    show_inventory(diana['inventory'], "Diana")
    
    transfer_item(diana, alice, "data_crystal", 1)
    
    show_inventory(alice['inventory'], "Alice")
    show_inventory(diana['inventory'], "Diana")

if __name__ == '__main__':
    ft_inventory_system()
