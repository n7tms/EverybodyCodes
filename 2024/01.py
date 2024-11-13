# Everybody Codes: 01


# Part 1
creatures1 = "BBACBBBCABBCBBCBACAABBCAABBBBCABCACBAAABCCBBBBBACABCCCCBBAABBBACBBACCAAACBBBBAABAABBABCBBBCCCCAACAAAABABACABCABCCABACBBCBBBCBBCCCBBACACBBCCCCBBCAACAAACBABBCBCACCBBACACACAAACCABBACBACAABCACCBABAAACCCABCCBCCCCACABBBCBBACBAACBCACCAAACAABAAACCBCCBCCBBAACCCABABBBBBAAABABCCBBCCBABABCBBBBBCBACBABCBBABBCBBBBACCCCCBAABAAAAABACBCBCBBCBABBBCBAAABBACAAAAACABAACABACBABCCCBCBCBABACBCCCBCBBCBCABCCABCCCBAABAAACACBCCACCBBCCBBBBCACAABBCABACACBAAAACCBCABBABBBCACCACBABAACACCACBBBCACABCBBBBBBACAACACACBCACBBAAACACABCCCBABACCCAABBCBCAABBCABBABCBBABAABAACBBABBABBCCABABBBBABBABCBCAABCCABCBBBBACCACACAACAACAAAAABBCAAACABABBCBACABCBCAACABCBBABBBBCBACCABBCBBBCCCCBCAACCCBBCBABACAABABABCCCABBACABAACBBABACAAAACAACCAAAAABCCBCACCBCCCBBBABBBCAAACCACCBBABBCBBBCCABBBACCBCCACAABACAACCCAABCCBAABABCCBCAABCCAABABBCCAACAACCABBACCABBBBACAABBBBBACABABABBCCCBBACCACCACBAABACABBCCCBCABCCCBCBCCBAACACCBABABCBCCBACACBBABBACACBAABCBACBABCAABBCBAABBAABBACCCCCACCCCBACBBCABBAABBCCACCABBCBCACBBCBCCAACACCBCBAAABBCABCBBACBBCCBCACACBBCACBCCCA"

potions_needed1 = 0

for creature in creatures1:
    if creature == "A":
        potions_needed1 += 0
    elif creature == "B":
        potions_needed1 += 1
    else:
        potions_needed1 += 3

print("Potions needed",potions_needed1) # 1334

