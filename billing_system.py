class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


class Bill:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        total = 0

        for product in self.products:
            total += product.total_price()

        return total

    def calculate_tax(self):
        subtotal = self.calculate_total()
        tax = subtotal * 0.18
        return tax

    def display_bill(self):
        subtotal = self.calculate_total()
        tax = self.calculate_tax()
        final_total = subtotal + tax

        print("\n========== BILL ==========")
        print(f"{'Product':<20}{'Price':<10}{'Qty':<10}{'Total':<10}")
        print("-" * 50)

        for product in self.products:
            total = product.total_price()
            print(f"{product.name:<20}{product.price:<10}{product.quantity:<10}{total:<10}")

        print("-" * 50)
        print(f"Subtotal: ₹{subtotal:.2f}")
        print(f"Tax (18%): ₹{tax:.2f}")
        print(f"Final Total: ₹{final_total:.2f}")
        print("===========================")


# Create products
product1 = Product("Laptop", 50000, 1)
product2 = Product("Mouse", 800, 2)
product3 = Product("Keyboard", 1500, 1)

# Create bill
bill = Bill()

# Add products to bill
bill.add_product(product1)
bill.add_product(product2)
bill.add_product(product3)

# Display final bill
bill.display_bill()