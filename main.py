"""This module returns the Navam's Numbers with provided attributes"""

from itertools import combinations
import pandas as pd

def check_minmax(minimum: int, maximum: int) -> tuple:
    """Checks the validity of the range of the Contributors"""

    if minimum >= maximum:
        print('Maximum Number should be Greater than Minimum Number!')
        minimum = int(input('Enter the Valid Minimum Number: '))
        maximum = int(input('Enter the Valid Maximum Number: '))
        return check_minmax(minimum, maximum)
    return minimum, maximum

def check_expo(exponent: int) -> int:
    """Checks if the specified Exponent is valid"""

    if exponent < 0:
        print('Exponent must be a Whole Number!')
        exponent = int(input('Enter the Valid Exponent: '))
        return check_expo(exponent)
    return exponent

def check_term(term_count: int) -> int:
    """Checks if the specified Term Count is valid"""

    if term_count < 1:
        print('Number of Terms must be a Natural Number!')
        term_count = int(input('Enter the Valid Number of Terms: '))
        return check_term(term_count)
    return term_count

def check_parity(parity: int) -> int:
    """Checks if the specified Parity is valid"""

    if parity < 2:
        print('Parity must be Greater than 1!')
        parity = int(input('Enter the Valid Parity: '))
        return check_parity(parity)
    return parity

def logic():
    """Prints Navam's Numbers with provided attributes"""

    mini = int(input('Enter the Minimum Number: '))
    maxi = int(input('Enter the Maximum Number: '))
    mini, maxi = check_minmax(mini, maxi)
    expo = int(input('Enter the Exponent: '))
    expo = check_expo(expo)
    term = int(input('Enter the Term Count: '))
    term = check_term(term)
    pari = int(input('Enter the Parity: '))
    pari = check_parity(pari)

    # Creating all the Possible Combinations with the numbers in the range of Contributors
    numbers_list = []
    contributors_list = []
    for contributors in combinations(range(mini, maxi + 1), term):
        contributors_list.append(contributors)
        number = 0
        for contributor in contributors:
            number += contributor ** expo
        numbers_list.append(number)

    # Extracting the Navam's Numbers from the Possible Combinations
    navams_numbers_list = []
    navams_numbers_contributors_list = []
    for index, number in enumerate(numbers_list):
        if numbers_list.count(number) >= pari:
            navams_numbers_list.append(number)
            navams_numbers_contributors_list.append(contributors_list[index])

    # Filtering out the non-duplicate Navam's Numbers along with their Contributors
    if navams_numbers_list:
        navams_numbers = {}
        for index, navams_number in enumerate(navams_numbers_list):
            if navams_number not in navams_numbers:
                navams_numbers[navams_number] = [navams_numbers_contributors_list[index]]
            elif len(navams_numbers[navams_number]) != pari:
                navams_numbers[navams_number].append(navams_numbers_contributors_list[index])
        df = pd.DataFrame(navams_numbers)
        print("\nThe Navam's Numbers are:")
        print(df.T.sort_index().to_string(header=False))
    else:
        print('There are no Navam\'s Numbers in the given Range of Contributors!')

if __name__ == '__main__':
    logic()
