# Elite_inventory_management
# ETG-Inventory-Management-System-Assignment
This repository is having all the  codes with json files for making an Inventory Management System during ETG AI/ML Internship.

## This inventory management system works on NOSQL based database
1. I have used json file system to make it work 
2. These json files are linked with code to perform tasks

### Functions performed in Inventory Management System :
1. Add products to store which automatically update record.json file
2. Purchase product from store which again update record.json file 
3. Generete the bill of purchased product 
4. Purchased product get added to purchased file to keep treck of purchased product.

### Features of product:
1. The Id of product
2. Name of the product
3. Price of product
4. Quantity of product in store
5. Time when product is purchased get printed in purchased.json file

#### Detail description of Inventory System

This whole code is wrapped in while loop which run itself again and again till we enter 'exit' then again it ask that 
you (user) want to sell or purchase product according to choise thai block get executed .If you want to sell product 
which already exit in store then it tells you about it's existance and take qantity of that product and update the 
quantity for that particular product and also tell if product is not available in that much quantity which user want.
