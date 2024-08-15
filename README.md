Union test unification issue
===

Due to the ongoing development of typing.Generic, mypy and pydantic have divergent results when trying to typecheck either `main.py` or `minified.py`.

The error seen is:

    Argument 1 to "dump_python" of "TypeAdapter" has incompatible type "FooInA | FooInB"; expected "<typing special form>"  [arg-type]

Running yourself
===

```bash
poetry install
poetry run mypy main.py
poetry run mypy minified.py
```
