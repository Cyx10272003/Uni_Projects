#Christine Leong Jia Yean #Chua Yu Xiang
#TP063364 #TP063598

from datetime import datetime

print("-------------------------------------------")
print("ASIAN EVENT MANAGEMENT SERVICES")
print("-------------------------------------------")

def RegisterasAdmin(): #To register the Admin.
    Adminlist = []
    while True:
        Recordlist = []
        Name = input("Enter Name:")
        Age = int(input("Enter Age:"))
        Phone = input("Enter Phone Number:")
        Email = input("Enter Email:")
        IDnum = input("Enter ID number:")
        separator = ','
        while True:
            Pass = int(input("Enter Password:"))
            Confirm = int(input("Confirm Password:"))
            if Pass == Confirm:
                print("You are registered!")
                break
            else:
                print("Password does not match with original")
                Confirm = int(input("Confirm Password:"))
                break
        Recordlist.append(f"{Name}")
        Recordlist.append(f"{Age}")
        Recordlist.append(f"{Phone}")
        Recordlist.append(f"{Email}")
        Recordlist.append(f"{IDnum}")
        Recordlist.append(f"{Pass}")
        Adminlist.append(separator.join(Recordlist))

        break

    return Adminlist

def AdminStorage(admindata): #To store the admin data.
    fhandler = open("Admin.txt", "a")
    for record in admindata:
        for value in record:
            fhandler.write(value)
        fhandler.write("\n")

    fhandler.close()

def RegisterasCustomer(): #to register the customer.
    Customerlist = []
    while True:
        Recordlist = []
        Name = input("Enter Name:")
        Age = int(input("Enter Age:"))
        Phone = input("Enter Phone Number:")
        Email = input("Enter Email:")
        IDnum = input("Enter ID number:")
        separator = ','
        while True:
            Pass = int(input("Enter Password:"))
            Confirm = int(input("Confirm Password:"))
            if Pass == Confirm:
                print("You are registered!")
                break
            else:
                print("Password does not match with original")
                Confirm = int(input("Confirm Password:"))
                break
        Recordlist.append(f"{Name}")
        Recordlist.append(f"{Age}")
        Recordlist.append(f"{Phone}")
        Recordlist.append(f"{Email}")
        Recordlist.append(f"{IDnum}")
        Recordlist.append(f"{Pass}")
        Customerlist.append(separator.join(Recordlist))
        break
    return Customerlist

def CustomerStorage(customerdata): #Storing customer data.
    fhandler = open("Customer.txt", "a")
    for record in customerdata:
        for value in record:
            fhandler.write(value)
        fhandler.write("\n")
    fhandler.close()

def Registration(): #General registration page that directs to other registration.
    print("---------------------------------")
    print(" 1. Register as Admin")
    print(" 2. Register as Customer")
    print(" 3. Back")
    print("---------------------------------")
    option = int(input("Choose an option :"))
    if option == 1:
        Admindata = RegisterasAdmin()
        AdminStorage(Admindata)
        Response = input("Would you like to log in? [Y/N]:")
        if Response == "Y" or Response == "y":
            LoginSystem()
            return
        else:
            print("Thank you for registering, we hope to see you soon!")
            return
    elif option == 2:
        Customerdata = RegisterasCustomer()
        CustomerStorage(Customerdata)
        Response = input("Would you like to log in? [Y/N]:")
        if Response == "Y" or Response == "y":
            LoginSystem()
            return
        else:
            print("Thank you for registering, we hope to see you soon!")
            return
    elif option == 3:
        Menu()
    else:
        print("Invalid input.")

def loginasadmin(): #Admin login 
    IDnum = input("Enter ID number:")
    Password = input("Enter Password:")
    fhand = open("Admin.txt",'r')
    for x in fhand:
        f = x.strip().split(",")
        if IDnum == f[4] and Password == f[5]:
            adminsection()
            return
        else:
            print("Password or Email is invalid please try again")
            
