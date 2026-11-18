# Number text lines: implementation

## What the example does

splitlines recognizes several line separators. A final newline does not create an extra empty line; numbering here starts at one.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
"alpha\nbeta\n"
```

Expected result:

```json
[
  {
    "line": 1,
    "text": "alpha"
  },
  {
    "line": 2,
    "text": "beta"
  }
]
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
