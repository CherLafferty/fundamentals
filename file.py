#- variable declaration
num1 = 42
num2 = 2.3
boolean = True
string = 'Hello World'
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
fruit = ('blueberry', 'strawberry', 'banana')

#- log statement, print type of fruit which is a 'tuple'
print(type(fruit))

# prints inex 1 in pizza_toppings
print(pizza_toppings[1])

# adds 'Mushrooms' to end of pizza_toppings
pizza_toppings.append('Mushrooms')

# prints the name of person
print(person['name'])

""" changes name of person from John to George
and adds 'eye_color' to person array """
person['name'] = 'George'
person['eye_color'] = 'blue'

# prints item indexed at 2 in fruit array, which is bananna
print(fruit[2])

"""- type check, - conditional
if num1 is greater than 45 will print it's greater
if not prints 'it's lower'"""
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

"""- length check, - conditional
if string length is less than 5 will print 'it's a short world'
but if greater than 15 will print 'it's a long world
if between 5 and 14 will print 'Just right!' """
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

"""- for loop
runs loop first thru 0-4 and prints x"""
for x in range(5):
    print(x)
"""then runs loop 2-4 and prints x"""
for x in range(2,5):
    print(x)
"""then runs loop 2-9 in increments of 3
and prints x"""
for x in range(2,10,3):
    print(x)

# sets x = 0
x = 0
"""while loop that will print 0-4"""
while(x < 5):
    print(x)
    x += 1

# removes last item in pizza_toppings array
pizza_toppings.pop()
# removes the item indexed at 1 from pizza_toppings array
pizza_toppings.pop(1)

# prints person array
print(person)
# removes 'eye_color' from person array
person.pop('eye_color')
#prints person array
print(person)


#runs through all 'topping' in pizza_toppings array
for topping in pizza_toppings:
    """conditional boolean if topping is same as 'Pepperoni' will keep
    going through array topping"""
    if topping == 'Pepperoni':
        continue
    """when topping is not equal to 'Pepperonie' will pint 'After 1at if statement"""
    print('After 1st if statement')
    # if/when topping is equal to 'Olives' will end/leave if loop
    if topping == 'Olives':
        break

def print_hello_ten_times():
    # sets num loop to run 0 to 10
    for num in range(10):
        # prints message 10 times
        print('Hello Num range 10')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello X')

# prints function message 4 times
print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello X or 10 times')

# prints message 10 times
print_hello_x_or_ten_times()
# prints message 4 times
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)