def adminsection():      # from login directed to this section, display the functions that admin can use
    print("WELCOME TO ADMIN SECTION")
    print("----------------------------------------------------")
    print("1. Modify event")
    print("2. Display records of each category")
    print("3. Display records of events in each category")
    print("4. Display records of customer registration")
    print("5. Display records of customer payment")
    print("6. Search specific records of customer registration")
    print("7. Search specific records of customer payment")
    print("8. Search for specific event in category")
    print("9. Exit.")
    print("-----------------------------------------------------")
    while True:
            choice = int(input("Choose an option:"))
            if choice == 1:
                addeventincategory()  
            elif choice == 2:
                displayallcategory()
            elif choice == 3:
                displayallevent()
            elif choice == 4:
                displaycustomer()
            elif choice == 5:
                displaycustomerpayment()
            elif choice == 6:
                searchforcustomer()
            elif choice == 7:
                searchforpayment()
            elif choice == 8:
                searchforspecificevent()
            ask = input("Do you still want to access to admin section? [Y/N]:")
            if ask == "N" or ask == "n":
                question = input("Do you want to log out?:")
                if question == "Y" or question == "y":
                    return
                else:
                    adminsection()
            else:
                adminsection()

def displayallcategory(): #shows the category
    file = open("category.txt", "w")
    file.write("----------------------------------")
    file.write("\n")
    c_list = ['1. Sporting', '2. Entertainment arts & culture', '3. Festivals', '4. Family', '5. Promotional']
    for i in c_list:
        file.write(i)
        file.write("\n")
    file.write("---------------------------------")
    file = open("category.txt", 'r')
    x = file.read()
    print(x)

def displaycustomer(): #shows customer
    file = open("Customer.txt", 'r')
    x = file.read()
    print(x)

def displaycustomerpayment(): #shows customer payments
    file = open("Payment.txt", 'r')
    x = file.read()
    print(x)

def searchforpayment(): #search payment with IDnum and Eventcode
    IDnum = input("Enter customer ID number:")
    Eventcode = input("Enter Event code:")
    fhand = open("Payment.txt", 'r')
    for x in fhand:
        f = x.strip().split(",")
        if IDnum == f[2] and Eventcode == f[1]:
            print(x)
        elif IDnum != f[2] or Eventcode != f[1]:
            print("")
        else:
            print("payment not found.")

def searchforcustomer(): #search customer with IDnum
    IDnum = input("Enter customer ID number:")
    fhand = open("Customer.txt", 'r')
    for x in fhand:
        f = x.strip().split(",")
        if IDnum == f[5]:
            print(x)
        elif IDnum != f[5]:
            print("")
        else:
            print("Customer not found")

