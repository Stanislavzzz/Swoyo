from datetime import datetime, date, time, timedelta


# t = time(14, 30, 17)
# print(t)
# print(type(t))


# d1 = date(2026, 10, 17)
# d2 = date(2026, 8, 11)
# print(d1)
# print(d2)

# print(d1 > d2)
# print(d1 == d2)
#
# delta = d1 - d2
# print(delta)
# print(delta.days)
# print(type(delta))

# d3 = date.today()
# print(d3)
# print(d3 + timedelta(days=7))
# print(d3 - timedelta(days=17))


now = datetime.now()
print(now)

formatted = now.strftime(" %m * %Y * * %d %H - %M - %S")
print(formatted)


text = "2026_09_10 18-16-36"
dt = datetime.strptime(text, "%Y_%m_%d %H-%M-%S")
print(dt)
print(type(dt))