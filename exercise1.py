# #Problem 1
# s = 'django'
#
# print(s[0])
# print(s[-1])
# print(s[:4])
# print(s[1:4])
# print(s[4:])

# #Problem 2
# l = [3, 7, [1,4,'hello']]
# #Reassign hello to goodbye
# l[2][2] = "goodbye"
#
# print(l)

# #Problem 3
# #Using key and indexing, grab the 'hello' from the following dictionaries
#
# d1 = {'simple_key': 'hello'}
#
# d2 = {'k1':{'k2':'hello'}}
#
# d3 = {'k1':[{'nest_key':['this is deep', ['hello']]}]}
#
# print(d1['simple_key'])
# print(d2['k1']['k2'])
# print(d3['k1'][0]['nest_key'][1][0])

# #Problem 4
# #Use  a set to find the unique values of the list below:
#
# mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
#
# print(set(mylist))


#Problem 5
#You are given two variables:
age = 4
name = 'sammy'

#Use print formatting to print the following string:
#"Hello my dog's name is sammy and he is four years old"

sent = "Hello my dog's name is {a} and he is {b} years old".format(a = name, b = age)

print(sent)
