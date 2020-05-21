#Read and Write to CSV File
# Import pandas as pd
import pandas as pd
# Import the sales.csv data: sales
sales = pd.read_csv('sales.csv')
# Print out sales
print(sales)
#write to csv files
c= {'Roll Number': [10,20,30],
    'Student Name':['Kala','Vimala','Harish'],
    'Age':[30,28,17],
    'Maths':[100,34,90],
    'Science':[39,89,29],
    'Date of Birth':['4/5/1990','9/12/1992','17/10/2003']
    }
df = pd.DataFrame(c,columns=['Roll Number','Student Name','Age','Maths','Science','Date of Birth'])
export_csv = df.to_csv (r'C:\Users\jasmathi\Documents\KloudOne\Python\Class4Assignment\pandaresult.csv', index = None, header=True) 
