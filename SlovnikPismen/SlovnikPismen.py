sentence = input("ZADEJTE VETU, SLOVO NEBO JMENO")
abeceda = ['a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z,']

vysledek = {}

for sentence in sentence:
    
    if sentence in abeceda:
        vysledek[sentece] += 1

    else:
        vysledek[sentence] = 1
print(vysledek)


#Hacky, carky jsem udelal jen takto, protoze i presto ze jsem se vsude mozne dival nedokazal jsem na to prijit.
