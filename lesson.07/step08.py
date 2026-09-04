class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __add__(self, other):
        if isinstance(other, Time):
            hour = self.hour + other.hour
            minute = self.minute + other.minute
            hour += minute // 60
            minute = minute % 60
            return Time(hour=hour, minute=minute)

    def __sub__(self, other):
        if isinstance(other, Time):
            hour = self.hour - other.hour
            minute = self.minute - other.minute
            # hour += minute // 60
            # minute = minute % 60
            return Time(hour=hour, minute=minute)

    # def __mul__(self, other):
    # def __mod__(self, other):
    # def __div__(self, other):
    # def __truediv__(self, other):

    # def __pow__(self, other):

    def __str__(self):
        return f"{self.hour}:{self.minute}"


t1 = Time(hour=1, minute=15)
t2 = Time(hour=2, minute=47)

print(t1)
print(t2)

t3  = t1 + t2
print(t3)

t4  = t2 - t1
print(t4)