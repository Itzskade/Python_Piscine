#!/usr/bin/env python3

def create_inventories() -> dict:
    """
    Creates inventories data_base based on
    data_generator given on the exercise
    """
    inventories = {
        'players': {
            'alice': {
                'items': {
                    'pixel_sword': 1,
                    'code_bow': 1,
                    'health_byte': 1,
                    'quantum_ring': 3
                },
                'total_value': 1875,
                'item_count': 6
            },
            'bob': {
                'items': {
                    'code_bow': 3,
                    'pixel_sword': 2
                },
                'total_value': 900,
                'item_count': 5
            },
            'charlie': {
                'items': {
                    'pixel_sword': 1,
                    'code_bow': 1
                },
                'total_value': 350,
                'item_count': 2
            },
            'diana': {
                'items': {
                    'code_bow': 3, 'pixel_sword': 3,
                    'health_byte': 3,
                    'data_crystal': 3
                },
                'total_value': 4125,
                'item_count': 12
            }
            },
        'catalog': {
            'pixel_sword': {
                'type': 'weapon',
                'value': 150,
                'rarity': 'common'
            },
            'quantum_ring': {
                'type': 'accessory',
                'value': 500,
                'rarity': 'rare'
            },
            'health_byte': {
                'type': 'consumable',
                'value': 25, 'rarity': 'common'
            },
            'data_crystal': {
                'type': 'material',
                'value': 1000,
                'rarity': 'legendary'
            },
            'code_bow': {
                'type': 'weapon',
                'value': 200,
                'rarity': 'uncommon'
            }
            }
        }
    return inventories


def build_inventory(player_items: dict, catalog: dict) -> dict:
    """Builds a detailed inventory dict from player items and catalog info."""
    inventory = dict()
    for item_name, quantity in player_items.items():
        info = catalog.get(item_name)
        item = {
            'name': item_name,
            'category': info.get('type'),
            'rarity': info.get('rarity'),
            'value': info.get('value'),
            'quantity': quantity
        }
        inventory[item_name] = item
    return inventory


def transfer_item(sender: dict, receiver: dict,
                  item_name: str, quantity: int) -> None:
    """Transfers quantity of item_name from sender to receiver inventories."""
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

    print(f"=== Transaction: {sender['name']} gives "
          f"{receiver['name']} {quantity} {item_name}s ===")
    print("Transaction successful!\n")
    print("=== Updated Inventories ===")
    print(f"{sender['name']} {item_name}s: "
          f"{sender_inv[item_name]['quantity']}")
    print(f"{receiver['name']} {item_name}s: "
          f"{receiver['inventory'][item_name]['quantity']}")
    print()


def show_inventory(inventory: dict, player_name: str) -> None:
    """Prints inventory summary for a player."""
    total_value = 0
    total_items = 0
    categories = dict()

    print(f"=== {player_name}'s Inventory ===")
    for item_name in inventory.keys():
        item = inventory.get(item_name)
        stack = item.get('quantity') * item.get('value')
        total_value += stack
        total_items += item.get('quantity')
        cat = item.get('category')

        categories.update({cat: categories.get(cat, 0) + item['quantity']})
        print(f"{item['name']} ({item['category']}, {item['rarity']}) "
              f"{item['quantity']}x @ {item['value']} "
              f"gold each = {stack} gold")

    print(f"\nInventory value: {total_value} gold")
    print(f"Item count: {total_items} items")
    print("Categories: ", end="")

    first = True
    for cat in categories.keys():
        if not first:
            print(", ", end="")
        print(f"{cat}({categories[cat]})", end="")
        first = False
    print("\n")


def ft_inventory_system() -> None:
    """Demonstrates the inventory system with sample transactions."""
    inventories = create_inventories()
    catalog = inventories['catalog']
    players_data = inventories['players']

    players = {}
    for name in ['alice', 'bob', 'charlie', 'diana']:
        players[name] = {
            'name': name.capitalize(),
            'inventory': build_inventory(players_data[name]['items'], catalog)
        }

    alice = players['alice']
    bob = players['bob']  # noqa
    charlie = players['charlie'] # noqa
    diana = players['diana']

    print("=== Player Inventory System ===\n")

    show_inventory(alice['inventory'], "Alice")
    show_inventory(diana['inventory'], "Diana")

    transfer_item(diana, alice, "data_crystal", 1)

    show_inventory(alice['inventory'], "Alice")
    show_inventory(diana['inventory'], "Diana")


if __name__ == '__main__':
    ft_inventory_system()
