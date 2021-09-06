'''
MR.UJWAL SHARMA
ujwalsharma.pro1@gmail.com
9326303601
ETG-INTERNSHIP  : PYTHON FOR AI/ML
'''

import json             #importing json module in the program
x=1;T={};data={}    #inititalizing  'T' & 'data' dictionary, x variable for the while loop 
while(x==1):
    ch=int(input(" PRESS : \n 1 : CREATE A NEW INVENTORY \n 2. ADD NEW PRODUCTS IN THE INVENTORY \n 3 : WITHDRAW PRODUCTS FROM INVENTORY \n 4 : DISPLAY PRODUCTS IN INVENTORY : \n 5 : DISPLAY SALES MADE \n"))
    #taking int value from user to choose from the 5 different task listed above
    if(ch==1):              #if user entered 1, do this 
        n=int(input(" ENTER TOTAL PRODUCTS TO ENTER : "))   #input to iterate 'for' loop 
        for i in range(n):                                                      
            pid=int(input(" ENTER PRODUCT-ID : "))              #product id-ip from user
            T["NAME"]=input(" ENTER PRODUCT NAME : ")   #product name-ip from user
            T["PRICE"]=float(input(" ENTER PRODUCT'S PRICE  : ")) #product price-ip from user
            T["QUANTITY"]=int(input(" ENTER PRODUCT QUANTITY  : "))#product quant-ip from user
            T["TYPE"]=input(" ENTER TYPE OF PRODUCT : ")#product type-ip from user
            data[pid]={"NAME":T["NAME"],"PRICE":T["PRICE"],"QUANTITY":T["QUANTITY"],"TYPE":T["TYPE"]}
            #assigning 'T'  to 'data', to create a nested dictionary
            print("\n")
        js=json.dumps(data)         #converting 'data' variable which is dictionary to String, since file doesn't take Dictionary
        f=open("INVENTORY-PRODUCTS.json","w")    #opening file for writing 
        f.write(js)                                                                #writing converted string to a File
        f.close()                                                                   #closing the file
        
    elif(ch==2):                     #if user entered 2, do this
        f=open("INVENTORY-PRODUCTS.json","r")       #opening file for reading
        t=f.read()                                                                  #reading the data and initializing it to t var
        f.close()                                        #closing the file
        data=json.loads(t)                              #converts the string to dictionary 
        keyss=data.keys()                              # the list 'keyss' contain all the keys of 'data' dictionary 
        c=0                                                        
        n=int(input(" ENTER TOTAL PRODUCTS TO ENTER : "))       #input to iterate 'for' loop
        for i in range(n):
            pid=int(input(" ENTER PRODUCT-ID : "))          #product id-ip from user
            pidinstr=str(pid)                                                   #converting product id from int to string, to search in 'data' dict
            for j in keyss:                                                         
                if(j == pidinstr) :                                                 #checking weather the user entered product is already in the Inventory or Not 
                    c=c+1                                                                # if it is there make c=1, else keep it c=0 only
            if(c==1):                                                                   # if c=1(product already exists in the Inventory) do this :
                c=0                                                                         # make c=0 else it will disturb the next iteration of for loop(starting from line 30)
                quant=int(input(" Enter Total Quantity : "))        #product quant-ip from user
                print("\n")
                data[pidinstr]["QUANTITY"]=data[pidinstr]["QUANTITY"]+quant     #add the user taken quantity to the existing count of quantity in inventory
            else:                                               #if product is not exists in the Inventory, do this : 
                T["NAME"]=input(" ENTER PRODUCT NAME : ")               
                T["PRICE"]=float(input(" ENTER PRODUCT'S PRICE  : "))
                T["QUANTITY"]=int(input(" ENTER PRODUCT QUANTITY  : "))
                T["TYPE"]=input(" ENTER TYPE OF PRODUCT : ")
                print("\n")
                data[pid]={"NAME":T["NAME"],"PRICE":T["PRICE"],"QUANTITY":T["QUANTITY"],"TYPE":T["TYPE"]}#assigning new values entered by user to 'data' dictionary 
        js=json.dumps(data)                         #converting 'data' variable which is dictionary to String for writing it to file, since file doesn't take Dictionary
        f=open("INVENTORY-PRODUCTS.json","w")     #opening file for writing
        f.write(js)
        f.close()
        
    elif(ch==3):     #if user entered 3, do this
        f=open("INVENTORY-PRODUCTS.json","r")           #opening file for reading the exisitng data 
        t=f.read()
        f.close()
        data=json.loads(t)                #converts the string to dictionary                  
        
        f=open("SALES.json","r")         # Opening Sales.json file
        t=f.read()
        f.close()
        sales=json.loads(t)                     #converts the string to dictionary, as the data from file is in string format and we want to manipulate the dicitonary

        no=int(input(" ENTER TOTAL PRODUCTS YOU WANNA WITHDRAW : "))
        keyss=data.keys();c=0;m=0;am=0;store={}
        for i in range(no):
            pid=int(input(" ENTER PRODUCT-ID : "))
            pstr=str(pid)   #converting product id from int to string, to access data from 'data' dict            
            for j in keyss:  #checking weather the user entered product is already in the Inventory or Not                        
                if(j == pstr) :  
                    c+=1
            if(c==0):  #if entered product-id not present in inventory, BREAK for loop 
                print(" the Product-Id which u entered is not in the Inventory, Please Re-Enter !!!! ")
                break;
            else :   #if entered product-id is present in inventory, do this : 
                quant=int(input(" Enter Total Quantity You WANNA WITHDRAW  : "))    
                print("\n")
                if(data[pstr]["QUANTITY"]<=0):                                  # if the product in the inventory has 0 quantity, do this :
                    print(" OOPS, DESIRED PRODUCT IS NOT PRESENT IN THE INVENTORY !!! ")
                else :                                                  #else do this : 
                    data[pstr]["QUANTITY"]-=quant
                keyss=sales.keys()                              # the list 'keyss' contain all the keys of 'data' dictionary
                d=len(keyss)                                            #calculating the length of keyss var(to know the total existing values in 'Sales' dictionary)
                sales[d+1]={"Product-ID":pid,"Name":data[pstr]["NAME"],"Price":data[pstr]["PRICE"],"Quantity":quant,"Type":data[pstr]["TYPE"]}
                            #storing the user withdrawal record in sales dictionary at (d+1) key, to avoid over-writing of values
                m+=1
                store[m]=sales[d+1]
                am+=(sales[d+1]["Price"])*(sales[d+1]["Quantity"])
        print("******************************************************************************************")
        print(" YOUR ORDERs : \n \t")
        for i in store:
            print("NAME : ",store[i]["Name"],",  PRICE :  ",store[i]["Price"],",  QUANTITY :  ",store[i]["Quantity"], "\n")
        print(" TOTAL AMOUNT : ",am)
        print("******************************************************************************************")
        ji=json.dumps(data)                                 
        f=open("INVENTORY-PRODUCTS.json","w")                                   #opening file for writing
        f.write(ji)                                         
        f.close()

        js=json.dumps(sales)        #converting 'data' variable which is dictionary to String for writing it to file, since file doesn't take Dictionary
        f=open("SALES.json","w")                                #opening file for writing
        f.write(js)                                                                 
        f.close()
        
    elif(ch==4):     #if user entered 4, do this
        fa=open("INVENTORY-PRODUCTS.json","r")              #opening file for reading
        a=fa.read()                                             #reading the data and initializing it to a var
        fa.close()
        ja=json.loads(a)                                        #converts the string to dictionary, as the data from file is in string format and we want to manipulate the dicitonary
        print(ja,"\n")

    elif(ch==5):             #if user entered 5, do this
        f=open("SALES.json","r")                                        #opening file for reading
        k=f.read()                                                          #reading the data and initializing it to k var
        f.close()
        js=json.loads(k)                                        #converts the string to dictionary, as the data from file is in string format and we want to manipulate the dicitonary
        print(js,"\n")
        
    x=int(input("\t\t Press 1 to Continue    OR    Press 0 to EXIT : "))
print(" THANK-YOU !! ")

