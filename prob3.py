def string_match(str_one,str_two):
    count=0
    for x in range(0,min(len(str_one),len(str_two))-1):
        if str_one[x:x + 2] == str_two[x:x+2]:
            count+=1
    return count

first_str=input("Enter the first:")
second_str=input("Enter the second:")

print(string_match(first_str,second_str))