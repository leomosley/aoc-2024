from collections import Counter

total_dif = 0
left = []
right = []

with open("1/input.txt", "r") as file:
  lines = file.readlines()
  for n, line in enumerate(lines, start=1):
    left.append(int(line[0:5]))
    
    if n == 1000:
      right.append(int(line[-5:]))
    else:
      right.append(int(line[-6:-1]))

left = sorted(left)
right = sorted(right)

# for i in range(len(left)):
#   total_dif += abs(left[i] - right[i])

total_sim_score = 0
right_map = Counter(right)

for num in left:
  if num in right_map:
    m = right_map[num]
  else:
    m = 0

  total_sim_score += num * m

print(total_sim_score)