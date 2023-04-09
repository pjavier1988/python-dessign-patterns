from observer import (NewsPublisher,
                      EmailSubscriber,
                      SMSSuscriber)
import pytest

@pytest.fixture
def news_publisher():
    return NewsPublisher()


def test_register_subscriber(news_publisher):
    email_suscriber = EmailSubscriber("test@example.com")

    news_publisher.register(email_suscriber)

    assert email_suscriber in news_publisher.subscribers


def test_unregister_subscriber(news_publisher):
    email_suscriber = EmailSubscriber("test@example.com")
    email_suscriber2 = EmailSubscriber("test@example.com")

    news_publisher.register(email_suscriber)
    news_publisher.register(email_suscriber2)
    news_publisher.unregister(email_suscriber)

    assert email_suscriber not in news_publisher.subscribers
    assert email_suscriber2 in news_publisher.subscribers


def test_notify_subscribers(news_publisher, capsys):
    expected_email = "test@example.com"
    expected_number = "+123123123132"
    expected_title = "Test title"
    expected_content = "Test content"
    email_subscriber = EmailSubscriber(expected_email)
    sms_subscriber = SMSSuscriber(expected_number)
    news_publisher.register(email_subscriber)
    news_publisher.register(sms_subscriber)
    news_publisher.publish(expected_title, expected_content)

    captured = capsys.readouterr()
    assert f"Breaking news: {expected_title}\n{expected_content}\nEmail received by {expected_email}\n" in captured.out
    assert f"Breaking news: {expected_title}\n{expected_content}\nSMS received by {expected_number}\n" in captured.out
