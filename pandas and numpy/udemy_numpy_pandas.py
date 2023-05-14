import numpy as np

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