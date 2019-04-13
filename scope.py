#
# name = "This is a global name!"
#
#
# def greeting():
#     # name = "sammy"
#
#     def hello():
#         print("Hello " + name)
#     hello()
#
# greeting()
# print(name)

x = 50


def func():
    global x
    x = 1000
    return x

print("before function call:", x)
x = func()
print("After function call:", x)