from datetime import datetime, timedelta

today = datetime.now()
print(f"Today is {today}")

yesterday = today - timedelta(days=1)
print(f"Yesterday was {yesterday}")

tomorrow = today + timedelta(days=1)
print(f"Tomorrow is {tomorrow}")

