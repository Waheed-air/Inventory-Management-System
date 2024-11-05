# Inventory Management System

This Inventory Management System is a console-based application that allows users with different roles to manage a product inventory. It includes features for adding, editing, viewing, and deleting products, as well as managing stock levels. 

## Features

- **User Authentication and Role-based Access Control**
  - Admin users have full access to inventory management functions.
  - Standard users can view and search for products.
  
- **Product Management**
  - Admins can add, edit, and delete products.
  - Admins can adjust stock levels.
  - Products are searchable by name and category.

- **Stock Alerts**
  - Products with low stock (below 10 units) are flagged for restocking.

## Classes

### User
Handles user data and authentication. Each user has:
- `username`
- `password`
- `role` (Admin or User)

### Product
Represents a product in the inventory. Each product has:
- `product_id`
- `name`
- `category`
- `price`
- `stock_quantity`

### InventoryManagementSystem
Main class for managing users and products. Features:
- User management (`add_user`, `login`)
- Product management (`add_product`, `edit_product`, `delete_product`)
- Stock adjustment (`adjust_stock`)
- Product search and display (`view_products`, `search_product`)

## Usage

1. Run the script to start the Inventory Management System.
2. Choose "Login" and enter a username and password.
   - Example credentials:
     - Admin: `username: admin`, `password: adminpass`
     - User: `username: user`, `password: userpass`
3. Based on the user's role, the appropriate menu will be displayed with available options.

## Sample Admin Menu Options

1. **Add Product**: Adds a new product with `product_id`, `name`, `category`, `price`, and `stock_quantity`.
2. **Edit Product**: Modifies existing product attributes.
3. **Delete Product**: Deletes a product by `product_id`.
4. **View All Products**: Displays a list of products, highlighting items below the stock threshold.
5. **Search Product**: Searches by `name` or `category`.
6. **Adjust Stock**: Increases or decreases product stock.
7. **Logout**: Ends the admin session.

## Getting Started

### Prerequisites
- Python 3.x installed on your machine.

### Running the Program
To start the program, simply run:
```bash
python inventory_management_system.py
