def rotate(vector, i):
    rvector = [''] * len(vector)
    for pos in range(len(vector)):
        rvector[pos-i] = vector[pos]

    return rvector


v = ['a','b','c','d','e','f','g','h']

res = rotate(v, 3)

print(res)
