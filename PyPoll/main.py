#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 19:31:55 2020

@author: justine.skyler
"""

import os
import csv

csvpath=("/Users/justine.skyler/Documents/GitHub/python-challenge/PyPoll/Resources/election_data.csv")


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")  
    csv_header = next(csvreader)
    
    total_votes = 0
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0
    
    for rows in csvreader:
        total_votes +=1
        
        if rows[2] == "Khan":
            khan_votes +=1
        elif rows[2] == "Correy":
            correy_votes +=1
        elif rows[2] == "Li":
            li_votes +=1
        elif rows[2] == "O'Tooley":
            otooley_votes +=1
    
    khan_percent = (khan_votes/total_votes) * 100
    correy_percent = (correy_votes/total_votes) * 100
    li_percent = (li_votes/total_votes) * 100
    otooley_percent = (otooley_votes/total_votes) * 100
    
    
    candidates_list = ["Khan","Correy","Li","O'Tooley"]
    votes_list = [khan_votes,correy_votes,li_votes,otooley_votes]
    
    dict_candidates_votes = dict(zip(candidates_list,votes_list))
    maxholder= max(dict_candidates_votes, key=dict_candidates_votes.get)
    
    
    print(f"Election Results")
    print(f"----------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"----------------------------")
    print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    print(f"Correy: {correy_percent:.3f}%  ({correy_votes})")
    print(f"Li: {li_percent:.3f}%  ({li_votes})")
    print(f"O'Tooley: {otooley_percent:.3f}%  ({otooley_votes})")
    print(f"----------------------------")
    print(f"Winner: {maxholder}")
    print(f"----------------------------")
    
    
output_file=("/Users/justine.skyler/Documents/GitHub/python-challenge/PyPoll/Analysis/output.txt")

with open(output_file,"w") as output:
    writer = csv.writer(output)
    
    writer.writerow(["Election Results"])
    writer.writerow(["----------------------------"])
    writer.writerow([f"Total Months: {total_votes}"])
    writer.writerow(["----------------------------"])
    writer.writerow([f"Khan: {khan_percent:.3f}% ({khan_votes})"])
    writer.writerow([f"Correy: {correy_percent:.3f}%  ({correy_votes})"])
    writer.writerow([f"Li: {li_percent:.3f}%  ({li_votes})"])
    writer.writerow([f"O'Tooley: {otooley_percent:.3f}%  ({otooley_votes})"])
    writer.writerow(["----------------------------"])
    writer.writerow([f"Winner: {maxholder}"])
    writer.writerow(["----------------------------"])
    