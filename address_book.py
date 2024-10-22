from collections import UserDict
from record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        return self.data[name]

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]
