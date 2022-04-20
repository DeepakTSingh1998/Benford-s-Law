  # -*- coding: utf-8 -*-

## -------------------- Benford's Law ---------------------------------------##
## ------------------ Made by Deepak Singh ----------------------------------##

## Libraries
import pandas as pd
import numpy as np
import Benford_Functions as BF
import matplotlib.pyplot as plt

"""
Initilisation of Number Variables and Dictionary
"""

Zero=One=Two=Three=Four=Five=Six=Seven=Eight=Nine=N_A=0
Numbers = {"Zero":Zero,"One":One,"Two":Two,"Three":Three,"Four":Four,
           "Five":Five,"Six":Six,"Seven":Seven,"Eight":Eight,"Nine":Nine,
           "N/A":N_A}

## FILE OPEN
print('Please select the file type you will like to open:\n')
print('[1] .txt')
print('[2] .csv\n')

Data_type = float(input())

if Data_type != 1 and Data_type != 2:
    print('Only [1] or [2] can be selected.')
    
else:
    print('Please also name the file (*Without .txt/.csv):\n')
    Data_name = input()
    
    if Data_type == 1:
        print('How is the txt Data organised?:\n')
        print('[1] Rows and Columns')
        print('[2] Normal txt file')
        Txt_Type = float(input())
        
        if Txt_Type == 1:
            Data = np.loadtxt(Data_name+str('.txt'),dtype = float)
            BF.Method_1a_Main_Code(Data,Numbers)
            
        else:
            Data = open(Data_name+".txt","r")
            Data_List = []
            for line in Data:
                Stripped_Line = line.strip()
                Line_list = Stripped_Line.split()
                Data_List.append(Line_list)
            Data.close()
            BF.Method_1b_Main_Code(Data_List,Numbers)
            
    elif Data_type == 2:
        CSV_Type = input('Does the file have headers (True or False)\n')
        if CSV_Type == "True":
            df = pd.read_csv(Data_name+'.csv')
        else:
            df = pd.read_csv(Data_name+'.csv', header=None)
        BF.Method_2_Main_Code(df, Numbers)
        

"""
Bar chart
"""
Names = ("1","2","3","4","5","6","7","8","9")
y_pos = np.arange(len(Names))
Num_Values = [Numbers["One"],
              Numbers["Two"],
              Numbers["Three"],
              Numbers["Four"],
              Numbers["Five"],
              Numbers["Six"],
              Numbers["Seven"],
              Numbers["Eight"],
              Numbers["Nine"],
              ]

plt.bar(y_pos,Num_Values,align="center")
plt.xticks(y_pos,Names)
plt.ylabel('Number Counts')
plt.title('Benford''s Law Bar Chart')
        