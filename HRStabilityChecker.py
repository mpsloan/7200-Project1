
# input and output files opened
in_file = open('input/HRInput.txt', 'r')
out_file = open('output/HROutput.txt', 'w')

in_lines = in_file.readlines()

num_hospitals = int(in_lines[0])
num_residents = int(in_lines[1])

# hospitals is a dictionary
# the key is the hospital's name
# the values are their preferred list of residents (in decreasing order)
hospitals = {}

# offset is 2 because the first two lines of the file have already been read
offset = 2
i = 0

while i < num_hospitals:
    # parts is a list of the line split by spaces
    parts = in_lines[i + offset].split()
    hospitals[parts[0]] = parts[2:]
    i += 1


# residents is a dictionary
# the key is the resident's name
# the values are their preferred list of hospitals (in decreasing order)
residents = {}

# offset is increased because the hospitals have now been read
offset = offset + num_hospitals
j = 0

while j < num_residents:
    parts = in_lines[j + offset].split()
    residents[parts[0]] = parts[1:]
    j += 1

# assignments = dict.fromkeys(hospitals, [])

assignments = {}

for resident in residents:
    resident_list = residents[resident]
    for hospital in resident_list:
        hospital_list = hospitals[hospital]
        if hospital in resident_list and resident in hospital_list:
            print(hospital + ' is in', resident + ' list and', resident + ' is in', hospital, 'list')
            # assignments[hospital].append(resident)
            if assignments.get(hospital) is None:
                assignments[hospital] = [resident]
                print(assignments.get(hospital))
            else:
                assignments[hospital].append(resident)


print(assignments)

in_file.close()
out_file.close()


