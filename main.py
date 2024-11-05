# User class for authentication and role-based access
class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def authenticate(self, password):
        return self.password == password

# Product class with attributes and methods for inventory management
class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def update_stock(self, quantity):
        self.stock_quantity += quantity

# Inventory Management System class containing main functionalities
class InventoryManagementSystem:
    MINIMUM_STOCK_THRESHOLD = 10

    def __init__(self):
        self.users = {}  # Dictionary to store users
        self.products = {}  # Dictionary to store products

    def add_user(self, username, password, role):
        self.users[username] = User(username, password, role)

    def login(self, username, password):
        user = self.users.get(username)
        if user and user.authenticate(password):
            return user
        else:
            raise ValueError("Invalid username or password")

    def add_product(self, user, product_id, name, category, price, stock_quantity):
        if user.role != "Admin":
            print("Permission denied. Only Admin can add products.")
            return
        if product_id in self.products:
            print("Product with this ID already exists.")
            return
        self.products[product_id] = Product(product_id, name, category, price, stock_quantity)
        print("Product added successfully.")

    def edit_product(self, user, product_id, name=None, category=None, price=None, stock_quantity=None):
        if user.role != "Admin":
            print("Permission denied. Only Admin can edit products.")
            return
        product = self.products.get(product_id)
        if not product:
            print("Product not found.")
            return

        if name:
            product.name = name
        if category:
            product.category = category
        if price is not None:
            product.price = price
        if stock_quantity is not None:
            product.stock_quantity = stock_quantity
        print("Product updated successfully.")

    def delete_product(self, user, product_id):
        if user.role != "Admin":
            print("Permission denied. Only Admin can delete products.")
            return
        if product_id in self.products:
            del self.products[product_id]
            print("Product deleted successfully.")
        else:
            print("Product not found.")

    def view_products(self):
        if not self.products:
            print("No products available.")
            return
        for product_id, product in self.products.items():
            print(f"ID: {product_id}, Name: {product.name}, Category: {product.category}, "
                  f"Price: ${product.price}, Stock: {product.stock_quantity}")
            if product.stock_quantity < self.MINIMUM_STOCK_THRESHOLD:
                print(" - Low stock! Consider restocking.")

    def search_product(self, name=None, category=None):
        results = [product for product in self.products.values()
                   if (name and product.name == name) or (category and product.category == category)]
        if not results:
            print("No matching products found.")
            return
        for product in results:
            print(f"ID: {product.product_id}, Name: {product.name}, Category: {product.category}, "
                  f"Price: ${product.price}, Stock: {product.stock_quantity}")

    def adjust_stock(self, user, product_id, quantity):
        if user.role != "Admin":
            print("Permission denied. Only Admin can adjust stock levels.")
            return
        product = self.products.get(product_id)
        if not product:
            print("Product not found.")
            return
        product.update_stock(quantity)
        print("Stock adjusted successfully.")

# Sample data setup
ims = InventoryManagementSystem()
ims.add_user("admin", "adminpass", "Admin")
ims.add_user("user", "userpass", "User")

# Console menu for system interaction
def main_menu():
    print("\nInventory Management System")
    print("1. Login")
    print("2. Exit")

def admin_menu():
    print("\nAdmin Menu")
    print("1. Add Product")
    print("2. Edit Product")
    print("3. Delete Product")
    print("4. View All Products")
    print("5. Search Product")
    print("6. Adjust Stock")
    print("7. Logout")

def user_menu():
    print("\nUser Menu")
    print("1. View All Products")
    print("2. Search Product")
    print("3. Logout")

# Main program loop
current_user = None
while True:
    if not current_user:
        main_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            try:
                current_user = ims.login(username, password)
                print(f"Welcome, {current_user.username}!")
            except ValueError as e:
                print(e)
        elif choice == "2":
            print("Exiting the system.")
            break
    else:
        if current_user.role == "Admin":
            admin_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                product_id = input("Product ID: ")
                name = input("Product Name: ")
                category = input("Category: ")
                price = float(input("Price: "))
                stock_quantity = int(input("Stock Quantity: "))
                ims.add_product(current_user, product_id, name, category, price, stock_quantity)
            elif choice == "2":
                product_id = input("Product ID to edit: ")
                name = input("New Name (leave blank to skip): ")
                category = input("New Category (leave blank to skip): ")
                price = input("New Price (leave blank to skip): ")
                stock_quantity = input("New Stock Quantity (leave blank to skip): ")
                ims.edit_product(current_user, product_id, name or None, category or None,
                                 float(price) if price else None,
                                 int(stock_quantity) if stock_quantity else None)
            elif choice == "3":
                product_id = input("Product ID to delete: ")
                ims.delete_product(current_user, product_id)
            elif choice == "4":
                ims.view_products()
            elif choice == "5":
                name = input("Search by name (leave blank to skip): ")
                category = input("Search by category (leave blank to skip): ")
                ims.search_product(name or None, category or None)
            elif choice == "6":
                product_id = input("Product ID to adjust stock: ")
                quantity = int(input("Quantity (positive to add, negative to reduce): "))
                ims.adjust_stock(current_user, product_id, quantity)
            elif choice == "7":
                current_user = None
                print("Logged out.")
        elif current_user.role == "User":
            user_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                ims.view_products()
            elif choice == "2":
                name = input("Search by name (leave blank to skip): ")
                category = input("Search by category (leave blank to skip): ")
                ims.search_product(name or None, category or None)
            elif choice == "3":
                current_user = None
                print("Logged out.")