def addeventincategory(): #admin usage to add event choices
    print("---------------------------------")
    print("1. Sporting")
    print("2. Entertainment arts and culture")
    print("3. Festivals ")
    print("4. Family")
    print("5. Promotional")
    print("---------------------------------")
    while True:
        choose = int(input("Choose option:"))
        if choose == 1: 
            f = open("Sporting.txt", "a")
            Event = input("Enter event name: ")
            Event_number = input("Enter event code: ")
            Event_capacity = input("Enter event capacity: ")
            Event_desc = input("Enter Short description (2-3lines): ")
            Event_cost = input("Enter event cost: ")
            f.write("Event: " + Event + ", ")
            f.write("Event code: " + Event_number + ", " + "Event capacity: " + Event_capacity + ", ")
            f.write("About Event: " + Event_desc + ", " + "Event cost: " + Event_cost + ", ")
            f.write("Down Payment for Sports: 50")
            ask = input("Do you want to add another event? [Y/N]:") 
            if ask == "N" or ask == "n": 
                break
        elif choose == 2:
            f = open("Entertainment arts and culture.txt", 'a')
            Event = input("Enter event name: ")
            Event_number = input("Enter event code: ")
            Event_capacity = input("Enter event capacity: ")
            Event_desc = input("Enter Short description (2-3lines): ")
            Event_cost = input("Enter event cost: ")
            f.write("Event: " + Event + ", ")
            f.write("Event code: " + Event_number + ", " + "Event capacity: " + Event_capacity + ", ")
            f.write("About Event: " + Event_desc + ", " + "Event cost: " + Event_cost + ", ")
            f.write("Down Payment for EAC: 50")
            ask = input("Do you want to add another event? [Y/N]:")
            if ask == "N":
                break
        elif choose == 3:
            f = open("Festivals.txt", 'a')
            Event = input("Enter event name: ")
            Event_number = input("Enter event code: ")
            Event_capacity = input("Enter event capacity: ")
            Event_desc = input("Enter Short description (2-3lines): ")
            Event_cost = input("Enter event cost: ")
            f.write("Event: " + Event + ", ")
            f.write("Event code: " + Event_number + ", " + "Event capacity: " + Event_capacity + ", ")
            f.write("About Event: " + Event_desc + ", " + "Event cost: " + Event_cost + ", ")
            f.write("Down Payment for Festivals: 50")
            ask = input("Do you want to add another event? [Y/N]:")
            if ask == "N":
                break
        elif choose == 4:
            f = open("Family.txt", 'a')
            Event = input("Enter event name: ")
            Event_number = input("Enter event code: ")
            Event_capacity = input("Enter event capacity: ")
            Event_desc = input("Enter Short description (2-3lines): ")
            Event_cost = input("Enter event cost: ")
            f.write("Event: " + Event + "\n")
            f.write("Event code: " + Event_number + ", " + "Event capacity: " + Event_capacity + ", ")
            f.write("About Event: " + Event_desc + ", " + "Event cost: " + Event_cost + ", ")
            f.write("Down Payment for Family: 30")
            ask = input("Do you want to add another event? [Y/N]:")
            if ask == "N":
                break
        elif choose == 5:
            f = open("Promotional.txt", 'a')
            Event = input("Enter event name: ")
            Event_number = input("Enter event code: ")
            Event_capacity = input("Enter event capacity: ")
            Event_desc = input("Enter Short description (2-3lines): ")
            Event_cost = input("Enter event cost: ")
            f.write("Event: " + Event + ", ")
            f.write("Event code: " + Event_number + ", " + "Event capacity: " + Event_capacity + ", ")
            f.write("About Event: " + Event_desc + ", " + "Event cost: " + Event_cost + ", ")
            f.write("Down Payment for Promotional: 50")
            ask = input("Do you want to add another event? [Y/N]:")
            if ask == "N":
                break

def displayallevent(): #Shows event, the ones added by admin, won't run if theres no data
    s = open("Sporting.txt", "r")
    e = open("Entertainment arts and culture.txt", "r")
    f = open("Festivals.txt", "r")
    fam = open("Family.txt", "r")
    P = open("Promotional.txt" , "r")
    sporting = s.read()
    entertainment = e.read()
    festivals = f.read()
    family = fam.read()
    promotional = P.read()
    print("------------------------------")
    print("1. SPORTING")
    print(sporting)
    print("------------------------------")
    print("------------------------------")
    print("2. ENTERTAINMENT ARTS AND CULTURE")
    print(entertainment)
    print("------------------------------")
    print("------------------------------")
    print("3. FESTIVALS")
    print(festivals)
    print("------------------------------")
    print("------------------------------")
    print("4. FAMILY")
    print(family)
    print("------------------------------")
    print("------------------------------")
    print("5. PROMOTIONAL")
    print(promotional)
    print("-------------------------------")