# Part 2
creatures2 = "ADACxCBBCABCBBACABBCBAABxCAxACCCBDCDDxDCABBAxCBCxDBDxADCBxDBBABDCBCCBBDBxDAADxACxBCBBADBADAxBCBBDBxAABDDAACBBACBCDADCBBBACBBACACCxxCCBCDABBDBCDCDDDCxCxAxADBDBDDAABACCxADADBCCADBBADAxACxBACDCCCCCDCxAADAxDxCAABBBxDxAAAxDCDDCDBDCBCACxBAACBCBDAACDBCCBCxBCBABBxCAABDBBABAADBBBCDAACABAACxAABBDAAxAABACABBCCADBCABBBxDDBxCAxDBxDxDCCDAxxxACBxDDACDxADBABDABDBCDCCBCBxCCDxBCxABCDABDDCCCxCBCDBBBBACDCxCACACABCCAAAxBxDAxAxADBCxDDxxCBBACxCABABxAABCDADCBABABBCxBDxDBBCADCACDBxDAABBABCCDCAADxABCADBAACCDxBABBCADCxAAADDDDCBCDAABCxCADxABxAACDDDBCACCCDBxBDDBBADDCBDDCCDBxAADACDxxACBCCBxAxACCBCBACABCACxDDBCADACBACDDACBDxBABDACCBBBxxDCBxDBBBBxBDADCADADABDDDDDBDCCCBCCDBxADCCACACACCBDxACBADDDAAxABDCCCCBCDCCADCxDACBACBxABxxBCCDBCADADDADACADDCCBDAAABBAxDDADBBADDxDAxABCDADADCCCDAACBDDBBBABCDACBCACxDCDABxBDBxCBADxDCAACADCABxCDACABDCCBxCDDAxDDABCAACCAACBxxCBCBCAxABDxCDCAxBACBBDBCACAACDCACBADDCxCABCACxCCABCDCABBAAxxxDACCBxDADADCDAAxADDDACACBDCBCCDCBBBxBBBBCBDABCCCDDDDADABDBADDxDCDCxCDBDxDCDBBBAxAACBxDDAxxDADDBxDACAxDxDDADAABBDxxBCACxxDACADDBDBDDBACxBBBAxBBDBxDBDACCDADDAACxCABBCABABxCADBBABDACACxABCDAADBDDCBCDCDDBBABCDBAxCBDAAABAADBCxxBBDBBAADACCxAxDADAxCCCxxCBCACDCAACDABBxCAxABCABBCCAABDBCDBDDxACACADDABBDCDxCCAAxDBxDCxBDBxCACCCCDDCCBxABxDxDCDDxxBCCCCCBBxBBBDADxCCDACBBBxCxACBCBCDDxBBxDBxBACBAAADCCACAACBBAADBBBDACDxCxAABCBxDDACBABCABADCxBAAABAAxBCBBBBDABBDCDCCxCBCDCxxDACDDADAAACCCACxxBCxDxDBxAAxxAADACAABADABxBCCDDBCBDBAACCBAxADCxDABDACBDxxCACDABDBADCACCDDAABBCAABDADCAAxDDBADCBABADxCCCCDDBABBxDCDCDADDDCxDxDCAxDCDABCDBABCCCCDDDBBCCDBBBADDAADCADDCDACAADBCBCBAACDxACDACAABCAACDCDxCACBACAABBBBDBDAABBDABCBxDCADBDxACADBCBBABCAxCCAxxBxAACAADDACADACxBDABBCBCBDAACBCDDABAxBAxADAxCxCDBBBACDBDBxDADDDDBCxABDCCDBCCDBACDCDBCBAAxCAAACCDAxxCDAABCBADxDxxBBBABBABBCxCCDADBACDABDxCxAADBCxxDCxBAxACDCBACBDBAAxBDAAABDDDxACAADBxACCCACDAAAABDAxACADDCABACBBAADCADBxBxBDBCCxCABACCxCAABCAAxDCACBBCBCDABxxCDCDCBADBxDxBABBCxCDCBxCADxxDAADBABxADCxDBBxDxCCCAxCAABAAACDCADBBBAADCxBABCBADCxBBxBCBDCCBABBxBDxDCDDCxxxBBCBCADADxBBBxDABDCCDCDDDCxD"
creature_values = {"A":0, "B":1, "C":3, "D":5, "x":0}
creature_names = ["A","B","C","D"]
potions_needed2 = 0

for c in range(0,len(creatures2),2):
    alpha = "x"
    bravo = "x"

    if creatures2[c] in creature_names and creatures2[c+1] in creature_names:
        potions_needed2 += creature_values[creatures2[c]] + creature_values[creatures2[c+1]] + 2
    else:
        potions_needed2 += creature_values[creatures2[c]] + creature_values[creatures2[c+1]]


print("Potions needed",potions_needed2) #5383


