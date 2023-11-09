filename = input("Enter the file name:")
total = 0
count = 0
with open(filename, 'r') as file:
    for line in file:
        if line.startswith("X-DSPAM-Confidence:"):
            starting_postion = line.find(":") + 1
            sample_number = float(line[starting_postion:])
            count += 1
            total += sample_number
if count > 0:
    average = total/count
    print("There are",count,"Samples and ",average,"at average")
else:
    print("No line found with the condition")