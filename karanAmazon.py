from easygui import *
import sys
list=[]
sum=0

while 1:
    msgbox("Welcome to NEW E Bazaar")

    msg ="In which category you want to buy items?"
    title = "NEW E Bazaar"
    choices=["Smartphones", "Clothing", "Stationary", "Grocery"]
    choice = choicebox(msg, title, choices)
     
    msgbox("You chose: " + str(choice), "Confirm your choice")

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if choice=="Smartphones":
        msgbox("Welcome to Smartphone bazaar")
        msg="Which Smartphone?"
    	title= "NEW E Smartphone Bazaar"
    	choices= ["SAMSUNG GALAXY S9 price=50000", "ASUS ZENFONE 5Z price=38000", "ONEPLUS 6T price=42000", "REDMI 5A price=4999"]
    	choice= choicebox(msg, title, choices)

        msgbox("You chose: " + str(choice), "Confirm your choice")

        msg = "Is it your final choice(Press continue to continue shopping)"
        title = "Please Confirm"
        msgbox("Thank you for buying at NEW E Bazaar")
    elif choice=="Clothing":
        msgbox("Welcome to Clothes bazaar")
        msg="What type of clothes?"
    	title= "NEW E Clothes Bazaar"
    	choices= ["L size Tshirt UNISEX=Rs 500","M size Tshirt for women=Rs 500","Levis Joggers=Rs1000","FCB Shorts=Rs1000"]
    	choice= choicebox(msg, title, choices)

        msgbox("You chose: " + str(choice), "Confirm your choice")

        msg = "Is it your final choice(Press continue to continue shopping)"
        title = "Please Confirm"
        msgbox("Thank you for buying at NEW E Bazaar")
    elif choice=="Grocery":
        msgbox("Welcome to Grocery bazaar")
        msg="Which Item?"
    	title= "NEW E Grocery Bazaar"
    	choices= ["10kg basmati rice price=750", "Biryani rice 5kg=550"]
    	choice= choicebox(msg, title, choices)

        msgbox("You chose: " + str(choice), "Confirm your choice")

        msg = "Is it your final choice(Press continue to continue shopping)"
        title = "Please Confirm"
        msgbox("Thank you for buying at NEW E Bazaar")
    elif choice=="Stationary":
        msgbox("Welcome to Stationary bazaar")
        msg="Choose your item?"
    	title="NEW E Smartphone Bazaar"
    	choices= ["MONT BLANC---- price=Rs1000 ", "5 RULERS----- price=Rs50"]
    	choice= choicebox(msg, title, choices)

        msgbox("You chose: " + str(choice), "Confirm your choice")

        msg = "Is it your final choice(Press continue to continue shopping)"
        title = "Please Confirm"
        msgbox("Thank you for buying at NEW E Bazaar")

    if ccbox(msg, title):    #show a Continue/Cancel dialog
        list.append(choice)  
        pass   #user chose continue 
    else:
         list.append(choice)
         textbox(msg="FINAL BILL",title="BILL",text=list)
sys.exit(0)