def searchforspecificevent(): #for admin use to view the events
    print("---------------------------------")
    print("1. Sporting")
    print("2. Entertainment arts and culture")
    print("3. Festivals ")
    print("4. Family")
    print("5. Promotional")
    print("---------------------------------")
    while True:
        choose = int(input("Choose option:"))
        if choose == 1:
            s = open("Sporting.txt", "r")
            sporting = s.read()
            print(sporting)
        elif choose == 2:
            e = open("Entertainment arts and culture.txt", "r")
            entertainment = e.read()
            print(entertainment)
        elif choose == 3:
            f = open("Festivals.txt", "r")
            festivals = f.read()
            print(festivals)
        elif choose == 4:
            fam = open("Family.txt", "r")
            family = fam.read()
            print(family)
        elif choose == 5:
            P = open("Promotional.txt", "r")
            promotional = P.read()
            print(promotional)
        ask = input("Do you still want to continue? [Y/N]:")
        if ask == "N":
            break

def searchforeventcustomer(): #for custtomer use to view events
    print("---------------------------------")
    print("1. Sporting")
    print("2. Entertainment arts and culture")
    print("3. Festivals ")
    print("4. Family")
    print("5. Promotional")
    print("---------------------------------")
    while True:
        choose = int(input("Choose option:"))
        if choose == 1:
            s = open("Sporting.txt", "r")
            sporting = s.read()
            print(sporting)
        elif choose == 2:
            e = open("Entertainment arts and culture.txt", "r")
            entertainment = e.read()
            print(entertainment)
        elif choose == 3:
            f = open("Festivals.txt", "r")
            festivals = f.read()
            print(festivals)
        elif choose == 4:
            fam = open("Family.txt", "r")
            family = fam.read()
            print(family)
        elif choose == 5:
            P = open("Promotional.txt", "r")
            promotional = P.read()
            print(promotional)
        ask = input("Do you still want to continue? [Y/N]:")
        if ask == "N":
            question = input("Would you like to purchase an Event management service? [Y/N]")
            if question == "Y" or question == "y":
                displayallevent()
                purchasingevents()
                return
            break

def LoginSystem():  #login, add back to menu
    print("---------------------")
    print("LOGIN ACCESS SYSTEM")
    print("---------------------")
    print("1. Login as admin")
    print("2. Login as customer")
    print("3. Back")
    print("---------------------")
    choice = int(input("Choose option:"))
    if choice == 1:
        loginasadmin()
    elif choice == 2:
        loginascustomer()
    elif choice == 3:
        Menu()
    else:
        print("Invalid input")

def NonRegisteredCustomer(): #Guest, limited access
    print("----------------------------------------------------")
    print("WELCOME DEAREST CUSTOMER")
    print("----------------------------------------------------")
    print("1. Categories of Events")
    print("2. Register to see more!")
    print("3. Back to Menu")
    print("-----------------------------------------------------")
    while True:
            choice = int(input("Choose an option:"))
            if choice == 1:
                displayallcategory()
                ask = input("Would you like to see more?[Y/N]:")
                if ask == "Y" or ask == "y":
                    print("Register to see more!")
                    Registration()
                    return
                else:
                    NonRegisteredCustomer()
            elif choice == 2:
                ask = input("Would you like to register? [Y/N]:")
                if ask == "Y":
                    Registration()
                    return             
                elif ask == "N":
                    print("Register to see more!")
                    NonRegisteredCustomer()
                else:
                   NonRegisteredCustomer() 
            elif choice == 3:
                Menu()
                return
            else: 
                print("Invalid input")

def loginascustomer(): #customer login, validate by idnum and password
    IDnum = input("Enter ID number:")
    Password = input("Enter Password:")
    fhand = open("Customer.txt",'r')
    for x in fhand:
        f = x.strip().split(",")
        if IDnum == f[4] and Password == f[5]:
            RegisteredCustomer()
            return
        else:
            print("Password or Email is invalid please try again")
            
