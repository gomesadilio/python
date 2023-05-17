import numpy as np
import pandas as pd

arr = np.arange(12)

print(arr[:5])
print(arr[5:])
print(arr[::-1])
print(arr[::2])

narr = arr.reshape(3,4)

print(narr)

print(narr[:,:])
print(narr[1:,:])
print(narr[:,1:3])
print(narr[:,1:])


rng = np.random.default_rng(616)

inventory = rng.integers(0, 100, 10)

inventory - 24

inventory / 2

price = (rng.random(10) * 10).round(2)

(price * inventory).sum()

inventory_list = list(inventory)

inventory_list

sales_array = np.array([[0,5,155,0,518],[0,1827,616,317,325]])

sales_array

sales_array != 0

sales_array[sales_array != 0]

sales_array[(sales_array == 616) | (sales_array < 100)]

sales_array[(sales_array > 100) & (sales_array < 500)]

mask = (sales_array > 100) & (sales_array < 500)

sales_array[mask]

my_array = np.arange(20)

my_array % 2 == 0

my_array[my_array % 2 == 0]

even_odd = np.array(['even', 'odd'] * 10)

even_odd[even_odd != 'odd']

my_array[even_odd != 'odd'] = 0

inventory_array = np.array([12, 102, 18, 0, 0])

np.where(inventory_array <= 0, 'Out of Stock', 'In Stock')

product_array = np.array(['fruits', 'vegetables', 'cereal', 'dairy', 'eggs'])

np.where(inventory_array <= 0, 'Out of Stock', product_array)

my_array

np.where( my_array % 2, 'even', 'odd')

np.where( my_array % 2 == 0, 'even', np.where(my_array == 9, my_array, 'odd'))

sales_array

sales_array.sum()

sales_array.mean()

sales_array.max()

sales_array.min()

sales_array.sum(axis=0)

sales_array.sum(axis=1)

# Inventory array

rng = np.random.default_rng(616)

price = (rng.random(10) * 10).round(2)

inventory = rng.integers(0, 100, 10)

price.mean()

inventory.sum()

inventory.mean()

inventory.std()

(price * inventory).argmin()

product_value = (price * inventory).reshape(2,5)

product_value.sort()

price_2d = price.reshape(5, 2)

price_2d.sum(axis=1)

np.median(sales_array)

np.percentile(sales_array, 90)

np.unique(sales_array)

np.sqrt(sales_array)

np.median(product_value)

sales_array.sort()

sales_array = np.array([[0,5,155,0,518],[0,1827,616,317,325]])

sales_array.sort(axis=0)

s = pd.Series(name='Sales', data=[1,2,3,4,5,6,7,8,9])

s.values
s.index
s.name
s.dtype

array = np.arange(5)

pd.Series(array)

series = pd.Series(np.arange(5), name='Test Series')

series.values

series.values.mean()

series.mean()

series.index = [10, 20, 30, 40, 50]

series.name = 'Special series'

series.dtype

series.astype('float')
series.astype('int')  

series.index = list('abcde')

sales_array.astype('bool')

pd.Series(range(5)).astype('float')
pd.Series(range(5)).astype('bool')
pd.Series(range(5)).astype('object')
pd.Series(range(5)).astype('string')


sales = [0,5,155,0,518]

sales_series = pd.Series(sales, name='Sales')

sales_series[2]
sales_series[2:4]

items = ['coffe', 'bananas', 'tea', 'coconut', 'sugar']

sales_series = pd.Series(sales, index=items, name='Sales')

sales_series['tea']

my_series = pd.Series(range(5))
my_series

my_series[3]

my_series[1:3]

my_series = pd.Series(range(5), index=['Day0','Day1','Day2','Day3','Day4',])

my_series.loc['Day2']

my_series[::2]

my_series[::-2]

sales = [0, 3, 155, 0, 518]
items = ['coffee', 'coffee', 'tea', 'coconut', 'sugar']

sales_series = pd.Series(data= sales, name = 'Sales Series', index = items)

sales_series

sales_series['coffee']

sales_series.reset_index()

sales_series.reset_index(drop=True)

sales_series.loc[sales_series > 0]

mask = (sales_series > 0 ) & (sales_series.index == 'coffee')

sales_series.loc[mask]

sales_series == 5

sales_series.eq(5)

sales_series.index.isin(['coffee', 'tea'])
~sales_series.index.isin(['coffee', 'tea'])

my_series = pd.Series(
    data = [0,1,2,3,4],
    index = ['day 0', 'day 1', 'day 2', 'day 3', 'day 4'],
    name = 'Seeeries'
)

my_series['day 0']

my_series.loc[~(my_series == 2)]
my_series.loc[my_series.ge(2)]
my_series.loc[my_series.gt(2)]

sales_series.sort_values()
sales_series.sort_values(ascending=False)

sales_series.sort_index()
sales_series.sort_index(ascending=False)

my_series.sort_values(ascending=False)

sales_series

sales_series['tea'] = np.NaN

sales_series.add(1_000, fill_value = 0)

sales_series + 2