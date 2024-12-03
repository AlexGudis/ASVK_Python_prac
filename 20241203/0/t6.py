t = "cj wcejhcw qkcw cqkjchqw qekhq"

match t.split():
    case ["mov", r1, r2]:
        print(f"moving {r1} to {r2}")
    case ["push" as p, *reglist] | ["pop" as p, *reglist]:
        print(f'{p}ing {reglist}')
    case [cmd, r1]:
        print(f'making {cmd} with {r1}')
    case [*_]:
        print("Parse error")

