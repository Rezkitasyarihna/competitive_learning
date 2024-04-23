'''
Write a solution to find all customers who never order anything.
Return the result table in any order.
The result format is in the following example.
'''
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    #select which customer id from customer dataframe isn't in the customer id from orders dataframe
    df = customers[~customers['id']. isin(orders['customerId'])]
    #make a new dataframe consist of the customer who never order, rename the column name
    df = df[['name']].rename(columns={'name':'Customers'})
    return df
