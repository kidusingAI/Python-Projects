def is_weekend(day):
  match day:
    case "Sunday"|"Saturday":
      return print("Woo-Hoo! its the weekend")
    case _:
      return print("That is not the weeekend :(")

is_weekend(day = input("What day of the week is it").capitalize())
