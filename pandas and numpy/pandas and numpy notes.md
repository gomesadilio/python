# Numpy 

```py
arr_two = np.array([[0,1,2,3],[4,5,6,7]])

arr_two.sum(axis=0) # column axis
arr_two.sum(axis=1) # row axis

```

## Aggregate and Statistical Functions In Numpy

function | Use
-|-
**np.sum(m)**     |Used to find out the sum of the given array.
**np.prod(m)**    |Used to find out the product(multiplication) of the values of m.
**np.mean(m)**    |It returns the mean of the input array m.
**np.std(m)**     |It returns the standard deviation of the given input array m.
**np.var(m)**     |Used to find out the variance of the data given in the form of array m.
**np.min(m)**     |It returns the minimum value among the elements of the given array m.
**np.max(m)**     |It returns the maximum value among the elements of the given array m.
**np.argmin(m)**  |It returns the index of the minimum value among the elements of the array m.
**np.argmax(m)**  |It returns the index of the maximum value among the elements of the array m.
**np.median(m)**  |It returns the median of the elements of the array m.

```py
np.percentile(array, n)     # returns a value in the nth percentile in an array
np.unique(array)            # returns the unique values in an array
np.sqrt(array)              # returns the square root of each value in an array
np.sort(array, axis=0)      # sort values by columns
```

- - -

# Series

Key properties:
- values
- index
- name
- dtype 

Series has inclusive if slicing index is above custom indices

## iloc

Access values by index positional

## loc

Access values by custom labels

## Logical operators & methods

description | python operator | pandas method
-|:-:|:-:
equal | == | .eq()
not equal | != | .ne()
less than or equal | <= | .le()
less than | < | .lt()
greater than or equal | >= | .ge()
greater than | > | .gt()
membership test | in | .isin()
inverse membership test | not in | ~.isin()

## Arithmetic operators & methods

operation | python operator | pandas method
-|:-:|:-:
addition | + | .add()
subtraction | - | .sub() <br> .subtract()
multiplication | * | .mul() <br> .multiply()
division | / | .div() <br> .truediv() <br> .divide()
floor division | // | .floordiv()
modulo | % | .mod()
exponentiation | ** | .pow()

## String methods

method|-
-|-
`.strip()`, `.lstrip()`, `.rstrip()` 
`.upper()`, `.lower()`
`.slice(start:stop:step)`
`.count("string")`
`.contains("string")`
`.replace("a","b")`
`.split("delimiter",expand=True)` 
`.len()`
`.startswith("string")`, `.endswith("string")`

## Numeric series aggregation

method|-
-|-
`.count()`
`.first()`, `.last()`
`.mean()`, `.median()`
`.min()`, `.max()`
`.argmax()`, `.argmin()` | index fot the smallest or largest
`.std()`, `.var()`
`.mad()` | mean absolute deviation
`.prod()` | product of all items
`.sum()`
`.quantile()` | (list) specific percentile

If use `.quantile([.5], interpolation='nearest')` return real value in series

### Aggregate categorical series

method |-
-|-
`.unique()` | array of distinct items
`.nunique()` | number of distincts
`.value_counts()` | items and frequency

If use `.value_counts(normalize=True)` return percent of each element over the total

## Identifying missing data

 - Use `.isna()` for this purpose 
 - `df.isna().sum()` return the count of NaN values 
 - `df.value_counts(dropna=False)` count the all values, include NaN 

## Handling missing data

- `.dropna()` - remove rows
- `fillna()` - replace with other value


`reset_index(drop=True)` -> drop old index

## Apply method

`df.apply(lambda x: x[-1] if len(x) > 3 else 0)``

## Where method

`df.where(logical test, value if False, inplace=False)`

\# of `numpy.where`

trick: invert condition with `~`

you can **chain.where() methods** to combine logical expressions

```py
(clean_wholesale
.where(~(clean_wholesale > 20), round(clean_wholesale * 0.9, 2))
.where(clean_wholesale > 10, 0)
)
```

# Dataframes

## Dataframes properties

- **shape** - number of rows and columns
- **index** - by default a range of integers (axis = 0)
- **columns** - columns index in a DataFrame (axis = 1)
- **axes** - the row and column indice in a DF
- **dtypes** - for each Series in DF

## Exploring a dataframe

- **head** - first n rows
- **tail** - last n rows
- **sample** - n random rows `df.sample(5, random_state=12345)`
- **info** - details: size, columns and memory usage `df.info(show_counts=True)`, for always display null count (limit aprox ~1.7m rows by default)
- **describe** - statistics for the columns - only numerical columns by default `df.describe(include='all).round()` for show all columns, round make output more readable

## Drop rows and columns

- `df.drop('column1', axis=1)`
- `df.drop(2, axis=0)`

## Identifying duplicate rows

- `df.duplicated()`
- `df.duplicated(subset='product')` - column(s) to look for duplicates

## Dropping duplicate rows

- `df.drop_duplicates()`
- `df.drop_duplicates(subset='product', keep='last', ignore_index=True)` - ign_idx reset index if necessary

## Identify missing data

- `df.isna().sum`
- `df.info()`

## Handling missing data

- `df.fillna(0)`
- `df.fillna({'price': 0, 'product': 'none'})`
- `df.dropna()`
- `df.dropna(subset='price')`