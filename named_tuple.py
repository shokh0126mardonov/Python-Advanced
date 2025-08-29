from collections import namedtuple


Person = namedtuple("Person", ["name", "email", "password"])

person = Person(name="ali", email="ali@gmail.com", password="1234")

person.name
person.email
person.password

from collections import namedtuple

users = namedtuple("users",["name",'age','is_male'])
user = users(name="Shohjahon",age=19,is_male=True)

print(user.name)
print(user.age)
print(user.is_male)