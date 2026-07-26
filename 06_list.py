# Lists and List Operations

score = [90, 70, 60, 50, 80]
friends = ["Alice", "Bob", "Charlie", "David"]
things = [90, "Alice", True]
yy = [100, 200, 300]

print(score)
print(friends)
print(things)
print(yy)

print(score[0])
print(score[-1])   # Get the last element
print(score[-2])   # Get the second to last element
print(friends[1])
print(score[1:3])  # Get elements from index 1 to 2 (excludes index 3)
print(score[1:])   # Get elements from index 1 to the end
print(score[:4])   # Get elements from the beginning up to index 3 (excludes index 4)

score[0] = 100     # Modify the first element to 100
print(score)

# List Methods
score.extend(yy)     # Append elements from list 'yy' to the end of list 'score'
print(score)
score.append(20)     # Add 20 to the end of the list
print(score)
score.insert(1, 30)  # Insert 30 at index 1 (second position)
print(score)
score.remove(30)     # Remove the first occurrence of 30 from the list
print(score)
score.pop()          # Remove the last element from the list
print(score)
score.sort()         # Sort the list in ascending order
print(score)
score.reverse()      # Reverse the order of the list
print(score)
score.index(80)      # Find the index of 80 (returns the first occurrence if there are multiple)
print(score.index(80)) # Print the index
score.count(80)      # Count how many times 80 appears in the list
print(score.count(80)) # Print the count
score.clear()        # Remove all elements from the list (empty the list)
print(score)