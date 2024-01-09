class PersonalAssistant: # Define Class
    def __init__(self, todos, birthdays, contacts):  # parameters
      
      # Arguments passed when PersonalAssistant class is used:
      self.todos = todos
      self.birthdays = birthdays
      self.contacts = contacts

## Todo Section ## 
    # Get a todos
    def add_todo(self, new_item):
      self.todos.append(new_item)
    # Remove a todo item
    def remove_todo(self, todo_item):
      if todo_item in self.todos:
        index = self.todos.index(todo_item)
        self.todos.pop(index)
        return f'{todo_item} was removed'
      else:
        print("Todo is not in list!")
    # Get ALL todo items
    def get_todos(self):
      return self.todos
## Birthday Section ##
    # Get ALL birthdays
    def get_birthdays(self):
      return self.birthdays
    # Get a birthday 
    def get_birthday(self, name):
      if name in self.birthdays:
        return f"{name}'s birthday is on {self.birthdays[name]}."
      else:
        return "Can't find birthday for this person"
    # Add a birthday
    def add_birthday(self, name, date):
      if name in self.birthdays:
        return f"You already have a birthday for {name}"
      else:
        self.birthdays[name] = date
        return f"{name}'s birthday has been added."
    # Remove a birthday
    def remove_birthday(self, name):
      if name in self.birthdays:
        self.birthdays.pop(name)
        return f"{name}'s birthday has been removed."
      else:
        return "Sorry there is no recorded birthday for that person"
## Contacts Section ##
    # Get ALL contacts
    def get_contacts(self):
        return self.contacts
    # Get a contact
    def get_contact(self, name):
      if name in self.contacts:
        return f"{name}'s title is {self.contacts[name]}."
      else:
        return "Can't find contact for this person"
    # Add a contact
    def add_contact(self, name, position):
      if name in self.contacts:
        return f"You already have a contact for {name}"
      else:
        self.contacts[name] = position
        return f"{name} has been added to contacts."
    # Remove a contact
    def remove_contact(self, name):
      if name in self.contacts:
        self.contacts.pop(name)
        return f"{name} has been removed from contacts."
      else:
        return "Sorry there is no recorded contact for that person"
