pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]
def pair_exponentiation(pairs):
    for pair in pairs:
        if pair[1] >= 0:
            exponentiated = pair[0] ** pair[1]
            print(f"Exponentiated: {exponentiated}")
        else:
            continue

pair_exponentiation(pairs)