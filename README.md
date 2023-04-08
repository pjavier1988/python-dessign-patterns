# Python Dessign Patterns

## Why is this important?
It is important to know about design patterns in Python (or any programming language) because they provide proven solutions to common programming problems. By following these patterns, developers can create more efficient, maintainable, and scalable code.

Design patterns also facilitate communication among developers. They provide a common vocabulary that developers can use to discuss code and its design. This is particularly important in larger development teams, where multiple developers need to work on the same codebase.

In addition, knowledge of design patterns can also help developers to recognize and apply existing solutions to new problems, rather than trying to reinvent the wheel. This can save development time and result in more robust and reliable code.

### Singleton

In this example, we define a class called Logger which has a private class-level variable called __instance. The __new__ method is used to check if the instance already exists, and if it does, it returns the existing instance. If the instance doesn't exist, it creates a new instance.

By using the Singleton pattern in this example, it ensures that only one instance of the Logger class is created throughout the application, which helps to reduce the memory footprint and improve performance.

### Decorator
In Python, properties are used to encapsulate class attributes and provide controlled access to them. A @property decorator allows a class attribute to be accessed like a normal attribute, but with additional logic and constraints.

In the example, the Circle class has a radius attribute that can be accessed and modified using @property and @radius.setter decorators. These decorators allow us to implement validation logic to ensure that the radius is always positive.

Additionally, the diameter attribute is calculated based on the radius attribute, and the area attribute is calculated based on the radius attribute as well.

By using the @property and @setter decorators, we can encapsulate these attributes and provide controlled access to them, while also enforcing constraints and providing additional functionality.


### Facade

The CheckoutFacade class provides a simplified interface for placing an order. It encapsulates the complexities of the payment, shipping, and order objects behind a single interface. The client can create a CheckoutFacade object and call its place_order method, without worrying about the details of payment, shipping, or order processing.


### Adapter

Suppose we have a third-party library that provides functionality to work with data in a specific format, let's say it works with data in a CSV format. Now, let's say we want to use this library in our project, but we work with data in a different format, such as JSON. In this case, we can use the Adapter pattern to make the third-party library work with our data format.

In this example, we have a CSVLibrary class that works with data in CSV format. We also have a JSONAdapter class that works with data in JSON format. The CSVToJSONAdapter class is an adapter class that adapts the CSVLibrary class to work with JSON data.

We create instances of CSVLibrary and CSVToJSONAdapter classes and use them to create instances of JSONAdapter class to work with JSON data. We can then use the get_value() method of the JSONAdapter class to retrieve values from the JSON data.

This is an example of how the Adapter pattern can be used in Python to make two incompatible interfaces work together.