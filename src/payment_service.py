class PaymentService:
    def process_payment(self, payment_type):
        if payment_type == "card":
            print("Procesando tarjeta...")
        elif payment_type == "paypal":
            print("Procesando PayPal...")
        elif payment_type == "cash":
            print("Pago en efectivo...")
        else:
            raise Exception("Método de pago inválido")