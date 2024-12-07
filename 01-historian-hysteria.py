file_path = "01-location-ids.txt"

left_list = []
right_list = []

with open(file_path, "r") as file:
    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

left_list.sort()
right_list.sort()

print("Left list: ", left_list)
print("Right list: ", right_list)

difference = 0

for i in range(len(left_list)):
    difference += abs(left_list[i] - right_list[i])

print(difference)

right_count = {}

for num in right_list:
    if num in right_count:
        right_count[num] += 1
    else:
        right_count[num] = 1

similarity_score = 0

for num in left_list:
    count = right_count.get(num, 0)
    similarity_score += num * count

print(similarity_score)
