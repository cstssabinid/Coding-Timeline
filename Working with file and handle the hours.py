filename = input("Enter file name:")
hours = {}
with open(filename,'r') as file:
    for line in file:
        if line.startswith("From"):
            text = line.split()
            time = text[5]
            hour = time.split(":")[0]
            hours[hour] = hours.get(hour , 0) + 1
sorted_hours = sorted(hours.items())
for hour , count in sorted_hours:
    print(hour,count)