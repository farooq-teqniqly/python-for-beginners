from datetime import datetime

birthday = input("When is your birthday (dd/mm/yyyy)? ")
print(f"Your birthday is on {datetime.strptime(birthday, '%d/%m/%Y')}")