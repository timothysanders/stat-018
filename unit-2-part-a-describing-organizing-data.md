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

## Z-scores
- Allows you to compare different data sets, as long as they are normally distributed
- Z-scores can be used to translates from one distribution to another
  - For example, if someone has a z-score of 1.0 in another distribution
    - x = x-bar + (s<sub>new</sub>)(z<sub>old</sub>)
- Z-score percentile ranks
  - Based on the normal curve
  - Normal curves are symmetric, with mean, median, and mode at the same location

## Python Code
```python
import numpy as np
from scipy import stats

array_one = np.array([7, 7, 7, 3, 1])
stats.kurtosis(array_one)
stats.skew(array_one)
stats.moment(array_one, 3)
stats.moment(array_one, 4)

def find_quartile_values(array):
    """
    Find the given quartile value for an array with an odd number of elements.
    """
    def find_quartile_location(quartile_array, quartile):
        quartile_location = quartile * (len(quartile_array) / 4)
        return quartile_location
    
    def get_lower_real_limit(number):
        return number - 0.5
    result_json = {}
    for loc in [1, 2, 3]:
        location = find_quartile_location(array, loc)
        location_value = np.sort(array)[int(location // 1)]
        quartile_value = get_lower_real_limit(location_value) + (location % 1)
        result_json[f"Q{loc}"] = {"location": location, "value": quartile_value}
    result_json["IQR"] = result_json["Q3"]["value"] - result_json["Q1"]["value"]
    return result_json
```

### Unit 2 Part A Overview of Central Tendency Quiz
#### Question 1
- Text: You have data measured on an interval / ratio scale of measurement.  There are no outliers in the data.  What is the most appropriate measure of central tendency to use in this situation? 
- Answer: Mean
#### Question 2
- Text: You have data measured on an interval / ratio scale of measurement.  There are outliers in the data.  You do not care to exclude the effects of the outliers on the measure of central tendency.  What is the most appropriate measure of central tendency to use in this situation? 
- Answer: Mean
#### Question 3
- Text: You have data measured on an interval / ratio scale of measurement.  There are outliers in the data.  You want to exclude the effects of the outliers on the measure of central tendency.  What is the most appropriate measure of central tendency to use in this situation? 
- Answer: Median
#### Question 4
- Text: You have data measured on an ordinal scale of measurement.  What is the most appropriate measure of central tendency to use in this situation? 
- Answer: Median
#### Question 5
- Text: You reported the Mode as your measure of Central Tendency.  What measure of Dispersion should you report?
- Answer: Index of Dispersion
#### Question 6
- Text: You reported the Median as your measure of Central Tendency.  What measure of Dispersion should you report?
- Answer:  Interquartile Range
#### Question 7
- Text: You reported the Mean as your measure of Central Tendency.  What measure of Dispersion should you report?
- Answer:  Standard Deviation or Variance
#### Question 8
- Text: When the data are normally distributed, where is the mean located relative to the median? 
- Answer: Mean and Median are at the same exact location.
#### Question 9
- Text: When the data are positively skewed, where is the mean located relative to the median? 
- Answer: Mean located to the right of the median.
#### Question 10
- Text: When the data are negatively skewed, where is the mean located relative to the median?
- Answer: Mean located to the left of the median.
#### Question 11
- Text: Which of the following measures of central tendency has exactly 50 percent of the scores falling below it and 50 percent of the scores falling above it? 
- Answer: Median
#### Question 12
- Text: Which measures of central tendency is simply the name of the most frequently occurring category? 
- Answer: Mode
#### Question 13
- Text: Which of the following measures of central tendency is the sum of the scores divided by the total number of scores?
- Answer: Mean
#### Question 14
- Text: Which of the following measures of variability is the middle 50 percent of the data? 
- Answer: Interquartile Range
#### Question 15
- Text: Which measure of variability has value equal to zero when every frequency is in one category and value equal to one when frequencies are equally distributed among all categories?
- Answer: Index of Dispersion
#### Question 16
- Text: Which measure of central tendency should be used whenever it is possible to use it because it takes all of the data values into account?
- Answer: Mean
#### Question 17
- Text: Which of the following has 25% of the scores falling below it?
- Answer: Q1
#### Question 18
- Text: Which of the following has 75% of the scores falling below it?
- Answer: Q3
#### Question 19
- Text: Which of the following has to do with the height of middle of the distribution and the height of the tails?
- Answer: Kurtosis
#### Question 20
- Text: Which of the following has to do with the shift of the data either left or right?
- Answer: Skew
#### Question 21
- Text: Which measure of dispersion reports the percent of dispersion in the data as compared to Maximal Dispersion. 
- Answer: Index of Dispersion
#### Question 22
- Text: For a Continuous, Unimodal Distribution, moving from left to right, which of the following is the usual order of the mean, median, and mode for a positively skewed distribution. 
- Answer: "Mode, Median, Mean"
#### Question 23
- Text: For a Continuous, Unimodal Distribution, moving from right to left, which of the following is the usual order of the mean, median, and mode for a negatively skewed distribution.
- Answer: "Mode, Median, Mean"
#### Question 24
- Text: Which of the following is NOT true regarding the mean?
- Answer:  The mean is good for data sets that contain outliers.
#### Question 25
- Text: In a Positively Skewed Distribution, the long tail is to the Right.
- Answer: True
#### Question 26
- Text: In a Negatively Skewed Distribution, the long tail is to the Right.
- Answer: False
#### Question 27
- Text: In a Normal Distribution, the Mean, Median, and Mode are at the same location. 
- Answer: True
#### Question 28
- Text: The mean can only be used when the data are measured on an Interval/Ratio Scale of Measurement. 
- Answer: True