def RegisteredCustomer():      #Login customer is directed here, shows the functionalites of a customer
    print("----------------------------------------------------")
    print("WELCOME DEAREST CUSTOMER")
    print("----------------------------------------------------")
    print("1. Categories of Events")
    print("2. All Events")
    print("3. Search for Events")
    print("4. Shopping cart")
    print("5. Payment")
    print("6. Exit")
    print("-----------------------------------------------------")
    while True:
            choice = int(input("Choose an option:"))
            if choice == 1:
                CategoriesForCustomer()
            elif choice == 2:
                Eventsforcustomer()
                return
            elif choice == 3:
                searchforeventcustomer()
                return
            elif choice == 4:
                Shoppingcart()
                return
            elif choice == 5:
                paymentforcustomer()
                return
            elif choice == 6:    
                ask = input("Would you like to log out? [Y/N]:")
                if ask == "Y":
                    print("Goodbye!")
                    return
                break

def CategoriesForCustomer(): #show customer categories and the option to buy
    displayallcategory()
    ask = input("Would you like to see the events? [Y/N]: ")
    if ask == "Y" or ask == "y":
        Eventsforcustomer()
        return
    elif ask == "N" or ask == "n":
        question = input("Would you like to return to customer selections? [Y/N]: ")
        if question == "Y" or question == "y":
            RegisteredCustomer()
            return
        else:
            CategoriesForCustomer()
            return
    else:
        print("Invalid input.")

def Eventsforcustomer(): #Display events and for customer to select 
    displayallevent()
    while True:
         option = input("Would you like to purchase an event management service? [Y/N]:")
         if option == "Y":
            purchasingevents()
            break
         else: 
             RegisteredCustomer() 
             break

price = []

def purchasingevents(): #purchases of customer
        username = input("Enter your ID:")
        selection = int(input("Select your event:"))
        now = datetime.now()
        nowstr = now.strftime("%d-%m-%Y %X") 
        if selection == 1:
            SportsEventcode = str(input("Select event code:"))
            fhand = open("Sporting.txt", 'r')
            for x in fhand:
                f = x.strip().split(",")
                if SportsEventcode == f[1]:
                    print("Added to cart.")
                    price.append (50)
                    fhandler = open ("ShoppingCart.txt", "a")
                    fhandler.write ("Event: Sporting," )
                    fhandler.write(SportsEventcode) 
                    fhandler.write(", Customer ID: ")
                    fhandler.write(username)
                    fhandler.write(", Time Ordered: ")
                    fhandler.write(nowstr)
                    fhandler.write("\n")
                    fhandler.close()
                    Buymoreevents()
                    break
                else:
                    print("Event code not found.")
                    Eventcode()
                    break 

        elif selection == 2:                  #Part 2
            EACEventcode = input("Select event code:")           
            fhand = open("Entertainment arts and culture.txt", 'r')
            for x in fhand:
                f = x.strip().split(",")
                if EACEventcode == f[1]:
                    print("Added to cart.")
                    price.append(50)
                    fhandler = open ("ShoppingCart.txt", "a")
                    fhandler.write ("Event: Entertainment arts and culture, ")
                    fhandler.write(EACEventcode) 
                    fhandler.write(", Customer ID: ")
                    fhandler.write(username)
                    fhandler.write(", Time Ordered: ")
                    fhandler.write(nowstr)
                    fhandler.write("\n")
                    fhandler.close()
                    Buymoreevents()
                    break
                else:
                    print("Event code not found.")
                    Eventcode()
                    break

        elif selection == 3:                  #Part 3
            FestiveEventcode = input("Select event code:")
            fhand = open("Festivals.txt", 'r')
            for x in fhand:
                f = x.strip().split(",")
                if FestiveEventcode == f[1]:
                    print("Added to cart.")
                    price.append(50)
                    fhandler = open ("ShoppingCart.txt", "a")
                    fhandler.write ("Event: Festival, ")
                    fhandler.write(FestiveEventcode) 
                    fhandler.write(", Customer ID: ")
                    fhandler.write(username)
                    fhandler.write(", Time Ordered: ")
                    fhandler.write(nowstr)
                    fhandler.write("\n")
                    fhandler.close()
                    Buymoreevents()
                    break
                else:
                    print("Event code not found.")
                    Eventcode()
                    break

        elif selection == 4:                  #Part 4
            FamilyEventcode = input("Select event code:")
            fhand = open("Family.txt", 'r')
            for x in fhand:
                f = x.strip().split(",")
                if FamilyEventcode == f[1]:
                    print("Added to cart.")
                    price.append(30)
                    fhandler = open ("ShoppingCart.txt", "a")
                    fhandler.write ("Event: Family, ")
                    fhandler.write(FamilyEventcode) 
                    fhandler.write(", Customer ID: ")
                    fhandler.write(username)
                    fhandler.write(", Time Ordered: ")
                    fhandler.write(nowstr)
                    fhandler.write("\n")
                    fhandler.close()
                    Buymoreevents()
                    break
                else:
                    print("Event code not found.")
                    Eventcode()
                    break

        elif selection == 5:                  #Part 5
            PromotionalEventcode = input("Select event code:")
            fhand = open("Promotional.txt", 'r')
            for x in fhand:
                f = x.strip().split(",")
                if PromotionalEventcode == f[1]:
                    print("Added to cart.")
                    price.append(50)
                    fhandler = open ("ShoppingCart.txt", "a")
                    fhandler.write ("Event: Promotional, ")
                    fhandler.write(PromotionalEventcode) 
                    fhandler.write(", Customer ID: ")
                    fhandler.write(username)
                    fhandler.write(", Time Ordered: ")
                    fhandler.write(nowstr)
                    fhandler.write("\n")
                    fhandler.close()
                    Buymoreevents()
                    break
                else:
                    print("Event code not found.")
                    Eventcode()
                    break
        else:
            print("Event not found. Try Again")
            
