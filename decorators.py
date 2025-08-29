correct_username = "ali"
correct_password = "1234"


def requires_login(func):

    def wrapper():
        username = input("username: ")
        password = input("password: ")

        if username != correct_username or correct_password != password:
            print("login qilishiz kerak")
        else:
            func()

    return wrapper

def function(func):
    
    def wratter(word):
        print("Started")
        func(word)
        print("End")
    return wratter

@function
def say_hi(a):
    print(a)
    
# say_hi("Hi")
def check_positive(func):
    def writer(num):
        
        for i in num:
            if  not isinstance(i,(int,float)) or i <0:
                raise Exception("Faqat musbat raqam kiriting ")
            
        return func(num)
            
    return writer
            
@check_positive
def sum_list(nums: list):
    return sum(nums)

print(sum_list([1, 2, 3, 4]))   # 10
print(sum_list([5, -2, 3]))     # Exception: Faqat musbat sonlar kiritilishi kerak!
import datetime

def check_time(func):
    def writer(name):
        print(f"Funksiya ishga tushdi: {datetime.datetime.now()}")
        return func(name)   # asl funksiyani ishlatyapmiz
    return writer
    
@check_time
def say_hello(name):
    return f"Salom, {name}!"

print(say_hello("Shohjahon"))
