# Here goes the imports

# coding: utf-8

# Here goes the imports
import csv
import matplotlib.pyplot as plt

# Let's read the data as a list
print("Reading the document...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Let's check how many rows do we have
print("Number of rows:")
print(len(data_list))

# Printing the first row of data_list to check if it worked.
print("Row 0: ")
print(data_list[0])
# It's the data header, so we can identify the columns.

# Printing the second row of data_list, it should contain some data
print("Row 1: ")
print(data_list[1])

input("Press Enter to continue...")
###########################################################################
# TASK 1
# TODO: Print the first 20 rows using a loop to identify the data.
print("\n\nTASK 1: Printing the first 20 samples")

# Let's change the data_list to remove the header from it.
data_list = data_list[1:]

# We can access the features through index
# E.g. sample[6] to print gender or sample[-2]
for i in range(20):
    print(data_list[i])
    
############################################################################
input("Press Enter to continue...")
###########################################################################
# TASK 2
# TODO: Print the `gender` of the first 20 rows

print("\nTASK 2: Printing the genders of the first 20 samples")

# Cool! We can get the rows(samples) iterating with a for and the columns(features) by index.
# But it's still hard to get a column in a list. Example: List with all genders

#data_list_gender = []
for i in range(20):
    #data_list_gender.append(data_list[i][6])
    print(i+1, data_list[i][6])
##################################################################################
input("\nPress Enter to continue...")
##################################################################################
# TASK 3
# TODO: Create a function to add the columns(features) of a list in another list in the same order
def column_to_list(data, index):
    """
    Function to transform columns into lists
    Args:
        data: the list
        index: the item position
    Returns:
        List of indexed items

    """
    column_list = []
    # Tip: You can use a for to iterate over the samples, get the feature by index and append into a list
    for i, value in enumerate(data):
        column_list.append(value[index])

    return column_list

# Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples")
print(column_to_list(data_list, -2)[:20])
####################################################################################
# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, -2)) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, -2)) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TASK 3: The list doesn't match."
# -----------------------------------------------------

input("\nPress Enter to continue...")
# Now we know how to access the features, let's count how many Males and Females the dataset have
####################################################################################
# TASK 4
# TODO: Count each gender. You should not use a function to do that.
male = 0
female = 0

for i, value in enumerate(data_list):
    if value[-2] == "Male":
        male += 1
    elif value[-2] == "Female":
        female += 1
    else:
        None

# Checking the result
print("\nTASK 4: Printing how many males and females we found")
print("Male: ", male, "\nFemale: ", female)
#################################################################################
# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------

input("\nPress Enter to continue...")
# Why don't we creeate a function to do that?
#################################################################################
# TASK 5
# TODO: Create a function to count the genders. Return a list
# Should return a list with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)
def count_gender(data_list):
    """
    Count males or females
    Args:
        data_list: List of data 
            obs:The gender MUST be in column = -2
    Returns:
        List of genders

    """
    male = 0
    female = 0
    
    for i, value in enumerate(data_list):
        if value[-2] == "Male":
            male += 1
        elif value[-2] == "Female":
            female += 1
        else:
            None

    return [male, female]


print("\nTASK 5: Printing result of count_gender")
print(count_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong lenght returned."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------

input("\nPress Enter to continue...")
# Now we can count the users, which gender use it the most?
######################################################################################
# TASK 6
# TODO: Create a function to get the most popular gender and print the gender as string.
# We expect to see "Male", "Female" or "Equal" as answer.
def most_popular_gender(data_list):
    """
    Find the most popular gender in a list
    Args:
        data_list: list of data
              obs: The gender MUST be in column = -2
              because this function depeds of count_gender
    Returns:
        Male, Female or Equal 

    """

    answer = ""
    gender = count_gender(data_list)
    if gender[0] > gender[1]:
        answer = "Male"
    elif gender [0] < gender [1]:
        answer = "Female"
    elif gender [0] == gender [1]:
        answer = "Equal"
    return answer


print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(data_list) == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------

# If it's everything running as expected, check this graph!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)

input("\nPress Enter to continue...")
######################################################################################
# TASK 7
# TODO: Plot a similar graph for user_types. Make sure the legend is correct.
print("\nTASK 7: Check the chart!")

# Data to plot
labels = 'Male', 'Female', 'NaN'
quantity = count_gender(data_list)
norm = len(data_list)
NaN = norm - quantity[0] + quantity[1]
sizes = [int(1000*(quantity[0]/norm)), int(1000*(quantity[1]/norm)), int(1000*(NaN/norm))]
colors = ['lightskyblue', 'lightcoral', 'gray']
explode = (0.05, 0, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=90)
 
plt.axis('equal')
plt.show()

input("\nPress Enter to continue...")

######################################################################################
# TASK 8
# TODO: Answer the following question
male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Some users leave the answer empty so there is no data to count"
print("Answer:", answer)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Let's work with the trip_duration now. We cant get some values from it.

######################################################################################
# TASK 9
# TODO: Find the Minimum, Maximum, Mean and Median trip duration.
# You should not use ready functions to do that, like max() or min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

### here is my first try, but i can't find the median ##
"""
for i in range(len(trip_duration_list)):
    aux = trip_duration_list[i]
    aux = float(aux)

    if max_trip < aux:
        max_trip = aux
        if i == 0:
            min_trip = aux
    if min_trip > aux:
        min_trip = aux
    
    mean_trip += aux
    i += 1


mean_trip = round(mean_trip/len(trip_duration_list))
max_trip = int(max_trip)
min_trip = int(min_trip)

"""

#so, i searched for sort algorithms withou use ready functions like sort()
#-----sort algorith find in: http://python3.codes/popular-sorting-algorithms/  #
def sort_without_built_in_function(arr):
    """
    Quick sort function without .sort()
    Args:
        arr: list of data
    Returns:
        The same input list but now sorted 

    """
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = sort_without_built_in_function(less)
        more = sort_without_built_in_function(more)
        return less + pivotList + more
#-----------------------------------------------------------------------------#

float_trip_duration_list = []
#mean
n = len(trip_duration_list)
for i in range(n):
    mean_trip += float(trip_duration_list[i])
    float_trip_duration_list += [float(trip_duration_list[i])]
mean_trip /= n
mean_trip = round(mean_trip)

sorted_trip_duration_list = sort_without_built_in_function(float_trip_duration_list)

#max and min
min_trip = sorted_trip_duration_list[0]
max_trip = sorted_trip_duration_list[-1]

#median
if len(sorted_trip_duration_list)%2 != 0:
    #print(len(sorted_trip_duration_list)/2)
    i = int(len(sorted_trip_duration_list)//2) + 1
    median_trip = sorted_trip_duration_list[i]
else:
    i = int(len(sorted_trip_duration_list)//2)
    median_trip = (sorted_trip_duration_list[i] + sorted_trip_duration_list[i+1])/2 


print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", min_trip, "Max: ", max_trip, "Mean: ", mean_trip, "Median: ", median_trip)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")

########################################################################################
# TASK 10
# Gender is easy because usually only have a few options. How about start_stations? How many options does it have?
# TODO: Check types how many start_stations do we have using set()
user_types = column_to_list(data_list, 3)
user_types = set(user_types)

print("\nTASK 10: Printing start stations:")
print(len(user_types))
print(user_types)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(user_types) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------

input("Press Enter to continue...")
########################################################################################
# TASK 11
# Go back and make sure you documented your functions. Explain the input, output and what it do. Example:
# def new_function(param1: int, param2: str) -> list:
"""
Example function with annotations.
Args:
    param1: The first parameter.
    param2: The second parameter.
Returns:
    List of X values

"""
print("\n\nAll functions documented\n\n")

input("Press Enter to continue...")
###########################################################################################3
# TASK 12 - Challenge! (Optional)
# TODO: Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
print("Will you face it?")
answer = "yes"
print("OF COURSE!!!")

def count_items(column_list):
    item_types = []
    count_items = []

    for value in column_list:
        if value not in item_types:
            item_types.append(value)
            c = column_list.count(value)
            idx = item_types.index(value)
            count_items.insert(idx, c)

    return item_types, count_items


if answer == "yes":
    # ------------ DO NOT CHANGE ANY CODE HERE ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTASK 11: Printing results for count_items()")
    print("Types:", types, "Counts:", counts)
    assert len(types) == 3, "TASK 11: There are 3 types of gender!"
    assert sum(counts) == 1551505, "TASK 11: Returning wrong result!"
    # -----------------------------------------------------

print("waiting for the next challenge")
input("Press Enter to continue...")


