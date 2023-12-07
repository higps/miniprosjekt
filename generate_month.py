def int_to_month(value):
    # Ensure the value is non-negative
    value = value % 12

    # Adjust 0 to 11 to match the index of months
    if value == 0:
        value = 12

    # Define the list of month names
    months = [
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"
    ]

    # Return the corresponding month as uppercase
    return months[value - 1].upper()

# Example usage:
# integer_value = 34
# month_name = int_to_month(integer_value)
# print(f"{integer_value} corresponds to {month_name}")
# the_list = [0,0,0,0,1,2,3,4,5]
# for i in (the_list):
#     print(int_to_month(i))