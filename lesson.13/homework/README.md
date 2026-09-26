# Домашнее задание. Анализ табличных данных с Pandas

## Общие правила

Используйте:

```text
laptop.csv
```

Загрузите его через Pandas с кодировкой:

```text
windows-1251
```

Задачи решайте средствами Pandas, разобранными на занятии.

Не перебирайте строки DataFrame вручную через `for`.

> В примерах индекс DataFrame иногда не показан. Наличие индекса слева в вашем выводе не является ошибкой.

Задания 4–8 выполняются последовательно: созданные ранее столбцы используйте дальше, повторно создавать их не нужно.
Примеры вывода могут отличаться у вас от показанных тут ;-)

---

# Задание 1. Ноутбуки с Chrome OS

Найдите все ноутбуки с:

```text
OpSys = Chrome OS
```

Выведите количество моделей и первые 5 строк со столбцами:

```text
Company
Product
TypeName
OpSys
Price_euros
```

### Пример результата

```text
Количество: 27
```

```text
Company  Product              TypeName   OpSys      Price_euros
Acer     Chromebook C910-C2ST Notebook   Chrome OS       199.0
Lenovo   ThinkPad 13          Notebook   Chrome OS       459.9
Samsung  Chromebook 3         Netbook    Chrome OS       269.0
Google   Pixelbook (Core      Ultrabook  Chrome OS      2199.0
Google   Pixelbook (Core      Ultrabook  Chrome OS      1275.0
```

---

# Задание 2. Подбор ноутбука клиенту

Клиенту нужен ноутбук:

- `8GB` или `16GB` RAM;
- Windows 10;
- цена не выше `500` евро.

Определите количество вариантов и выведите первые 5:

```text
Company
Product
Ram
OpSys
Price_euros
```

### Пример результата

```text
Количество вариантов: 13
```

```text
Company  Product                                      Ram  OpSys       Price_euros
Acer     Aspire E5-475                                8GB  Windows 10       389.0
Dell     Inspiron 3567                                8GB  Windows 10       459.0
HP       15-BW094nd (A6-9220/8GB/128GB/W10)          8GB  Windows 10       445.9
HP       17-BS037cl (i3-6006U/8GB/1TB/W10)           8GB  Windows 10       489.0
Acer     ES1-523-84K7 (A8-7410/8GB/256GB/FHD/W10)    8GB  Windows 10       469.0
```

---

# Задание 3. Самая маленькая диагональ

Определите минимальную диагональ экрана в наборе данных.

Выведите **все** ноутбуки с такой диагональю:

```text
Company
Product
TypeName
Inches
Price_euros
```

### Пример результата

```text
Минимальная диагональ: 10.1
Количество моделей: 4
```

```text
Company  Product    TypeName              Inches  Price_euros
Lenovo   Yoga Book  2 in 1 Convertible     10.1       319.00
Lenovo   Yoga Book  2 in 1 Convertible     10.1       646.27
Lenovo   Yoga Book  2 in 1 Convertible     10.1       549.00
Lenovo   Yoga Book  2 in 1 Convertible     10.1       479.00
```

---

# Задание 4. Тип экрана

Создайте столбец:

```text
Display_type
```

Правила:

```text
есть IPS Panel и Touchscreen -> IPS Touch
есть только Touchscreen      -> Touch
есть только IPS Panel        -> IPS
остальные                    -> Обычный
```

Логику вынесите в отдельную функцию.

Посчитайте количество ноутбуков каждого типа.

### Пример результата

```text
IPS Touch: 85
Touch: 107
IPS: 280
Обычный: 831
```

---

# Задание 5. Недорогие трансформеры с IPS Touch

Используйте `Display_type` из задания 4.

Найдите ноутбуки:

```text
Display_type = IPS Touch
TypeName = 2 in 1 Convertible
Price_euros <= 1500
```

Отсортируйте по цене, а при одинаковой цене — по `laptop_ID`.

Выведите количество и первые 5 моделей.

### Пример результата

```text
Количество: 44
```

```text
laptop_ID  Company   Product                               Inches  Price_euros
436        Mediacom  FlexBook Edge                           11.6        299.0
51         Lenovo    Yoga Book                               10.1        319.0
567        Acer      Spin SP111-31                           11.6        349.0
626        Acer      CB5-132T-C9KK (N3160/4GB/32GB/Chrome   11.6        379.0
973        Acer      Chromebook C738T-C2EJ                   11.6        389.0
```

