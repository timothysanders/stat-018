# Unit 1 Part A - What are Statistics and Why are they Needed?

## Reading Notes
### Chapter 1: Statistics and Scientific Method
#### Introduction
- How can we find out the truth about the world or ourselves in some manner?
- Much of our lives are spent seeking and acquiring the truth
#### Methods of Knowing
- Typically four different methods of acquiring knowledge, or knowing
- **Authority**
  - Something is considered to be true because of tradition or someone distinguished says so
  - For example, our professor said so, therefore it is true
  - This method is seen as being in disfavor, but it is still used a lot because we may not have time/expertise to validate something
    - Examples being that electrons exist because physics authorities tell me so, I believe that smoking is bad because the surgeon general tells me so
- **Rationalism**
  - Uses reasoning alone to arrive at knowledge
  - Assumption is that if the premises are sound and reasoning is done correctly (according to logic), then conclusions will lead to truth
  - Reasoning process is extremely important, but there are situations where it is not completely adequate to determine truth
  - Relying on reason/rationalism alone cannot help us if we do not know if the premises are sound
- **Intuition**
  - Meaning, the sudden insight or clarifying idea that springs into consciousness all at once
  - Intuitive ideas may often occur after conscious reasoning has failed and the individual has put the problem aside for some time
  - Intuition is still a mysterious process, we don't understand much about why it happens
  - Think how you go to sleep and then wake up knowing the answer to your problem
- **Scientific Method**
  - The scientific method incorporates reason, but does not rely only on it. It also incorporates intuition
  - Main differentiator is the scientific method's reliance on objective assessment
  - Experiments are conducted where a hypothesis is established (either through rationalism or intuition) and then an experiment is designed to objectively test the hypothesis
  - Data collected is then analyzed and the hypothesis is either supported or rejected
  - Scientific methodology means any assertions about reality must be demonstrated before they are considered truth
  - This method may be slow, but does have a high probability of yielding truth over the long run
#### Definitions
- `population`: population is a complete set of individuals, objects, or scores that the investigator is interested in studying. 
- `sample`: a sample is a subset of a population. 
- `variable`: a variable is any property or characteristic of some event, object, or person that may have different values at different times depending on the conditions.
- `independent variable`: the independent variable in an experiment is the variable that is systematically manipulated by the investigator.
- `dependent variable`: the dependent variable in an experiment is the variable that the investigator measures to determine the effect of the independent variable.
- `data`: the measurements that are made on the subjects of an experiment are called data.
- `statistic`: a statistic is a number calculated on sample data that quantifies a characteristic of the sample
- `parameter`: a parameter is a number calculated on population data that quantifies a characteristic of the population
#### Scientific Research and Statistics
- Scientific research can be divided into two categories: observational studies and true experiments
- **Observational Studies**
  - No variables are actively manipulated by the investigators
  - Because of this, observational studies cannot determine causality
  - Three subcategories
    - Naturalistic observation
      - major goal is to obtain an accurate description of the situation being studied
    - Parameter estimation
      - conducted on samples to estimate the level of one or more population characteristics
      - Examples being surveys, marketing research, public opinion polling
    - Correlational studies
      - Focused on two or more variables to determine whether they are related
      - Example being, measuring body fat and blood pressure for adults over 30, do these variables have a relationship?
- **True Experiments**
  - In this research, attempt is made to determine whether changes in one variable cause changes in another variable
  - Independent variable is manipulated and its effect on the dependent variable is studied
  - Can have more than one independent variable and more than one dependent variable, though simplest is one of each
#### Random Sampling
- In research, data is usually collected from a sample, rather than the entire population
- Ideally, data would be collected on the entire population, but this is usually far too costly
- Samples however, should be random, which means that the laws of probability apply to the data and help achieve a representative sample of the population
  - If we can achieve a representative sample, we can say that our results should apply to the population
