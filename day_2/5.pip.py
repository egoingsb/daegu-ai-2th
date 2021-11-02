import pandas
house = pandas.read_csv('https://gist.githubusercontent.com/egoing/65a3ab6f5decef22d3ef49dcdcc9b33e/raw/eca4ed834144351aa238f00efc07a50e69171d93/boston_house_prices_dataset.csv')

print(house)
print(house.head(2))
print(house.describe())