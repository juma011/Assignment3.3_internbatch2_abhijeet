
str = "Day 1"
print(str)


print(2 + 2)

a = 20
b = 3
sum = a + b

print(sum)

my_bill = 2000
gst_applied = 0.18

total_bill = (my_bill * gst_applied) + my_bill
print(total_bill)

name = "abhijeet"

print("s" + name[2:6])


last_name = "saxena"
print(last_name[3])

str1 = "how old are you?"

print(str1[4:7])

print(str1[2:15:3])

print(name[3] * 10)

print(name.upper())

print(str1.split())

print(str1.split("o"))

print(f'my name is {name} and my age is {sum}')

print()

print()
print("Day 2")

list_num = [1,20,45,30,57,83,72,81]
print(list_num)

list_mixed = [120,20,"good"]
print(list_mixed)

print(list_num[5])

print(list_mixed[0::2])

list_1 = [1,2,3,4]
list_2 = [9,8,7,6]
list_3 = list_1 + list_2
print(list_3)



list_4 = ['M','o','o','l','y','a']
list_4[0] = 'm'
list_4[3] = 'L'
print(list_4)



list_num.append(15)
print(list_num)

list_num.pop()
print(list_num)

list_num.pop(3)
print(list_num)


list_sort = [20,45,30,55,27]
list_sort.sort()
print(list_sort)

list_new = list_sort.sort()
print(list_new)

list_name = ['kolhi','pujara','rahane','sharma']
print(len(list_name))

list_name.reverse()
print(list_name)

my_dic = {'name':'travis', 'age': 28, 'designation': 'rapper'}
print(my_dic)

wages = {'sid': 5000, 'john': 4000, 'shaun': 9000}
print(wages['shaun'])

wages['michelle'] = 6500
print(wages)

print(wages.keys())

print(wages.values())

print(wages.items())

dict_new = {'name':'kendrick', 'wages':[2000,5500,6500,3500]}
print(dict_new['wages'])
print(dict_new['wages'][2])

tuple_1 = (1,2,3)
list_1 = [1,2,3]
list_1[0] = 5
print(list_1)

print(tuple_1[1:2])
tuple_2 = (1,3,2,2,2,3,1,2,3,3,3,2,1,2)
print(tuple_2.count(3))

tuple_mixed = (1, 'ram', 'shyam', 3)
print(tuple_mixed)
print(tuple_mixed.index('shyam'))

set_new = {'bonjour', 'bonsoir', 'bonnuit', 'bonappetit'}
print(set_new)

print(set(tuple_2))

set_num = {1,2,3,4,5,6,7,8}
set_num.add(19)
print(set_num)

True
False
print(1.8>2)
print(2.1>1.9)

a = 'hello'
b = 'hello'
c = 'bye'
print(a==b)
print(a==c)
print(a!=c)

print(4>2>3)
print(5>1 or 1<0)

name = 'james'
if name == 'rick':
    print("login as rick")
elif name == 'morty':
    print("login as morty")
else:
    print("check the user")

x = 10
while x > 11:
    print(x)
    x = x + 1
else:
    print("the condition is false")

print()
print()
print("Day 3")

list_num = [1,2,3,4]
for item in list_num:
    print(item)
    print("the items are listed")


list_num = [1,2,3,4]
for num in list_num:
    print("hi")

my_num = [11,22,33,44,55,66,77,88,99,110]
for num in my_num:
    if num % 2 == 1:
        print(f'{num} is odd')
    else:
        print(f'{num} is even')

my_num = [15,30,45,60]
sum_num = 0
for num in my_num:
    sum_num = sum_num + num
    print(sum_num)

my_msg = "Bonjour Madam"
for letter in my_msg:
    print(letter)

list_tup = [(1,3,5),(2,4,6),(7,8,9)]
for item in list_tup:
    print(item)

for a,b,c in list_tup:
    print(a)
    print(b)
    print(c)

