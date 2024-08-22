# def hello():
#     pass
# print("Hello world")
# hello()

# def hello():
#     print("Hello world !")
# hello()
# hello()
# hello()
# hello()

# def hello():
#     return "hello function" #it dosn't print anything.it means that the string inside the return function will be equal to hello function
# hello()

# def hello():
#     return "how's everything" #now we are printing the function which is equal to the value in the return
# print(hello())

# def hello():
#     return "hi guys"
# print(hello().upper())

# def name(names):
#     return f' {names} is my name '
# print(name("Miminchandran"))

# def name(name,age =21):
#     return '{} is my name and {} is my age'.format(name,age)
# print(name("mimin"))

# def name(names,age=21):
#     return '{} is me and i am {} years old'.format(names,age)
# print(name("Mimin",age =40))

# def details(*args,**kwargs):
#     return '{} are the students and {} these are their details'.format(args,kwargs)
# print(details("Mimin","mimi","Praseetha", mimiage=19,Miminage=21,praseethaage=41))


# def details(*args,**kwargs):
#     print(args)
#     print(kwargs)
# list1=['mimin','nihal','anees']
# dictio ={'mimin': 19, 'nihal': 21,'anees':45}
# details(list1,**dictio)

# def details(*args,**kwargs):
#     return args,kwargs
# list1=['mimin','nihal','anees']
# dictio ={'mimin': 19, 'nihal': 21,'anees':45}
# print(details(list1,**dictio))
# days_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
# def leapyear(year):
#     if year%4==0 and (year%100!=0 or year%400==0):
#         return f'{year} is Leap year'
#     else:
#         return f'{year} is not leap year'
# print(leapyear(2020))

""#collecting name""

# def greet(name):
#     print('Hello {}!'.format(name))
# greet("Alice")


#area of circle

# def area_of_circle(radius):
#     return 3.14*(radius**2)
# print(area_of_circle(10))

#area of circle using import math

# import math
# def area_of_circle(radius):
#     return math.pi*radius**2
# print(area_of_circle(10))

#odd or even
# def number(even):
#     if even%2==0:
#         return "true"
#     else:
#         return "false"
# print(number(10))

# def number(even):
#     return even%2==0
# print(number(51))

#maximum of three numbers
# def max_of_three(a,b,c):
#     return max(a,b,c)
# print(max_of_three(12,13,14))


# count the vowels in a string

# a="aeiouAEIOU"
# def word(string):
#      return sum(1 for i in string if i in a)
# print(word("aeiou"))


#Reverse the string

# def reversed_string(string):
#     return string[::-1]
# print(reversed_string("Hello world"))

#prime number or not

# def is_prime_number(integer):
#     if integer<=1:
#         return False
#     for prime in range(2,int(integer**0.5)+1):
#         if integer%prime ==0:
#             return False
#     print(True)
# print(is_prime_number(2))


#sum of numbers in a list

# def sum_of_list(numbers):
#     return sum(numbers)
# print(sum_of_list([1,2,3,4,5,7,8,9,10]))


#removing duplicates from a list

# def remove_duplicates(list):
#     return set(list)
# print(remove_duplicates([1,2,3,44,5,5,5,5]))

#convert celsius to fahrenheit
# def cels_to_far(celsius):
#     return   (9/5*celsius)+32
# print(cels_to_far(45))

# def count_words(sentence):
#     return sum((1 for i in sentence))
# print(count_words("killhim"))



# def count(sentence):
#     return len(sentence.split())
# print(count("hi guys hi kill"))
