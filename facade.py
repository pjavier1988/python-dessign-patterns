class Shipping:
    def __init__(self, name, address, city):
        self.name = name
        self.address = address
        self.city = city


class Payment:
    def __init__(self, card_number, cvv):
        self.card_number = card_number
        self.cvv = cvv


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self, items):
        self.items = items

    def get_total(self):
        total = 0
        for item in self.items:
            total += item.price

        return total


class CheckoutFacade:
    def __init__(self, name, address, city, card_number, cvv, items):
        self.shipping = Shipping(name, address, city)
        self.payment = Payment(card_number, cvv)
        self.order = Order(items)

    def place_order(self):
        print("Processing payment...")
        print(f"Payment of ${self.order.get_total()} accepted.")
        print("Shipping items...")
        print(f"Items shipped to {self.shipping.name} at "
              f"{self.shipping.address}, {self.shipping.city}")


if __name__ == "__main__":
    item1 = Item("Pizza", 20)
    item2 = Item("Water", 1)
    items = [item1, item2]
    payment = CheckoutFacade("Customer", "Street1", "Great City",
                             "5434344", "123", items)

    payment.place_order()
