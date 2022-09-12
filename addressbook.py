import logging

logging.basicConfig(filename='Address Book.log', filemode='a', level=logging.DEBUG)

TABLE = "{:<20}{:<20}{:<20}{:<20}{:<20}"


class Contact:
    def __init__(self, record_dict):
        """
        Constructor for contact class
        :param record_dict:
        """
        self.name = record_dict.get("name")
        self.email = record_dict.get("email")
        self.phone = record_dict.get("phone")
        self.city = record_dict.get("city")
        self.state = record_dict.get("state")

    def show_details(self):
        """
        Function for showing details entered in dictionary
        :return:
        """
        try:
            return self.__dict__
            # return {"name": {self.name}, "email": {self.email}, "phone": {self.phone}, "city": {self.city},
            #         "state": {self.state}}
        except Exception as e:
            logging.exception(e)


class AddressBook:
    def __init__(self, book_name):
        """
        Constructor for AddressBook class
        :param book_name:
        """
        self.book_name = book_name
        self.records = {}

    def add_contacts(self, contact_obj):
        """
        Function to add contacts in address book
        :param contact_obj:
        :return:
        """
        try:
            self.records.update({contact_obj.name: contact_obj})
            # return self.records
        except Exception as e:
            logging.warning("Error occurred")
            logging.exception(e)

    def display_contacts(self):
        """
        Function to display stored contacts
        :return:
        """
        try:
            objs = self.records.values()
            if objs:
                print(TABLE.format("name", "email", "phone", "city", "state"))
                for item in objs:
                    values = item.show_details().values()
                    print(TABLE.format(*values))
                return
            print("########### No data found ###########")
        except Exception as e:
            logging.exception(e)

    def delete_record(self, name):
        """
        Function to remove stored contacts
        :param name:
        :return:
        """
        try:
            self.records.pop(name)
        except Exception as e:
            logging.exception(e)


if __name__ == '__main__':
    contact1 = Contact(
        {"name": "Amit", "email": "amit836@gmail.com", "phone": "9936958584", "city": "Vns", "state": "UP"})
    details1 = contact1.show_details()
    book1 = AddressBook("my_book")
    print(book1.add_contacts(contact1))
    print(book1.display_contacts())
    print(book1.delete_record("Amit"))
    print(book1.display_contacts())