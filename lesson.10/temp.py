# Задание 6. Доставка посылок
#
# Создайте родительский класс:
#
# Delivery
#
# При создании передавайте:
#
#     город;
#     вес посылки.
#
# Добавьте метод:
#
# calculate_price()
#
# Создайте два дочерних класса:
#
# CourierDelivery
# PostDelivery
#
# Переопределите метод calculate_price().
# Правила
#
# Курьерская доставка:
#
# 500 + 50 * вес
#
# Почтовая доставка:
#
# 200 + 30 * вес
#
# Пример работы
#
# courier = CourierDelivery("Москва", 3)
# post = PostDelivery("Казань", 3)
#
# print(courier.calculate_price())
# print(post.calculate_price())
#
# Результат
#
# 650
# 290
#
# После этого создайте список разных доставок и одним циклом выведите стоимость каждой.
class Delivery:
    def __init__(self, city, weight):
        self.city = city
        self.weight = weight

    def calculate_price(self):
        pass


class CourierDelivery(Delivery):
    def calculate_price(self):
        return  500 + 50 * self.weight


class PostDelivery(Delivery):
    def calculate_price(self):
        return 200 + 30 * self.weight


courier = CourierDelivery("Москва", 3)
post = PostDelivery("Казань", 3)

print(courier.calculate_price())
print(post.calculate_price())



delivery_list = ("Moscow", 3), ("SPB", 4), ("Minsk", 5)
print(delivery_list)

# С запоминанием(пониманием) типов у меня плохо - поэтому проверял тут
print(type(delivery_list))

# Проверял, возвращается ли пара "город + вес" по индексу в надежде скормить эту пару функции
print(delivery_list[2])

# Я тут некорректно итерируюсь по списку доставок, или у меня некорректный формат самого списка delivery_list? Пробовал ещё со словарём - тоже не получилось
for item in delivery_list:
    courier = CourierDelivery(*item)
    print(courier.calculate_price())



# for key, value in delivery_list.items():
#     print(courier.calculate_price(key, value))
#     print(post.calculate_price(key, value))