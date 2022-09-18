import csv
import json
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

    def json_write(self):
        """
        Function to add dictionary dta into json file
        :return:
        """
        try:
            records_dict = {}
            for k, v in self.records.items():
                records_dict.update({k: v.show_details()})
            return {"name": self.book_name, "records": records_dict}
        except Exception as e:
            logging.exception(e)


def create_addressbook():
    """
    Hanging function to create address books
    :return:
    """
    try:
        book = input("Enter addressbook name : ")
        book_obj = AddressBook(book)
        addressbook_dict.update({book_obj.book_name: book_obj})
        return addressbook_dict
    except Exception as e:
        logging.exception(e)


def display_list_of_addressbook():
    """
    Hanging function to show all the address books
    :return:
    """
    try:
        print("Book_name")
        for book_name in addressbook_dict:
            print(book_name)
    except Exception as e:
        logging.exception(e)


def add_person():
    """
    Hanging function to add person in different address books
    :return:
    """
    try:
        book = input("Enter addressbook name : ")
        book_obj = addressbook_dict.get(book)
        if book_obj is None:
            book_obj = AddressBook(book)
            addressbook_dict.update({book_obj.book_name: book_obj})
        name = input("\nEnter your Name : ")
        email = input("Enter your Email : ")
        phone = input("Enter your Phone Number : ")
        city = input("Enter your City Name : ")
        state = input("Enter your State Name : ")

        dict_person = {"name": name, "email": email, "phone": phone, "city": city, "state": state}
        contact_obj = Contact(dict_person)
        book_obj.add_contacts(contact_obj=contact_obj)
    except Exception as e:
        logging.exception(e)


def display_person():
    """
    Hanging function to display all contacts from all address books
    :return:
    """
    try:
        book = input("Enter addressbook name : ")
        book_obj = addressbook_dict.get(book)
        if book_obj is None:
            print("Addressbook doesn't exit")
            return
        book_obj.display_contacts()
    except Exception as e:
        logging.exception(e)


def delete_person():
    """
    Hanging function to delete contacts from address books
    :return:
    """
    try:
        book = input("Enter addressbook name : ")
        book_obj = addressbook_dict.get(book)
        if book_obj is None:
            print("Addressbook doesn't exit")
            return
        person_name = input("Enter person name : ")
        book_obj.delete_record(person_name)
    except Exception as e:
        logging.exception(e)


def json_write():
    """
    Function to store addressbook details in json file
    :return:
    """
    ab = {}
    for k, v in addressbook_dict.items():
        ab.update({k: v.json_write()})
    with open('json_file.json', 'w') as file:
        file.write(json.dumps(ab, indent=4, sort_keys=True))


def json_read():
    """
    Function to read data from json file
    :return:
    """
    with open('json_file.json', 'r') as file:
        data = json.loads(file.read())
        print(data)


def csv_write():
    """
    Function to write addressbook data in csv
    :return:
    """
    ab = []
    for book_name, book_obj in addressbook_dict.items():
        for contact_name, contact_obj in book_obj.records.items():
            # contact_dict = contact_obj.show_details()
            contact_dict = contact_obj.show_details().copy()
            contact_dict.update({'book_name': book_name})
            ab.append(contact_dict)
    with open('csv_file.csv', 'w', newline='') as file:
        fieldnames = ['book_name', 'name', 'email', 'phone', 'city', 'state']
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for line in ab:
            csv_writer.writerow(line)


def csv_read():
    """
    Function to read data from csv
    :return:
    """
    with open('csv_file.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        data = list(csv_reader)
        print(data)
        # for line in csv_reader:
        #     print(line)


if __name__ == '__main__':
    print("\nWelcome to Address Book Program\n ")
    addressbook_dict = {}
    # try:
    choice = {
        1: create_addressbook,
        2: display_list_of_addressbook,
        3: add_person,
        4: display_person,
        5: delete_person,
        6: json_write,
        7: json_read,
        8: csv_write,
        9: csv_read
    }
    while True:
        print("1.Create AddressBook \n2.Display list of Addressbook \n3.Add Person \n4.Display persons record"
              "\n5.Update person record \n6.Delete record of person \n0.Exit")

        a = int(input("Enter your choice : "))
        if a == 0:
            break
        try:
            choice.get(a)()
        except Exception as e:
            print(e)
            logging.exception(e)
