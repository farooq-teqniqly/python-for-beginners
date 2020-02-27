try:
  print(1 / 0)
except ZeroDivisionError as e:
  print(f"Cannot divide by zero.\n{e}")
else:
  print(f"Something else went wrong.")
finally:
  print("Done.")