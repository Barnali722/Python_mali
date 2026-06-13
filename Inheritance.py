# Base Class (Parent)
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_details(self):
        return f"{self.name} - ₹{self.price:.2f}"

    def calculate_tax(self):
        # Default tax is 5%
        return self.price * 0.05


# Derived Class (Child) for Electronics
class Electronics(Product):
    def __init__(self, name, price, warranty_months):
        # Inherit name and price from Product
        super().__init__(name, price)
        self.warranty_months = warranty_months

    # Overriding the details method to include warranty
    def get_details(self):
        return f"{self.name} (₹{self.price:.2f}) [Warranty: {self.warranty_months} months]"


# Derived Class (Child) for Clothing
class Clothing(Product):
    def __init__(self, name, price, size):
        # Inherit name and price from Product
        super().__init__(name, price)
        self.size = size

    # Overriding the tax method because clothing has a different tax rate (e.g., 2%)
    def calculate_tax(self):
        return self.price * 0.02

    def get_details(self):
        return f"{self.name} - Size: {self.size} (₹{self.price:.2f})"
    
class Sports(Product):
    def __init__(self, name, price,size,):
        super().__init__(name, price)
        self.size = size

    def calculate_tax(self):
        return self.price * 0.01
    
    def get_details(self):
        return f"{self.name} - Size: {self.size} (₹{self.price:.2f})"


# --- Running the E-commerce System ---

# Creating a shopping cart with different items
cart = [
    Electronics("Wireless Headphones", 150.00, warranty_months=12),
    Clothing("Winter Jacket", 80.00, size="L"),
    Sports("Indian Team Jersey",2000.00, size="XL"),
    Sports("Cricket Bat",80.00, size= "null"),
    Product("Coffee Mug", 12.00) # A generic product
]

print("--- YOUR RECEIPT ---")
total_bill = 0

for item in cart:
    # Python automatically knows which 'get_details' and 'calculate_tax' to call!
    details = item.get_details()
    tax = item.calculate_tax()
    item_total = item.price + tax
    total_bill += item_total
    
    print(f"{details} | Tax: ₹{tax:.2f} | Total: ₹{item_total:.2f}")

print("-" * 20)
print(f"GRAND TOTAL: ₹{total_bill:.2f}")