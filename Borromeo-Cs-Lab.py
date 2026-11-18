##Easy
#E1
snacks = []
for i in range(5):
  s = input("Snacks: ")
  snacks.append(s)
print(snacks)

#E2
name = []
n = int(input("How many students?: "))
for i in range(n):
  names = input("Name: ")
  name.append(names)
print(name)
print(len(name), "names stored")

#E3
scores = []
for i in range(5):
  score = int(input("Score: "))
  scores.append(score)
print(scores)


##Average
#A2
scores = []
for i in range(5):
  scores.append(float(input("Score: ")))

total = sum(scores)
average = total / len(scores)
print("total:, ", total)
print("Average:", average)

#A3
count_75_or_higher = 0

scores = []
for i in range(5):
  scores.append(float(input("Score: ")))
  if scores[i] >= 75:
    count_75_or_higher += 1

print(f"{count_75_or_higher} passed out of 5")

#A4
highest_score = 0

scores = []
for i in range(5):
  score = float(input("Score: "))
  scores.append(score)
  if score > highest_score:
    highest_score = score

print(f"Highest: {highest_score}")


##Hard
#H1
def find(items, target):
  for i in range(len(items)):
    if items[i] == target:
      return i
  return -1

members = []
while True:
  member = input("Member (done or stop): ").strip()
  if member.lower() == "done":
    break
  members.append(member)

target = input("Target: ").strip()
index = find(members, target)
if index != -1:
    print(f"{target} is member number {index + 1}.")
else:
    print(f"{target} is not a member.")

#H2
def find(items, target):
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1

titles = []
copies = []

for i in range(3):
    title = input(f"Title: ").strip()
    num_copies = input("Copies: ")
    titles.append(title)
    copies.append(num_copies)

search_title = input("search title: ").strip()
index = find(titles, search_title)

if index != -1:
    print(f"'{titles[index]}' has {copies[index]} copies.")
else:
    print(f"'{search_title}' was not found.")

#H3
def count(items, target):
  count = 0
  for item in items:
    if item == target:
      count += 1
  return count

votes = []
while True:
  vote = input("Vote (done or stop): ").strip()
  if vote.lower() == "done":
    break
  votes.append(vote)

target = input("Target: ").strip()
vote_count = count(votes, target)
print("Candidate:", target)
print(f"{target} got {vote_count} vote(s).")
