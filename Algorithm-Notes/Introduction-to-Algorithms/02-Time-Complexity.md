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

_n represents the number of values in the series_

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
  * big O is also referred to the "Upper Bounds" of the algorithm, which means big O measures how the algorithm performs in the worst case scenario.

### Big O Variables
  * O(n) - Linear Search - The worst case run time is equal to the size of the data set (if n is 5 run time is 5, is n is 1000 run time is 1000)
    * Any time you know a problem involves reading every item in a list, then that it a linear run time.
  * O(log n) - Binary Search - Logarithmic Time - The worst case run time increases logarithmically as the size of the data set increases.
    * A logarithm is the inverse(opposite) of an exponent. An example of a logarithms is log<sub>2</sub>(8) = 3. The base is 2, the argument is 8, and the answer is 3. You divide the argument **8** by the base of **2**, **3** times before you get 1, the base. 8 / 2 (**1st x**) = 4 / 2 (**2nd x**) = 2 / 2 (**3rd x**).
    * In binary search, the base is 2. So log n could be written as log<sub>2</sub>(n). So if n (size of data set) is 8, then the worst case scenario is it will take 3 tries to find the value. If n is 16, then worst case scenario is 4 tries. If n is 10,000, then the worst case scenario is 13.28 tries (so either 13 or 14 tries).
    * Logarithmic run times are called sublinear, and are preferred to linear run times. You can calculate (log n) like so: (<kbd>(ln(n)</kbd>) / (<kbd>ln(2)</kbd>). Calculate log of n in JS like this: `Math.log(n)/Math.LN2`.


## CONSTANT AND LOGARITHMIC TIME

### More Big O Variables
  * O(1) - Constant Time - The runtime of the algorithm is independent of the size of the data set. If n is 1 or 1 million it takes the same amount of time to execute the algorithm. 
    * An example of this would be reading the element from a known position in an array (ie. If the days of the week were placed in an array, with Sunday being at index 0, selecting the value at the index of 3 would not change even if you were to switch the array to one containing the months in the year as opposed to the days in a week. We're just selectin whatever is at index 3, _Wednesday_ and _April_).

## LINEAR & QUADRATIC TIME

### Why Ever Use Linear Search Over Binary Search?
  Binary search requires that the inputs be sorted, and sorting algorithms have varying complexities. For this reason (in practice), linear search ends up being more performant up to a certain value of n.

### Even More Big O Variables
  * O(n<sup>2</sup>) - Quadratic Time - For any small increase in the value of n, the worst case run time increases significantly.
    * An example. If you were to tell your friend to do as many pushups as they could in thirty seconds and you would match each rep with a set of pushups of your own and each set would match the same amount of reps as your friend's one set. If your friend did five pushups in thirty seconds, you'd have to do twenty-five (five sets of five reps). If your friend did just one more pushup (six), you'd have to do eleven more pushups (thirty-six).  
  * O(n<sup>3</sup>) - Cubic Time - For any small increase in the value of n, the worst case run time increases significantly.
    * Same example as above, but this time if your friend does five pushups, your're doing five sets of five pushups for five rounds (one hundred twenty-five) and if your friend does six, you're doing two hundred sixteen. 

## QUASILINEAR TIME

### Even EVEN More Big O Variables
  * O(n log n) - Quasilinear Time - Given a data set of size n, the algorithm executes a number of operations where each operation runs in <kbd>log n</kbd>(logarithmic) time.
    * Found in Sorting Algorithms (ie. Merge Sort)

## EXPONENTIAL TIME

### Polynomial Run Times
  * O(n<sup>k</sup>): An algorithm is considered to have a polynomial run time if, for a given value of n, it's worst case run time is in the form of n raised to the k power. Examples of this are O(n<sup>2</sup>) and O(n<sup>3</sup>). Algorithms with polynomial run times are considered efficient. All of the above run times are polynomal run times.

  _k is the nummber of operations_

### Exponential Run Times
  * O(k<sup>n</sup>): A run time where the number of operations increases exponentially as the size of the data set increases. Exponential run times are considered inefficient.
    * Brute Force Algorithm:
      * Lock example: A lock with two dials (each dial has a range from 0 to 9 (inclusive of 0 and 9). The lock would have 100 possible combinations. 10<sup>2</sup> is the run time, because there are ten values on each dial, raised to two dials. With just one more dial, the run time is 10<sup>3</sup>, or 1,000 possible combinations.

### Combinatorial or Factorial Run Times
  * O(n!): Run times where as the size of n increases, the number of operations increases by n! where n! is the factorial of n.
    A factorial works like this: 5! = 5 * 4 * 3 * 2 * 1 = 120, 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720
    * Traveling Salesman Problem: Given a list of cities and a distance between each pair of cities what is the shortest possible route that visits each city and returns to the origin city.
      * With 3 cities, we have six routes. With 4 cites, we have twenty-four routes. With 5 cities, we have one-hundred twenty routes.

## DETERMINING COMPLEXITY

### How Do We Determine What the Worst Case Complexity of an Algorithm Is?

* Each step in an algorithm can have a different run time.

Binary Search Analysis (Steps)

  1. Determine the middle position of the list. (Constant Time - O(1))
  2. Compare the element in the middle position to the target element. (Constant Time - O(1))
  3. Current element matches target element (Best Case Scenario).
    * In the best case scenario, binary search's run time is constant time.
  4. If we don't match, split list into sublists. (Logarithmic Time - O(log n))

  The algorithm has, as its upper bound, the same run time as the **least** efficient step in the algorithm.
