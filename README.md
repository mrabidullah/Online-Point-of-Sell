
# Online Point of Sale (POS) System

A Django-based Point of Sale (POS) and e-commerce system designed for managing products, orders, and users with a role-based admin dashboard.

The system provides a complete workflow from product browsing to order management with secure authentication and session-based cart functionality.

---

## System Overview

This application is structured as a modular Django project with separate apps for authentication, products, orders, and dashboard management.

The main workflow:

User → Browse Products → Add to Cart → Checkout → Order Creation → Admin Processing → Status Update

---

## Core Features

### Authentication System
- User registration and login
- Auto login after signup
- Session-based authentication
- Staff-only access control for dashboard

---

### Store (Customer Side)
- Product listing with search functionality
- Category-based filtering
- Product detail page
- Session-based shopping cart
- Quantity update and item removal
- Checkout system
- Order success confirmation page
- User order history

---

### Admin Dashboard (Staff Panel)
- Sales analytics dashboard
- Total orders tracking
- Pending orders monitoring
- Revenue calculation
- Product management (CRUD)
- Order management system
- Order status workflow management

Order statuses:
- Pending
- Confirmed
- Shipped
- Delivered
- Cancelled

---

### Cart and Checkout System
- Add products to cart
- Update item quantity
- Remove items from cart
- Persistent session cart
- Checkout form handling
- Automatic order creation from cart
- Stock deduction after purchase

---

## Technology Stack

- Python
- Django Framework
- SQLite Database
- HTML, CSS, Tailwind CSS
- Django Authentication System
- Session-based Cart System

---

## Project Structure

accounts/        User authentication and registration  
dashboard/       Admin panel and analytics  
orders/          Cart, checkout, and order management  
products/        Product and category management  
pos_project/     Main Django configuration  
templates/       Frontend templates  
media/           Uploaded product images  

---

## Installation Guide

### 1. Clone Repository
```bash
git clone https://github.com/mrabidullah/Online-Point-of-Sell.git
cd Online-Point-of-Sell
````

---

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Apply Migrations

```bash
python manage.py migrate
```

---

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

---

### 6. Run Development Server

```bash
python manage.py runserver
```

---

## Application Flow

### Product Flow

Products are created by admin users and displayed in the store for customers.

### Cart Flow

Products are added to a session-based cart where users can update quantities or remove items.

### Checkout Flow

Cart data is converted into an order with customer details and stored in the database.

### Order Flow

Orders move through different statuses:
Pending → Confirmed → Shipped → Delivered / Cancelled

---

## Database Models

### Product

* name
* description
* price
* stock
* category
* image
* is_active
* created_at

---

### Category

* name
* slug

---

### Order

* user
* full_name
* phone
* address
* city
* payment_method
* status
* total
* created_at

---

### OrderItem

* order
* product
* name
* price
* quantity
* subtotal (calculated property)

---

## Permissions

* Normal users can browse products and place orders
* Staff users have access to the dashboard
* Protected routes using authentication decorators

---

## Security Features

* Login required for checkout and orders
* Staff-only access for dashboard
* Order ownership validation
* Safe session-based cart handling

---

## Business Logic

* Stock automatically reduces after purchase
* Revenue calculated from completed orders
* Orders filtered by status
* Session-based cart persistence

---
##Project images
<img width="1895" height="954" alt="image" src="https://github.com/user-attachments/assets/a173134c-79e0-4b44-a2c9-8dc322f76c7b" />
<img width="1908" height="811" alt="image" src="https://github.com/user-attachments/assets/18869cba-157c-4ca4-97bd-1b840e9af06a" />
<img width="1914" height="938" alt="image" src="https://github.com/user-attachments/assets/46adbe30-170e-469d-b4af-680999dd98ab" />
<img width="1871" height="892" alt="image" src="https://github.com/user-attachments/assets/ff5b8f59-2bce-4c07-9b6f-bf0d90218913" />
<img width="1902" height="932" alt="image" src="https://github.com/user-attachments/assets/66fc7d64-a328-4fa9-a37f-e5e676dd2df6" />
<img width="1870" height="950" alt="image" src="https://github.com/user-attachments/assets/4d8c0538-e8a3-46f2-b70b-d13e9007ec6a" />
<img width="1854" height="928" alt="image" src="https://github.com/user-attachments/assets/49b503c5-9489-41bd-9157-b4845f45ad61" />
<img width="1869" height="829" alt="image" src="https://github.com/user-attachments/assets/de002abd-ca92-47c4-9acc-b5febda09ad3" />

---

## License

This project is developed for educational and commercial use.

---

## Developer

Abidullah

Django Backend Developer
Python Web Developer
E-commerce & POS System Builder

```
```
