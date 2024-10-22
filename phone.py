from field import Field
from exceptions import PhoneValidationException
import re


class Phone(Field):
    def __init__(self, phone_number: str):
        if not re.match(r"^\d{10}$", phone_number):
            raise PhoneValidationException(f"Phone {phone_number} is not valid")

        super().__init__(phone_number)
