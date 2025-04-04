"""
Functions to be imported into the golfers Flask app
"""

import csv

def convert_to_dict(filename):
    """
    Convert a CSV file to a list of Python dictionaries
    """
    # Open a CSV file - note - must have column headings in top row
    datafile = open(filename, newline='')

    # Create DictReader object
    my_reader = csv.DictReader(datafile)

    # Create a regular Python list containing dicts
    list_of_dicts = list(my_reader)

    # Close original CSV file
    datafile.close()

    # Return the list
    return list_of_dicts


def make_ordinal(num):
    """
    Create an ordinal (1st, 2nd, etc.) from a number.
    """
    base = num % 10
    if base in [0, 4, 5, 6, 7, 8, 9] or num in [11, 12, 13]:
        ext = "th"
    elif base == 1:
        ext = "st"
    elif base == 2:
        ext = "nd"
    else:
        ext = "rd"
    return str(num) + ext


# Test functions
def test_make_ordinal():
    # Test ordinals for ranks 1 to 23 (number of golfers in the table)
    for i in range(1, 24):
        print(make_ordinal(i))


def search_the_list(golfers_list):
    # Search for golfers who have won more than 5 majors
    for item in golfers_list:
        if int(item['Majors']) > 5:
            print(f"{item['Player']} has won {item['Majors']} majors.")
    
    # Print the column headers of the golfers CSV
    for k in golfers_list[0].keys():
        print(k)


# Run test functions
if __name__ == '__main__':
    # Test the make_ordinal function
    test_make_ordinal()
    
    # Load the golfers data and test the search function
    golfers_list = convert_to_dict("golfers.csv")
    search_the_list(golfers_list)
    
    # Additional tests for make_ordinal
    print(make_ordinal(12))
    print(make_ordinal(32))