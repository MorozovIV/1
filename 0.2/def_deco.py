def decorator (func):
    def wrapper():
        print("код до выполнения функции")
        func()
        print("код после функции")
    return wrapper
@decorator
def show ():
    print("Я обычная функция")

# show = decorator(show)
show()