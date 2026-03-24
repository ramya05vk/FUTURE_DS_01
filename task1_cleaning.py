import pandas as pd
import numpy as np
df = pd.read_csv("online_retail.csv", encoding='ISO-8859-1')
df.shape                #confirming whether csv file is loaded correctly
df.head()
df.isnull().sum()       #checking for missing values like customerID and Description in the dataset
df=df.dropna(subset=['CustomerID'])      #removing rows where there is no customer ID
df=df[~df['InvoiceNo'].astype(str).str.startswith('C')]  #remove the cancelled transcations which starts with letter 
df=df[df['Quantity']>0]
df=df[df['UnitPrice']>0]
df=df.drop_duplicates()
df['InvoiceDate']= pd.to_datetime(df['InvoiceDate'])
df['Revenue']=df['Quantity']* df['UnitPrice']
print("\n cleaned data shape:", df.shape)
print("\n Remaoning Missing values:\n",df.isnull().sum())
print(df.head())

df.to_csv("cleaned_online_retail.csv",index=False)

print("\n data cleaning completed and saved as cleaned csv file")
