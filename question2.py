from datetime import date

class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state

    def __repr__(self):
        return f"{self.city}, {self.state}"

class Employee:
    def __init__(self, name, emp_id, doj, addresses):
        self._name = name
        self._id = emp_id
        self._doj = doj
        self._addresses = tuple(addresses)  
    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def doj(self):
        return self._doj

    @property
    def addresses(self):
        return self._addresses

#examples i have taken 
addr1 = Address("Rajahmundry", "Andhra Pradesh")

emp = Employee("Keerthi", "EMP100", date(2025, 2, 15), [addr1])

print("Name:", emp.name)
print("ID:", emp.id)
print("Date of Joining:", emp.doj)
print("Addresses:", emp.addresses)
