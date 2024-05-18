class Contact:
  def __init__(self,name,phone_number,email,address):
    self.name= name
    self.phone_number=phone_number
    self.email=email
    self.address=address
class ContactManager:
  def __init__(self):
    self.contacts= []
  def add_contact(self,contact):
    self.contacts.append(contact)
    print(f"Contact {contact.name} added successfully")
  def view_contacts(self):
    if not self.contacts:
      print("contact is not found")
      return
    for contact in self.contacts:
      print(f"Name  {contact.name} , Phone number {contact.phone_number}")
  def search_contact(self,search_item):
    for contact in self.contacts:
      if search_item in [contact.name , contact.phone_number]:
        print(f" Name {contact.name} , phone number{contact.phone_number} , email {contact.email}, address {contact.address}")
  def update_contact(self,search_item,New_contact):
    for contact in self.contacts:
      if search_item in [contact.name,contact.phone_number]:
        contact.name=New_contact.name
        contact.phone_number=New_contact.phone_number
        contact.email=New_contact.email
        contact.address=New_contact.address
        print(f"contact {contact.name}, contact {contact.phone_number},contact {contact.email}, contact {contact.address} is successfully updated!!")
        return
    print(f"Contact with name or phone number '{search_item}'not found ")  
  def delete_contact(self,search_item):
    for contact in self.contacts:
      if search_item in [contact.name, contact.phone_number]:
        self.contacts.remove(contact)
        print(f"Contact {contact.name} is successfully deleted")
        return
    print(f"Contact with name or phone number '{search_item}' is not found")
    
    
#usage 
contact_list= ContactManager()
contact1= Contact("ram", "123456891", "ram@gmail.com", "1st street green medows chennai")    
contact2= Contact("varsh", "2314589961", "varsh@gmail.com", "2st  ram street chennai")
contact3= Contact("shylesh", "3365214785", "shy@gmail.com", "ram nagar 29th street chennai")
contact4= Contact("sita", "9854712563", "sitaram@gmail.com", " 2nd hanumanthalal street  chennai")
#adding contacts
contact_list.add_contact(contact1)
contact_list.add_contact(contact2)
contact_list.add_contact(contact3)
contact_list.add_contact(contact4)
#viewing contacts
contact_list.view_contacts()
#updating contacts
contact_list.update_contact("ram",Contact("rama","8939658741","rama@gmail.com","23rd ram lal street"))
#search
contact_list.search_contact("sita")
#delete
contact_list.delete_contact("shylesh")
contact_list.view_contacts()
