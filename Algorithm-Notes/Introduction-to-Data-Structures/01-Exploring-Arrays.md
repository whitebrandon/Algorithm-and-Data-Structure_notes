# INTRO TO DATA STRUCTURES | PART ONE: Exporing Arrays

a COURSE BY TREEHOUSE
taught by Pasan Premaratne

PY CODE by Brandon White | white.brandonsean@gmail.com

## INTRODUCTION

### Objectives
1. Explore how arrays work
2. Learn what the common operations of an array are
3. Learn what the run times associated with those common operations are
4. Build a data type called a linked list
5. Explore ways to store data
6. Explore what motivates us to build specific types of structures
7. Expore the pros and cons of those structures
8. Explore four common operations:
    1. Accessing a value
    2. Searching for a value
    3. Inserting a value
    4. Deleting a value
9. Explore how the choice of data structure potentially influences the run tim of an algorithm

## ARRAY BASICS

[Arrays](https://en.wikipedia.org/wiki/Array_data_structure) are a fundamental data structure and can be used to represent a collection of values.

#### **Arrays are used as building blocks to create even more custom data types and structures**.
  * A **string**, in most programming languages, is just a bunch of characters stored in a particular order in an array.

### What is a [Data Structure](https://en.wikipedia.org/wiki/Data_structure)?
A way of storing data when programming. It is the collection of values and the format they are stored in, the relationships between the values in the collection as well as the operations applied on the data stored in the structure.
  * In general, a collection of values where each value is referenced using an index (or key).

In languages like Swift and Java, arrays are **homogeneous structures**, which means they _can only contain values of the same type_. 
  * If you use an array to store integers in Java, it can **only** store integers.

In other languages like Python and JavaScript, arrays are **heterogeneous structures**, which means they _can contain values of different types_.

The fundamental concept of the array is the index. It is used for every operation on the array.
  * Accessing values
  * Inserting values
  * Updating values
  * Deleting values

In Python an array is best represented as a **list**. 
  * **NOTE**: In computer science a list is actually a different structure than an array, generally it is called a **linked list**.

An array is a contiguous data structure. 

### Contiguous Memory
Blocks of memory situated right beside each other with no gaps.

In a _noncontiguous_ data structure, the structure stores a values as well as a **reference** to where the next value is.  
To retrieve that next value the langage has to follow that reference (pointer) to the next block of memeory.  
This adds overhead which increases the runtime of common operations.

* In languages where arrays are homogeneous, when an array is created, **because the value is know to the language compiler**, the language can choose a contiguous block of memory that fits the array's size and values created.

* In languages where arrays are heterogeneous, when an array is created, the language allocates contiguous memory and stores in it, not the values, but a reference to the value that's stored elsewhere in memory. 

## ARRAY CHARACTERISTICS AND STORAGE

### PYTHON:

<kbd>Python defines both an array and a list type and while they look and feel similar to one another they have their own uses. The array.array class in Python is a thin wrapper around a C array and this introduces some limitations. For example, Python arrays are homogeneous and can only hold data of a single kind. The type does take up much less space in memory than Python lists however so in general you would use an array if space was a concern or if you wanted to expose some C functionality.</kbd>

<kbd>As mentioned in the course, Python lists are the more frequently used type and the de facto representation of an array like structure. They are a heterogeneous and contiguous data structure.</kbd>

## ACCESSING A VALUE IN AN ARRAY

## ARRAY SEARCH, INSERT AND DELETE

## OPERATIONS ON ARRAYS