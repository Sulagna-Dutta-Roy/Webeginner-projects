a=int(input("Enter the number of which the multiplication table you want: "))
b=int(input("Enter the range of the multiplication(e.g 10): "))

with open(f'Multiplication_Table_of_{a}.txt','w') as f:
    for i in range(1,b+1):
        f.write(f'{a} X {i} = {a*i}\n')
    f.close