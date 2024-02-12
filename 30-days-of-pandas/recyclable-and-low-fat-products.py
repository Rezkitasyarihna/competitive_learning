import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
  df_products = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
  return df_products[['product_id']]
