from collections import namedtuple


Person = namedtuple("Person", ["name", "email", "password"])

person = Person(name="ali", email="ali@gmail.com", password="1234")

person.name
person.email
person.password

