import csv
import random
import json
import numpy as np


class Product:
    def __init__(self, category_id):  # Tylko category_id podajemy z zewnątrz
        # Najpierw sprawdzamy błędy
        if not isinstance(category_id, int) or not (1 <= category_id <= 5):
            raise ValueError("category_id must be an integer between 1 and 5")

        # Potem przypisujemy wartości
        self.category_id = category_id
        self.price = 0.0  # Atrybut zerowany (float)
        self.quantity = 0  # Atrybut zerowany


   def restock(self,amount,unit_price):
    self.quantity += amount
    self.price = unit_price

    def dump(self):
        return[self.category_id,self.price,self.quantity]
def save_warehouse(object_list,filename"warehouse.csv"):
    with open(filename, mode='w',newline='') as file:
        writer = csv.writer(file)
        for obj in objects_list:
            writer.writerow(obj.dump())

warehouse = []
for r in range(40):
        random_category_id = random.randint(1,5)
        new_product = Product(random_category_id)

        random_amount = random.randint(1,100)
        random_unit_price = random.uniform(10.0,500.0)

        new_product.restock(random_amount,random_unit_price)

        warehouse.append(new_product)


save_warehouse(warehouse)


data = np.genfromtxt('warehouse.csv',delimiter=',')

avg_price = np.mean(data[:,1])
total_qty = np.sum(data[:,2])
cat_1_count = np.sum(data[:,0]==1)

print(f"Średnia cena: {avg_price:.2f}")
print(f"Łącznie sztuk: {int(total_qty)}")
print(f"Kategoria 1: {int(cat_1_count)} szt.")

report = {
    "total_quantity": int(total_qty),
    "average_price": int(avg_price),
}
with open("report.json", "w") as f:
    json.dump(report, f,indent =4)
print("Raport JSON wygenerowany!")