def Eventcode(): #to direct back to purchases
    EC = input("Would you like to try again? [Y/N]:")
    if EC == "Y":
        purchasingevents()
        return
    elif EC =="N":
        Eventsforcustomer()
        return
    else: 
        print("Invalid input.")
        Eventcode()
        return

def Buymoreevents(): #to direct back to purchases
    BME = input("Would you like to add more event? [Y/N]")
    if BME == "Y":
        purchasingevents()
        return
    elif BME == "N":
        Eventsforcustomer()
        return
    else: 
        print("Invalid input.")
        Buymoreevents()
        return
    
def Shoppingcart(): #shows purchases of customer
    print("Cart")
    f = open("ShoppingCart.txt","r")
    x = f.read()
    print(x)
    while True:
        ask = input("Enter 'B' to back: ")
        if ask == "B" or ask =="b":
            RegisteredCustomer()
            return
        else:
            print("Invalid input.")

def calculation(): #increment of downpayment when buying multiple events
    total = 0
    for ele in range(0, len(price)):
        total = total + price[ele]
    print("The total payment is: ", total)
    

def paymentforcustomer(): #payment check and direct to another platform for payment
    f = open("ShoppingCart.txt","r")
    x = f.read()
    print(x)
    fhand = open("payment.txt", 'a')
    fhand.write(x)
    fhand.close

    calculation()

    print("Payment")
    proceeds = input("Complete the payment? [Y/N]: ")
    if proceeds == "Y":
        f = open("ShoppingCart.txt","w")
        f.close()
        price.clear()
        print("Payment proceeded.")
        RegisteredCustomer()
        return
    else:
        print("Please complete your payment!")
        RegisteredCustomer()
        return

def Menu(): #The starting page of the program
    print("------------------")
    print("MENU PAGE")
    print("------------------")
    print("1. Registration")
    print("2. Login")
    print("3. View as guest")
    print("------------------")
    while True:
         Option = int(input("Choose an option:"))
         if Option == 1:
            Registration()
            return
         elif Option == 2:
            LoginSystem()
            return
         elif Option == 3:
            NonRegisteredCustomer()
            return
         else:
            print("Invalid input")

Menu()
