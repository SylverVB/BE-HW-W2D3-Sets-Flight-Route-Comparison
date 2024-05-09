# Lesson 3: Assignments | Sets

# 1. Python Sets Adventure
# Objective:
# The aim of this assignment is to deepen your understanding and application of Python sets in various scenarios, ranging from basic operations 
# to advanced manipulations and best practices. You will correct given codes, use sets in everyday contexts, and tackle challenges that require 
# creative thinking and problem-solving.

# Task 1: Flight Route Comparison
# Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, 
# one for each airline. Write a Python program to find out:

# 1. Destinations that both airlines fly to.
# 2. Destinations unique to your airline.
# 3. Whether there are any destinations that neither airline shares.

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

def common_destinations(airline_one, airline_two):
    common_routes = our_routes.intersection(competitor_routes)
    return common_routes

def unique_destinations(airline_one, airline_two):
    unique_destinations = our_routes.difference(competitor_routes)
    print(f"\nUnique destinations for our airline: {unique_destinations}")
    unique_destinations = competitor_routes.difference(our_routes)
    print(f"Unique destinations for competitor airline: {unique_destinations}")
    
    return unique_destinations

def potential_new_routes(airline_one, airline_two):
    airport = input('\nWhat destination do you have in mind? \n')
    new_routes = set()
    for route in airline_one:
        for destination in airline_two:
            if airport not in airline_one and airport not in airline_two:
                new_routes.add(airport)
                break
    return new_routes

def flight_route_comparison(airline_one, airline_two):

    while True:
        print("\nWelcome to our Flight Route Comparison!")
        print("\nMenu:")
        print("1. Find common routes")
        print("2. Find unique destinations to your airline")
        print("3. Find out if airlines serve your destination")
        print("4. Quit")

        choice = input("\nWhat would you like to do? Enter your choice from 1 to 4: \n")
        if choice == "1":
            flights = common_destinations(our_routes, competitor_routes)
            print(f"\nCommon destinations: {flights}")
        elif choice == "2":
            unique_destinations(airline_one, airline_two)
        elif choice == "3":
            potential_routes = potential_new_routes(our_routes, competitor_routes)
            print(f"No airline offer flights to these destinations: {potential_routes}")
        elif choice == "4":
            print("\nThank you for using our program!\n")
            break
        else:
            print("\nPlease enter a valid response!\n")

flight_route_comparison(our_routes, competitor_routes)

print("===============================================\n")

# 2. Set Operations in Data Analysis
# Objective:
# The aim of this assignment is to enhance your skills in using Python sets for data analysis tasks. You will apply various set operations 
# to handle real-world data scenarios, focusing on their practical application and efficiency.

# Task 1: Duplicate Entries Cleanup
# You are given a list of customer IDs, some of which are duplicated. Write a Python script to remove duplicates and display the unique customer IDs.

# Example Code:

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

# Expected Outcome:
# A set of unique customer IDs, ensuring no duplicates. For instance, {'C001', 'C002', 'C003', 'C004'}.

def remove_duplicates(ids):         
    return set(ids)         # Removing duplicates by converting the list to a set

print("\nThe unique customer IDs:\n")
print(remove_duplicates(customer_ids))
print("\n")