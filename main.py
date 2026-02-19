from utils import is_it_your_birthday

def main():
    byear = int(input("Insert the year of your birth as YYYY "))
    bmonth = int(input("Insert the month of your birth as mm "))
    bday = int(input("Insert the day of your birth as dd "))
    result = is_it_your_birthday(byear, bmonth, bday)
    return result

if __name__ == "__main__":
    main()