def is_base11_number( base11 ):
    split_base11 = base11.split(".")

    # Validation, is a marcian number???
    result = True
    for part in split_base11:
        for digit in part:
            if not (0<=int(digit)<11):  # remember type of digit is str
                result = False
                break
        if not result:
            break

        return result

def base11_to_base10( base11_number ):
    split_number = base11_number.split(".")
    # display and compute numeric expansion
    print("\nExpansion in power series: \n\t",end="")

    # integer part
    integer_part = 0
    max_exponent = len(split_number[0]) - 1
    for i, d in enumerate(split_number[0]):
        integer_part += int(d) * (11**(max_exponent-i))

        if i < max_exponent:
            print("{0}*11^{1}".format( d, max_exponent-i ),end=" + ")
        else:
            print("{0}*11^{1}".format( d, max_exponent-i ),end="")

    # decimal part  
    decimal_part = 0
    if len(split_number) > 1:
        max_exponent = len(split_number[1]) - 1

        print(" + ",end="")
        for i, d in enumerate(split_number[1]):
            decimal_part += int(d) * (11**( -(i+1) ))

            print("{0}*11^-{1}".format(d,i+1),
                                end = " + " if i < max_exponent else "\n")

    return integer_part + decimal_part

def main():
    print("\n"*3)
    print("="*50)
    print("From base 11 to base 10 numeric system".center(50))
    print("="*50)
    print("\n")

    base11 = input("input the number in base 11: ")
    print("you enter: ", base11)

    if is_base11_number( base11 ):
        value_base10 = base11_to_base10( base11 )
        print("\nnumber in base 11 ", base11, " in base 10 is: ", value_base10)
    else:
        print(base11, """ is not a number in base 11!!!
    I can't help you ...
    *note: base 11 digits are only: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 """)

    print("\n"*2)

if __name__ ==  "__main__":
    main()
