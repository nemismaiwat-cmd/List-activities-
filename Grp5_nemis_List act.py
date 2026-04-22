# ========== 1. Basic List Activities ==========
print("=" * 50)
print("1. Basic List Activities")
print("=" * 50)

# Activity 1: Create a List
print("\n Activity 1: Create a List")
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Activity 2: Access Items
print("\n Activity 2: Access Items")
fruits = ["apple", "banana", "cherry"]
print("First item:", fruits[0])
print("Last item:", fruits[-1])

# Activity 3: List Length
print("\n Activity 3: List Length")
colors = ["red", "blue", "green", "yellow"]
print("Number of items:", len(colors))

# ========== 2. Modify Lists ==========
print("\n" + "=" * 50)
print("2. Modify Lists")
print("=" * 50)

# Activity 4: Change Item
print("\n Activity 4: Change Item")
fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"
print(fruits)

# Activity 5: Add Items
print("\n Activity 5: Add Items")
fruits = ["apple", "banana"]
fruits.append("mango")
fruits.insert(1, "grape")
print(fruits)

# Activity 6: Remove Items
print("\n Activity 6: Remove Items")
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
fruits.pop()
print(fruits)

# ========== 3. Looping Through Lists ==========
print("\n" + "=" * 50)
print("3. Looping Through Lists")
print("=" * 50)

# Activity 7: For Loop
print("\n Activity 7: For Loop")
animals = ["dog", "cat", "bird"]
for animal in animals:
    print(animal)

# Activity 8: With Index
print("\n Activity 8: With Index")
numbers = [10, 20, 30]
for index, value in enumerate(numbers):
    print(f"{index} : {value}")

# ========== 4. List Operations ==========
print("\n" + "=" * 50)
print("4. List Operations")
print("=" * 50)

# Activity 9: Check if Item Exists
print("\n Activity 9: Check if Item Exists")
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("'banana' is in the list")

# Activity 10: Sorting
print("\n Activity 10: Sorting")
numbers = [5, 2, 9, 1]
numbers.sort()
print("Ascending:", numbers)
numbers = [5, 2, 9, 1]
numbers.sort(reverse=True)
print("Descending:", numbers)

# Activity 11: Copy List
print("\n Activity 11: Copy List")
list1 = ["a", "b", "c"]
list2 = list1.copy()
print("list1:", list1)
print("list2:", list2)
