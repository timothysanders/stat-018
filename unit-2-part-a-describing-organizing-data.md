# Unit 2: Describing and Organizing Data - Central Tendency and Dispersion

| Scale of Data                               | Central Tendency | Variability         |
|---------------------------------------------|------------------|---------------------|
| Interval / Ratio w/no outliers              | mean             | s, s<sup>2</sup>    |
| Interval / Ratio w/outliers, but don't care | mean             | s, s<sup>2</sup>    |
| Interval / Ratio w/outliers, but do care    | median           | IQR                 |
| Ordinal                                     | Median           | IQR                 |
| Nominal                                     | Mode             | Index of Dispersion |

- When reporting mean, **ALWAYS** report standard deviation and variance (s and s<sup>2</sup>)
- When reporting median, **ALWAYS** report Interquartile Range (IQR)

## Mode
- `mode`: name of category with the highest frequency
- Not a measure of the "center" of the data
- Important to remember that mode is **NOT** the frequency, it is the name of the category with the highest frequency

## Index of Dispersion
- If no dispersion in the data, the value is 0
  - This would mean that all values are in the same category, with no one else in other categories
- If there is maximum dispersion, then the value is 1
  - Exact same number of values in every category
- Proportion of maximum dispersion
  - If value is 0.7, data is "70% maximally dispersed"
- To calculate dispersion
  1. Get total number of values in all categories (N)
  2. Get N<sup>2</sup>
  3. Count number of categories (K)
  4. Get sum of the frequencies squared (Σ*fi*<sup>2</sup>)

## Python Code
```python
import numpy as np

def find_quartile_value(quartile, array):
    """
    Find the given quartile value for an array with an odd number of elements.
    """
    def find_quartile_location(array, quartile):
        quartile_location = quartile * (len(array) / 4)
        return quartile_location
    
    def get_lower_real_limit(number):
        return number - 0.5
    
    location = find_quartile_location(array, quartile)
    location_value = np.sort(array)[int(location // 1)]
    quartile_value = get_lower_real_limit(location_value) + (location % 1)
    return quartile_value
```

### Unit 2 Part A Overview of Central Tendency Quiz
