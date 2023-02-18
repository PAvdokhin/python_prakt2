import csv
with open("stage3_test.csv", "r") as f:
    reader = csv.DictReader(f, delimiter=",")
    for row in reader:
        print(row["First name"])
        print(row["Last name"])


with open("stage3_test.csv", "w") as m:
    fieldnames = ["first name", "last name"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({
            'first name': 'Ivan',
            'last name': 'Ivanov'
    })
