def safe(l: list[int]) -> bool:
  prev = l[0]  
  trend = None

  for num in l[1:]:  
    dif = num - prev

    if dif == 0:
      return False

    if trend is None:
      if dif > 0:
        trend = 'i'  
      elif dif < 0:
        trend = 'd'  

    elif (trend == 'i' and dif < 0) or (trend == 'd' and dif > 0):
      return False
    
    if abs(dif) < 1 or abs(dif) > 3:
      return False

    prev = num  

  return True

def safe_with_dampener(l: list[int]) -> bool:
  if safe(l):
    return True

  for i in range(len(l)):
    temp = l[:i] + l[i + 1:]  
    if safe(temp):
      return True

  return False

total_safe = 0

with open("2/input.txt", "r") as file:
  lines = file.readlines()

  for line in lines:
    parsed = [int(i) for i in line.rstrip("\n").split(" ")]
    if safe_with_dampener(parsed):
      total_safe += 1

print(total_safe)