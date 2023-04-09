from observer import NewsPublisher, EmailSubscriber
import pytest

@pytest.fixture
def news_publisher():
    return NewsPublisher()


def test_add_subscriber(news_publisher):
    email_suscriber = EmailSubscriber("test@example.com")

    news_publisher.register(email_suscriber)

    assert email_suscriber in news_publisher.subscribers


def test_remove_subscriber(news_publisher):
    email_suscriber = EmailSubscriber("test@example.com")
    email_suscriber2 = EmailSubscriber("test@example.com")

    news_publisher.register(email_suscriber)
    news_publisher.register(email_suscriber2)
    news_publisher.unregister(email_suscriber)

    assert email_suscriber not in news_publisher.subscribers
    assert email_suscriber2 in news_publisher.subscribers


def test_notify_subscribers(news_publisher, capsys):
    email_subscriber = EmailSubscriber("test@example.com")

    news_publisher.register(email_subscriber)

    news_publisher.publish("Test title", "Test content")

    captured = capsys.readouterr()
    assert "Breaking news: Test title\nTest content\nPublished by test@example.com\n" in captured.out
