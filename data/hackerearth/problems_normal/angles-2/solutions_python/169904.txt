first_line = [int(x) for x in raw_input().split()]
number_of_angles_raju = first_line[0]
number_of_angles_rani = first_line[1]
raju_angles = [int(x) for x in raw_input().split()]
rani_angles = [int(x) for x in raw_input().split()]

for rani_angle in rani_angles:
    found = False
    for raju_angle in raju_angles:
        for i in range(1, 360):
            _rem = (raju_angle * i) % 360
            if _rem == rani_angle or (_rem == 0 and rani_angle == 360):
                found = True
                break
            if _rem == 0:
                found = False
                break
        if found:
            break

    if found:
        print('YES')
    else:
        print('NO')