"""
Name : Counting Sunday
Date created : 04-06-2024
"""

MONTHS = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
# Leap year : Feb has 28 + 1 = 29 days, only if year divisible by 4 but not 100 unless 400
START = 1
END = 100

def iterate_year(weekday, month, year):
    leap_check(year)
    weekday += MONTHS[month]
    weekday = weekday % 7
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    return weekday, month, year


def leap_check(year):
    year = 1900 + year
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        MONTHS[2] = 29
    else:
        MONTHS[2] = 28
    return None


def main():

    sunday = 0
    current_weekday = 1
    current_month = 1
    current_year = 0
    # Sets start day to 1st Jan 1901
    while current_year != START:
        current_weekday, current_month, current_year = iterate_year(
            current_weekday, current_month, current_year
        )

    count = 0
    while current_year != END + 1:
        if current_weekday == sunday:
            count += 1
        current_weekday, current_month, current_year = iterate_year(
            current_weekday, current_month, current_year
        )

    print(current_weekday, current_month, 1900 + current_year)
    print(count)
    return None


if __name__ == "__main__":
    main()
