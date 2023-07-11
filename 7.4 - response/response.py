from validator_collection import checkers

email = input("Email: ").strip()
if checkers.is_email(email):
    print("Valid")
else:
    print("Invalid")