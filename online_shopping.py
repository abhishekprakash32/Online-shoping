# Using if else,elif and While loop
a = ("  Welcome to Amazon  ")
print(a.center(72, '*'))

b = ("  Bag Product  ")
print(b.center(72, '!'))

print("Sr no.\tBag Type\tPrice")
print("1\tSchool Bag\t250")
print("2\tOffice Bag\t500")
print("3\tDoctor bag\t150")
print("4\tLaptop bag\t300")
print("Note:If bill is above Rs.500 then delivery charge will be free\
or less Rs.500 then delivery charge will apply Rs.100")
print("Press 0 or type=Exit for exit.")
print("**************************************************************")

choice = 'yes'
while(choice == 'yes'):
    f = input("Enter  Sr no. or Bag type=")
    h = f.upper()

    if h=='1' or h=='SCHOOL BAG':
        price = 250
        print("Your Bag type is School bag")
        print("price of per bag= 250")
        #print(f"Bag type = {c}")
        e = float(input("Enter quantity="))
        if e<=5:
            print(f"Quantity = {e}")
            r = price * e
            print(f"Your total price is {r}")
            print("You got 5% Discount")
            percentage1 = (r/100) * 5
            print(f"You will Discount amount is {percentage1}")
            after_discount = r - percentage1
            print(f"Price after discount is {after_discount}")
            charge=100
            if after_discount>500:
                print("Your  delivery is free")
            else:
                print("Delivery charge = 100")
                print(f"Your total bill amount is\
    ={after_discount} + {charge} ={after_discount+charge}")
            print("THANK YOU")
            print("VISIT AGAIN")
            choice=input("Do you want to continue for more shoping? yes/no=")    

        elif e>=6 and e<=10:
            print(f"Quantity = {e}")
            r = price * e
            print(f"Your total price is {r}")
            print("You got 10% Discount")
            percentage1 = (r/100) * 10
            print(f"You will Discount amount is {percentage1}")
            after_discount = r - percentage1
            print(f"Price after discount is {after_discount}")
            charge=100
            if after_discount>500:
                print("Your  delivery is free")
            else:
                print("Delivery charge = 100")
                print(f"Your total bill amount is\
    ={after_discount} + {charge} ={after_discount+charge}")
            print("THANK YOU") 
            print("VISIT AGAIN")
            choice=input("Do you want to continue for more shoping? yes/no=")

        elif e>=11 and e<=14:
            print(f"Quantity = {e}")
            r = price * e
            print(f"Your total price is {r}")
            print("You got 15% Discount")
            percentage1 = (r/100) * 15
            print(f"You will Discount amount is {percentage1}")
            after_discount = r - percentage1
            print(f"Price after discount is {after_discount}")
            charge=100
            if after_discount>500:
                print("Your  delivery is free")
            else:
                print("Delivery charge = 100")
                print(f"Your total bill amount is\
    ={after_discount} + {charge} ={after_discount+charge}")
            print("THANK YOU") 
            print("VISIT AGAIN")
            choice=input("Do you want to continue for more shoping? yes/no=")

        elif e>=15:
            print(f"Quantity = {e}")
            r = price * e
            print(f"Your total price is {r}")
            print("You got 20% Discount")
            percentage1 = (r/100) * 20
            print(f"You will Discount amount is {percentage1}")
            after_discount = r - percentage1
            print(f"Price after discount is {after_discount}")
            charge=100
            if after_discount>500:
                print("Your  delivery is free")
            else:
                print("Delivery charge = 100")
                print(f"Your total bill amount is\
    ={after_discount} + {charge} ={after_discount+charge}")
            print("THANK YOU") 
            print("VISIT AGAIN")
            choice=input("Do you want to continue for more shoping? yes/no=")



    if h=='2' or h=='OFFICE BAG':
        price = 500
        print("Your Bag type is Office bag")
        print("price of per bag= 500")
        #print(f"Bag type = {c}")
        e = float(input("Enter quantity="))
        if e<=5:
            print(f"Quantity = {e}")
            r = price * e
            print(f"Your total price is {r}")
            print("You got 5% Discount")
            percentage1 = (r/100) * 5
            print(f"You will Discount amount is {percentage1}")
            after_discount = r - percentage1
            print(f"Price after discount is {after_discount}")
            charge=100
            if after_discount>500:
                print("Your  delivery is free")
            else:
                print("Delivery charge = 100")
                print(f"Your total bill amount is\
    ={after_discount} + {charge} ={after_discount+charge}")
            print("THANK YOU")
            print("VISIT AGAIN")
            choice=input("Do you want to continue for more shoping? yes/no=")

        elif e>=6 and e<=10:
            print(f"Quantity = {e}")
            r = price * e
            print(f"Your total price is {r}")
            print("You got 10% Discount")
            percentage1 = (r/100) * 10
            print(f"You will Discount amount is {percentage1}")
            after_discount = r - percentage1
            print(f"Price after discount is {after_discount}")
            charge=100
            if after_discount>500:
                print("Your  delivery is free")
            else:
                print("Delivery charge = 100")
                print(f"Your total bill amount is\
    ={after_discount} + {charge} ={after_discount+charge}")
            print("THANK YOU") 
            print("VISIT AGAIN")
            choice=input("Do you want to continue for more shoping? yes/no=")

        elif e>=11 and e<=14:
            print(f"Quantity = {e}")
            r = price * e
            print(f"Your total price is {r}")
            print("You got 15% Discount")
            percentage1 = (r/100) * 15
            print(f"You will Discount amount is {percentage1}")
            after_discount = r - percentage1
            print(f"Price after discount is {after_discount}")
            charge=100
            if after_discount>500:
                print("Your  delivery is free")
            else:
                print("Delivery charge = 100")
                print(f"Your total bill amount is\
    ={after_discount} + {charge} ={after_discount+charge}")
            print("THANK YOU") 
            print("VISIT AGAIN")
            choice=input("Do you want to continue for more shoping? yes/no=")

        elif e>=15:
            print(f"Quantity = {e}")
            r = price * e
            print(f"Your total price is {r}")
            print("You got 20% Discount")
            percentage1 = (r/100) * 20
            print(f"You will Discount amount is {percentage1}")
            after_discount = r - percentage1
            print(f"Price after discount is {after_discount}")
            charge=100
            if after_discount>500:
                print("Your  delivery is free")
            else:
                print("Delivery charge = 100")
                print(f"Your total bill amount is\
    ={after_discount} + {charge} ={after_discount+charge}")
            print("THANK YOU") 
            print("VISIT AGAIN")
            choice=input("Do you want to continue for more shoping? yes/no=")




    if h=='3' or h=='DOCTOR BAG':
        price = 150
        print("Your Bag type is Doctor Bag")
        print("price of per bag= 150")
        #print(f"Bag type = {c}")
        e = float(input("Enter quantity="))
        if e<=5:
            print(f"Quantity = {e}")
            r = price * e
            print(f"Your total price is {r}")
            print("You got 5% Discount")
            percentage1 = (r/100) * 5
            print(f"You will Discount amount is {percentage1}")
            after_discount = r - percentage1
            print(f"Price after discount is {after_discount}")
            charge=100
            if after_discount>500:
                print("Your  delivery is free")
            else:
                print("Delivery charge = 100")
                print(f"Your total bill amount is\
    ={after_discount} + {charge} ={after_discount+charge}")
            print("THANK YOU")
            print("VISIT AGAIN")
            choice=input("Do you want to continue for more shoping? yes/no=")

        elif e>=6 and e<=10:
            print(f"Quantity = {e}")
            r = price * e
            print(f"Your total price is {r}")
            print("You got 10% Discount")
            percentage1 = (r/100) * 10
            print(f"You will Discount amount is {percentage1}")
            after_discount = r - percentage1
            print(f"Price after discount is {after_discount}")
            charge=100
            if after_discount>500:
                print("Your  delivery is free")
            else:
                print("Delivery charge = 100")
                print(f"Your total bill amount is\
    ={after_discount} + {charge} ={after_discount+charge}")
            print("THANK YOU") 
            print("VISIT AGAIN")
            choice=input("Do you want to continue for more shoping? yes/no=")

        elif e>=11 and e<=14:
            print(f"Quantity = {e}")
            r = price * e
            print(f"Your total price is {r}")
            print("You got 15% Discount")
            percentage1 = (r/100) * 15
            print(f"You will Discount amount is {percentage1}")
            after_discount = r - percentage1
            print(f"Price after discount is {after_discount}")
            charge=100
            if after_discount>500:
                print("Your  delivery is free")
            else:
                print("Delivery charge = 100")
                print(f"Your total bill amount is\
    ={after_discount} + {charge} ={after_discount+charge}")
            print("THANK YOU") 
            print("VISIT AGAIN")
            choice=input("Do you want to continue for more shoping? yes/no=")
            
        elif e>=15:
            print(f"Quantity = {e}")
            r = price * e
            print(f"Your total price is {r}")
            print("You got 20% Discount")
            percentage1 = (r/100) * 20
            print(f"You will Discount amount is {percentage1}")
            after_discount = r - percentage1
            print(f"Price after discount is {after_discount}")
            charge=100
            if after_discount>500:
                print("Your  delivery is free")
            else:
                print("Delivery charge = 100")
                print(f"Your total bill amount is\
    ={after_discount} + {charge} ={after_discount+charge}")
            print("THANK YOU") 
            print("VISIT AGAIN")
            choice=input("Do you want to continue for more shoping? yes/no=")




    if h=='4' or h=='LAPTOP BAG':
        price = 300
        print("Your Bag type is Laptop Bag")
        print("price of per bag= 300")
        #print(f"Bag type = {c}")
        e = float(input("Enter quantity="))
        if e<=5:
            print(f"Quantity = {e}")
            r = price * e
            print(f"Your total price is {r}")
            print("You got 5% Discount")
            percentage1 = (r/100) * 5
            print(f"You will Discount amount is {percentage1}")
            after_discount = r - percentage1
            print(f"Price after discount is {after_discount}")
            charge=100
            if after_discount>500:
                print("Your  delivery is free")
            else:
                print("Delivery charge = 100")
                print(f"Your total bill amount is\
    ={after_discount} + {charge} ={after_discount+charge}")
            print("THANK YOU")
            print("VISIT AGAIN")
            choice=input("Do you want to continue for more shoping? yes/no=")

        elif e>=6 and e<=10:
            print(f"Quantity = {e}")
            r = price * e
            print(f"Your total price is {r}")
            print("You got 10% Discount")
            percentage1 = (r/100) * 10
            print(f"You will Discount amount is {percentage1}")
            after_discount = r - percentage1
            print(f"Price after discount is {after_discount}")
            charge=100
            if after_discount>500:
                print("Your  delivery is free")
            else:
                print("Delivery charge = 100")
                print(f"Your total bill amount is\
    ={after_discount} + {charge} ={after_discount+charge}")
            print("THANK YOU") 
            print("VISIT AGAIN")
            choice=input("Do you want to continue for more shoping? yes/no=")

        elif e>=11 and e<=14:
            print(f"Quantity = {e}")
            r = price * e
            print(f"Your total price is {r}")
            print("You got 15% Discount")
            percentage1 = (r/100) * 15
            print(f"You will Discount amount is {percentage1}")
            after_discount = r - percentage1
            print(f"Price after discount is {after_discount}")
            charge=100
            if after_discount>500:
                print("Your  delivery is free")
            else:
                print("Delivery charge = 100")
                print(f"Your total bill amount is\
    ={after_discount} + {charge} ={after_discount+charge}")
            print("THANK YOU") 
            print("VISIT AGAIN")
            choice=input("Do you want to continue for more shoping? yes/no=")

        elif e>=15:
            print(f"Quantity = {e}")
            r = price * e
            print(f"Your total price is {r}")
            print("You got 20% Discount")
            percentage1 = (r/100) * 20
            print(f"You will Discount amount is {percentage1}")
            after_discount = r - percentage1
            print(f"Price after discount is {after_discount}")
            charge=100
            if after_discount>500:
                print("Your  delivery is free")
            else:
                print("Delivery charge = 100")
                print(f"Your total bill amount is\
    ={after_discount} + {charge} ={after_discount+charge}")
            print("THANK YOU") 
            print("VISIT AGAIN")
            choice=input("Do you want to continue for more shoping? yes/no=")
