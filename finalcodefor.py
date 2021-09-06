entry = "0"
import json
import time
# below while loop help to keep in loop till we enter "exit"
while entry!= "exit":
    print("Wlcome to store 🙂🙂")
    print ("Prefer below list to order")

    fd = open("record.json",'r')
    r = fd.read()
    fd.close()

    record = json.loads(r)

    print(record)
    # It ask for choise i.e user want to sale something to us or want to purchase
    print("Would you like to 'sale' or 'purchase'")
    print("Enter 'bill' to print Bill")
    wt = str(input())
    # section to sale something to us
    if wt == "sale":

        # qn = 0

        prod_id = str(input("Enter product id:"))
        if prod_id in record.keys():
            print('This product is already in stock')
            print(record[prod_id]['name'])
            name = record[prod_id]['name']
            print(record[prod_id]['pr'])
            pr = record[prod_id]['pr']
            qn = int(input("Enter the quantity to add"))
            qn += record[prod_id]['qn']
            print("Record updated..")
            record[prod_id] = {'name': name, 'pr': pr, 'qn': qn}
        else:
            name = str(input("Enter name:"))
            pr = int(input("Enter price:"))
            qn = int(input("Enter quantity:"))

        record[prod_id] = {'name': name, 'pr': pr, 'qn': qn}

        js = json.dumps(record)

        fd = open("record.json",'w')
        fd.write(js)
        fd.close()

        print(record)

        # import json

        fd = open("record.json",'r')
        r = fd.read()
        fd.close()

        records = json.loads(r)

        # records
    # section to purchase 
    if wt == "purchase":
        # fb = open("purchesed.json",'r')
        # p = fb.read()
        # fb.close()

        # s = json.loads(p)
        s = {}
        transaction_id = len(s)
        ui_prod  = str(input("Enter the product_Id: "))
        if ui_prod not in record.keys():
            print("Sorry this product is not in store")
        else:
            t = time.ctime()    
            ui_quant = int(input("Enter the quantity: "))
            if ui_quant > record[ui_prod]['qn']:
                print("OOPS we have only ", record[ui_prod]['qn'], record[ui_prod]['name'])
                print("Would you like to buy ", record[ui_prod]['qn'], record[ui_prod]['name'],"'yes' or 'no'")
                choise = str(input())
                if choise == "yes":
                    ui_quant = record[ui_prod]['qn']
                    print("************ BILL ***************")
                    print("Product: ", record[ui_prod]['name'])
                    print("Price: ", record[ui_prod]['pr'])
                    print("Billing Amount: ", record[ui_prod]['pr'] * ui_quant)
                    print("------------------------------------")
                    record[ui_prod]['qn'] = record[ui_prod]['qn'] - ui_quant


                    js = json.dumps(record)

                    fd = open("record.json",'w')
                    fd.write(js)
                    fd.close()

                    print(js)

                    {'prod' : ui_prod, 'qn' : ui_quant, 'amount': record[ui_prod]['pr'] * ui_quant}

                    sales = {transaction_id : {'prod' : ui_prod, 'qn' : ui_quant, 'amount': records[ui_prod]['pr'] * ui_quant, "Time": t}}

                    sale = json.dumps(sales)

                    # print(sales)

                    fd = open("purchesed.json",'a')
                    fd.write(sale)
                    fd.close
                else:
                    print("Visit again.......")

            else:
                print("************ BILL ***************")
                print("Product: ", record[ui_prod]['name'])
                print("Price: ", record[ui_prod]['pr'])
                print("Billing Amount: ", record[ui_prod]['pr'] * ui_quant)
                print("------------------------------------")
                record[ui_prod]['qn'] = record[ui_prod]['qn'] - ui_quant



                js = json.dumps(record)

                fd = open("record.json",'w')
                fd.write(js)
                fd.close()

                print(js)



                {'prod' : ui_prod, 'qn' : ui_quant, 'amount': record[ui_prod]['pr'] * ui_quant}

                sales = { transaction_id: {'prod' : ui_prod, 'qn' : ui_quant, 'amount': record[ui_prod]['pr'] * ui_quant, "Time": t}}


                sale = json.dumps(sales)

                # print(sales)

                fd = open("purchesed.json",'a')
                fd.write(sale)
                fd.close
    if wt == "bill":

        transaction_id = str(input("Enter Transaction Id: "))
        print("Your Bill is : \n")
        print("**** Welcome *******\n")
        print("Time: ",sales[transaction_id]['Time'])
        print("Product Id: ", sales[transaction_id]['prod'])
        print("Quantity: ", sales[transaction_id]['qn'])
        print("Price: ",sales[transaction_id]['pr'])
        print("Total Amount: ",sales[transaction_id]['amount'])
        print("\n\n")
        print("....... Thank you for Purchasing .......")
        print("***** Visit Again ******")
    print(" #####Type 'exit' to get out of loop or anything to continue....######")
    entry = str(input())
print("Visit again , Have a good day 🙂🙂🙂")