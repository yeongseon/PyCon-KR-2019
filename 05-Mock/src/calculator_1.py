"""

"""
import logging

logging.basicConfig(level=logging.INFO)


class Calculator():
    """Calculator class"""

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def add(self, a, b):
        self.logger.info(
            "add {a} to {b} is {result}".format(
                a=a, b=b, result=a + b
            ))
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b


calculator = Calculator()
calculator.add(1, 2)
