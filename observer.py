class NewsPublisher:
    def __init__(self):
        self.subscribers = set()

    def register(self, subscriber):
        self.subscribers.add(subscriber)

    def unregister(self, subscriber):
        self.subscribers.remove(subscriber)

    def publish(self, article_title, article_content):
        for subscriber in self.subscribers:
            subscriber.update(article_title, article_content)


class Subscriber:
    def update(self, article_title, article_content):
        pass


class EmailSubscriber(Subscriber):
    def __init__(self, email) -> None:
        super().__init__()
        self.email = email

    def update(self, article_title, article_content):
        print("Breaking news: %s" % article_title)
        print(article_content)
        print(f"Published by {self.email}")


if __name__ == "__main__":
    publisher = NewsPublisher()
    suscriber = EmailSubscriber("mail@mail.com")

    publisher.register(suscriber)
    publisher.publish("New article", "First article published by suscriber")




