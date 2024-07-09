#Functional prompt Answer
#A function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.
    
    #flatten function processes the input by applying flatten to each item if the input is list and and concatenates the result. 
    #It wraps the input into a list if it is not a list.
def flatten(lst):
    if isinstance(lst, list):
        return sum([flatten(item) for item in lst], [])
    else:
        return [lst]

    #sort_array function for implementing sort
def sort_array(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        less = [x for x in lst[1:] if x < pivot]
        greater = [x for x in lst[1:] if x >= pivot]
        return sort_array(less) + [pivot] + sort_array(greater)

    #Combining the flatten and sort operations
def flatten_and_sort(lst):
    flattened_list = flatten(lst)
    sorted_list = sort_array(flattened_list)
    return sorted_list

print(flatten_and_sort([3, [2, 1], [4, [5, [6]]]]))
print(flatten_and_sort([3,4,7,2,1,0,9,6,]))

#Immutability
    #This is ensured by creating new list at each point of the computation.
    #No changes are made to the original list
#Pure function solution?
    #Yes, the function is pure because it doesn't have any side effects. 
    #It only depends on its input and produces a result without modifying the input.
#Higher-order function?
    #Partly, this solution is a higher order function. 
    #The function 'flatten' and 'sort_array' are not receiving any other function as an argument.
    #They are standalone functions that perform their tasks.
    #The 'flatten_and_sort' function is a higher-order function because it takes another function as an argument.
#Would it have been easier to solve this problem using a different programming style?
    #The functional approach offers clarity and guarantees of immutability and purity
    #While a procedural style may be easier to understand for some users
    #In some cases, a more object-oriented or imperative style might be more appropriate.
#Why in particular is functional programming a helpful paradigm when solving this problem?
    #It promotes code reusability, readability, and maintainability.
    #Functional programming encourages the use of pure functions, which are easier to test and reason about.
    #Functional programming also supports parallel and concurrent programming, which can be more efficient in certain cases.
    #In this problem, functional programming provides a clear and concise solution that is easy to understand and maintain.


#Object Oriented Prompts Solution
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2

class SebulbasPod(Podracer):
    def flame_jet(self, other_podracer):
        other_podracer.condition = "trashed"

#How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
    #Encapsulation: Each Podracer class encapsulates its own attributes and methods.
    #Inheritance: The AnakinsPod and SebulbasPod classes inherit from the Podracer class.
    #Polymorphism: The boost() and flame_jet() methods are overridden in the AnakinsPod and SebulbasPod classes.
    #Abstraction: The Podracer class provides a base structure for the other classes.

#Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
    #No, the use of OOP makes the solution easier to maintain and scale by providing a modular way for extending the functionality. 
    #It also promotes code reusability and encapsulation, which can make it easier to understand and modify the code.
#How in particular did Object Oriented Programming assist in the solving of this problem?
    #Object Oriented Programming allowed for a clear and organized way to structure the data and the behavior of the Podracers.
    #It allowed for easier extension and modification of the Podracer class, making it easier to add new features or change existing behavior.
    #It also promoted code reusability and encapsulation, making it easier to understand and maintain the code.