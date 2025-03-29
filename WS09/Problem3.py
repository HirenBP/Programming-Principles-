def distance(ref1, ref2):
  x1 = ord(ref1[0]) - ord('A')
  y1 = int(ref1[1:])
  x2 = ord(ref2[0]) - ord('A')
  y2 = int(ref2[1:])

  return 0.5 * ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def is_valid(ref):
  if not ref:
    return False
  if not ref[0].isupper():
    return False
  for char in ref[1:]:
    if not char.isdigit():
      return False
  return True

def total_distance(trip):
  refs = trip.split()
  dist = 0
  for i in range(len(refs) - 1):
    ref1 = refs[i]
    ref2 = refs[i + 1]
    if not is_valid(ref1) or not is_valid(ref2):
      print("Bad reference:", ref1 if not is_valid(ref1) else ref2)
      exit()
    dist += distance(ref1, ref2)
  return dist

trip = input("Enter trip map references: ")
print("Total distance =", "{:.2f}".format(total_distance(trip)),"km")