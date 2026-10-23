import csv

#write
with open("student.csv", "w", newline='') as f:
    writer=csv.writer(f)
    writer.writerow(["name", "roll", "mark"])
    writer.writerow(["Amanda", 45, 88])
    writer.writerow(["Raj", 30, 90])

#read
with open("student.csv", "r") as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)
    print("\n")