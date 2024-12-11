with open("4/input.txt", "r") as file:
  lines = file.readlines()

  count = 0
  word = "XMAS"

  for i in range(len(lines)):
    for j in range(len(lines[i])):
      if j + 4 <= len(lines[i]) and lines[i][j:j+4] == word:
        count += 1

      if j - 3 >= 0 and lines[i][j:j-4:-1] == word:
        count += 1

      if i + 4 <= len(lines) and all(lines[i+k][j] == word[k] for k in range(4)):
        count += 1

      if i - 3 >= 0 and all(lines[i-k][j] == word[k] for k in range(4)):
        count += 1

      if i + 4 <= len(lines) and j + 4 <= len(lines[i]) and all(lines[i+k][j+k] == word[k] for k in range(4)):
        count += 1

      if i - 3 >= 0 and j - 3 >= 0 and all(lines[i-k][j-k] == word[k] for k in range(4)):
        count += 1

      if i + 4 <= len(lines) and j - 3 >= 0 and all(lines[i+k][j-k] == word[k] for k in range(4)):
        count += 1

      if i - 3 >= 0 and j + 4 <= len(lines[i]) and all(lines[i-k][j+k] == word[k] for k in range(4)):
        count += 1

  print(count)
