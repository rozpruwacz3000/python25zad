import csv

header = ["Date", "Product", "Units Sold", "Price per Unit"]
sales_data = [
    ("2023-10-01", "Laptop", 5, 1200.0),
    ("2023-10-01", "Phone", 10, 500.0),
    ("2023-10-02", "Laptop", 3, 1200.0),
    ("2023-10-02", "Phone", 7, 500.0),
    ("2023-10-03", "Laptop", 4, 1200.0),
    ("2023-10-03", "Phone", 12, 500.0),
]

file_name = 'sales_data.csv'

with open(file_name,'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(header)
    writer.writerows(sales_data)

print(f"Dane zostały zapisane do pliku {file_name}.\n")

total_laptop_value = 0.0
with open(file_name,'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        product_name = row[1]

        if product_name == "Laptop":
            units_sold = int(row[2])
            price_per_unit = float(row[3])
            total_laptop_value += units_sold * price_per_unit


print(f"Łączna wartość sprzedanych laptopów: {total_laptop_value}")