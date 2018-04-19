def calcAlgorithm(input1, input2):
    if input1 > input2:
        one = input1
        two = input2
    else:
        one = input2
        two = input1
    startone = one
    starttwo = two

    a = list()
    a.append(1)
    a.append(0)
    b = list()
    b.append(0)
    b.append(1)
    c = list()
    c.append(0)
    c.append(0)

    print()
    i = 0
    print("  i%8s%8s       a       b       c" % (' ', ' '))
    print("%3d%8s%8s%8d%8d%8d" % (i, ' ', ' ', a[i], b[i], c[i]))

    i += 1
    print("%3d%8d%8d%8d%8d%8d" % (i, one, two, a[i], b[i], c[i]))

    while two != 0:
        i += 1
        dm = divmod(one, two)
        c.append(dm[0])
        one = two
        two = dm[1]

        a.append(a[i - 2] - c[i] * a[i - 1])
        b.append(b[i - 2] - c[i] * b[i - 1])

        print("%3d%8d%8d%8d%8d%8d" % (i, one, two, a[i], b[i], c[i]))

    # ggT
    greatestcommondivisor = one
    print("gcd: " + str(one))
    # inverse
    inverse = b[i-1]
    print("inverse: " + str(inverse))
    while inverse < 0:
        inverse += startone
    print("inverse: " + str(inverse))
    # 1 = a*p + b*q
    a_end = a[i-1]
    b_end = b[i-1]

    print("done")
    return {'gcd': one,
            'inverse': inverse,
            'a_end': a_end,
            'b_end': b_end}
