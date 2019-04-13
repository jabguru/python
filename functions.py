# def my_function(param1 = "default"):
#
#     """
#     THIS IS MY DOC STRING
#     """
#
#     print("My first python function! {}".format(param1))
#
# my_function(2)


# def hello():
#     return "hello"
#
# val = hello()
#
# print(val)

# def add_num(val1, val2):
#     if type(val1)==type(val2)==type(1):
#         return val1 + val2
#     else:
#         return "Please input integers"
#
# sum = add_num(2, 3)
# print(sum)


# #LAMBDA EXPRESSION
#
# #Filter
#
# my_list = [1,2,3,4,5,6,7,8,9,10]
#
# # def even_bool(num):
# #     return num%2 == 0
# #
# # evens = filter(even_bool, my_list)
#
#
# evens = filter(lambda num: num%2 == 0, my_list)
#
#
# print(list(evens))


# tweet = "Go sport! #sport"
# splitted = tweet.split('#')[1]
# print(splitted)

print('x' in [1,2,3,4,'x'])
