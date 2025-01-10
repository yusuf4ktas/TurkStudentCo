import os

class Market:
    def __init__(self, filename='product.txt'):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                pass  # Create the file if it doesnt exist

    def __del__(self):
        pass  # Close automatically

    def list_products(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
            if not lines:
                print("Product could not be found.")
            else:
                print("\n--- Item List ---")
                for i, line in enumerate(lines, 1):
                    name, category, price, stock = line.strip().split(',')
                    print(f"{i}) Item: {name}, Category: {category}, Price: {price} TL, Stock: {stock}")

    def add_product(self):
        name = input("Item name: ")
        category = input("Category: ")
        price = input("Price: ")
        stock = input("Item number in stock: ")
        with open(self.filename, 'a') as file:
            file.write(f"{name},{category},{price},{stock}\n")
        print("Item has been added succesfully.")

    def delete_product(self):
        self.list_products()
        product_number = input("Enter the item's number to be deleted: ")
        with open(self.filename, 'r') as file:
            lines = file.readlines()
        try:
            product_number = int(product_number)
            if 1 <= product_number <= len(lines):
                deleted_product = lines.pop(product_number - 1)
                with open(self.filename, 'w') as file:
                    file.writelines(lines)
                print(f"{deleted_product.strip()} Item has been deleted.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    market = Market()
    while True:
        print("\n*** MENU ***")
        print("1) List Items")
        print("2) Add Item")
        print("3) Delete Item")
        print("4) Exit")
        choice = input("Your choice: ")
        if choice == '1':
            market.list_products()
        elif choice == '2':
            market.add_product()
        elif choice == '3':
            market.delete_product()
        elif choice == '4':
            print("Exitting the program...")
            break
        else:
            print("Invalid choice,please try again.")

if __name__ == "__main__":
    main()
