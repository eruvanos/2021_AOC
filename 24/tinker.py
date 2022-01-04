def fr1(a):
    return (0 * ((25 * int(int(((0 % 26) + 12) == a) == 0)) + 1)) + ((a + 7) * int(int(((0 % 26) + 12) == a) == 0))


def fr2(b, r1):
    return (r1 * ((25 * int(int(((r1 % 26) + 12) == b) == 0)) + 1)) + ((b + 8) * int(int(((r1 % 26) + 12) == b) == 0))


def fr3(c, r2):
    return (r2 * ((25 * int(int(((r2 % 26) + 13) == c) == 0)) + 1)) + ((c + 2) * int(int(((r2 % 26) + 13) == c) == 0))


def fr4(d, r3):
    return (r3 * ((25 * int(int(((r3 % 26) + 12) == d) == 0)) + 1)) + ((d + 11) * int(int(((r3 % 26) + 12) == d) == 0))


def fr5(e, r4):
    return ((r4 // 26) * ((25 * int(int(((r4 % 26) + -3) == e) == 0)) + 1)) + ((e + 6) * int(int(((r4 % 26) + -3) == e) == 0))


def fr6(f, r5):
    return (r5 * ((25 * int(int(((r5 % 26) + 10) == f) == 0)) + 1)) + ((f + 12) * int(int(((r5 % 26) + 10) == f) == 0))


def fr7(g, r6):
    return (r6 * ((25 * int(int(((r6 % 26) + 14) == g) == 0)) + 1)) + ((g + 14) * int(int(((r6 % 26) + 14) == g) == 0))


def fr8(h, r7):
    return ((r7 // 26) * ((25 * int(int(((r7 % 26) + -16) == h) == 0)) + 1)) + ((h + 13) * int(int(((r7 % 26) + -16) == h) == 0))


def fr9(i, r8):
    return (r8 * ((25 * int(int(((r8 % 26) + 12) == i) == 0)) + 1)) + ((i + 15) * int(int(((r8 % 26) + 12) == i) == 0))


def fr10(j, r9):
    return ((r9 // 26) * ((25 * int(int(((r9 % 26) + -8) == j) == 0)) + 1)) + ((j + 10) * int(int(((r9 % 26) + -8) == j) == 0))


def fr11(k, r10):
    return ((r10 // 26) * ((25 * int(int(((r10 % 26) + -12) == k) == 0)) + 1)) + ((k + 6) * int(int(((r10 % 26) + -12) == k) == 0))


def fr12(l, r11):
    return ((r11 // 26) * ((25 * int(int(((r11 % 26) + -7) == l) == 0)) + 1)) + ((l + 10) * int(int(((r11 % 26) + -7) == l) == 0))


def fr13(m, r12):
    return ((r12 // 26) * ((25 * int(int(((r12 % 26) + -6) == m) == 0)) + 1)) + ((m + 8) * int(int(((r12 % 26) + -6) == m) == 0))


def fr14(n, r13):
    return ((r13 // 26) * ((25 * int(int(((r13 % 26) + -11) == n) == 0)) + 1)) + ((n + 5) * int(int(((r13 % 26) + -11) == n) == 0))


for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        for g in range(10):
                            for h in range(10):
                                for i in range(10):
                                    print(f"{a=},{b=},{c=},{d=},{e=},{f=},{g=},{h=},{i=}")
                                    t = fr1(a)
                                    print(f"fr1: {t}")
                                    t = fr2(b, t)
                                    print(f"fr2: {t}")
                                    t = fr3(c, t)
                                    print(f"fr3: {t}")
                                    t = fr4(d, t)
                                    print(f"fr4: {t}")
                                    t = fr5(e, t)
                                    print(f"fr5: {t}")
                                    t = fr6(f, t)
                                    print(f"fr6: {t}")
                                    t = fr7(g, t)
                                    print(f"fr7: {t}")
                                    t = fr8(h, t)
                                    print(f"fr8: {t}")
                                    t = fr9(i, t)
                                    print(f"fr9: {t}")

                                    print()
