# Should probably functionalize reading input files

# def is_unstable(resident, hospital, matches)

def get_resident_list(resident_name):
    return residents_pref[resident]


def get_hospital_list(hospital_name):
    return hospitals_pref[hospital_name]


# input and output files opened
in_file = open('input/HRInput.txt', 'r')
out_file = open('output/HROutput.txt', 'w')

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

match_file = open('input/HRMatch.txt', 'r')
match_lines = match_file.readlines()
assignments = {}

# read in matches
for lines in match_lines:
    parts = lines.split()
    assignments[parts[0]] = parts[2:]


for assigned_hospital in assignments:
    print(assigned_hospital)
    matched_residents = assignments[assigned_hospital]
    for matched_resident in matched_residents:
        print(matched_resident)


in_file.close()
out_file.close()
match_file.close()