#### Descriptive and Inferential Statistics
- Statistical analysis is divided into two areas, descriptive statistics and inferential statistics
- Both of these involve analyzing data
- **Descriptive Statistics**
  - concerned with the techniques that are used to describe or characterize the obtained data
  - Done for the purpose of describing or characterizing data
  - Other descriptive statistics might involve the *central tendency* or the *variability* or the *shape* of the data
- **Inferential Statistics**
  - involves techniques that use the obtained sample data to infer to populations
  - Embraces techniques that allow one to use obtained sample data to draw conclusions/make inferences about populations
  - This is the more complicated part of statistical analysis, involves probability and inference tests, like *Student's t test* and *analysis of variance*
#### Using Computers in Statistics
- Usage of computers in statistics has grown greatly, almost all research data in behavioral sciences are analyzed by computer programs
- Computers can save time and labor, minimize the chance of errors, allow easy display of data, etc. 
#### Statistics and the "Real World"
- Statistics has very important and practical applications to real life

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

## Video Notes
### Video 1: Crash Course Statistics Preview
- Video link: https://youtu.be/zouPoc49xbk
- Statistics are everywhere!
  - Sports, lottery, etc.
  - Insurance rates, research study effectiveness
  - Marketing, stocking, pricing, etc.
  - Siri, Alexa, etc.
- Statistics are meant to help find the truth, to find simplicity in complexity
- Statistics are about our world and the people in it 
### Video 2: What is Statistics
- Video link: https://youtu.be/sxQaBpKfDRk
- Why do we use statistics and how?
- Statistics is about making sense of data
- "Field of statistics" - study and practice of analyzing data
- "Statistics" - facts about, or summaries of data
- "Proxy" - something related to what we want to measure, but isn't exactly what we want to measure
- What can statistics do?
  - Statistics are tools that can help us make determinations about data in the world
  - We need to understand how to use the tools at our disposal
- Descriptive vs inferential statistics
  - Descriptive
    - usually includes things like where the middle of the data is (measures of central tendency) and measures of how spread out the data is
    - make data we get more digestible
  - Inferential
    - Allow us to make conclusions beyond the data we have access to
    - Lets us test an idea or hypothesis
    - Allows us to make these decisions when we have uncertainty 
### Video 3: Mathematical Thinking
- Video link: https://youtu.be/tN9Xl1AcSv8
- Statistics are math
- Mathematical thinking means seeing beyond our "gut thinking"
- Once numbers get extremely large, we lose our ability to easily reason about them
- Can start to have reference points for larger numbers
- Scientific notation can be helpful for calculating big numbers, but exponents can be non-intuitive
- Law of truly large numbers
  - If you have extremely large numbers, you eventually have very unlikely things that can happen
- Law of very small numbers
  - Worth taking time to put small numbers in context
- Thinking mathematically means asking questions about the world around us and using numbers to think about the answers
### Video 4: Populations and Samples
- Video link: https://youtu.be/eIZD1BFfw8E
- Population vs sample
- population (`N`)
  - Collection of all items of interest to our study
  - Numbers obtained when working with a population are called "parameters"
  - Populations are hard to define and hard to observe in real life
- Sample (`n`)
  - A subset of the population
  - Numbers obtained when working with a sample are called "statistics"
  - Easier to contact, less time-consuming, less costly
- Random sample
  - Collected when each member is chosen by chance (equally likely)
- Representative sample
  - Subset of population which accurately reflects the entire population
- After you have some experience, you can recognize if a sample is representative
- Statistical tests are also capable of working with incomplete data
### Video 5: Descriptive and Inferential Statistics
- Video link: https://youtu.be/SFPGVTThJNk
- Statistics is science of collecting and analyzing data
- Sampling methods
  - How we collect our data
  - Extremely important area as the rest of our statistical process depends on having a good sample
- Descriptive statistics
  - Summarizing or highlighting important aspects of our data
- Inferential statistics
  - Making predictions from our data
