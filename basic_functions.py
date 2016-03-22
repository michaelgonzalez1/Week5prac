



"""
CP1404/CP5632 Workshop 04
Basic functions
demonstrating various parameters, returns and the use of a main function
"""
__author__ = 'Michael Gonzalez'


def main():
    lowest, highest = get_limits()
    print("lowest =", lowest, "highest =", highest)
    print_between(lowest, highest)


def get_limits():
    minimum = int(input("Enter the minimum: "))
    maximum = int(input("Enter the maximum(must be greater than)" + str(minimum)))
    while maximum <= minimum:
        print("Invalid maximum")
        maximum = int(input("Enter the maximum(must be greater than)" + str(minimum)))
    return minimum, maximum


def print_between(start, end):
    for i in range(start, end+1):
        print(i, end=' ')

main()
