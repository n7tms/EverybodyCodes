#Everybody Codes: Quest 1, part 1

# part 1 data
names = "Shaelnixis,Selpyros,Eldentaril,Azmaradar,Xaneldrin,Maralendris,Zraaldaros,Norakeldrith,Caelkris,Krynnrilor"
moves = "L1,R5,L3,R2,L2,R4,L2,R9,L6,R2,L1"

lstNames = [n for n in names.split(",")]
lstMoves = [m for m in moves.split(",")]

current_index = 0 
max_index = len(lstNames) - 1

for m in lstMoves:
    dir = m[0]
    mag = int(m[1:])

    if dir == "L": 
        mag = mag * -1

    current_index += mag
    if current_index > max_index: 
        current_index = max_index
    elif current_index < 0:
        current_index = 0

print("Quest 1, Part 1:", lstNames[current_index]) # -> Xaneldrin


# part 2 data
names = "Brynadarin,Xillith,Quennyn,Olarparth,Quarnxel,Nyroth,Eadfroth,Jarvel,Urzyth,Kyulrix,Azsyron,Raelfelix,Ulmarulth,Thardaros,Felmargonn,Gorathpyros,Tharilaelor,Orymyr,Ralvoran,Rythanris"
moves = "L6,R18,L15,R14,L7,R18,L19,R13,L14,R18,L5,R17,L5,R16,L5,R12,L5,R8,L5,R17,L11,R8,L17,R15,L19,R9,L5,R14,L7"

lstNames = [n for n in names.split(",")]
lstMoves = [m for m in moves.split(",")]

current_index = 0
for m in lstMoves:
    dir = m[0]
    mag = int(m[1:])

    if dir == "L": 
        mag = mag * -1

    current_index = (current_index + mag) % len(lstNames)

print("Quest 1, Part 2:", lstNames[current_index])  # -> Ulmarulth




# part 3 data
names = "Sildrith,Lazirlorath,Tarleldrin,Selardith,Sartaril,Brivoryx,Hazroth,Palddrith,Fyndeldrith,Thalaes,Ravjoris,Myrjorath,Kazrax,Gorathaes,Rahmir,Ulmarsyron,Eldenzeth,Ignulth,Malithgarath,Zyrixnylor,Raelxel,Tharnaelor,Eltzion,Xilxel,Variniral,Ilmargyth,Dalendris,Vanhynd,Nyrixpyxis,Quorxel"
moves = "L6,R22,L7,R42,L34,R23,L30,R9,L39,R11,L12,R24,L34,R36,L46,R45,L8,R42,L15,R9,L5,R27,L5,R6,L5,R15,L5,R38,L5,R30,L5,R36,L5,R44,L5,R11,L5,R40,L5,R36,L15,R43,L37,R16,L9,R11,L12,R23,L15,R32,L7,R49,L37,R5,L19,R7,L33,R41,L11"

# names = "Vyrdax,Drakzyph,Fyrryn,Elarzris"
# moves = "R3,L2,R3,L3"

lstNames = [n for n in names.split(",")]
lstMoves = [m for m in moves.split(",")]

def swap_names(i: int):
    # swap the name at index i with the name at index 0

    actual_index = i % len(lstNames)
    lstNames[0], lstNames[actual_index] = lstNames[actual_index], lstNames[0]


for m in lstMoves:
    dir = m[0]
    mag = int(m[1:])

    if dir == "L":
        mag = mag * -1

    swap_names(mag)

print("Quest 1, Part 3:", lstNames[0]) # -> Myrjorath

    
