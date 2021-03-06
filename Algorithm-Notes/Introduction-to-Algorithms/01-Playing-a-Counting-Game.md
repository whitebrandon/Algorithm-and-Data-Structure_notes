# INTRO TO ALGORITHMS | PART ONE: Playing a Counting Game

a COURSE BY TREEHOUSE
taught by Pasan Premaratne

PY CODE by Brandon White | white.brandonsean@gmail.com


## WHAT IS AN ALGORITHM?

### An **algorithm** is a set of steps or instructions for completing a task.
  * In computing, an algorithm is a set of steps a *program* takes to finish a task.

### Examples of Algorithms
  * Recipe
  * Morning routine you take when you wake up
  * Driving directions you follow to get to a destination

### Two Components of Understanding Algorithms
1. **Point One**: There's an established body of know on how to solve particular problems well. And it's important to know what these solutions are so that we don't waste time/resources trying to come up with a new solution that likely won't be as good as or efficient to those that have been more thoroughly reviewed.
2. **Point Two**: Once you know these vetted solutions, it's important to understand *when* to apply them. To do this, one must properly understand the problem at hand.
  * This is *arguably* the most important part of learning about algorithms and data structures. It's a concept refered to as "**Agorithmic Thinking**".

Learning about algorithms gives you a deeper understanding about *complexity* and *efficiency* in programming.

## GUESS THE NUMBER (AN EXAMPLE)

### The Scenario
Two people are playing a number guessing game (after each guess, the player is told whether the guess is correct, too low, or too high). The objective is to take the least amount of tries to guess the number.
  * The number is between 1 and 10. (The number is 3).
    * The first player asks a question. Does the range include 1 and 10? Yes.
      * This is referred to as *establishing the bounds* of the problem. No solution works on every problem, so an important part of algorithmic thinking is to clearly define what the problem set is and clarify what values count as inputs.
    * The first player guesses 1, then 2, then 3. It takes the first player three tries to guess the number.
    * the second player guesses 5, then 2, then 3. It takes the second player three tries to guess the number.
  * A new game with the same range. (The number is 10).
    * The first player guesses 1, then 2, then 3, then 4, 5...9, then 10. It takes the first player ten tries to guess the number.
    * The second player guesses 5, then 8, then 9, then 10. It takes the second player four tries to guess the number.
  * The second round was the first player's worst case scenario. And in terms of strategy, the second player's seems to win the day.
  #### Player Strategies
    The first player's strategy is to guess each number in an ascending order, starting with the lowest possible value in the range.
    The second player's strategy is to start at the midpoint of the range of values, and dismiss half of the values based on the feedback given.
  * In terms of algorithmic thinking (given the players' strategies), the specific value the players search for doesn't seem to matter as much as where that value lies within the range they're given.
    * In the same scenario, but with a range of 1 to 100, and the value falling at the end of that range (100), the first player needs one-hundred tries to get the correct answer, while the second player only needs seven (50, 75, 88, 94, 97, 99, 100).
  * If we pretend that the number of tries is the number of *seconds* it takes the first player and the second player to run through their attempts, this would be a good estimate of how *fast* their solutions are.

## DEFINING AN ALGORITHM

The approaches taken by the first player and second player in the number guessing game are examples of *searching* algorithms.

### Test Case:
  Facebook (as of December of 2019) had [2.45 billion active users](https://blog.hootsuite.com/facebook-demographics/). Let's say you're traveling in a different company and meet someone you want to add on Facebook. You go into the searchbar and type out that person's name. Facebook has to search across 2.45 billion records to find the person you're looking for. What if you searched for a friend and took a couple of hours for Facebook to comb through their records to show you your friend?

### Linear Search
The strategy the first player took is a type of search called [linear search](https://en.wikipedia.org/wiki/Linear_search) (or sequential search, or simple search).

  1. Start at the beginning of a list or range of values
  2. Compare the current value to the target value.
  3. If the current value is the target value, we're done.
  4. If not, we'll move sequentially to next value in range, and repeat step 2.
  5. If the end of the list is reached, then the target value is not in the list. 

The specificity of how this is defined is what makes it an algorithm. An follows a certain set of guidelines and will use the same steps to solve the problem each time it's faced.

1. Guideline 1: An algorithm must have a clearly defined problem statement, input and output.
    * For linear search: problem statment = find a particular value
    * For linear search: input = series of values
    * For linear search: output = value matching the target value
2. Guideline 2: The steps in the algorithm must be in a very specific/particular order.
3. Guideline 3: Each step in the algorithm needs to be distinct.
    * Each step should not be able to be broken down further into substeps.
4. Guideline 4: The algorithm should produce a result.
5. Guildine 5: The algorithm should complete in a finite amount of time.

### Binary Search
The strategy the second player took is a type of search called [binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm) (or half-interval search, logarithmic search, or binary chop).

## EVALUATING LINEAR SEARCH

### Correctness and Efficiency
  1. Correctness: An algorithm is deemed correct if **1**) on every run of the agorithm, against all possible values in the input data, we always get the output we expect (ie. if given an input range of 1 to 10, with a target value of 5, the algorithm should always return 5), and if **2**) for any possible input, the algorithm always terminates, or ends.
    * If these two are not true, then the algorithm isn't correct.
    * In an algorithm textbook, a search for the term *correctness* would lead to mathematical theory. Traditionally, algorithm correctness is proved by mathematical induction (which involves writing what is called a specification and correctness proof).

  2. Efficiency: helps us solve problems faster, and delivers better end user experience in a variety of fields
    1. Time Complexity - a measure of the **running time** of an algorithm.
      * Running Time (definition by example): the run times for the first player in the number guessing game's were {round-one: 3 tries}, {round-two: 10 tries}, {round-three: 100 tries}.
      * Running Time is the amount of time an algorithm takes to run in relation to the size of its input/data set.
    2. Space Complexity - a measure of the storage taken up by an algorithm.

    Good algorithms need to balance between the two to be useful.

### Worst-Case-Scenario

Analyzing how an algorithm runs during its worst-case scenario is useful becasue it indicates that the algorithm will never perform worse than that.

![alt text](../../images/bigOnot-chart.png "Big O Notation Chart")
 
## EVALUATING BINARY SEARCH

**problem statement** = find a target value in a series of values
**input** = a **sorted** series of values
**output** = a position in the input of the value that matches the target value, or some sort of value to indicate that the target value does not exist within the input
  1. Start at the middle position of a list or range of values
  2. Compare the value at the current postition to the target value.
  3. If the current value is the target value, return the value or position of the current value, and end.
  4. If not, is the current value greater than or less than the target value.
  5. If greater than, eliminate all values less than the current value.
  6. If less than, eliminate all values greater than the current value.
  7. Start at the middle of the new list or range of values.
  8. Repeat step 2.
  9. If we reach a sublist of one value and that one value does not match the target value, then the target value is not in the list, and we end the algorithm.

With *linear search* the input does not need to be sorted, but with *binary search* the input has to be sorted.