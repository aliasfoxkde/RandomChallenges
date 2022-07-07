from random import randint, sample
from datetime import datetime


def one_hundred_prisoners_problem(number_of_boxes_and_prisoners, sample_size):
    """ The 100 prisoners problem is a mathematical problem in probability theory and combinatorics.
    In this problem, 100 numbered prisoners must find their own numbers in one of 100 drawers in order
    to survive. The rules state that each prisoner may open only 50 drawers and cannot communicate with
    other prisoners. At first glance, the situation appears hopeless, but a clever strategy offers the
    prisoners a realistic chance of survival. Danish computer scientist Peter Bro Miltersen first proposed
    the problem in 2003. Source: https://en.wikipedia.org/wiki/100_prisoners_problem """

    timer_script_start = datetime.now()  # Used to calculate script runtime
    attempts_successful = 0  # Count used to determine success rate

    for number_of_prisoner_problems_to_try in range(sample_size):
        # For example, generates a random integer between 1 and N (default 100)
        randomly_assigned_number = randint(1, number_of_boxes_and_prisoners)
        number_to_find = randomly_assigned_number

        # Warden goes through and rearranges box labels and their contents
        list_of_rnd_box_labels = sample(range(number_of_boxes_and_prisoners), number_of_boxes_and_prisoners)
        list_of_rnd_box_contents = sample(range(number_of_boxes_and_prisoners), number_of_boxes_and_prisoners)
        arranged_boxes_by_sets = dict(zip(list_of_rnd_box_labels, list_of_rnd_box_contents))

        # Prisoner searches the box with their number on it, for it's contents
        for num_of_boxes_opened in range(number_of_boxes_and_prisoners):

            # Prisoner opens the box to find the number inside
            number_to_find = arranged_boxes_by_sets.get(number_to_find)

            # If the prisoner finds the their number in the box, sets success flag
            successfully_found_box = number_to_find == randomly_assigned_number
            if successfully_found_box:   # Validates whether True or False

                # Prisoner is allowed to look through half the boxes
                half_of_all_boxes = number_of_boxes_and_prisoners//2

                # If prisoner finds their number within allowed attempts, sets win condition
                number_has_been_found_in_boxes_searched = num_of_boxes_opened <= half_of_all_boxes  # True or False

                # Increments successful attempt condition if criteria met.
                if number_has_been_found_in_boxes_searched:
                    attempts_successful += 1

                # Breaks when Box is found, regardless of attempts
                # but keeps count and only records success if less
                # than 50% of boxes were checked.
                break

    # Output Calculations
    failures = sample_size - attempts_successful
    success_percentage = round(attempts_successful/float(sample_size)*100, 2)

    # Final Output
    print(f'{attempts_successful} Success Rate out of {sample_size} ({failures} Failures) at {success_percentage}%')
    print(f'\nThe script executed in: {datetime.now() - timer_script_start}')


# Usage:
# one_hundred_prisoners_problem(number_of_boxes_and_prisoners, sample_size)
# 
# Typical Output (49% to 52% "Success Rate"):
#   518 Success Rate out of 1000 (482 Failures) at 51.8%
#   The script executed in: 0:00:00.109937
one_hundred_prisoners_problem(100, 1000)
