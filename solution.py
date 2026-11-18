

def solve(value):
    return [{"line": n, "text": line} for n, line in enumerate(value.splitlines(), 1)]
