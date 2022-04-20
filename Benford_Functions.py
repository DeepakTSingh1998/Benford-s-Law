'''
                                                         Deepak Singh
                              ---------------------
                              Benford Law Functions
                              ---------------------
'''

'''
Method 1 (Rows and Colums)
--------------------------
'''
def Method_1_Old_New(String,Number_Dict):
    Old = Number_Dict[String]
    New = Old + 1
    Number_Dict[String] = New
    return Number_Dict
    
def Number_Function(Number_Dict,Value):
    if Value == 0:
        Num_String = "Zero"
    elif Value == 1:
        Num_String = "One"
    elif Value == 2:
        Num_String = "Two"
    elif Value == 3:
        Num_String = "Three"
    elif Value == 4:
        Num_String = "Four"
    elif Value == 5:
        Num_String = "Five"
    elif Value == 6:
        Num_String = "Six"
    elif Value == 7:
        Num_String = "Seven"
    elif Value == 8:
        Num_String = "Eight"
    elif Value == 9:
        Num_String = "Nine"
    else:
        Num_String = "N/A"

    New_Numbers = Method_1_Old_New(Num_String,Number_Dict)
    return New_Numbers


def Method_1a_Main_Code(Data,Numbers):
    for i in range(0,len(Data)):
        for j in range(0,len(Data[0])):
            if Data[i,j] == float(0):
                Current = str(0)
            else:
                Current = str(Data[i,j])
            First_num = int(Current[0])
            New_Numbers = Number_Function(Numbers,First_num)
            
    return New_Numbers
            
'''
Method 2 (Text file)
--------------------
'''
def Method_1b_Main_Code(Data_List,Numbers):
    for i in range(0,len(Data_List)):
        for j in range(0,len(Data_List[0])):
            Zero_error = False
            while Zero_error == False:
                if Data_List[i][j][0] == "0":
                    Data_List[i][j] = Data_List[i][j][:0]+Data_List[i][j][0+1:]
                    if Data_List[i][j][0] != "0":
                        Zero_error = True
                else:
                    Zero_error = True
            
            try:
                Current = str(Data_List[i][j][0])
                First_num = int(Current[0])
            except:
                First_num = "N/A"
                
            New_Numbers = Number_Function(Numbers,First_num)
        
    return New_Numbers


'''
Method 3 (csv Pandas)
'''
def Method_2_Main_Code(df,Numbers):
    for col in range(0,len(df.columns.values)):
        Current_index = df.columns.values[col]
        for row in range(0,len(df[0])):
            try:
                Current = str(df[Current_index][row])
                First_num = float(Current[0])
            except:
                First_num = "N/A"
                    
            New_Numbers = Number_Function(Numbers,First_num)
    
    return New_Numbers



















