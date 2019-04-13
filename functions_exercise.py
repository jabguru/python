# #Problem 1
#
# def array_checks(nums):
#     if 1 in nums and 2 in nums and 3 in nums:
#         print("True")
#     else:
#         print("False")
#
# array_checks([2,3,4,5])



# #Problem 2
#
# def string_bits(str):
#     print(str[::2])
#
# string_bits("heeellooo")

# #Method 2
# def string_bits(my_string):
#     result = ""
#     for i in range(len(my_string)):
#         if i%2 == 0:
#             result = result + my_string[i]
#     return result
#
# print(string_bits('hello'))




#Problem 3

# def end_other(a, b):
#     a = a.lower()
#     b = b.lower()
#     if a in b.format(a) or b in a.format(b):
#         print("True")
#     else:
#         print("False")
#
# end_other("abc", "Helloab")

# #Method 2
# def end_other(a,b):
#     a = a.lower()
#     b = b.lower()
#     return (b.endswith(a) or a.endswith(b))
#
# print(end_other("go", "mango"))

# #Method 3
# def end_other(a,b):
#     a = a.lower()
#     b = b.lower()
#     return a[-len(b):] == b or a == b[-len(a):]
#
# print(end_other("go", "mang"))


# #Problem 4
# def double_char(str):
#     x = 0
#     y = len(str)
#     while x<y:
#         z = str[x] * 2
#         print(z, end=''),
#         x = x + 1
#
# double_char("Jabguru")

# #Method2
# def double_char(my_string):
#     result = ''
#     for char in my_string:
#         result += char*2
#     return result
#
# print(double_char("Jabguru"))

# #Problem 5
# def no_teen_sum(a,b,c):
#     if a == 15:
#         a = 15
#     elif b == 15:
#         b = 15
#     elif c == 15:
#          c = 15
#     elif a == 16:
#         a = 16
#     elif b == 16:
#         b = 16
#     elif c == 16:
#          c = 16
#     else:
#         if (a >=13 and a <=19):
#             a = 0
#         elif (b >=13 and b <=19):
#             b = 0
#         elif (c >=13 and c <=19):
#             c = 0
#         else:
#             a = a
#
#     return a + b + c
#
# def fix_teen(n):
#     if n == 15:
#         n = 15
#     elif n == 16:
#          n = 16
#     elif (n >=13 and n <=19):
#         n = 0
#     else:
#         n = n
#     return n
#
# print(no_teen_sum(2,1,14))
# print(fix_teen(13))

# #Method 2
# def no_teen_sum(a, b, c):
#     return fix_teen(a) + fix_teen(b) + fix_teen(c)
#
# def fix_teen(n):
#     if n in [13,14,17,18,19]:
#         return 0
#     return n
#
# print(no_teen_sum(2,1,14))

# #Problem 6
# def count_evens(nums):
#     evens = filter(lambda oprnd: oprnd%2 == 0, nums)
#     print(len(list(evens)))
#
# count_evens([2,2,0])

#Method 2
def count_evens(nums):
    count = 0
    for num in nums:
        if num%2 == 0:
            count += 1
    return count

print(count_evens([2,2,0]))
