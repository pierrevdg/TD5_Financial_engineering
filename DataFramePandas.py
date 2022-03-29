import pandas as pd 
Buy = {'Buy' : pd.Series([(10,10),(5,10),(2,11)])}
DataFrame_Buy = pd.DataFrame(Buy) 

Sell = {'Sell' : pd.Series([(120,12),(1,10),(10,10)])}
DataFrame_Sell = pd.DataFrame(Sell) 

print(DataFrame_Buy) 
print(DataFrame_Sell)
