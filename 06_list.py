score = [90, 70, 60, 50, 80]
friends = ["Alice", "Bob", "Charlie", "David"]
things = [90, "Alice", True]
yy = [100, 200, 300]

print(score)
print(friends)
print(things)
print(yy)

print(score[0])
print(score[-1])
print(score[-2])
print(friends[1])
print(score[1:3])
print(score[1:])
print(score[:4])

score[0] = 100
print(score)

score.extend(yy)
print(score)
score.append(20)
print(score)
score.insert(1, 30)
print(score)
score.remove(30)
print(score)
score.pop()
print(score)
score.sort()
print(score)
score.reverse()
print(score)
print(score.index(80))
print(score.count(80))
score.clear()
print(score)
