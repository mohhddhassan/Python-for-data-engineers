import csv

# Writing CSV
with open('users.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name"])
    writer.writerow([1, "Alice"])

# Reading CSV
with open('users.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
