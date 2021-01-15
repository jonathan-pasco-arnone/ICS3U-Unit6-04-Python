#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: January 2021

import random


def average_of_numbers(passed_in_two_d_list):
    # this function gets the average of the numbers in the two_d_array

    amount_of_digits = 0
    average = 0
    total = 0
    # runs this the same amount of times as the length
    # of the passed_in_two_d_list
    for row_value in passed_in_two_d_list:
        # runs this the same amount of times as the length of the row value
        for single_element in row_value:
            total += single_element
            amount_of_digits += 1

    average = total / amount_of_digits

    return average


def main():
    # this function generates the designated amount of random
    # numbers and puts them into an array

    two_d_list = []

    try:
        rows = int(input("Please input the number of rows: "))
        columns = int(input("Please input the number of columns: "))
    except Exception:
        print("This was not an integer")
    else:
        if rows < 0 or columns < 0:
            print("")
            print("Please input positive values")
        else:
            for loop_counter_rows in range(0, rows):
                new_column = []
                for loop_counter_columns in range(0, columns):
                    random_number = random.randint(0, 50)
                    new_column.append(random_number)
                    print("{0}".format(random_number), end=" ")
                two_d_list.append(new_column)
                print("")
            average = average_of_numbers(two_d_list)
            print("The average is: {0}".format(average))


if __name__ == "__main__":
    main()
