arr1 = []
arr2 = []
diff = 0
sim = 0

input = open("input.txt", "r")
lines = input.readlines()

locationCount = len(lines)

for line in lines:
    split = line.split("   ")
    arr1.append(int(split[0].strip()))
    arr2.append(int(split[1].strip()))

arr1.sort()
arr2.sort()

for i in range(locationCount):
    location = arr1[i]
    sim += location * (arr2.count(location))

print(sim)