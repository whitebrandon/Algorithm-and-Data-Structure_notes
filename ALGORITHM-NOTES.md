# INTRO TO ALGORITHMS

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

## Guess the Number (An Example)

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



 

