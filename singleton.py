class Logger:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Logger, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def log(self, message):
        print(message)

# Creating instances of the Logger class


logger1 = Logger()
logger2 = Logger()

# Both logger1 and logger2 refer to the same instance
print(f"Both instances are the same? {logger1 == logger2}")  # Output: True

# Logging messages using loggers
logger1.log("Logog message from logger1")

logger2.log("Log message from logger2")
