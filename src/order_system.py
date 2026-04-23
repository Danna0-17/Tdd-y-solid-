import random
from discount_service import DiscountService
from tax_service import TaxService
from shipping_service import ShippingService
from payment_service import PaymentService

class OrderSystem:
    def __init__(self):
        self.orders = []
        self.discount_service = DiscountService()
        self.tax_service = TaxService()
        self.shipping_service = ShippingService()
        self.payment_service = PaymentService()

    def create_order(self, user, items, payment_type):
        total = sum(item["price"] * item["quantity"] for item in items)

        total = self.discount_service.apply_discount(user, total)
        total = self.discount_service.extra_discount(total)
        total = self.tax_service.apply_tax(total)
        total += self.shipping_service.calculate_shipping(user)

        self.payment_service.process_payment(payment_type)

        order = {
            "id": random.random(),
            "user": user,
            "items": items,
            "total": total,
            "status": "created"
        }

        self.orders.append(order)

        if "email" in user:
            print(f"Enviando correo a {user['email']}")

        return order