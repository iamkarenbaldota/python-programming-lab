from easygui import *
import sys

while 1:
    msgbox("E-mall!")

    msg ="what do you wish to buy??"
    title = "Domains"
    choices = ["Electronics", "Clothing", "Furniture"]
    choice = choicebox(msg, title, choices)
    
    if choice=='Electronics':
     msg1="choose desired Category"
     title1="Electronics"
     choices1=["Computers","Mobiles","Home Appliences","Accesories"]
     choice1= choicebox(msg1, title1, choices1)
     if choice1=='Computers':
      msg11="choose your product"
      title11="Computers"
      choices11=["Lenovo - $1000","HP - $1250","Apple - $1750"]
      choice11= choicebox(msg11, title11, choices11) 
     elif choice1=='Mobiles':
      msg11="choose your product"
      title11="Mobiles"
      choices11=["Vivo - $199","Samsung - 699$","Apple - $999"]
      choice11= choicebox(msg11, title11, choices11) 
     elif choice1=='Home Appliences':
      msg11="choose your product"
      title11="Home Appliences"
      choices11=["Stove - $99","Mixer - 80$","Oven - $130"]
      choice11= choicebox(msg11, title11, choices11) 
     elif choice1=='Accessories':
      msg11="choose your product"
      title11="Accessories"
      choices11=["Auc Cable - $19","Samsung watch - 299$","JBL speaker - $99"]
      choice11= choicebox(msg11, title11, choices11)   
    elif choice=='Clothing':
     msg3="choose desired Category"
     title3="Clothing"
     choices3=["Topwear","Bottomwear","Footwear"]
     choice3= choicebox(msg3, title3, choices3)
     if choice3=='Topwear':
      msg13="Choose your product"
      title13="Topwear"
      choices13=["Shirt - $30","Sweater - $60","Jacket - $80"]
      choice13=(msg13, title13, choices13)
    elif choice=='Furniture':
     msg4="choose desired Category"
     title4="Furniture"
     choices4=["Beds","Dinning Tables","Wardrobes","Lamps","Chairs","Sofa Sets"]
     choice4= choicebox(msg4, title4, choices4)
    
     if choices1=='Computer':
       msg11="choose your product"
       title11="Computers"
       choices11=["Lenovo - $100","HP - $200","Apple - $400"]
       choice11= choicebox(msg11, title11, choices11) 
