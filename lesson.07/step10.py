from functools import total_ordering


@total_ordering
class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __eq__(self, other):
        min_1 = self.minute + self.hour * 60
        min_2 = other.minute + other.hour * 60
        return min_1 == min_2

    def __lt__(self, other):
        min_1 = self.minute + self.hour * 60
        min_2 = other.minute + other.hour * 60
        return min_1 < min_2

    def __str__(self):
        return f"{self.hour}:{self.minute}"

#
# __and__
# __or__
# __not__

t1 = Time(hour=2, minute=47)
t2 = Time(hour=2, minute=47)

print(t1)
print(t2)

print(t1 != t2)
print(t1 >= t2)
print(t1 <= t2)
print(t1 == t2)