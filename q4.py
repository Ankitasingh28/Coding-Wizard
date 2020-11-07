d = [31, 28, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31]
def doy(d) :
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:])
    if (month > 2 and year % 4 == 0 and
            (year % 100 != 0 or year % 400 == 0)):
        day += 1
    month -= 1
    while month > 0:
        day = day + d[month - 1]
        month -= 1
    return day
if __name__ == '__main__':
    date = input('input date in string format and in yyyy-MM-DD format with - as seperator' )
    print(doy(d))