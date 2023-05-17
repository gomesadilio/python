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