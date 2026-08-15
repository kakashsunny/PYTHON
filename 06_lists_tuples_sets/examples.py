# Lists, Tuples & Sets Examples and Practice

# 1. List Mutability and Copying
a = [1, 2, 3]
b = a
c = a.copy()
a.append(4)
print("a:", a)  # [1, 2, 3, 4]
print("b:", b)  # [1, 2, 3, 4] (points to same object)
print("c:", c)  # [1, 2, 3] (independent copy)

# 2. Tuple Unpacking and Single-item Tuple
single_tuple = (42,)
print("single_tuple type:", type(single_tuple))

record = ("Alice", 30, "Engineer")
name, age, role = record
print(f"{name} is a {age}-year-old {role}")

# 3. Set Operations for Venn Diagrams
group_a = {"Python", "Java", "C++"}
group_b = {"JS", "Python", "Go"}

print("Union:", group_a.union(group_b))
print("Intersection:", group_a.intersection(group_b))
print("Difference (A - B):", group_a.difference(group_b))

# Practice: Remove duplicates from a list preserving order
def unique_ordered(seq):
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]

raw_list = [1, 2, 3, 2, 1, 4]
print("Unique ordered:", unique_ordered(raw_list))
