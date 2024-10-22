from phone import Phone
from name import Name


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone_number: str):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number: str):
        self.phones = [p for p in self.phones if p.value != phone_number]

    def edit_phone(self, current_number: str, new_number: str):
        for index, phone in enumerate(self.phones):
            if phone.value == current_number:
                self.phones[index] = Phone(new_number)

    def find_phone(self, number: str) -> Phone | None:
        for phone in self.phones:
            if phone.value == number:
                return phone
