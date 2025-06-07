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

df = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250607.csv')






