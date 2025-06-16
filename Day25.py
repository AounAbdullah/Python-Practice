# import csv
import pandas as pd
# with open('weather_data.csv') as file:
#     # lines = file.read()
#     # print(lines)
#     data = csv.reader(file)
#     temperature = []
#     for row in data:P
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))


# print(temperature)

# df = pd.read_csv('weather_data.csv')

# data_dict = df.to_dict()
# temp = df['temp']
# temp_list = df['temp'].to_list()

# sum_Temp = 0
# count = 0
# for temp in temp_list:
#     sum_Temp = sum_Temp + temp
#     count += 1

# avg_temp = sum_Temp/count
# print(temp.mean())
# print(temp.max())
# avg_temp = sum(temp_list)/ len(temp_list)

# print(round(avg_temp, 2))

# Get Data in row
# print(df[df['temp'].max() == df.temp])

# Creating a new dataframe of how many squares are there of each color

df = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250607.csv')
# print(df.head())

# Solution One
count_Gray = df[df['Primary Fur Color'] == 'Gray']
grey = count_Gray['Primary Fur Color'].count()

count_cinnamon = df[df['Primary Fur Color'] == 'Cinnamon']
cinnamon = count_cinnamon['Primary Fur Color'].count()

count_black = df[df['Primary Fur Color'] == 'Black']
black = count_black['Primary Fur Color'].count()


d =  {
    'Fur Color': pd.Series(['Gray', 'Black', 'Cinnamon'], index= [0,1,2]),
    'Count': pd.Series([grey, black, cinnamon])
}
new = pd.DataFrame(d)
# print(new)
new.to_csv()
# solution 2
color_Count = df['Primary Fur Color'].value_counts()
new_df = color_Count.reset_index()
new_df.columns = ['Fur Color', 'Count']
# print(new_df)
new_df.to_csv('Squirrel_count.csv')