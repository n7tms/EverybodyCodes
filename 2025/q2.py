# Quest 2

A = [143,53]

R = [0,0]

def multiply(a: list, b: list) -> list:
    x1, y1 = a
    x2, y2 = b

    ar = (x1 * x2) - (y1 * y2)
    br = (x1 * y2) + (y1 * x2)

    return [ar, br]

def add(a: list, b: list) -> list:
    x1, y1 = a
    x2, y2 = b

    ar = x1 + x2
    br = y1 + y2

    return [ar, br]


def divide(a: list, b: list) -> list:
    x1, y1 = a
    x2, y2 = b

    ar = x1 // x2
    br = y1 // y2

    return [ar, br]

for _ in range(3):
    R = multiply(R, R)
    R = divide(R, [10,10])
    R = add(R, A)

    print(R)

# part 2
# A = [-3324,-69783]
A=[35300,-64910]

# breastplate[r][c] = {"coord": [Ax, Ay], "engraved": 0}
# breastplate[][] = dict()


total_engraved = 0
exceeds = False
breastplate = [[None for _ in range(101)] for _ in range(101)]
Ac, Ar = A
for r in range(101):
    for c in range(101):
        R = [0,0]
        exceeds = False
        for _ in range(100):
            R = multiply(R, R)
            R = divide(R, [100000, 100000])
            R = add(R, [Ac, Ar])

            if R[0] < -1000000 or R[0] > 1000000 or R[1] < -1000000 or R[1] > 1000000:
                exceeds = True
                break
        
        if not exceeds:
            breastplate[r][c] = {"coord": [Ac, Ar], "engraved": 1}
            total_engraved += 1
        else:
            breastplate[r][c] = {"coord": [Ac, Ar], "engraved": 0}

        Ac += 10
    Ar += 10

# for r in range(101):
#     for c in range(101):
#         if breastplate[r][c]["engraved"] == 1:
#             total_engraved += 1

print("Total Engraved:", total_engraved)