- Additional topics
  - When to apply a particular formula or method?
  - Probability
  - etc.


## Population and Samples Quiz
#### Question 1
- Text: In terms of a Research Study, the Population is:
  - b. Defined by the researcher
  - c. The entire group to which the researcher wishes to generalize results
- Answer
  - f. Both b and c are correct
#### Question 2
- Text: In terms of a research study, the sample is:
  - b. a subset of the population
  - c. the group that participates in the study
- Answer
  - e. both b and c
#### Question 3
- Text: A researcher investigates the effects of Drug A on ADHD Symptoms in elementary school children.  The researcher selects 100 children who attend Longden Elementary School who have been diagnosed with ADHD.  The Population in this example consists of:
  - d. all elementary school children who have been diagnosed with ADHD
- Answer
  - d. all elementary school children who have been diagnosed with ADHD
#### Question 4
- Text: A researcher investigates the effects of Drug A on ADHD Symptoms in elementary school children.  The researcher selects 100 children who attend Longden Elementary School who have been diagnosed with ADHD.  The Sample in this example consists of:
  - c. the 100 children who have been selected to participate in the study
- Answer
  - c. The 100 children who have been selected to participate in the study
#### Question 5
- Text: A parameter is:
  - a. A numerically measurable characteristic of the population
  - c. represented by Greek letters
- Answer
  - e. both a and c are correct
#### Question 6
- Text: A statistic is:
  - b. a numerically measurable characteristic of the sample
  - d. represented by the roman alphabet
- Answer
  - f. both b and d are correct
#### Question 7
- Text: The most important issue for a sample is:
  - d. it is representative of the population
- Answer
  - d. it is representative of the population
#### Question 8
- Text: A random sample is a sample in which:
  - c. each and every member of the population has an identically equal probability of being selected
- Answer
  - c. each and every member of the population has an identically equal probability of being selected
#### Question 9
- Text: A convenience sample is a sample in which
  - b. Participants are selected by selecting anyone able and willing to participate who qualifies for the study
- Answer
  - b. Participants are selected by selecting anyone able and willing to participate who qualifies for the study
#### Question 10
- Text: A random sampling process usually results in a random sample
  - False
- Answer
  - False
#### Question 11
- Text: Most samples used in research are most often
  - d. convenience samples
- Answer
  - d. convenience samples
#### Question 12
- Text: A true random sample is relatively easy to obtain
  - False
- Answer
  - False
#### Question 13
- Text: A true random sample is virtually impossible to obtain
  - True
- Answer
  - True
#### Question 14
- Text: Convenience samples are
  - b. are fine as long as they are representative of the population in terms of the variables under investigation
- Answer
  - b. are fine as long as they are representative of the population in terms of the variables under investigation
#### Question 15
- Text: Volunteer bias refers to the fact that
  - a. People who volunteer to participate in a research study may differ in systematic ways from people who do not volunteer to participate. 
  - b. People who do not volunteer to participate in a research study may differ in systematic ways from people who do volunteer to participate. 
- Answer
  - d. both a and b are correct
#### Question 16
- Text: A systematic sample is a special type of a random sample
  - False
- Answer
  - False
#### Question 17
- Text: The Greek letter Mu (μ) would be used to designate
  - a. a population parameter
- Answer
  - a. a population parameter
#### Question 18
- Text: The Roman alphabet letter 's' would be used to designate
- Answer
  - d. a sample statistic
#### Question 19
- Text: Why are samples necessary
  - Incorrect: They are easier to obtain than populations
- Answer
  - d. it is never possible to obtain the entire population
#### Question 20
- Text: Fifty bottles of water were randomly selected from a large collection of bottles in a company's warehouse. These fifty bottles are referred to as the
  - Sample
- Answer
  - Sample
#### Question 21
- Text: Specifically, the greek letter Mu (μ) represents
  - Population mean
- Answer
  - Population mean
