
            # Exercise 1
            # Make students list. Print second student. Print last student.
from xml.dom import WrongDocumentErr


students = ['Douglas', 'Hunter', 'Michelle', 'Betty']

print(students[1])
print(students[3])

            # Exercise 2
            # Create foods tuple with same length as students.
            # Use for loop to print '(food goes here) is a good food'
foods = ('pizza', 'burgers', 'brats', 'steak')

for food in foods:
    print(f'{food} is a good food')

            # Exercise 3
            # Using for loop, print the last two food strings

print(foods[-2:])

            # Exercise 4
            # Create dictionary named home_town containing the keys of
                    # city, state & population

            # Print string with format
                    # I was born in 'city, state' population of 'population'
home_town = {
    'city': 'Shabbona',
    'state': 'Illinois',
    'population': '900'
}

city = home_town['city']
state = home_town['state']
population = home_town['population']
print(f'I was born in {city}, {state} with a population of {population}')

            # Exercise 5
            # Iterate over key:value in home_town and print
                #string for each

print(f'{home_town}')

            # Exercise 6
            # Create empty list named cohort
            # Using for loop, add one dictionary to the cohort 
                # list for each student name

cohort = []

my_dictionary = {'student': 'Tina',
'fav_food': 'Cheeseburger'}

my_dictionary_copy = my_dictionary.copy()
cohort.append(my_dictionary_copy)
for key, value in my_dictionary.items():
    print(f'{key} : {value}')   


            # Exercise 7
            # Using list of students and list comprehension, assign
                #variable named awesome_students a new list
                #containing strings similar to...

for awesome_student in students:
    print(f'{awesome_student} is awesome')


           # Exercise 8
           #Using tuple foods and list comprehension within a for loop,
              #print each food string that caontains the letter a.



# a = []
# for key in foods:
#     if 'a' in key:
#         a.append(key)
# print(a)   

a = [food for food in foods if 'a' in food]
print(a)
