import pytest

from strategy import (PaymentProcessor,
                      StripeGateway,
                      PayPalGateway,
                      WrongGateway)





def test_process_payment_with_stripe():
    amount = 10
    stripe_gateway = StripeGateway()
    payment_processor = PaymentProcessor(stripe_gateway)

    assert payment_processor.process_payment(amount) == f"Paying {amount} using Stripe"


def test_process_payment_with_paypal():
    amount = 10
    paypal_gateway = PayPalGateway()
    payment_processor = PaymentProcessor(paypal_gateway)

    assert payment_processor.process_payment(amount) == f"Paying {amount} using Paypal"


def test_process_payment_with_unknown_payment_type():
    with pytest.raises(ValueError):
        payment_processor = PaymentProcessor(WrongGateway)
        payment_processor.process_payment("invalid payment type")