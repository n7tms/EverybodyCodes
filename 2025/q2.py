# Quest 2


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

    ar = int(x1 / x2)
    br = int(y1 / y2)

    return [ar, br]


def part1():
    A = [143,53]

    R = [0,0]
    for _ in range(3):
        R = multiply(R, R)
        R = divide(R, [10,10])
        R = add(R, A)

    print(f"Part 1: [{R[0]},{R[1]}]")


def part2(): #-> 566
    # part 2
    A = [-3324,-69783]

    total_engraved = 0
    exceeds = False
    Ac, Ar = A
    Aco, Aro = A # the original values
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
                total_engraved += 1

            Ac += 10
        Ar += 10
        Ac = Aco

    print(f"Part 2: {total_engraved}")


def part3(): # -> 53799
    # part 2
    A = [-3324,-69783]

    total_engraved = 0
    exceeds = False
    Ac, Ar = A
    Aco, Aro = A # the original values
    for r in range(1001):
        for c in range(1001):
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
                total_engraved += 1

            Ac += 1
        Ar += 1
        Ac = Aco


    print(f"Part 3: {total_engraved}")



part1()

part2()

part3()

