## Histograms

Histograms are great ways of visualizing single variables. 

## Box plots

To visualize multiple variables, boxplots are useful, especially when one of the variables is categorical. Boxplots are great when you have a numeric column that you want to compare across different categories. 

Visualize basic summary statistics:

 * Outliers
 * Min/max
 * 25th, 50th, 75th percentiles
 
```python
import matplotlib.pyplot as plt

df.boxplot(column='population', by='continent')

plt.show()
```


## Scatter plots

When you want to visualize two numeric columns, scatter plots are ideal.

* Relationship between two numeric variables

* Flag potentially bad data

    * Errors not found by looking at 1 variable
	
	
	
## Tidy data

Principles of tidy data

* Columns represent separate variables
* Rows represent individual observations
* Observational units form tables

### Melting data

Common data problem is that columns contain values instead of variables. In order to fix it, we should use melt

```
pd.melt(frame=df, id_vars='name', values_vars=['treatment a', 'treatment b'], var_name='treatment', value_name='result')
```

There are two parameters you should be aware of: `id_vars` and `value_vars`. The `id_vars` represent the columns of the data you do not want to melt (i.e., keep it in its current shape), while the `value_vars` represent the columns you do wish to melt into rows. By default, if no `value_vars` are provided, all columns not set in the `id_vars` will be melted. This could save a bit of typing, depending on the number of columns that need to be melted.

### Pivot

Pivoting data is the opposite of melting it. While melting takes a set of columns and turns it into a single column, pivoting will create a new column for each unique value in a specified column.

`.pivot_table()` has an `index` parameter which you can use to specify the columns that you don't want pivoted: It is similar to the `id_vars` parameter of `pd.melt()`. Two other parameters that you have to specify are `columns` (the name of the column you want to pivot), and `values` (the values to be used when the column is pivoted). 

* Opposite of melting
* In melting, we turned columns into rows
* Pivoting: turn unique values into separate columns
* Analysis friendly shape to reporting friendly shape
* Violates tidy data principle: rows contain observations

```python
weather_tidy = weather.pivot(index='date', columns='element', values='value', aggfunc=np.mean)

airquality_pivot = airquality_melt.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading')
```

## Concat

Think of column-wise concatenation of data as stitching data together from the sides instead of the top and bottom. To perform this action, you use the same pd.concat() function, but this time with the keyword argument axis=1. The default, axis=0, is for a row-wise concatenation.

```python
row_concat = pd.concat([uber1, uber2, uber3])

ebola_tidy = pd.concat([ebola_melt, status_country], axis=1)
```

## Globbing

* Pattern matching for file names
* Wildcards: *?
    * Any csv file: *.csv
    * Any single character file: file_?.csv
* Returns list of files
* Can use this list to load into separate DataFrames

### Plan
* Load files from globbing into pandas
* Add the DataFrames into a list
* Concatenate multiple datasets at once

```python
import glob

csv_files = glob.glob('*.csv')

print(csv_files)

list_data = []

for filename in csv_files:
   data = pd.read_csv(filename)
   list_data.append(data)
   
pd.concat(list_data)
```

## Merge data

* Similar to joining tables in SQL
* Combine disparate datasets based on common columns


```python
pd.merge(left=state_populations, right=state_codes, on=None, left_on='state', right_on='name')
```

### Types of merges
* One-to-one
* Many-to-one/one-to-many
* Many-to-many

## Data types

```python
df['treatment b'] = df['treatment b'].astype(str)

df['sex'] = df['sex'].astype('category')
```

Cleaning bad data
```python
df['treatment a'] = pd.to_numeric(df['treatment a'], errors='coerce')
```

## Regular Expressions

The most effective way to use regular expressions

* Compile the pattern
* Use the compiled pattern to match values
* This lets use the pattern over and over again

```python
import re

pattern = re.compile('\$\d*\.\d{2}')

result = pattern.match('$17.77')

bool(result)
```
### Find all

```python
# Import the regular expression module
import re

# Find the numeric values: matches
matches = re.findall( '\d+', 'the recipe calls for 10 strawberries and 1 banana')

# Print the matches
print(matches)
```

## Duplicates and Missing Data

```python
countries = countries.drop_duplicates()
```

### Drop missing values

```python
tips_dropped = tips_nan.dropna()
```

### Fill missing values

It's now time to deal with the missing data. There are several strategies for this: You can drop them, fill them in using the mean of the column or row that the missing value is in (also known as imputation), or, if you are dealing with time series data, use a forward fill or backward fill, in which you replace missing values in a column with the most recent known value in the column. 

In general, it is not the best idea to drop missing values, because in doing so you may end up throwing away useful information. In this data, the missing values refer to years where no estimate for life expectancy is available for a given country. You could fill in, or guess what these life expectancies could be by looking at the average life expectancies for other countries in that year, for example. Whichever strategy you go with, it is important to carefully consider all options and understand how they will affect your data.

* Fill with provided value
```python
tips_nan['sex'] = tips_nan['sex'].fillna('missing')

tips_nan[['total_bill', 'size']] = tips_nan[['total_bill, 'size']].fillna(0)
```
* Use a summary statistics (median is better statistic in the presence of outliers)

```python
mean_value = tips_nan['tip'].mean()

tips_nan['tip'] = tips_nan['tip'].fillna(mean_value)
```

## Assert Statements

Helps to verify and prevent errors

```python
assert google.Close.notnull().all()

# Assert that there are no missing values
assert pd.notnull(ebola).all().all()

# Assert that all values are >= 0
assert (ebola >= 0).all().all()
```

## Common approach

```python
# Import libraries
import pandas as pd 
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data.csv')

# Look at a few records
df.head()

# Look at missing values and column types
df.info()

# Look at columns
df.columns

# Look at stats. Screen for outliers and bad data
df.describe()

df.column.value_counts()

# Visualize data
df.column.plot('hist')

# Use a function to clear the data. Arguments can be row or column data
def cleaning_func(row_data):
	# data cleaning steps
	
	return ...
	
# axis=0 - by column, axis=1 - by row
df.apply(cleaning_func, axis=1)

# Check data
assert (df.column_data > 0).all()

# Convert data to be tidy data
# 1) Rows contain observations
# 2) Columns contain variables

# Check data types. If numeric data are string than we have a problem
df.dtypes

df['column'] = df['column'].to_numeric()

df['column'] = df['column'].astype(str)

# Additional calculations and saving your data
df['new_column'] = df['column_1'] + df['column_2']

df['new_column'] = df.apply(my_function, axis=1)

df.to_csv('my_data.csv')	
```