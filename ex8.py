## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass
## ??
class Dog(Animal):
    def __init__(self, name):
        ## ??
        self.name = name
## ??
class Cat(Animal):
    def __init__(self, name):
        ## ??
        self.name = name
## ??
class Person(object):
    def __init__(self, name):
        ## ??
        self.name = name
        ## Person has-a pet of some kind

self.pet = None 28
## ??
class Employee(Person):

    def 33

__init__(self, name, salary):
## ?? hmm what is this strange magic? super(Employee, self).__init__(name) ## ??
self.salary = salary
36 37
38 ## ??
39 class Fish(object):
40 pass
41
42 ## ??
43 class Salmon(Fish):
44 pass
45
46 ## ??
47 class Halibut(Fish):
48 pass
49
50
51 ## rover is-a Dog
52 rover 53
54 ## ??
55 satan
56
= Dog("Rover")
= Cat("Satan")
57 ## ??
58 mary = Person("Mary")
59
60 ## ??
61 mary.pet = satan
62
63 ## ??
64 frank = Employee("Frank", 120000)
65
66 ## ??
67 frank.pet = rover
68
69 ## ??
70 flipper = Fish()
71
IS-A, HAS-A, OBJECTS, AND CLASSES 195
 72 ## ??
73 crouse = Salmon()
74
75 ## ??
76 harry = Halibut()