# Part 3
creatures3 = "AxACDAACDACxACDBBBABDDABBDBxBxxBxCBADxBDBBAxDCDBDABCxBAAABxADDCCDBDADBDCxxAAxDDAADAADDxxDAADAxxBxABCCCDBCDCDDACDxCxBxDCDDADxABxCCxCABBBxABAAxxCBxDAACBCxABBBBxABxBDADDCxxABCBxCADAAxDCxACxBBxABBBDCDABBxCAxADCCAADBDxxADCxDxCxCxxBxDDCxxxABAADxDxxBxBABDxAxBDBCCBABxCCCDCAABAxABBxADADCADABDCBADBADCADACAAxADDxBABBCBxADAxxAACDBABBDxxADxDDCDDCBBAxBACBxDBCDAxBBCADDBDDBBCDACCCBDxxADBDADAADBxBxABCAABDADAAADDxDBCBxCBDDCDxxABBDBBxCCxxCCBxDCxxDAxxAAADCDACxDBCAxCDCBDDBCAADBCADxCBDxCDAxAACBDxDBDBCCCDDDxxBDDxDCABCBxAxxCDABCADBCxCxCCxDCxABBxACBxxABxDCBxBCCABAACCCBCxxBAADxxBCxCxAxxDBBBCCBCxxDDCCDxACDAxCBxAAxAxDDxCDBCDxCAxABCxADDDCDCDDDCCDCCACCDxAAABCCCBxDBBBBDBDCxBAxxBBBABxCDAxCxxAADBAxxBADxDCxBDCDBADBxAxDDDABCABxDADxDBBCBCADBAABDxDBBBBBxAxCBxBBADxxBCABCxBDDCABAxABDCCCBxBCBCCBDDxDADCxDBxCDCABCBxAxBBxACxBxxBDCBDAABBCxDAxBDxDDCACBCxxBBDADxDACAxCCCADCBDBABxDDBBBADBxAxxCABxCDCDCDxACxCAxCBBADBxDBBBACBCDAADBABAxBBDCxCDBDDxBCAxCBCxBxDxABACxBCxxAxABBBACAxBDCBDxCCCCBCDAxAxABDCDxAADCCxAACCDCxxBBxDCACDADAACBCxxBxDxAxAxxACDABAACBCCBxADxDxCBDxxxCACCxxCACBCDAADBABBDDACABBCxDDDBCDDDCDCDBAxDCDAxDADBDCxAxBACACxxxCACBxCCBCBDCCCADAAxBDBxCxCCxxxBBxxBAACBDDABBBDDxxBxxCBBCxCDDDDADAxxCBDDBBCACACxCBDDDxABACBDCDxxAxBDxBCABBBxDDDCBBDCBxxBBCCADxBDBBxAACBxxxBCxAxxDxACCCAABBxxxDxxACABCDxADCDDxDxBDCCDAAACBDDxABxxxAxAABACBCxDDAABBCBxADCCxDxCBCCxDxDACDCBBBBxxBABAxBCBCBCAxAAxCCBAxAxDxxCDDxAxCDACBADCCxxBACBCCxBxADCABDxCDxxDADAxDCxAAxAxDAxBAxxABDDxBCBDCCxCCDCABxACCxxBBACDABBABAABBBxCBBBCCDABCBDDACxCCCBAACBDCCxBDxAABCxxADxxCDDBADCCDxACADCDxBCDxDBxAABDxxxBCxxBDBCAxCBxBDDBxDDCACABDAACxDACxDACCAACAxCxDCCBDxBCBCBCxxxDDBxxDBCCBCBBxBDxxBDxAABDBACCDxCDCBxCAAxCACDxxACDCDCCBxAxDDBDADDxBDACxADDCADCAADDxCCxCxDBDCxDCAxBCxABDCAAAACxDDADBABDBxBDCxDAxDBxDDxxCAADxCxCAAAAxDCDBxCxCCCCDDxxDxABDBBBAxCCCDBDAxCDxxBADADBABxxBCACDABxDADxBCBADBCxCCABBBBBDDCAxACBxADBBDBABAxBBCBxAABBxABCAABBAxBADBBDBBACxxABBxDxABBBDDBDDDDDAxxCDABBBCAABxCBADxCDxCDADAAADAxxxCxxCCBxCxxBABADxCxCxBBxCxCADDDDCxxDCBCxADCDBABDDDCxDxxABBAADDCCxAACACBAABDBBACxCCCACCAAxABDxxAxxDBDCBBBAAxBxCxCxBxxCxxAACxCBxADDDCDADADDCCCACDxxCxxxxADBDCxDDDCCCBDACBAxCxCACxxCABCAACADCCBxCDxAxBCBDADCADCxBDDxxCCCDBBCBxCxADCDCDADDCDCBxBABDxCACBCBCxDDADxAxCBCCBCBAxDCDBBABBCxBAxBDAAxxBDBDADBCDxABBxAAACCAxCABDxCxBDxCABCCxBBxBBDCBAABCDBAxDxxCABACBxCxACACBDDDDCBxCDDBxxCAxAAxCCDxxCxACBBBBxCCDxxABBABBCxDDxDBBBCADDDBxxACBCAADxCABCADAxAAxxCxxADDDCxxBxxBDDCDDCBDDCCACBBxBADDCxAxxADxCCxDxCDxADDCADAxBxDDxxADDADxACADxxACBCDxAxxACDDxBCxDxxxCBDADBCDxDCAAAAxACCBCAxBDACBAxDBDxxADBCADAAADDBCDADCCBDDDABABCxADCAxDAxACBBxxBDAACCCxCCBCAAxCDCDDCADACAxDxDAxACADDDABAxDCxADxxDxxAxDDxDAxCABxCDxCCDAxBDxAxAxCADAxABBBABDCACCDCxCDCCCCDAABBDAxDDDBBADDAxBCDxxDxxBABCDAACxCxBCxDBxCCxxDDxCCDDBDAAACDCxABxBCxDBBBCDBCADxAxAACDCDDxADADAAxCACCxxDDAxABCADAACCAxBBxDCxxCxCCCACxDAAACxxCBDBCADBDBBxDABCACAAACCBADxBCxDDAADAACBBxCCADDAxxBABDBBBBDxBxDBDAAxAxxDCCABCBDxCADACDxACABDACBDBCBxADxBxAADCBBCCDBxBxCCACxDxCCCCDxBCACBBDxxBBBxCACCBBCDABCAADACDCxBDCxABDDDADACADCxADAxxCACxDDCBCDBCDCCxCCBAAADBCxABBDxABxxACBCxACDABDCBCDDxABADCBDBCBAxADDBADxxDDCBBCCBCABBCCBBxCCDxxBABxxBDBDACxDBDACCBBDCBBCCABBAAACCDxAACxBxxDAxADxBCDBBBxAACACxBBBDBCxAxCAAxACBxDBxBCDBDDBDDBAxCCABBBAxBCxCxBCDCBDDCDxCBxCxCBCBCAxxACBDxxDCxADCADACAAxCDCCDAAxDDCCAADxBBBxxCABCxBCxBxABBBCCCBBACADCDADBxADBDCAADBDDCBADDDxBBxCDADDDDBDADDxCxCxBBDDABBABAxBxCAxDBxDxBAAxDDCCDCxAAxxAxBCxDxBCCDBxxDxCxDCCADBABADCDCABADBxBBCDBCAABDACxBCAABAACxACAAxBDBAxDDAABxCDDAAxAAABDDDxBCxCDxDDCxCDADADxADACCxBCACxCBBACACCxAxxCCCxAAxAxxDBDCBxBBDBBxAADDxADCCCAAACBxAAACxABCAxCCADBBCCADCDCxCxDCxCBCDBCCDADxABADDCCxCCxxxCDCBDCBCCBxAAxACxAxDxCDABDxDBBDxDCAADDDBBBBxxDxCDxADCAxCAAxxABCDBDDAAAACABBCxBBADBCCCDDDBxCDDBCxBxBBCBxDAACDxCxBBBAxBACABxABACxxBCAxBCCxAxxxBxDxBDDDxxDDBDAxBADDCDxxDBAxCBBBAxxABCDCxxDDCBCDABxAxxDBxDCDxxBxCxDBxxBCCCDxCCDCxxCBDAxBCDACCCxABDBxDBxBCAACADxCBBxBCxDBBBACDCxCDDBAxDBCxDxCCxBBADxDCCABBACAxDDBABCBCBCCBDxxAADCBxBDBDxxxBBCDxCBDBDxDDDDDBxBABBADCACCDxAxBCBAxBDDDBCAxAxBABxBBACCDAAxxCDBACBCxDABBxBCxCAxCxCBCACxCBCDDBxBCDBxDDBDDxCxCDADAACADDBCAxACCABBCDABxAxCAxBACxxABADDCxBxBAxxCDCBDCBDDBCBDCDxCCxBxDBBBxxCBAxDxxxDDAxBxAADCxDxDBxAADxDDAACxDABxCCxABBDDCACAxAxBxACCDDBDxDDBBCACxxxCBBCDxCCxABDCBBCDABAACDACxCBCDDBAAxABCBBDDDDxABDBCDxCDACCDCBBBABxBAxxxxAxADACBBBABBDADDCACADxABAxDBCBCAxACxDADDBAxAxDBACxBxxBxDDCCDxBCBABxACDDxADADACBxDDxBBBDxDDBxxDBxCBACDxCxxBCBBAACADBBCBCCBACBDCDDxDBxCxCDxxBCxDxCADBDDCDxCxCxCBADxBCABABxAADBDxBxACBBBABBDACDCDCxDBABDAABxCAACxADxCDBABDDBCBDxDCCABDBBCCCCxxCBCCCCBAADCCxxBAxAAABCAADCCDxBDCACCDBAxACBDxxxCxBCDADCCDBAxDxDxxDxBDBCCBCDxBDBDDDBxCBACCBCxCxxBBDCBxCxCADBCDAxCBCABDDDxBxDBCBAAxAxCBCBCBBBBxCBACABCBDDCxxBCCAxCABxCCCCDBAxADBBCxBDBBDADDAxADDBABCCADCCCDxAxxBABCDBBBACBBBBBBxADACAxBBCCADDBCADAxBCBABDDCDDxxBxBxDBADCABBBCCxBDDDDxBCDBDAAABCxDxBxCxDDxCBxxDBxBxCDCDDDDCCADABCABBxCDDxxxxCDABDDCBxACDDDDDCAxCCCBCBBxCxDCDBCBDBCxxCCxCBxBDxBADxADBDAxBxBAxxDAxxxACBACDDBDCBAAxABACBDxxDxAABBDCxxCDBDDBDCDCCBBDxADBCCxCBBBABADAACBDDDACAADADDxBCCAACCCACDxxxADCAxDAAxxCBxBxxABxDDxxxDABAABAABCCBBDABBDxCAxCxxAxCACBCBxAxDCBxxBBDDCACDAACBBCxDxxDxDBxACBCDABDDDxDxBxxxBAADCBDDCxxCCxCABDBBDCAxACxxBxACBCxCxAxABBAxDBCABxBBDDDCBBDBDBDDBDADDAAxBxACADDDCABBBADxBBAADCDAxCxDDDxCCxBxDBCBDAABBDCxABBAADDxCADAADCDABADCCACADBDDDBCBDABABDAACBCxxCBCDDCBxABABAxxBxBCDxADDxxDxxBBABxxxCDDBBACCACDDDDxCBADBCABxCxCAAABCDBCBBxDABABBACBBABBAAABCCxxCDBAAADADADDBDDDAABAxxDAADAAxADACxBABxDCADADxDDDCACAxDBCCACBBACCCBACACDxBxCDAxBADxAxACCBAADDCDCDDCCDxxAxDBCCAACBDADACAxCABBDDDCBBBxCxCxADBxCCxDAAxBADCAxCxDDDCAACAAADxDCBAAxCDADxABCBABxAxDDAxxxDCCBBxBACBAADxCAxxBDADCxADCACDDxCACADDBABCBxADDDAABxxCCCxDBCDBxAACxBxDAAxABADDBDACABxCBDAADBBBABCCBACDABxCDxBxABCxDAxDxxBxDxxDCDDxDBBBDBxxDxxDxACDAxBDxDDCDBBDxBBBCADACCDDCABDBBxACBADAABDxCBBBDxDCDBDBBxBDxBDxxAxBAABACCCxxBCAxBBDBCACDBCDxDDABCCxAAxABCxDxACADDxDBDxDACDDxxBBBxBxDBxDCCDCxxBDCDBCxDADBBDCBBDABDBDDADCBDBCDAxACBCxCADDADBACCDDDxADADAxxDBBxDABxBxDBBDABxCDADCBCxxDDCxAxDCADDxCDxAxAAAAxCDCBxCBACxACxBBDAxxxCAxxDBDBCACDDCCxCABACAxBBCAxABDCCBBDBxADDDAABCxCDADAxBBCCxCBCxCBDBDBABBBCBDBxDDDxABDACCBxxxxCDADxABABAAxCAACDDxADDACDCAACxBDBAxDDABxBDBAxADCBCBDDBBAAxACDBxACAxABDxBxxABxABDBxAACCBCDxDCAABDxDCABxBBBCACAxxAxDxDxxCxDxBCACDADDDxCACCDxCADDxBxAxCBCDCCBAxCDCAxDCDCxDxxADCCBxxDxxABxxABABxxxABBxBBxCDxCxDACxDBDxxxBDDCBAxxBAACCDDBxBCDxBBCCCxCDxBBBBDACBCBBCxxCBCABCDBCBxxDCxCACACDDxBCDBCCxxABCBCABxxCDxCxxDxBxDDxACBACBxADxACAAxCDDBBAxxBxCBACDDABAACADBxDDxDACxDACADDBDCADBDDAxCBxCBBCADABBxxBDBxABxBABDCCABDxDxAACBCBBCADBCCxxxDCCCCACxBCCCxAxACBxCDCCACBBxCDDCABBBBDBBABDCxxBxBCxxDBDDxCDDDAACACBDABDBADBCADCBxABADADCxCACCBAxCDCCxDBDCADCxADCCCBABCDBCBBCBCxBADAxxxBCDCADABBxDDxCDxBDADBDDCACDADxDxDCxADCBDBDBCCDCxxxBCBACBCDDCAxxDxAABAxCDABDDDxACDDBADBxDDABBCBCxCBDxAxCxCDBCADABDADBCxxCCBxxCAxADxCBxBBCACCBBABxDBCBBxDDCCDDxxBACBCDCCBBCDxAxxxCBBAACCBxDDxACBADBACCADCCAADBCBCAxCADCBBAxCDDxxxDAADxACDBAAxDBBDBDBxxCCACCCBACCCBBBADABCAxxCDxAAxxDDxBBxBCDABBBDDDxACBDxBDBDDBAxBxAxAAxBBxCBCABBxBDCBABBCAxDBCAACBABBDxADBDCBDCCCCDxCDBAxADCCCDAxxxCBDxxABACADDBDxADBBACBxBDDDDCAAABxxBxCCCCxABxCBACAxCACxCAADBAADDBBBBDAxDCCCDBDBDDAxAAADAxBDDxBBBCDBxxACADBCCCDACCCDCxxBAxACxxBDxDxBDBxCxDxCDBBACCDDCDDACCBAADADDxCxAxBBCxxAAACAxBDBCxADxDxBxxDDCAxDBCDADxxxDCxCABxDBADxBDBBBxxxBADCDDCDABBABCxBCBACBBBAADBDxBCBBCDCAAAxBACDCxBAAxCBACCCCAAxBxxADAxDAxxAAxBxxDxDCBDADBBADACxAAAACDDxDADBCCCCBCxDxxxDBxxBBCAxDxCBDDxBACxCCCBCAADACDDxABDCxCBCDCDxBCBxACxDBBACAACDxCADBxBACADCxDDCDBCxCCBDDAAAABDxDxxADDxCCDCBCxDDCCxBDBxDBBCDBACAAABCDACxxxDBCxDCDCBCDxxBBBBDBDCCACBCBxBDBxCxCxBDAAxDAACCDxxBBBCABxCCDxCDDBDABCBBDCABBDDxCDDCCACBxABCABxCxADADCDDDCABDADxxDAAAABAADAABBxDxBBDBxDBxBADCDDBDAxACCDxAxBBACxxDxADDBBCDCDxDBADBxAxBAACCAAACBBCxADADDCBxCDACAxxCxAADBDDxCxBAxCDxxBCDxDBDxBAACCxDxADAxxAxCxAxCADADCDADDxCADBDCBxxDCBxDCDDABADDDxBDCBAAxDxCDBBCxACADxxCBCDCBDBDCDBAxDDBAxBxBCABAxxAACABBxCBDAxCCBBxDCAxxDBDABADACxxDCACxBxAxCCxCDDBxCDCACBDAxAAABDBAxABxCAxBDxABDCCxADDDBxDDAxDxBBAxCADABBABxCCBADCDxBDACxxBABCxCDACADBACAxCBBAxBCCxBxxxxxACAxDBCxCCBCACCCxDCBDBDAAxxxBBAAAABDxDBDCAABxCAxCBxxDAAxxxCAABDBDDxCBBAxxxDxCDBDxxDBBBBCDADBDxBDCABBxCDxABDxDBBBCxxxDDBCxBCBxDxCxCDCACCACBABxxDBBxABDCABCABABxCDCDCxABADCxCBBCDAACxxADBBBCCCBxCBxDBxDxACBDAABBAAACACDAxCCCxxBBxBBADACxDBCAACCxxDBDADDCCBDxCxBACADxDDCDBDAxDCCDBxAABCBDBACxDBADCCCCDxDCABACCBBDABCxxBCBxCxBBCxBACADDAAAxBABBDxxCxxCxxBACDBxACDxxxCDACCAADDDCCCAxxACABDBxCBDxDCDxADBCDBBCCACCDAxBADDCxxDDxBxADCCCCxDABxAABxADBxCADCCxCDADBDBCxDAAxBBDAABCBBABDCxBBDABDxADABxDBBAxACCDCCABCxBCBCAxCCBxCAACBxBBBBAxxBDADAxxxxxDBBDCAxBxCCCxxADDxDBBAxDxAxBxBCADBxDCBBBDAADDABADxBCDADDAADABABCCCBDDBxDACxxBCDDACDxBABxAxBCBxAABACxADACBCBDDCDADCxDDCCACxDCBADACCDxDDDCxDBBBDDCxDCCCxDBABCxCDACxABBABxDxDBACxBBBBxAAxAAxDCCADDDxBAxAxABBACDDCAADCBDBCDxBBDBCDCAxCCBxACCxBDABDAADBCDxBxDACxDADCBxADDCAxBDAxxDxDAADxBxABBxAxDDBCxxDBAADDCCxDABDBAAxAxBABAxxAxDDxABxACCDCCCCBACBCBBDDBCCxCxDDDBDDCxxDCDBCAxDxBADxxAAxABCAACBACACCCCCABABDDADCAADDxBABADDCxCBDBxBxDAADxBACADCBxDCCAACACxBCCxxCABCCxCAABCDBCxCBAxBBCBBACxBBCDBCCAxBDDBCxDDBDDCCxxCBxxxBADCADxDCDBBCAAxxxxAxxDAxAxxDDCDCBCBxxAxDDBxBBBxxACBBBxxBABBxxCDBxDxxDCCDxAxAxCBBDAACxDCDxDACBxxDAABDBBDABDCBABBxCxDxDDBxAxDDADAx"
#creatures3 = "xBxAAABCDxCC"
creature_values = {"A":0, "B":1, "C":3, "D":5, "x":0}
creature_names = ["A","B","C","D"]
potions_needed3 = 0

for c in range(0,len(creatures3),3):
    group = creatures3[c:c+3]
    temp = 0
    temp += creature_values[creatures3[c]] + creature_values[creatures3[c+1]] + creature_values[creatures3[c+2]]

    xes = group.count("x")
    if xes == 1:
        temp += 2
    elif xes == 0:
        temp += 6 

    potions_needed3 += temp
  

print("Potions needed",potions_needed3) # 28000

