class DiscountService:
    def apply_discount(self, user, total):
        if user["type"] == "regular":
            return total * 0.95
        elif user["type"] == "premium":
            return total * 0.90
        elif user["type"] == "vip":
            return total * 0.80
        return total

    def extra_discount(self, total):
        if total > 500:
            return total * 0.95
        return total