def safe(l: list[int]): 
  prev = l[0]
  trend = None

  for num in l[1:]:
    dif = num - prev

    if dif == 0:
      return False, l

    if trend is None:
      if dif > 0:
        trend = 'i'  # Increasing
      elif dif < 0:
        trend = 'd'  # Decreasing

    elif (trend == 'i' and dif < 0) or (trend == 'd' and dif > 0):
      return False, l

    if abs(dif) < 1 or abs(dif) > 3:
      return False, l
    prev = num 

  return True, l


total_safe = 0

with open("2/input.txt", "r") as file:
  lines = file.readlines()

  for line in lines:
    parsed = [int(i) for i in line.rstrip("\n").split(" ")]
    res, l = safe(parsed)

    if res: 
      total_safe += 1

print(total_safe)
