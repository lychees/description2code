first_line = [int(x) for x in raw_input().split()]

repo = {}


def count_minimum(strength):
    if repo.get(strength) is not None:
        return repo.get(strength)

    if strength == 1:
        return 0
    if strength % 3 != 0 and strength % 2 != 0:
        count1 = count_minimum(strength - 1) + 1
        count2 = None
    elif strength % 3 == 0 and strength % 2 == 0:
        count1 = count_minimum(strength / 3) + 1
        count2 = count_minimum(strength / 2) + 1
    elif strength % 3 != 0 and strength % 2 == 0:
        count1 = count_minimum(strength / 2) + 1
        count2 = count_minimum(strength - 1) + 1
    elif strength % 3 == 0 and strength % 2 != 0:
        count1 = count_minimum(strength / 3) + 1
        count2 = count_minimum(strength - 1) + 1
    if count2 is None:
        repo[strength] = count1
        return count1
    if count1 < count2:
        repo[strength] = count1
        return count1
    else:
        repo[strength] = count2
        return count2


for i in range(first_line[0]):
    enemy_strength = [int(x) for x in raw_input().split()][0]
    print count_minimum(enemy_strength)