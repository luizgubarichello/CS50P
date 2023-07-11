from datetime import date
import sys
import inflect


p = inflect.engine()


def main():
    birthdate = check_date(input("Date of Birth (YYYY-MM-DD): "))
    dif = date.today() - birthdate
    dif_time = round(dif.total_seconds()/60)
    dif_time_words = p.number_to_words(dif_time, andword="").capitalize()
    print(f"{dif_time_words} minutes")


def check_date(d):
    try:
        bdate = date.fromisoformat(d)
        return bdate
    except ValueError:
        sys.exit("Invalid Date")



if __name__ == "__main__":
    main()