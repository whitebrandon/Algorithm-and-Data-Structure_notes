# INTRO TO ALGORITHMS | PART FOUR: Recursion and Space Complexity

a COURSE BY TREEHOUSE
taught by Pasan Premaratne

PY CODE by Brandon White | white.brandonsean@gmail.com

## RECURSIVE FUNCTIONS

### What is a Recursive Function?
  * A recursive function is one that calls itself.
  * When writing a recursive function you always need a stopping condition. The stopping condition is also known as the **base case**.

## SPACE COMPLEXITY

### What is Space Complexity?
Space complexity is a measure of how much working storage, or **extra** storage, is needed as a particular algorithm grows.
  * Everything we do on a computer takes up space and memory.
  * Space complexity is measured in the worst-case-scenario using Big O notation.

#### Space Complexity of Binary Search
  1. The **iterative** version of binary search has a space complexity of **constant space** || O(1)
  2. The **recursive** version of binary search has a space complexity of **logorithmic** space || O(log n)
    * This is because each time the binary search function is called recursively, the computer has to store in its memory a new sublist in addition to the original list.
      * This depends on the programming language (see [Tail Optimization](https://en.wikipedia.org/wiki/Tail_call)) 

## RECAP

1. Algorithmic thinking is an approach to problem solving that involves breaking a problem down into a clearly defined input and output, along with a distinct set of steps that solves the problem going from input to output.
2. The proper way to define and implement an algorithm.
3. Big O and measuring the time complexity of algorithms.
4. The Linear Search algorithm versus the Binary Search algorithm.
5. Writing algorithmic code through recursion.