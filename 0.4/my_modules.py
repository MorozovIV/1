if __name__ == "__main__":
    pass
def hello():
    print("привет!")

def vremya():
    import time
    vremya = time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime())
    print(vremya)