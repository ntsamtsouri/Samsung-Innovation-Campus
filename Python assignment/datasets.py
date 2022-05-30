import pandas as pd
import numpy as np

#DESCRIPTION OF DATASET

#question 1 - Read csv file
df = pd.read_csv('data.csv', delimiter=',')
#print(df)

#question 2 - Get last 5 records of dataframe
last5 = df.tail(5)
print(last5)
last5b = df.iloc[-5:] #this is an alternative way to get last 5 records

#question 3 - Number and name of dataset's columns
col = df.columns
print("Dataset's columns are: ", col)
print("Number of dataset's columns is equal to ", len(col))

#question 4 - Datatype(s) of dataset's columns
type = df.dtypes
print(type)

#question 5 - Columns with NaN values
missing = df.columns[df.isnull().any()]  #isna() is an alternative method to find NaN values and could be used for this question 
print(len(missing), " columns with missing values:", missing)

#question 6 - Total number of records without headers
total = len(df)
print("Total records equal to ", total)


#CLEANING DATASET

#question 1 - Remove rows with NaN values in "Description" or/and "CostumerID" columns 
df.dropna(axis=0, how='any', thresh=None, subset=['Description','CustomerID'], inplace=True)
print(df) #na to check again

#question 2 - Delete rows with 'Description' = "AMAZON FEE","Manual","SAMPLES","POSTAGE","PACKING CHARGE"
df.drop(df[(df['Description'] == 'AMAZON FEE') | (df['Description'] == "Manual") | (df['Description'] == "SAMPLES") | (df['Description'] == "POSTAGE") | (df['Description'] == "PACKING CHARGE")].index, inplace = True)
print(df)

#question 3 - Remove rows with negative value in "Quantity" column
df.drop(df[df['Quantity'] < 0].index, inplace = True)
print(df)

#question 4 - Create column ItemTotal = Quantity*UnitPrice
df['ItemTotal'] = df.apply(lambda r: r.Quantity * r.UnitPrice, axis=1)
print(df)


#UNDERSTANDING DATASET

#question 1 - Number of unique/different customers
n = len(pd.unique(df['CustomerID']))
print("Number of unique customers equals to: ", n)


#question 2 - Name the different countries with which the company cooperates
cntr = 0 
countries = []
for i in range(0, len(df['Country'])):
    if df['Country'].iloc[i] not in countries:
        countries.append(df['Country'].iloc[i])
        cntr += 1

print("Number of countries: ", cntr)
print("The countries: ", countries)

#question 3 - Time period of available data in dataset
min = df['InvoiceDate'].min()
max = df['InvoiceDate'].max()
print("Our available data range from ", min, " to ", max, ".")

#question 4 - Which product(s) can a customer buy with 100-150 euro?
prod_range = []
for i in range(0, len(df['ItemTotal'])):
    if ((df['ItemTotal'].iloc[i] >= 100) & (df['ItemTotal'].iloc[i] <= 150)):
        prod_range.append(df['Description'].iloc[i])
print("The product(s) a customer can buy with 100-150 euro are: ", prod_range, len(prod_range))
prod_rangeb = df.loc[(df['ItemTotal'] >= 100) & (df['ItemTotal'] <= 150)] #this is an alternative way to find products with ItemTotal ranging between [100,150]


#question 5 - Which products contain 'HANDBAG' in their description?
result = df['Description'].str.contains(pat='HANDBAG')
df['Result'] = result
products_handbag = []
for i in range(0, len(df['Description'])):
    if df['Result'].iloc[i]:
        products_handbag.append(df['Description'].iloc[i])
print("The products are: ", products_handbag, len(products_handbag))
