from email.mime import base


def is_base13_number( base13 ):
    split_base13 = base13.split(".")

    # Validation, is a marcian number???
    result = True
    for part in split_base13:
        for digit in part:
            if not (0<=int(digit)<13):  # remember type of digit is str
                result = False
                break
        if not result:
            break

        return result

def base13_to_base10( base13_number ):
    split_number = base13_number.split(".")
    # display and compute numeric expansion
    print("\nExpansion in power series: \n\t",end="")

    # integer part
    integer_part = 0
    max_exponent = len(split_number[0]) - 1
    for i, d in enumerate(split_number[0]):
        integer_part += int(d) * (13**(max_exponent-i))

        if i < max_exponent:
            print("{0}*13^{1}".format( d, max_exponent-i ),end=" + ")
        else:
            print("{0}*13^{1}".format( d, max_exponent-i ),end="")

    # decimal part  
    decimal_part = 0
    if len(split_number) > 1:
        max_exponent = len(split_number[1]) - 1

        print(" + ",end="")
        for i, d in enumerate(split_number[1]):
            decimal_part += int(d) * (13**( -(i+1) ))

            print("{0}*13^-{1}".format(d,i+1),
                                end = " + " if i < max_exponent else "\n")

    return integer_part + decimal_part

def main():
    print("\n"*3)
    print("="*50)
    print("From base 13 to base 10 numeric system".center(50))
    print("="*50)
    print("\n")

    base13 = input("input the number in base 13: ")
    print("you enter: ", base13)

    if is_base13_number( base13 ):
        value_base10 = base13_to_base10( base13 )
        print("\nnumber in base 13 ", base13, " in base 10 is: ", value_base10)
    else:
        print(base13, """ is not a number in base 13!!!
    I can't help you ...
    *note: base 5 digits are only: 0, 1, 2, 3, 4, ,6 , 7, 8, 9 """)

    print("\n"*2)

if __name__ ==  "__main__":
    main()