#### Question 22
- Text: Specifically, the roman letter X with a bar over it represents
  - Sample mean
- Answer
  - Sample mean
#### Question 23
- Text: Specifically, the greek letter sigma squared (σ^2) represents
  - population variance
- Answer
  - population variance
#### Question 24
- Text: Specifically, the roman letter s squared (s^2) represents
  - Sample variance
- Answer
  - sample variance
#### Question 25
- Text: Specifically, the greek letter sigma (σ) represents
  - Population standard deviation
- Answer
  - population standard deviation
#### Question 26
- Text: Specifically, the roman letter s represents
  - Sample standard deviation
- Answer
  - Sample standard deviation
#### Question 27
- Text: A researcher investigates the effects of listening to music on test performance in college students.  The researcher selects 50 Psychology majors enrolled at Pasadena city College students to participate in the study.  Most strictly, the population in this example consists of:
  - Incorrect: All college students
  - Incorrect: None of these
  - Incorrect: All psychology majors enrolled at Pasadena City College
- Answer
  - a. All Pasadena City College students
#### Question 28
- Text: A researcher investigates the effects of listening to music on test performance in college students.  The researcher selects 50 Psychology majors enrolled at Pasadena city College students to participate in the study.  The Sample in this example consists of:
- Answer
  - The 50 students selected to participate in the study
## Variables Quiz
#### Question 1
- Text: What is the most basic and defining characteristic of a variable?
- Answer: (4) "The Values of a Variable Must Vary"
#### Question 2
- Text: A Continuous Variable is a variable that
- Answer: (c) "Can potentially take on an infinite number of values"
#### Question 3
- Text: A Discrete Variable is a variable that
- Answer: (d) Alternatives (a) and (b) are both correct
#### Question 4
- Text: A Dichotomous Variable is a Variable that
- Answer: (a) Can only take on two values
#### Question 5
- Text: A Polychotomous Variable is a Variable that
- Answer: (b) Can only take on a limited number of values, but more than two values
#### Question 6
- Text: A Quantitative Variable:
- Answer: (d) Both (a) and (c)
  - (a) - Differs in amount
  - (c) - Can be continuous or discrete
#### Question 7
- Text: A Qualitative Variable
- Answer: (b) Differs in Kind
#### Question 8
- Text: An Independent Variable (IV) is a Variable that is
- Answer: (a) Manipulated
#### Question 9
- Text: A Between-Subjects Independent Variable is an Independent Variable for which:
- Answer: (a) Different, Unrelated Individuals in Each of the Different Levels of the IV
#### Question 10
- Text: A Within-Subjects Independent Variable is an Independent Variable for which:
- Answer: (e) Alternatives (b), (c), and (d) are all correct
  - (b) Same Individuals in Each of the Different Levels of the IV
  - (c) Different, but Genetically Related Individuals in Each of the Different Levels of the IV
  - (d) Different Individuals in Each of the Different Levels of the IV; however, the individuals in each level have been Matched on a Variable that is Related to the Dependent Variable
#### Question 11
- Text: A Dependent Variable (DV) is a Variable that is: 
- Answer: (b) Measured
#### Question 12
- Text: A Predictor Variable is a Variable that is:
- Answer: (b) Measured
#### Question 13
- Text: A Criterion Variable is a Variable that is:
- Answer: (b) Measured
#### Question 14
- Text: A Confounding Variable is a Variable that:
- Answer: (f) Both (c) and (d) are correct)
  - (c) May have an effect on the results, however, the researcher is not interested in the effect of this variable
  - (d) Varies Systematically with the levels of the Independent Variable (IV)
#### Question 15
- Text: An Extraneous Variable is a Variable that:
- Answer: (e) May or May Not Vary Systematically with the levels of the Independent Variable (IV)
  - Potentially (e)
