def convert_base_2(number):
    """
   Convert
   :param number: Number to convert
   :return: List of the number's digits in base 2 representation
    """
    digit_list=[]

    while number!= 0:
        """
        digit_list.append(number % 2)
        number //=2 #divide integer
        digit_list.reverse()
    """
        digit_list.insert(0,number % 2)
        number //= 2  # divide integer
    return digit_list

my_number=int(input("Enter the number to convert base 10 to base 2:"))
digit_list = convert_base_2(my_number)

as_string=""
for el in digit_list:
    as_string+=str(el)
print("Value", str(my_number))