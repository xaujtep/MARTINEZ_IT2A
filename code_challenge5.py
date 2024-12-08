pera = eval(input("Enter amount to deposit ---> "))

libo = pera // 1000
libo_sukli = pera - (libo * 1000)

five_h = libo_sukli // 500
five_sukli = libo_sukli - (five_h * 100)

two_h = five_sukli // 200
two_sukli = five_sukli - (two_h * 50)

one_h = two_sukli // 100
one_sukli = two_sukli - (one_h * 25)

print(libo , " - 1000")
print("current sukli ay ", libo_sukli)
print(five_h , " - 500")
print("current sukli ay ", five_sukli)
print(two_h , " - 200")
print("current sukli ay ", two_sukli)
print(one_h , " - 100")
print("current sukli ay ", one_sukli)