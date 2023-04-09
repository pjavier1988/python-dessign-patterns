class PaymentGateway:
    def pay(self, amount):
        pass


class PayPalGateway(PaymentGateway):
    def pay(self, amount):
        return f"Paying {amount} using Paypal"


class StripeGateway(PaymentGateway):
    def pay(self, amount):
        return f"Paying {amount} using Stripe"


class WrongGateway():
    def pay(self, amount):
        return f"Paying {amount} using Stripe"


class PaymentProcessor:
    def __init__(self, gateway):
        if not isinstance(gateway, PaymentGateway):
            raise ValueError("invalid payment typ.")
        self.gateway = gateway

    def process_payment(self, amount):
        return self.gateway.pay(amount)


paypal_gateway = PayPalGateway()
payment_processor = PaymentProcessor(paypal_gateway)
payment_processor.process_payment(100)

stripe_gateway = StripeGateway()
payment_processor = PaymentProcessor(stripe_gateway)
payment_processor.process_payment(100)
