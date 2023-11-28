# Importing the Necessary Packages
import pandas as pd
from itertools import combinations

# Defining Functions to check the validity of Features of Navam's Number
def check_minmax(min, max):
    if not max > min:
        print('Maximum Number should be Greater than Minimum Number!')
        min = int(input('Enter the Valid Minimum Number: '))
        max = int(input('Enter the Valid Maximum Number: '))
        return check_minmax(min, max)
    else:
        return min, max
    
def check_expo(expo):
    if expo < 0:
        print('Exponent must be a Whole Number!')
        expo = int(input('Enter the Valid Exponent: '))
        return check_expo(expo)
    else:
        return expo

def check_term(term):
    if term < 1:
        print('Number of Terms must be a Natural Number!')
        term = int(input('Enter the Valid Number of Terms: '))
        return check_term(term)
    else:
        return term

def check_parity(parity):
    if parity < 2:
        print('Parity must be Greater than 1!')
        parity = int(input('Enter the Valid Parity: '))
        return check_parity(parity)
    else:
        return parity

# Taking the Features of Navam's Numbers as inputs from the user
min = int(input('Enter the Minimum Number: '))
max = int(input('Enter the Maximum Number: '))
min, max = check_minmax(min, max)
expo = int(input('Enter the Exponent: '))
expo = check_expo(expo)
term = int(input('Enter the Number of Terms: '))
term = check_term(term)
parity = int(input('Enter the Parity: '))
parity = check_parity(parity)

# Creating all the Possible Combinations with the numbers in the range of Contributors
numbers_list = []
contributors_list = []
for contributors in combinations(range(min, max + 1), term):
    contributors_list.append(contributors)
    number = 0
    for contributor in contributors:
        number += contributor ** expo
    numbers_list.append(number)

# Extracting the Navam's Numbers from the Possible Combinations
navams_numbers_list = []
navams_numbers_contributors_list = []
for index, number in enumerate(numbers_list):
    if numbers_list.count(number) >= parity:
        navams_numbers_list.append(number)
        navams_numbers_contributors_list.append(contributors_list[index])

# Filtering out the non-duplicate Navam's Numbers along with their Contributors
if navams_numbers_list:
    navams_numbers = {}
    for index, navams_number in enumerate(navams_numbers_list):
        if navams_number not in navams_numbers:
            navams_numbers[navams_number] = [navams_numbers_contributors_list[index]]
        elif len(navams_numbers[navams_number]) != parity:
            navams_numbers[navams_number].append(navams_numbers_contributors_list[index])
    df = pd.DataFrame(navams_numbers)
    print(df.T.sort_index().to_string(header=False))
else:
    print('There are no Navam\'s Numbers in the given Range of Contributors!')
