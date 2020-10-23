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
    
    ledger = []
    months = []
    change = []
    
    for rows in csvreader:
        months.append(rows[0])
        ledger.append(int(rows[1]))
        
    for x in range(len(ledger)-1):
        change.append(ledger[x+1] - ledger[x])
        
    average_change = sum(change) / len(change)
    
    greatest_increase = max(change)
    increase_ref = change.index(greatest_increase) + 1
    increase_month = months[increase_ref]
    
    greatest_decrease = min(change)
    decrease_ref = change.index(greatest_decrease) + 1
    decrease_month = months[decrease_ref]


    # print (csvreader)  
    

    print(f"Financial Analysis")
    print(f"----------------------------")    
    print(f"Total Months: {len(months)}")
    print(f"Total: ${sum(ledger)}")
    print(f"Average Change: ${round(average_change,2)}")
    print(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")
        
output_file=("/Users/justine.skyler/Documents/GitHub/python-challenge/PyBank/Analysis/output.txt")

with open(output_file,"w") as output:
    writer = csv.writer(output)
    
    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------------------"])
    writer.writerow([f"Total Months: {len(months)}"])
    writer.writerow([f"Total: ${sum(ledger)}"])
    writer.writerow([f"Average Change: ${round(average_change,2)}"])
    writer.writerow([f"Greatest Increase in Profits: {increase_month} (${greatest_increase})"])
    writer.writerow([f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})"])
    
    
    
    
        