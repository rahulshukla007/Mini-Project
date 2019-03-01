#kirnana store

sum = 0
no = 1
print('for quit press --> q')
f = open("receipt.txt", "w")
f.write("--------->Hari kirana wala<----------\n\n")
f.write("Order Summary--\n")
while True:
    num = input("Please add a amount: \n ")
    if num != "q":
        f = open("receipt.txt", "a")
        f.write(f'{no} --  {num} RS \n')
        sum = sum + float(num)
        print(f"the grand total so far {sum}")
        no = no + 1
    else:
        print(f"Your grand total is {sum}\n" )
        f.write("--------------------------\n")
        f.write(f'Total {sum} RS \n\n')
        f.write("Thank you for shopping with us")
        f.close()
        break














