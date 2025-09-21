import pandas as pd
df=pd.read_csv("IPL2025Batters.csv")
import matplotlib.pyplot as plt
# """Conversion Exsisting Numerical data into Standaradized numerical data"""
#  """Standardscaling"""
from sklearn.preprocessing import StandardScaler
standard_scaler_object = StandardScaler()
df["Matches"] = standard_scaler_object.fit_transform(df[["Matches"]])
print(df)
df["Matches"].plot(kind="hist", color="yellow", edgecolor="black")
plt.xlabel("Value")
plt.ylabel("frquency")
plt.show()

"""MinMaxScalling"""

from sklearn.preprocessing import MinMaxScaler
min_max_scaler_object = MinMaxScaler()
df["Matches"] = min_max_scaler_object.fit_transform(df[["Matches"]])
print(df)
df["Matches"].plot(kind="hist", color="Red",edgecolor="Black")
plt.xlabel("IPL")
plt.ylabel("Scores")
plt.show()
