N = int (input ('Сколько билетов вы хотите приобрести? '))
sum = 0

for i in range (N):
    age = int (input ('Введите возраст посетителя: '))
    if age < 18:
        continue
    elif 18 <= age <= 25:
        sum += 990
    elif age > 25:
        sum += 1390

if N > 3: 
    sum *= 0.9       

print (f'Сумма вашего заказа: {int (sum)} руб.')