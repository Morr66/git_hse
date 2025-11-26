import requests
from bs4 import BeautifulSoup
import csv
from datetime import *

date_today = datetime.now().strftime("%Y-%m-%d")

try:
    req = requests.get("https://cbr.ru/currency_base/daily/")
    if req.status_code != 200:
        print('Error')
        exit()
    src = req.text
    soup = BeautifulSoup(src, 'html.parser')
    table = soup.find('table', class_='data')
    rows = table.find_all('tr')[1:]
    filename = f"currency_rates_{date_today}.csv"
    with open(filename, mode='w', newline='', encoding='utf-16') as f:
        writer = csv.writer(f)
        writer.writerow(['№', 'Цифровой код', 'Буквенный код', 'Единиц', 'Валюта', 'Курс'])
        i = 1
        for row in rows:
            cols = [i]

            for col in row.find_all('td'):
                cols.append(col.text.strip().replace(',', '.'))
            writer.writerow(cols)
            i += 1
    with open(filename, encoding='utf-16') as f:
        file = csv.reader(f, delimiter=',')
        a = [i for i in file]
        a += [['', '', 'RUB', '1', 'Рубль', '1']]
        all = input('Желаете узнать курсы всех валют на сегодня? (да/нет) ').strip()
        if all.lower() == 'да':
            for i in a[1:-1]:
                print(f"{i[2]} ({i[4]}): {round(float(i[5]), 2)} RUB (за {i[3]} единиц)")
        while True:
            print('------------------------------------')
            print('Введите данные для конвертации')
            try:
                s = float(input('Сумма: ').strip())
            except:
                print('Введите число и попроуйте еще раз')
                continue
            v1 = input('Введите название исходной валюты (код): ').strip().upper()
            v2 = input('Введите название целевой валюты (код): ').strip().upper()
            lst1 = []
            lst2 = []
            for i in a:
                if v1 in i:
                    lst1 = i
                if v2 in i:
                    lst2 = i
            if lst1 == [] and lst2 == []:
                print('Такие валюты не найдены, попробуйте еще раз')
                continue
            elif lst1 == []:
                print('Исходная валюта не найдена, попробуйте еще раз')
                continue
            elif lst2 == []:
                print('Целевая валюта не найдена, попробуйте еще раз')
                continue
            res = round(float(lst1[5]) * s / int(lst1[3]) / float(lst2[5]) * int(lst2[3]), 3)

            print(f'Результат: {s} {lst1[4]} = {res} {lst2[4]}')
            ans = input('Желаете продолжить конвертацию? (да/нет) ').strip()
            if ans.lower() == 'да':
                continue
            else:
                print('Спасибо за использование моего конвертера')
                exit()
except requests.exceptions.Timeout:
    print('Превышено время ожидания ответа от сервера')