#### Question 16
- Text: For Independent Variables, the operational definition defines: 
- Answer: (d) How the variable is manipulated
#### Question 17
- Text: For Dependent Variables, the operational definition defines:
- Answer: (c) How the variable is measured
#### Question 18
- Text: For Predictor Variables, the operational definition defines:
- Answer: (c) How the variable is measured
#### Question 19
- Text: For Criterion Variables, the operational definition defines:
- Answer: (c) How the variable is measured
#### Question 20
- Text: The Variable ‘Happiness’ is operationally defined as one-half of the participants are randomly assigned to listen to “upbeat” music and one-half of the participants are randomly assigned to listen to “depressing” music.  The operational definition is an operational definition of which of the following types of variables: 
- Answer: (d) Between-Subjects Independent Variable
#### Question 21
- Text: The Variable ‘Happiness’ is operationally defined as participants rating how happy they feel on a scale of 1 (Extremely Unhappy) to 7 (Extremely Happy).  The operational definition is an operational definition of which of the following types of variables: 
- Answer: (c) Dependent Variable
#### Question 22
- Text: The Variable ‘Happiness’ is operationally defined as pairs of monozygotic twins randomly assigned such that within each twin pair, one cotwin is randomly assigned to listen to “upbeat” music and the other cotwin is randomly to listen to “depressing” music.  The operational definition is an operational definition of which of the following types of variables: 
- Answer: (e) Within-Subjects Independent Variable
#### Question 23
- Text: The Variable ‘Happiness’ is operationally defined as the following.  Prior to the study, all participants are administered a standardized Happiness Inventory and Total Scores are calculated.  Participants are matched according to their Total Happiness Scores such that matched pairs are created.  Within each matched pair, one individual is randomly assigned to listen to “upbeat” music and the other individual is randomly to listen to “depressing” music.  The operational definition is an operational definition of which of the following types of variables:
- Answer: (e) Within-Subjects Independent Variable
#### Question 24 - 27
- Text: Scenario 1: A researcher investigates the effects of Caffeine (350 mg, 0 mg) and Color of Paper (Red, Green, Yellow) on Test Performance.  Two-hundred college undergraduates are randomly assigned to drink 350 mg of caffeine (n = 100) or to drink 0 mg of caffeine (n = 100).  All participants read three passages and took a 50-item multiple choice exam on each passage.  Each multiple-choice exam was printed on one of three colors (Red, Green, and Yellow).  Each participant took one exam printed on each color of paper.  Counterbalancing was used such that across all participants, each exam was printed on each color of paper.  The order of passages and exams was also counterbalanced using complete counterbalancing.  The mean total exam scores were compared for each of the six experimental conditions.  The researcher believes that time of day might affect the results and therefore conducted each experimental condition at 8:00 am in the morning.
  - Question 24 Text: The variable Time of Day is a:
  - Question 24 Answer: (f) Possible Confounding Variable
  - Question 25 Text: The variable Caffeine is a:
  - Question 25 Answer: (d) Between-Subjects Independent Variable
  - Question 26 Text: The variable Color of Paper is a:
  - Question 26 Answer: (e) Within-Subjects Independent Variable
  - Question 27 Text: The variable Test Performance is a:
  - Question 27 Answer: (c) Dependent Variable
#### Question 28
- Scenario 2: A researcher investigates the relationship between Caffeine Consumption and Academic Performance.  Five-hundred individuals participate in this study.  Each participant is asked to estimate the number of cups of coffee they drink per week and is asked to self-report their cumulative college GPA.  The researcher then calculates a measure of association in order to determine the strength and direction of the relationship between Caffeine Consumption and Academic Performance.  Furthermore, the researcher hopes to be able to predict Academic Performance from Caffeine Caffeine Consumption. 
- Text: Identify the following three from Scenario 2: (1) Caffeine Consumption is a: (2) Academic Performance is a: (3) The Design is a:
- Answer: (1) Predictor Variable, (2) Criterion Variable, Correlational Study
