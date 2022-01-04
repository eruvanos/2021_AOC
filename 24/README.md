# Day 24

Part 1: 97919997299495
Part 2: 51619131181131

## Code to generate string from code

``` python3

    def run_string(self, inputs: Iterable[int]) -> Dict:
        inputs = iter(str(i) for i in inputs)
        registers = {
            w: "0",
            x: "0",
            y: "0",
            z: "0",
        }

        def param(p: str) -> str:
            return registers[p] if p in REGISTERS else p

        for i, line in enumerate(self.code):
            match line.split():
                case "":
                    # skip empty line
                    continue
                case "#", *_:
                    continue
                case "inp", a:
                    registers[a] = next(inputs)

                case cmd, a, b:
                    a_var = a
                    a = param(a)
                    b = param(b)

                    match cmd, a, b:
                        case "add", "0", b:
                            registers[a_var] = b

                        case "add", a, "0":
                            registers[a_var] = a

                        case "add", a, b:
                            registers[a_var] = f"({a} + {b})"

                        case "mul", a, "0":
                            registers[a_var] = f"0"

                        case "mul", "0", b:
                            registers[a_var] = f"0"

                        case "mul", a, b:
                            registers[a_var] = f"({a} * {b})"

                        case "div", "0", b:
                            registers[a_var] = f"0"

                        case "div", a, b:
                            registers[a_var] = f"({a} // {b})"

                        case "mod", "0", b:
                            registers[a_var] = "0"

                        case "mod", a, b:
                            registers[a_var] = f"({a} % {b})"

                        case "eql", a, b:
                            registers[a_var] = f"int({a} == {b}))"

                        case _:
                            raise Exception(f"Unknown opp {cmd}")
```

``` python
{'w': 'n', 'x': 'int(int(((r13 % 26) + -11) == n) == 0)', 'y': '((n + 5) * int(int(((r13 % 26) + -11) == n) == 0))',
 'z': '(((r13 // 26) * ((25 * int(int(((r13 % 26) + -11) == n) == 0)) + 1)) + ((n + 5) * int(int(((r13 % 26) + -11) == n) == 0)))',
 'r0': '0',
 'r1': '((r0 * ((25 * int(int(((r0 % 26) + 12) == a) == 0)) + 1)) + ((a + 7) * int(int(((r0 % 26) + 12) == a) == 0)))',
 'r2': '((r1 * ((25 * int(int(((r1 % 26) + 12) == b) == 0)) + 1)) + ((b + 8) * int(int(((r1 % 26) + 12) == b) == 0)))',
 'r3': '((r2 * ((25 * int(int(((r2 % 26) + 13) == c) == 0)) + 1)) + ((c + 2) * int(int(((r2 % 26) + 13) == c) == 0)))',
 'r4': '((r3 * ((25 * int(int(((r3 % 26) + 12) == d) == 0)) + 1)) + ((d + 11) * int(int(((r3 % 26) + 12) == d) == 0)))',
 'r5': '(((r4 // 26) * ((25 * int(int(((r4 % 26) + -3) == e) == 0)) + 1)) + ((e + 6) * int(int(((r4 % 26) + -3) == e) == 0)))',
 'r6': '((r5 * ((25 * int(int(((r5 % 26) + 10) == f) == 0)) + 1)) + ((f + 12) * int(int(((r5 % 26) + 10) == f) == 0)))',
 'r7': '((r6 * ((25 * int(int(((r6 % 26) + 14) == g) == 0)) + 1)) + ((g + 14) * int(int(((r6 % 26) + 14) == g) == 0)))',
 'r8': '(((r7 // 26) * ((25 * int(int(((r7 % 26) + -16) == h) == 0)) + 1)) + ((h + 13) * int(int(((r7 % 26) + -16) == h) == 0)))',
 'r9': '((r8 * ((25 * int(int(((r8 % 26) + 12) == i) == 0)) + 1)) + ((i + 15) * int(int(((r8 % 26) + 12) == i) == 0)))',
 'r10': '(((r9 // 26) * ((25 * int(int(((r9 % 26) + -8) == j) == 0)) + 1)) + ((j + 10) * int(int(((r9 % 26) + -8) == j) == 0)))',
 'r11': '(((r10 // 26) * ((25 * int(int(((r10 % 26) + -12) == k) == 0)) + 1)) + ((k + 6) * int(int(((r10 % 26) + -12) == k) == 0)))',
 'r12': '(((r11 // 26) * ((25 * int(int(((r11 % 26) + -7) == l) == 0)) + 1)) + ((l + 10) * int(int(((r11 % 26) + -7) == l) == 0)))',
 'r13': '(((r12 // 26) * ((25 * int(int(((r12 % 26) + -6) == m) == 0)) + 1)) + ((m + 8) * int(int(((r12 % 26) + -6) == m) == 0)))'}
```

```python
# r1,r2,r3 vaished by mod 26, only d+11 stays
r1 = (a + 7)
r2 = ((r1 * 26) + (b + 8))
r3 = ((r2 * 26) + (c + 2))
r4 = ((r3 * 26) + (d + 11))
r5 = (((r4 // 26) * ((25 * int(int(((r4 % 26) - 3) == e) == 0)) + 1)) + ((e + 6) * int(int(((r4 % 26) - 3) == e) == 0)))

r6 = ((r5 * (26)) + (f + 12))
r7 = ((r6 * (26)) + (g + 14))
r8 = (((r7 // 26) * ((25 * int(int(((r7 % 26) - 16) == h) == 0)) + 1)) + ((h + 13) * int(int(((r7 % 26) - 16) == h) == 0)))

r9 = ((r8 * 26) + ((i + 15)))
r10 = (((r9 // 26) * ((25 * int(int(((r9 % 26) - 8) == j) == 0)) + 1)) + ((j + 10) * int(int(((r9 % 26) - 8) == j) == 0)))
r11 = (((r10 // 26) * ((25 * int(int(((r10 % 26) - 12) == k) == 0)) + 1)) + ((k + 6) * int(int(((r10 % 26) - 12) == k) == 0)))
r12 = (((r11 // 26) * ((25 * int(int(((r11 % 26) - 7) == l) == 0)) + 1)) + ((l + 10) * int(int(((r11 % 26) - 7) == l) == 0)))
r13 = (((r12 // 26) * ((25 * int(int(((r12 % 26) - 6) == m) == 0)) + 1)) + ((m + 8) * int(int(((r12 % 26) - 6) == m) == 0)))
r14 = (((r13 // 26) * ((25 * int(int(((r13 % 26) - 11) == n) == 0)) + 1)) + ((n + 5) * int(int(((r13 % 26) - 11) == n) == 0)))
```
