class ShippingService:
    def calculate_shipping(self, user):
        if user["country"] == "CO":
            return 20000
        return 50000