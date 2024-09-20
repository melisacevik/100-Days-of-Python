def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't enter any name"

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name(input("Enter your first name: "), input("Enter your last name: ")))


# def is_leap_year(year):
#     # Write your code here.
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False
#
#     # Don't change the function name.
#
#
# is_leap_year(2024)