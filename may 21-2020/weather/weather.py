def whether_cond(temp):
    if temp > 7:
        return "warm"
    else:
        return "cold"

user_input = float(input("enter the temperature:"))
print(whether_cond(user_input))
print(type(user_input), user_input)