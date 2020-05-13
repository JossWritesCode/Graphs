"""
# Earliest Ancestor

This is a take-home coding challenge from a top tech company. The spec is providied verbatim.


## Problem

Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

For example, in this diagram and the sample input, 3 is a child of 1 and 2, and 5 is a child of 4:

```
 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9
```

Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. If the input individual has no parents, the function should return -1.

```
Example input
  6

  1 3
  2 3
  3 6
  5 6
  5 7
  4 5
  4 8
  8 9
  11 8
  10 1
Example output
  10
```

Clarifications:
* The input will not be empty.
* There are no cycles in the input.
* There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
* IDs will always be positive integers.
* A parent may have any number of children.




"""


from graph import Graph


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    family_tree = g.create_graph(ancestors)
    paths = []
    #{1: {3}, 3: {6}, 2: {3}, 6: set(), 5: {6, 7}, 7: set(), 4: {8, 5}, 8: {9}, 9: set(), 11: {8}, 10: {1}}
    helper_function(family_tree, [starting_node], starting_node, paths)

    longest = len(paths[0])
    path_id = paths[0][-1]
    for path in paths:
        # or len is == and last id is lower
        if len(path) > longest or (len(path) == longest and path_id > path[-1]):
            longest = len(path)
            path_id = path[-1]

    if longest == 1:
        return -1
    else:
        return path_id


def helper_function(family_tree, current_path, starting_node, paths):
    flag = False  # we may not recurse
    for person in family_tree:
        if starting_node in family_tree[person]:
            flag = True  # turns out we did recurse
            new_path = current_path + [person]
            helper_function(family_tree, new_path, person, paths)
    if flag is False:  # if we didn't recurse, add this
        paths.append(current_path)


print(earliest_ancestor(test_ancestors, 1), "== 10")
print(earliest_ancestor(test_ancestors, 2), "==-1")
print(earliest_ancestor(test_ancestors, 3), "== 10")
print(earliest_ancestor(test_ancestors, 4), "== -1")
print(earliest_ancestor(test_ancestors, 5), "== 4")
print(earliest_ancestor(test_ancestors, 6), "== 10")
print(earliest_ancestor(test_ancestors, 7), "== 4")
print(earliest_ancestor(test_ancestors, 8), "== 4")
print(earliest_ancestor(test_ancestors, 9), "== 4")
print(earliest_ancestor(test_ancestors, 10), "== -1")
print(earliest_ancestor(test_ancestors, 11), "== -1")


# def find_earliest_ancestors(family_tree):
#   has_ancestor = False

#   for person in family_tree:
#     if person in family_tree[personn]
