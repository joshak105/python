import csv
with open("product.csv", "w") as csvfile:
    writer = csv.writer(csvfile)

writer.writerow(["Product Name", "Product Description"])
with open("product.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        writer.writerow([row[0], row[1]])
with open("quantity.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        writer.writerow([row[0], row[1]])
with open("price.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        writer.writerow([row[0], row[1]])
        writer.writerow(["Sales"])
        writer.writerow(["Price"])
        writer.writerow(["Region"])
