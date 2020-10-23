#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# """
# Created on Tue Oct 20 19:31:55 2020

# @author: justine.skyler
# """

import os
import csv

csvpath=("/Users/justine.skyler/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv")




with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")  
    csv_header = next(csvreader)
    
    ledger = 0
    months = 0
    # months = sum(1 for row in csvreader)
    
    # ledger = []
    
    for rows in csvreader:
        months += 1
        ledger += int(rows[1])
        
        average = ledger/months
    # print (ledger)
    # print (months)
    
    
    
    
    
    
    
        # title.append(row[1])
    #     total = total + int(row[1])
        
        # ledger = ledger + int(row[1])
        
        

    

    # print (csvreader)
    

    
   
    

    
    print(f"Total Months: {months}")
    print(f"Total: {ledger}")
    print(f"Total: {average}")
    # print("Total: " + "$" + {ledger})