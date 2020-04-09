# INTRO TO ALGORITHMS | PART TWO: Time Complexity

a COURSE BY TREEHOUSE
taught by Pasan Premaratne

PY CODE by Brandon White | white.brandonsean@gmail.com

## EFFICIENCY OF AN ALGORITHM

When measuring the **efficiency** of an algorithm we always want to evaluate how the algorithm performs in a worst-case scenario. We use these as a bench mark, because they can never perform worse than they do in these scenarios.

### Linear Search: Run Time Data
| n | Worst Case Run Time |
|---|---------------------|
| 10 | 10 |
| 100 | 100 |
| 1000 | 1000 |
| 10000 | 10000 |
| 100000 | 100000 |
| 1000000 | 1000000 |

### Binary Search: Run Time Data
| n | Worst Case Run Time |
|---|---------------------|
| 10 | 4 |
| 100 | 7 |
| 1000 | 10 |
| 10000 | 14 |
| 100000 | 17 |
| 1000000 | 20 |

####<i class=­"­ico­n-f­ile­"­></­i> n represents the number of values in the series

### Order of growth: a measure of how much the time taken to execute operations increases as the input size increases (also known as growth rate).
  * Different algorithms grow at different rates, and by evaluating their growth rates, we get a much better picture of their performance.
  * This is the standard way of evaluating an algorithm. 

### Big O: a theoretical definition of the complexity of an algorithm as a function of the size.
  * Big O is a notation used to describe complexity. 
  * An example of complexity written in terms of big O looks like this: **O(n)**
    * O stands for "order of magnitude of complexity"
    * Ex. If it takes 4 tries to find a number using binary search when n is 10. How long does it take when n is 10 million?
      When we use big O for this, the variable used (see Big O variables below) distills that information down so that by reading the variable, you get a big picture view without having to run through data points and graphs.
  * The last part of the big O defintion ("a function of size") means that big O measures complexity as the input size grows. **n** represents the size of the data set.
  * big O is also referred to the "Uppder Bounds" of the algorithm, which means big O measures how the algorithm performs in the worst case scenario.

### Big O Variables
  * O(n) - Linear Search - The run time is equal to the size of the data set (if n is 5 run time is 5, is n is 1000 run time is 1000)
  * O(log n) - Binary Search - Logarithmic Time - The run time increases logarithmically as the size of the data set increases.
    * A logarithm is the inverse(opposite) of an exponent. An example of a logarithms is log_2(8) = 3. The base is 2, the argument is 8, and the answer is 3. You divide the argument **8** by the base of **2**, **3** times before you get 1, the base. 8 / 2 (**1st x**) = 4 / 2 (**2nd x**) = 2 / 2 (**3rd x**).
    * In binary search, the base is 2. So log n could be written as log_2(n). So if n (size of data set) is 8, then the worst case scenario is it will take 3 tries to find the value. If n is 16, then worst case scenario is 4 tries. If n is 10,000, then the worst case scenario is 13.28 tries (so either 13 or 14 tries).
    * Logarithmic run times are called sublinear, and are preferred to linear run times. You can calculate (log n) like so: ((ln(n)) / (ln(2)). 


## CONSTANT AND LOGARITHMIC TIME

### More Big O Variables
  * O(1) - Constant Time - The runtime of the algorithm is independent of the size of the data set. If n is 1 or 1 million it takes the same amount of time to execute the algorithm. 
    * An example of this would be reading the element from a known position in an array (ie. If the days of the week were placed in an array, with Sunday being at index 0, selecting the value at the index of 3 would not change even if you were to switch the array to one containing the months in the year as opposed to the days in a week. We're just selectin whatever is at index 3, _Wednesday_ and _April_).
  * 

## LINEAR & QUADRATIC TIME

## QUASILINEAR TIME

## EXPONENTIAL TIME

## DETERMINING COMPLEXITY