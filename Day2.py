# decorator
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
# @my_decorator
# def say_hello():
#     print("Hello!,Salman Bhai.")
# say_hello()    
# Decorators with arguments
def arg_decorator(func):
    def wrapper(*args,**kwargs):
        print("Before the function is called.")
        result = func(*args,**kwargs)
        print("After the function is called.")
        return result
    return wrapper  
@arg_decorator
def Addition(a,b):
    print(f"Adding {a} and {b}")
    return a + b

result = Addition(5, 3)
print(f"Result: {result}")