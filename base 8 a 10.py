from email.mime import base


def is_base8_number( base8 ):
    split_base8 = base8.split(".")

    # Validation, is a marcian number???
    result = True
    for part in split_base8:
        for digit in part:
            if not (0<=int(digit)<8):  # remember type of digit is str
                result = False
                break
        if not result:
            break

        return result

def base8_to_base10( base8_number ):
    split_number = base8_number.split(".")
    # display and compute numeric expansion
    print("\nExpansion in power series: \n\t",end="")

    # integer part
    integer_part = 0
    max_exponent = len(split_number[0]) - 1
    for i, d in enumerate(split_number[0]):
        integer_part += int(d) * (8**(max_exponent-i))

        if i < max_exponent:
            print("{0}*8^{1}".format( d, max_exponent-i ),end=" + ")
        else:
            print("{0}*8^{1}".format( d, max_exponent-i ),end="")

    # decimal part  
    decimal_part = 0
    if len(split_number) > 1:
        max_exponent = len(split_number[1]) - 1

        print(" + ",end="")
        for i, d in enumerate(split_number[1]):
            decimal_part += int(d) * (8**( -(i+1) ))

            print("{0}*8^-{1}".format(d,i+1),
                                end = " + " if i < max_exponent else "\n")

    return integer_part + decimal_part

def main():
    print("\n"*3)
    print("="*50)
    print("From base 8 to base 10 numeric system".center(50))
    print("="*50)
    print("\n")

    base8 = input("input the number in base 8: ")
    print("you enter: ", base8)

    if is_base8_number( base8 ):
        value_base10 = base8_to_base10( base8 )
        print("\nnumber in base 8 ", base8, " in base 10 is: ", value_base10)
    else:
        print(base8, """ is not a number in base 8!!!
    I can't help you ...
    *note: base 8 digits are only: 0, 1, 2, 3, 4, 5, 6, 7 """)

    print("\n"*2)

if __name__ ==  "__main__":
    main()