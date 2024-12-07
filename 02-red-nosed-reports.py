file_path = "02-reports.txt"

reports = []

with open(file_path, "r") as file:
    for line in file:
        reports.append(list(int(level) for level in line.split()))

# print(reports)

def is_safe(level):
    return ((all(1 <= level[i] - level[i+1] <= 3 for i in range(len(level)-1))) or
            (all(1 <= level[i+1] - level[i] <= 3 for i in range(len(level)-1))))

def is_safe_with_dampner(level):
    if is_safe(level):
        return True
    
    for i in range(len(level)):
        modified_level = level[:i] + level[i+1:]
        if is_safe(modified_level):
            return True

    return False

safe_count = 0
safe_count_mod = 0

for levels in reports:
    check = is_safe(levels)
    if check:
        safe_count += 1
    # print(check)

for level in reports:
    if is_safe_with_dampner(level):
        safe_count_mod += 1
        
print(safe_count)
print(safe_count_mod)


