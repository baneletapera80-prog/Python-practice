inventory = {}

def add_item(product_id, product_name,product_category, product_quantity, product_price, product_supplier):
    if product_id in inventory:
        print("Item already exists in the inventory.")
    else:
        inventory[product_id] = {
            "name": product_name,
            "category": product_category,
            "quantity": product_quantity,
            "price": product_price,
            "supplier": product_supplier
        }
        print("Item added successfully.")

def view_product(product_id):
    if product_id in inventory:
        details = inventory[product_id]
        print(f"Product ID: {product_id}")
        print(f"Name: {details['name']}")
        print(f"Category: {details['category']}")
        print(f"Quantity: {details['quantity']}")
        print(f"Price: R{details['price']}")
        print(f"Supplier: {details['supplier']}")
    else:
        print("Product not found.")

def search_product(product_name):
    found = False
    for product_id, details in inventory.items():
        if details['name'].lower() == product_name.lower():
            print(f"Product ID: {product_id}")
            print(f"Name: {details['name']}")
            print(f"Category: {details['category']}")
            print(f"Quantity: {details['quantity']}")
            print(f"Price: R{details['price']}")
            print(f"Supplier: {details['supplier']}")
            found = True
    if not found:
        print("Product not found.")

def edit_product(product_id, product_name=None, product_category=None, product_quantity=None, product_price=None, product_supplier=None):
    if product_id in inventory:
        if product_name:
            inventory[product_id]['name'] = product_name
        if product_category:
            inventory[product_id]['category'] = product_category
        if product_quantity is not None:
            inventory[product_id]['quantity'] = product_quantity
        if product_price is not None:
            inventory[product_id]['price'] = product_price
        if product_supplier:
            inventory[product_id]['supplier'] = product_supplier
        print("Product details updated successfully.")
    else:
        print("Product not found.")

def delete_product(product_id):
    if product_id in inventory:
        del inventory[product_id]
        print("Product deleted successfully.")
    else:
        print("Product not found.")

def update_stock(product_id, quantity):
    if product_id in inventory:
        inventory[product_id]['quantity'] += quantity
        print("Stock updated successfully.")
    else:
        print("Product not found.")

def save_inventory_to_file(filename):
    with open(filename, 'w') as file:
        for product_id, details in inventory.items():
            line = f"{product_id},{details['name']},{details['category']},{details['quantity']},{details['price']},{details['supplier']}\n"
            file.write(line)

def load_inventory_from_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                product_id, name, category, quantity, price, supplier = line.strip().split(',')
                inventory[product_id] = {
                    "name": name,
                    "category": category,
                    "quantity": int(quantity),
                    "price": float(price),
                    "supplier": supplier
                }
    except FileNotFoundError:
        print("Inventory file not found.")

def main():
    load_inventory_from_file('inventory.txt')
    while True:
        print("=======================================")
        print("\nInventory Management System for Ndzilo ")
        print("1. Add Item")
        print("2. View Product")
        print("3. Search Product")
        print("4. Edit Product")
        print("5. Delete Product")
        print("6. Update Stock")
        print("7. Save Inventory to File")
        print("8. Exit")
        print("======================================")

        choice = input("Enter your choice: ")

        if choice == '1':
            product_id = input("Enter Product ID: ")
            product_name = input("Enter Product Name: ")
            product_category = input("Enter Product Category: ")
            product_quantity = int(input("Enter Product Quantity: "))
            product_price = float(input("Enter Product Price: "))
            product_supplier = input("Enter Product Supplier: ")
            add_item(product_id, product_name, product_category, product_quantity, product_price, product_supplier)
        elif choice == '2':
            product_id = input("Enter Product ID to view: ")
            view_product(product_id)
        elif choice == '3':
            product_name = input("Enter Product Name to search: ")
            search_product(product_name)
        elif choice == '4':
            product_id = input("Enter Product ID to edit: ")
            product_name = input("Enter new Product Name (leave blank to skip): ")
            product_category = input("Enter new Product Category (leave blank to skip): ")
            product_quantity_input = input("Enter new Product Quantity (leave blank to skip): ")
            product_price_input = input("Enter new Product Price (leave blank to skip): ")
            product_supplier = input("Enter new Product Supplier (leave blank to skip): ")

            product_quantity = int(product_quantity_input) if product_quantity_input else None
            product_price = float(product_price_input) if product_price_input else None

            edit_product(product_id, product_name or None, product_category or None, 
                         product_quantity, product_price, product_supplier or None)
        elif choice == '5':
            product_id = input("Enter Product ID to delete: ")
            delete_product(product_id)
        elif choice == '6':
            product_id = input("Enter Product ID to update stock: ")
            quantity = int(input("Enter quantity to add/remove (use negative for removal): "))
            update_stock(product_id, quantity)
        elif choice == '7':
            save_inventory_to_file('inventory.txt')
        elif choice == '8':
            save_inventory_to_file('inventory.txt')
            print("Exiting the system. Goodbye!")
            break 
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()