def hello():
    print("привет!")
#
def vremya():
    import time
    vremya_now=time.strftime("Today is %d %B %Y, %H:%m", time.localtime())
    print(vremya_now)
