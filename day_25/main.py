# # with open('./weather_data.csv', 'r') as weather_file:
# #     weather_data = weather_file.readlines()
# #
# # print(weather_data)
#
# # import csv
# #
# # with open('weather_data.csv') as data_file:
# #     data = csv.reader(data_file)
# #     temperature = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperature.append(int(row[1]))
# #     print(temperature)
#
# import pandas
# from numpy.ma.extras import average
#
# data = pandas.read_csv('weather_data.csv')
# # print(type(data['temp']))
# # print(data['temp'])
#
# data_dict = data.to_dict()
#
# # print(data_dict)
# temp_list = data['temp'].to_list()
#
# #
# # average_temp = sum(temp_list) / len(temp_list)
# #
# # print(round(average_temp))
#
# average_num = data['temp'].mean()
#
# # print(average_num)
# #
# max_temp = data['temp'].max()
# #
# # # Get data in columens
# # print(data['condition'])
# # print(data.condition)
# # print(temp_list)
#
# # Get Data in Row
# print(data[data.day == 'Monday'])
#
# print(data[data.temp == max_temp])
#
# monday = data[data.day == 'Monday']
# temp_Fahrenheit = monday.temp[0] * 9 / 5 + 32
# print(monday.temp[0], temp_Fahrenheit)
#
# # Create data from scratch
# data_dict_scratch={
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76,56,65]
# }
#
# data = pandas.DataFrame(data_dict_scratch)
# print(data)
# data.to_csv('new_data.csv')
import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250712.csv')
# print(data)

grey_squirrels = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels = len(data[data['Primary Fur Color'] == 'Black'])
print(grey_squirrels)
print(red_squirrels)
print(black_squirrels)

data_dict ={
    'Fur color': ['Grey', 'Cinnamon', 'Black'],
    'Count': [grey_squirrels, red_squirrels,black_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count')