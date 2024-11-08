import datetime


def input_vals():
    date = datetime.datetime.strptime(input(), "%Y %m %d")
    days = int(input())
    return (date, days)


def main():
    date, days = input_vals()
    date += datetime.timedelta(days=days)
    # datetime.datetime.strftime(date,"%Y %m %d")
    print(date.year, date.month, date.day)


if __name__ == "__main__":
    main()
