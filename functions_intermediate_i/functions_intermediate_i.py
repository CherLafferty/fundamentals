# 1. Update Values in Dictionaries and Lists
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# a
#. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# def change_ten(list):
#     list[1][0] = 15
#     return list
# print(change_ten(x))

# b. Change the last_name of the first student from 'Jordan' to 'Bryant'
# def change_last_name(dict):
#     # look for last_name and compare
#     for i in range(0,len(dict)):
#         for key,val in dict[i].items():
#             # print(key,val)
#     # If last_name is 'Jordan' change it to 'Bryant'
#             if val== "Jordan":
#                 val= "Bryant"
#             print(key,val)
#     #print last_name

# change_last_name(students)

# c. In the sports_directory, change 'Messi' to 'Andres'
# def sports_change(dict):
#     dict["soccer"][0]= "Andres"
#     return dict
# print(sports_change(sports_directory))

# d. Change the value 20 in z to 30
# def change_twenty(list):
#     list[0]["y"] = 30
#     return list
# print(change_twenty(z))

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# 2. Iterate Through a List of Dictionaries
# def iterate_dictionary(list):
    #loop thru list
    # for i in range(0,len(list)):
    #     for key,val in list[i].items():
    #         print(key,val)
    #print each key and assocciated value
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# print(iterate_dictionary(students))

# 3.Get Values From a List of Dictionaries
# def iterate_dictionary2(key_name, list):
#     for i in list:
#         print(i[key_name])

# iterate_dictionary2('first_name', students)
# iterate_dictionary2('last_name', students)

# 4. Iterate Through a Dictionary with List Values
dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(list):
    for key,val in list.items():
        print("-----------------")
        print(f"{len(val)} {key.upper()}")
        for i in range(0, len(val)):
            print(val[i])
        
        #print(i)//prints keys
        #print(list[i])//prints items


print_info(dojo)


