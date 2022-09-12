import logging

logging.basicConfig(filename='Address Book.log', filemode='a', level=logging.DEBUG)


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


if __name__ == '__main__':
    contact1 = Contact(
        {"name": "Amit", "email": "amit836@gmail.com", "phone": "9936958584", "city": "Vns", "state": "UP"})
    print(contact1.show_details())
