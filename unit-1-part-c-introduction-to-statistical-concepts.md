# Unit 1 Part C: Introduction to Statistical Concepts

## Lecture Notes
### Matrix Variables
- x<sub>i</sub> tells us the row
- x<sub>j</sub> tells us the column
- x<sub>ij</sub> tells us the row and column
  - First number tells us the row
  - Second number tells us the column
- Cannot use a single summation sign with a matrix, have to use two
  - First summation sign `∑` tells you what column to operate on
  - Second summation sign `∑` tells you what rows to operate on
  - ∑
- Just like `N` equals the last row, `K` is used to equal the last column
- Notation to refer to a whole column is `X.1` (for column one), `X.2` (for column 2)
  - The `.` means "every"
#### Creating matrices with Numpy
```python
import numpy as np
matrix = np.array([[2, 5, 9, 3, 1], [6, 8, 4, 2, 0], [10, 12, 5, 3, 5], [8, 12, 14, 5, 1]])
# Grand Mean
np.mean(matrix)
# Mean of first column "x̄.1"
np.mean(matrix[0])
# Mean of first row
np.mean(matrix[:, 0])
```

### Describing Interval / Ratio Data
- Need to understand the "center"
  - However, the center alone does not tell you enough as the spread/distribution may be radically different, but have the same mean
  - Infinite number of data sets may have the same center/mean
  - We need a number to represent the spread around the mean
- Whatever data set you have, when you subtract the mean from every number, the sum of those will always equal number
  - `∑(X - x̄) = 0`
- "Average absolute deviation"
  - Sum of absolute values `∑(|X - x̄|) = 0` divided by N
  - Typically is not used, because it only really describes the data set
- To get rid of negative numbers
  - ∑(X - x̄)<sup>2</sup>
- To get the variance of a data set...
  - S<sup>2</sup> = ∑(X - x̄)<sup>2</sup> / N
  - This is not the same metric as the scores
  - Take the square root of the variance, this is the standard deviation
  - S = √S<sup>2</sup>
- Calculating mean (xbar), variance, and standard deviation of an array
```python
import numpy as np
x = np.array([20, 21, 19, 30, 10, 25, 15, 20])
x_bar = np.mean(x)
x_variance = np.var(x)
x_stddev = np.std(x)
```
