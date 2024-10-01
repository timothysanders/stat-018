### Chapter 2: Basic Mathematical and Measurement Concepts
#### Mathematical Notation
- Statistics usually deals with group data resulting from one or more variables, derived from samples (though occasionally from populations)
- Typically, you use the capital letter **`X`** and sometimes **`Y`** to stand for the variable(s) measured
    - For example, if we are measuring age of subjects, *X* = age
- If there are a number of values of a variable, use *X* and a subscript, for example X<sub>1</sub>, X<sub>2</sub>, etc.
- If variable of age is represented by X, then **`N`** can represent the number of scores in the distribution
- In general, you can refer to a single score in the *X* distribution as X<sub>i</sub>
    - *i* can be any value from 1 to *N*
#### Summation
- One of the most frequent operations in stats is to sum all or part of the scores of a distribution
- The symbolic abbreviation of "sum of all the scores" is **∑**, the capital Greek letter sigma
- Algebraic phrase employed for summation
    - ![Summation Example](./images/summation-example.png)
    - This stands for "sum of the *X* variable from *i* = 1 to *N*"
    - Term below the summation sign tells us the first score in the summation
    - Term above the summation sign designates the last score
    - This translates to the following
    - ![Summation Equation](./images/summation-equation.png)
- If the summation is for all scores, often the summation phrase is omitted and written as ∑*X*
- Other summations frequently encountered are ∑*X*<sup>2</sup> and (∑*X*)<sup>2</sup>
    - ∑*X*<sup>2</sup> means that we first square the X scores and then sum them
    - (∑*X*)<sup>2</sup> means that we first sum the scores, then square the sum
#### Order of Mathematical Operations
- Mathematical operations should be done in the following order
    1. Parentheses first
    2. Exponents

    3. Multiplication and Division **FROM LEFT TO RIGHT**
    4. Addition and Subtraction **FROM LEFT TO RIGHT**
#### Measurement Scales
- The types of measurement scales that are used determine which statistical inference tests can be used to analyze the data
- Four different commonly encountered scales
- **Nominal**
    - A nominal scale has categories for the units
    - Lowest level of measurement, most often used with variables that are qualitative (vs quantitative)
    - Variables are divided into several categories, which are the "units" on the scale
    - Objects are "measured" by determining the category to which they belong
    - There is no magnitude relationship between units of a nominal scale
    - Fundamental property of nominal scales is that of *equivalence*, where all members of a given class are the same from the standpoint of the classification variable
    - Allows for categorization of objects into mutually exclusive categories
    - Main mathematical operation done with nominal scales is to count the number of objects in each category
- **Ordinal**
    - Ordinal scale is one in which the numbers on the scale represent rank orderings, rather than raw score magnitudes
    - Higher level of measurement than nominal, but still relatively low level of property of magnitude
    - With ordinal scale, we rank order the objects measured according to whether they possess more, less, or the same amount of the variable being measured
    - Ordinal scale allows for greater than, equal to, or less than comparisons
    - Does not have the property of equal intervals between the adjacent units
    - Does not tell us absolute level of the variable
    - Examples include ranking of finishers in a marathon, AP ranking of football teams, ranking of students by motivation level
- **Interval**
    - Interval scale is one in which the units represent raw score magnitudes, there are equal intervals between adjacent units on the scale, and there is no absolute zero point
    - Celsius scale is an example of the interval scale, each unit is separated by an equal interval and there is no "absolute zero" point (meaning there is no point where there is "no temperature")
    - Can determine the following mathematical operations
        - A = B, A > B, A < B, A - B = C - D, A - B > C - D, A - B < C - D
- **Ratio**
    - Ratio scale is one where the units represent raw score magnitudes, there are equal intervals between adjacent units, and there is an absolute zero point
    - Highest level of measurement
    - All the properties of the interval scale, and has an absolute zero point
    - Examples of ratio scales include reaction time, length, weight, age, frequency of event
    - Can perform all mathematical operations usually associated with numbers
#### Measurement Scales in the Behavioral Sciences
- In behavioral sciences, many scales used are often treated as though they are interval scales, without establishing that the scale does possess equal intervals between adjacent units
#### Continuous and Discrete Variables
- `continuous variable`: one that theoretically can have an infinite number of values between adjacent units on the scale
- `discrete variable`: one in which there are no possible values between adjacent units on the scale
- Weight, height, and time are examples of continuous variables
- "Number of children in a family" is a discrete variable, no half children exist
- Characteristic of discrete variable is that they change in fixed amounts, with no intermediate values possible
#### Real Limits of a Continuous Variable
- Since continuous variable may have infinite number of values between adjacent units, all measurements on continuous variables are *approximate*
- `real limits of a continuous variable`: values that are above or below the recorded value by one-half of the smallest measuring unit of the scale
    - For example, if our variable is weight and our smallest unit is 1lb, assuming a value of 180, the *lower real limit* would be 179.5 and the *upper real limit* would be 180.5
    - If smallest unit was .1lb, then lower limit would be 179.95 and upper limit would be 180.05
#### Significant Figures
- In physical sciences, usually follow the practice of carrying the same number of significant figures as are in the raw data
- This is not usually the case in the behavioral sciences, which typically reports data to two or three decimal places, regardless of source data
- Standard practice is to carry all intermediate calculations to two or more decimal places that will be reported in the final answer
#### Rounding
- Rounding rules are usually straightforward
    - If decimal remainder is greater than 1/2, round up
        - Ex: 18.497 -> 18.5
    - If decimal remainder is less than 1/2, round down
        - Ex: 18.447 -> 18.4
    - If decimal remainder is equal to 1/2, round up if last digit is odd, otherwise, round down
        - Ex: 18.45 -> 18.4
        - Ex: 18.35 -> 18.4
#### Exponents
- Remember with exponents that a negative number raised to an even power is even, raised to an odd power is negative
- For calculator, need to put the negative number in parentheses, ex: `(-1)^3`
- For negative exponents, ex: `2^(-3)`, this is the same as `1/(2^3)`
    - Negative exponent means to take the reciprocal of the number
    - So for a fraction raised to a negative power, ex: `(2/3)^(-4)` becomes `(3/2)^4`
- Fractional exponents, ex: `25^(1/2)` becomes the square root of 25
    - Ex: `25^(1/3)` becomes the cubed root of `25^1`
