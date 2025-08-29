def func(l: list):
    l.append(4)

l1 = [1, 2, 3]
func(l1)

print(l1)

d1 = {}
def add_dict(dict: dict,value):
    dict['name'] = value
    
add_dict(d1,'Shohjahon')

print(d1)