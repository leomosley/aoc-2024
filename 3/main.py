def get_mul(string: str, index: int):
  if index < 0 or index >= len(string):
    return None, index

  while index < len(string) and string[index] != "(":
    index += 1

  if index >= len(string) or string[index] != "(":
    return None, index

  index += 1
  start_index = index

  while index < len(string) and string[index] != ")":
    index += 1

  if index >= len(string) or string[index] != ")":
      return None, index

  content = string[start_index:index]
  parts = content.split(",")
  if len(parts) != 2:
    return None, index

  try:
    n1, n2 = parts
    x = int(n1.strip())
    y = int(n2.strip())
  except ValueError:
    return None, index

  if not (1 <= x <= 999 and 1 <= y <= 999):
    return None, index

  return (x * y), index + 1

with open("3/input.txt", "r") as file:
  content = file.read()

  i = 0
  total = 0
  while i < len(content) - 3:
    if content[i:i + 3] == "mul":
      result, new_index = get_mul(content, i + 3)
      if result is not None:
        total += result
        i = new_index
        continue
    i += 1

  print(total)
