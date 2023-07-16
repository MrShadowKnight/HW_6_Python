# TASK №1

number_one = int(input("Введіть початкове число: "))           # Вводимо початкове і кінцеве число діапазону
number_two = int(input("Введіть кінцеіе число: "))
list_diapasonu = []
if number_one > number_two:
    print("Початкове число не може бути більше кінцевого!") # Робимо перевірку
else:
    for num in range(number_one, number_two + 1):
        if num > 1:
            for i in range(2, num):                         # Якщо число з діапазону ділиться на інше окрім себе і 1 зупиняємо цикл в іншому випадку вводимо в список
                if (num % i) == 0:
                    break
                else:
                    list_diapasonu.append(num)
print("Прасті числа: ", list_diapasonu)                     # Виводимо список

TASK №2

for j in range(1, 11):                                      # Вводимо два масиви від 1 до 10
    for i in range(1, 11):
        production = j * i                                  # Виконуємо дію множення і виводимо на екран результат і дію         
        print(f"{j} * {i} = ", production)
    print("---------------")                                # Відділяємо від іншої таблиці

# TASK №3

start = int(input("Введіть початкове число: "))             # Вибираємо діапазон таблиці множення
end = int(input("Введіть кінцеве число: "))

if start > end:
    print("Початкове число не може бути більше кінцевого!") # Робимо перевірку
else:
    print(f"Таблиця множення від {start} до {end}: ")
    for t in range(start, end + 1):                         # Вводимо масив від start до end
        for k in range(1, 11):                              # Вводимо масив від 1 до 10
            product = t * k                                 # Виконуємо дію множення і виводимо на екран результат і дію 
            print(f"{t} * {k} = ", product)
        print("---------------")                            # Відділяємо від іншої таблиці

# ADDITIONAL TASK №1

import json

with open("products.json", "r", encoding="utf-8") as file:
    products = json.load(file)

sorted_product = sorted(products, key=lambda product: product["price"])
print(sorted_product)

# ADDITIONAL TASK №2

import json

with open("products.json", "r", encoding="utf-8") as file:
    products = json.load(file)

max_price = int(input("Введіть ціну яка буде максимально допустимою(Для виведення дорогих товарів): "))
sorted_product = sorted(products, key=lambda product: product["price"])
high_price = []
for item in products:
    product_price = int(item["price"].replace(" ", '').replace(' ', ''))
    if product_price > max_price:
        high_price.append(item),
print("Дорогі товари: ", high_price)

# ADDITIONAL TASK №3

import json

with open("product.json", "r", encoding="utf-8") as file:
    products = json.load(file)

amount_number = int(input("Введіть мінімальну кількість товару для продажі: "))
counter = 0
while counter < 20:
    for item in products:
        if item["amount"] < amount_number:
            print("Недостатньо товару:", item)
            counter += 1
        else:
            print("Достатньо товару для продажу:", item)
            counter += 1