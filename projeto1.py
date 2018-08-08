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