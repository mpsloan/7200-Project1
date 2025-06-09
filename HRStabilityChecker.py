# Michael Sloan
# CS 7200
# Project 1
# June 8th, 2025

# The definition of stability for the hospital-residents matching problem is
# when a resident doesn't prefer a hospital more than it's assigned hospital
# or if it does, that hospital doesn't prefer that resident over it's assigned
# residents

# function that returns any resident's preference list
def get_resident_list(resident_name):
    return residents_pref[resident_name]


# function that returns any hospital's preference list
def get_hospital_list(hospital_name):
    return hospitals_pref[hospital_name]


# function that returns any hospital's assigned residents
def get_hospital_assignments(hospital_name):
    return assignments[hospital_name]


# input and output files opened
in_file = open('input/HRInput.txt', 'r')
out_file = open('output/HRStable.txt', 'w')

in_lines = in_file.readlines()

num_hospitals = int(in_lines[0])
num_residents = int(in_lines[1])

# hospitals_pref is a dictionary
# the key is the hospital's name
# the values are their preferred list of residents (in decreasing order)
hospitals_pref = {}

# offset is 2 because the first two lines of the file have already been read
offset = 2
i = 0
# number of residents hospital wants
num_hospitals_pref = 0


# file parser loops
while i < num_hospitals:
    # parts is a list of the line split by spaces
    parts = in_lines[i + offset].split()
    hospitals_pref[parts[0]] = parts[2:]
    i += 1


# residents is a dictionary
# the key is the resident's name
# the values are their preferred list of hospitals_pref (in decreasing order)
residents_pref = {}

# offset is increased because the hospitals_pref have now been read
offset = offset + num_hospitals
j = 0

while j < num_residents:
    parts = in_lines[j + offset].split()
    residents_pref[parts[0]] = parts[1:]
    j += 1

# open and read the match file
match_file = open('input/HRMatch2.txt', 'r')
match_lines = match_file.readlines()
assignments = {}

# read in matches
for lines in match_lines:
    parts = lines.split()
    assignments[parts[0]] = parts[2:]

unstable = False

# iterate through each hospital that has residents assigned to it
for assigned_hospital in assignments:
    assigned_residents = assignments[assigned_hospital]
    # iterate through each resident that has been assigned to that hospital
    for assigned_resident in assigned_residents:
        assigned_residents_pref = get_resident_list(assigned_resident)
        # iterate through each hospital in assigned resident's preference list
        for current_hospital in assigned_residents_pref:
            # get assigned resident's preference on each hospital in their list by checking their index
            current_hospital_rank = assigned_residents_pref.index(current_hospital)

            # get assigned resident's preference on their assigned hospital by checking their index
            assigned_hospital_rank = assigned_residents_pref.index(assigned_hospital)

            # they prefer another hospital over current one
            if current_hospital_rank < assigned_hospital_rank:
                current_hospital_pref = get_hospital_list(current_hospital)
                current_hospital_assignees = get_hospital_assignments(current_hospital)

                # iterate through each resident in the current hospital's preference list
                for current_resident in current_hospital_pref:
                    # iterate through each assignee in current hospital assignees
                    for assignee in current_hospital_assignees:
                        if assignee not in current_hospital_pref:
                            unstable = True
                            break


if unstable:
    out_file.write("NO")
    print("Unstable")
else:
    out_file.write("YES")
    print("Stable")

in_file.close()
out_file.close()
match_file.close()
