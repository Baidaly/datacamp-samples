## Reducing functions
* mean
* std
* sum
* first, last
* min, maxs

## Examples
```py
sales.groupby('weekday')[['bread', 'butter']].sum()

sales.groupby(['city', 'weekday']).mean()

sales['weekday'].unique()

sales['weekday'].astype('category')
```

## Filtering

### groupby object
```py
splitting = auto.groupby('year')

for group_name, group in splitting:
    # filter by manufacturer
    avg = group.loc[group['name'].str.contains('chevrolet'), 'mpg'].mean()
    print(group_name, avg)
```

### groupby object: comprehension
```py
chevy_means = {year:group.loc[group['name'].str.contains('chevrolet'), 'mpg'].mean()}
                   for year, group in splitting}
pd.Series(chevy_means)
```

### Boolean groupby

```py
chevy = auto['name'].str.contains('chevrolet')

auto.groupby(['yr', chevy])['mpg'].mean()
```