---

# Задание 6. Игровые ноутбуки с GTX 1060

Найдите модели:

```text
TypeName = Gaming
Gpu = Nvidia GeForce GTX 1060
диагональ не равна 17.3
цена <= 1800 евро
```

Отсортируйте по цене, затем по `laptop_ID`.

Выведите количество и первые 5 моделей.

### Пример результата

```text
Количество: 16
```

```text
laptop_ID  Company  Product                                   Inches  Price_euros
1143       Lenovo   Legion Y520-15IKBN                         15.6        989.0
516        Lenovo   Legion Y520-15IKBN                         15.6       1149.0
1222       Asus     FX502VM-DM105T (i7-6700HQ/8GB/1TB/GeForce 15.6       1169.0
1001       Lenovo   Legion Y520-15IKBN                         15.6       1189.0
95         Dell     Inspiron 7577                              15.6       1195.0
```

---

# Задания со звёздочкой ⭐

## Задание 7 ⭐. Тип накопителя

Создайте столбец:

```text
Storage_type
```

Правила:

```text
есть SSD и HDD -> SSD + HDD
есть SSD       -> SSD
есть HDD       -> HDD
остальные      -> Другое
```

После этого найдите модели:

```text
Storage_type = SSD + HDD
TypeName = Gaming
OpSys = Windows 10
Price_euros <= 1800
```

Отсортируйте по цене, затем по `laptop_ID`.

### Пример результата

```text
Количество: 82
```

Первые 5:

```text
laptop_ID  Company  Product                            Memory                Price_euros
1203       Asus     Rog GL552VW-DM201T                 256GB SSD + 1TB HDD        909.0
140        Asus     FX753VD-GC086T (i5-7300HQ/8GB/1TB 128GB SSD + 1TB HDD        938.0
22         Lenovo   Legion Y520-15IKBN                 128GB SSD + 1TB HDD        999.0
959        Lenovo   IdeaPad Y700-15ACZ                 512GB SSD + 1TB HDD        999.0
1246       Lenovo   IdeaPad Y700-15ISK                 128GB SSD + 1TB HDD       1029.0
```

---

## Задание 8 ⭐. Итоговый каталог

Используйте:

```text
Display_type
Storage_type
```

из заданий 4 и 7.

Отберите ноутбуки:

```text
Display_type = IPS
Storage_type = SSD + HDD
OpSys = Windows 10
1000 <= Price_euros <= 1600
```

Оставьте:

```text
laptop_ID
Company
Product
TypeName
Memory
Price_euros
Display_type
Storage_type
```

Отсортируйте:

1. по компании;
2. внутри компании — по цене от большей к меньшей;
3. при одинаковой цене — по `laptop_ID`.

Обновите индексы и сохраните результат:

```text
final_catalog.csv
```

без индекса DataFrame.

### Пример результата

```text
Количество: 33
```

Первые 5:

```text
laptop_ID  Company  Product                            TypeName  Price_euros
1014       Acer     Nitro 5                            Gaming        1260.0
1263       Asus     Rog GL553VE-FY052T                 Gaming        1600.0
1107       Asus     Rog GL702VM-GC354T                 Gaming        1599.0
90         Asus     FX503VM-E4007T (i7-7700HQ/16GB/1TB Gaming        1449.0
1124       Asus     Rog GL552VW-CN470T                 Gaming        1339.0
```

---

# Проект: Телефонный справочник. Часть 10

Добавьте Pandas как основную зависимость проекта.

Создайте отчёт по контактам со столбцами:

```text
Name
Phone
Type
Name_length
```

Для `Type`:

```text
Личный
Рабочий
```

Длину имени получите через отдельную функцию.

Отсортируйте контакты по типу и имени и сохраните:

```text
data/contacts_report.csv
```

без индекса.

Добавьте пункт меню:

```text
10. Экспорт отчёта CSV
```

### Пример результата

```text
Name,Phone,Type,Name_length
Анна,+79991234567,Личный,4
Мария,+78881234567,Личный,5
Иван,89991234567,Рабочий,4
Константин,87771234567,Рабочий,10
```

---