dict_val = {'week1':1, 'week2':2}
for item in dict_val.items():
    print(item)


x = [1,3,5]
for num in x:
    pass

x = [1,3,5,7,9,11,13,15]
for num in x:
    if num == 11:
     continue
    print(num)

list_num = [0,1,2,3,4,5,6,7,8]
for num in list_num:
    if num== 4:
        break
        print(num)
print('outside for loop')

for num in range(0,8,2):
    print(num)

string_msg = "world"
index_count = 0
for char in string_msg:
    print(f'at index {index_count} is {char}')
    index_count = index_count + 1

for char in enumerate(string_msg):
    print(char)


mylist_1 = ['rick', 'morty', 'summer']
mylist_2 = [10,30,50]
mylist_3 = [40,60,80]
for item in zip(mylist_1, mylist_2, mylist_3):
    print(item)

list_num = [500,700,400,900]
print(max(list_num))

sex = input("what is your sex? ")
print(sex)
if sex == 'male':
    print("your sex is male")
elif sex == 'female':
    print('your sex is female')


print()
print("DAY 4")

my_list = ['a','b','c','d','e','f']
for char in my_list[0::2]:
    print(char)

my_msg = 'goodmorning'
my_list = []
for char in my_msg:
    my_list.append(char)

print(my_list)

my_name = 'abhijeet'
my_nameaslist = [char for char in my_name]
print(my_nameaslist)

for num in range(0,11):
    print(num**2)

my_oddlist = [num**2 for num in range(0,11) if num % 2 ==1]
print(my_oddlist)

for x in [11,22,33]:
    for y in [12,24,36]:
        print(x*y)


my_nestedlist = [x*y for x in [2,4,6] for y in [10,100,1000]]
print(my_nestedlist)

my_nestedlist.insert(4,40)

print(my_nestedlist)


def name_of_student():
    print('ravi')
    print('sanya')
    print('rahul')
    print('sharad')
print(name_of_student())

def print_name(name):
    print(f'hello {name}')
print_name('raju')

def multiply_num(a,b):
    print(a*b)
print(multiply_num(20,40))

def is_even(num):
    if num % 2 ==0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')

is_even(22)

num_list = [1,2,3,4,5,6,7,8]
def check_even(num_list):
    for num in num_list:
        if num%2 ==0:
            return True
        else:
            return False
num_list = [1,3,5]
print(check_even(num_list))


print()
print('DAY 5')
print()

stock_prices=[('Tata',500),('HDFC',2000),('Zomato',100)]
for stock_name,price in stock_prices:
    print(price)


def kw_example(**kwargs):
    if 'food' in kwargs:
        print(kwargs['food'])
    else:
        print('no food in the list')
kwargs = {'fruit':'kiwi','vegetable':'tomato'}
print(kwargs['fruit'])

list_cups = ['','0','']
from random import shuffle
shuffle(list_cups)

print(list_cups)

def shuffle_list(list_cups):
    shuffle(list_cups)
    return list_cups
result = shuffle_list(list_cups)


def get_guess():
    guess = ''
    guess = input("Pick the cup 0,1 or 2: ")
    return int(guess)
guess = get_guess()

def check_guess(list_cups_guess):
    if list_cups[guess] == '0':
        print("correct guess")


print(list_cups)

result = shuffle_list(list_cups)

guess = get_guess()

list_string = ['potato','ornage','chips']

def even_odd_check(string):
    if len(string) %2 == 0:
        return ' even'
    else:
        return 'odd'

print(list(map(even_odd_check,list_string)))



mylist = [1,2,3,4,5,6,7,8,9]
def even_odd_check(num):
    return num%2 != 0
print(list(filter(even_odd_check,mylist)))

lambda num: num%2 != 0
print(list(filter(even_odd_check,mylist)))
print(list(filter(lambda num: num%2 == 0,mylist)))



















































































































