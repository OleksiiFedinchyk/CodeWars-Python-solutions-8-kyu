# https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b

def human_years_cat_years_dog_years(human_years):
    number = 1 
    catYears = 0
    dogYears = 0
    humanYears = 0
    while number <= human_years:
        if number == 1:
            catYears += 15
            dogYears += 15
            humanYears += 1
            number += 1
        elif number == 2:
            catYears += 9
            dogYears += 9
            humanYears += 1
            number += 1
        else:
            catYears += 4
            dogYears += 5
            humanYears += 1
            number += 1
                            
    return [humanYears, catYears, dogYears]
