# Lesson 12: Inventory Management System

import os # operating system allows to check if the file exists in your computer
import json # read and write data in JSON format; json is a fancier version of dictionary
import sys # allow us to exit the program gracefully/nicely

INVENTORY_FILE = "inventory.txt"

def load_inventory():
    if not os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, "w") as file:
            json.dump([], file)
    try:
        with open(INVENTORY_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_inventory(inventory):
    with open(INVENTORY_FILE, "w") as file:
        json.dump(inventory, file, indent=4)

def add_item(inventory):
    name = input("Enter item name: ").strip().lower()
    if any(item['name'] == name for item in inventory):
        print("Item already exist")
    try:
        quantity = int(input("Enter quantity: ").strip())
        cost = float(input("Enter cost per item: ").strip())
    except ValueError:
        print("Invalid input. Quantity must be an integer, and cost must be a number.")
        return
    inventory.append({"name": name, "quantity": quantity, "cost": cost})
    save_inventory(inventory)
    print(f"Item '{name}' added successfully.")

def remove_item(inventory):
    name = input("Enter item name: ").strip().lower()
    for item in inventory:
        if item['name'] == name:
            inventory.remove(item)
            save_inventory(inventory)
            print(f"Item '{name}' removed successfully.")
            return
    print("Item not found.")

def update_item(inventory):
    name = input("Enter item name: ").strip().lower()
    for item in inventory:
        if item['name'] == name:
            print(f"Current details -> Quantity: {item['quantity']}, Cost: {item['cost']}")
            try:
                quantity = int(input("Enter new quantity: ").strip())
                cost = float(input("Enter new cost: ").strip())
                item['quantity'] = quantity
                item['cost'] = cost
                save_inventory(inventory)
                print("Item updated successfully")
                return
            except ValueError:
                print("Invalid input. Quantity must be an integer, and cost must be a number.")
                return
    print("Item not found.")

def view_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
        return
    print("\nItem Name         Quantity     Cost")
    print("-------------------------------------")
    for item in inventory:
        print(f"{item['name'].capitalize():<18} {item['quantity']}:<10 {item['cost']:.2f}")
    print("-------------------------------------")

def display_menu():
    print("\n===== Inventory Management System =====")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Update Item")
    print("4. View All Items")
    print("5. Exit")

def main():
    inventory = load_inventory()
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            add_item(inventory)
        elif choice == "2":
            remove_item(inventory)
        elif choice == "3":
            update_item(inventory)
        elif choice == "4":
            view_inventory(inventory)
        elif choice == "5":
            print("Exiting the Inventory Management System. Goodbye!")
            sys.exit() # gracefully exiting the program
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
