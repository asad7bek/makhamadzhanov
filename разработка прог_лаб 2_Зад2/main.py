class Seconds:
    def __init__(self, seconds):
        self._seconds = seconds

    def __str__(self):
        return f"{self._seconds}s"

    def __int__(self):
        return self._seconds


class Minutes:
    def __init__(self, minutes):
        self._minutes = minutes

    def __str__(self):
        return f"{self._minutes}m"

    def __int__(self):
        return self._minutes


class Hours:
    def __init__(self, hours):
        self._hours = hours

    def __str__(self):
        return f"{self._hours}h"

    def __int__(self):
        return self._hours


class Time(Seconds, Minutes, Hours):
    def __init__(self, hours=0, minutes=0, seconds=0):
        Seconds.__init__(self, seconds)
        Minutes.__init__(self, minutes)
        Hours.__init__(self, hours)

    def __str__(self):
        return f"{self._hours}h {self._minutes}m {self._seconds}s"

    def total_seconds(self):
        return int(self._hours) * 3600 + int(self._minutes) * 60 + int(self._seconds)

    def __add__(self, other):
        if isinstance(other, Time):
            total_sec = self.total_seconds() + other.total_seconds()
            return Time(total_sec // 3600, (total_sec % 3600) // 60, total_sec % 60)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Time):
            total_sec_self = self.total_seconds()
            total_sec_other = other.total_seconds()
            result_sec = total_sec_self - total_sec_other
            if result_sec < 0:
                result_sec = 0
            return Time(result_sec // 3600, (result_sec % 3600) // 60, result_sec % 60)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Time):
            return self.total_seconds() == other.total_seconds()
        return NotImplemented


# Пример использования
time1 = Time(hours=2, minutes=30, seconds=45)
time2 = Time(hours=1, minutes=15, seconds=30)

print(time1)               # "2h 30m 45s"
print(time2)               # "1h 15m 30s"
print(time1.total_seconds()) # Общее время в секундах
print(time2.total_seconds()) # Общее время в секундах

time3 = time1 + time2
print(time3)               # "3h 46m 15s"

time4 = time1 - time2
print(time4)               # "1h 15m 15s"

print(time1 == time2)      # False
print(time1 == time3)      # False