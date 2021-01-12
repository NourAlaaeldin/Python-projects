def Comparison_1():
    is_male = False
    is_tall = False

    if is_male and is_tall:
        print("You are a male and you are tall !!")
    elif is_male and not(is_tall):
        print("You are a male but you are not tall !!")
    elif not(is_male) and is_tall:
        print("You are a female and you are tall !!")
    else:
        print("You are a female but you are not tall !!")

def find_max(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        max = num1
    elif num2 > num1 and num2 > num3:
        max = num2
    else:
        max = num3
    return max

def find_min(num1,num2,num3):
    if num1 < num2 and num1 < num3:
        min = num1
    elif num2 < num1 and num2 < num3:
        min = num2
    else:
        min = num3
    return min

Comparison_1()
print("*********************************")
max_value = find_max(1,2,3)
print("Max value equals:",max_value)
print("*********************************")
min_value = find_min(1,2,3)
print("Min value equals:",min_value)