# Creating a set
my_set = {"apple", "banana", "cherry"}
print(my_set)

# Creating a set using the set() constructor
another_set = set(("orange", "grape"))
print(another_set)

# Adding elements to a set
my_set.add("date")
print(my_set)

# Performing set operations (union, intersection, difference)
set_A = {1, 2, 3, 4}
set_B = {3, 4, 5, 6}

union_set = set_A | set_B  # or set_A.union(set_B)
print(f"Union: {union_set}")

intersection_set = set_A & set_B  # or set_A.intersection(set_B)
print(f"Intersection: {intersection_set}")
