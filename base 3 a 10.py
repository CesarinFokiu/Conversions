def is_marcian_number( marcian ):
    split_marcian = marcian.split(".")

    # Validation, is a marcian number???
    result = True
    for part in split_marcian:
        for digit in part:
            if not (0<=int(digit)<3):  # remember type of digit is str
                result = False
                break
        if not result:
            break

        return result

def marcian_to_base10( marcian_number ):
    split_number = marcian_number.split(".")
    # display and compute numeric expansion
    print("\nExpansion in power series: \n\t",end="")

    # integer part
    integer_part = 0
    max_exponent = len(split_number[0]) - 1
    for i, d in enumerate(split_number[0]):
        integer_part += int(d) * (3**(max_exponent-i))

        if i < max_exponent:
            print("{0}*3^{1}".format( d, max_exponent-i ),end=" + ")
        else:
            print("{0}*3^{1}".format( d, max_exponent-i ),end="")

    # decimal part  
    decimal_part = 0
    if len(split_number) > 1:
        max_exponent = len(split_number[1]) - 1

        print(" + ",end="")
        for i, d in enumerate(split_number[1]):
            decimal_part += int(d) * (3**( -(i+1) ))

            print("{0}*3^-{1}".format(d,i+1),
                                end = " + " if i < max_exponent else "\n")

    return integer_part + decimal_part

def main():
    print("\n"*3)
    print("="*50)
    print("From marcian to christian numeric system".center(50))
    print("="*50)
    print("\n")

    marcian = input("input the marcian number: ")
    print("you enter: ", marcian)

    if is_marcian_number( marcian ):
        value_base10 = marcian_to_base10( marcian )
        print("\nmarcian number ", marcian, " in christian is: ", value_base10)
    else:
        print(marcian, """ is not a marcian number!!!
    I can't help you ...
    *note: marcian digits are only: 0,1,2 """)

    print("\n"*2)

if __name__ ==  "__main__":
    main()
    #by HeribertoCV
