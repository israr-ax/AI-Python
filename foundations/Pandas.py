import pandas as pd 
#Create a data table then perform basic statistics
data = {
    "Name" : ["AHMED", "ISRAR","ALI","TURAB"],
    "Age":[21,22,18,17],
    "Marks": [88,98,90,89]
}
df=pd.DataFrame(data)
print(df)

print("Average Marks",df['Marks'].mean())
print("Max marks",df["Marks"].max())
print(df.describe())