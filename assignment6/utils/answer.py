import math

# -----------------------
# basic helpers
# -----------------------

def _err(qid, msg):
    raise AssertionError(f"[{qid}] {msg}")

def _is_num(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)

def _as_float(qid, x):
    if not _is_num(x):
        _err(qid, f"expected a number, got {type(x).__name__}: {x!r}")
    y = float(x)
    if not math.isfinite(y):
        _err(qid, f"expected a finite float, got {y!r}")
    return y

def _as_int(qid, x):
    if not _is_num(x):
        _err(qid, f"expected an int, got {type(x).__name__}: {x!r}")
    if isinstance(x, float) and not x.is_integer():
        _err(qid, f"expected integer-valued number, got {x!r}")
    return int(x)

def _as_list(qid, items, N=None):
    if not isinstance(items, (list, tuple)):
        _err(qid, f"expected a list/tuple, got {type(items).__name__}")
    if N is not None and len(items) != N:
        _err(qid, f"expected length {N}, got {len(items)}")
    return list(items)


# -----------------------
# save (validate + store)
# -----------------------

def save_answer(answers, qid, value, kind, *, N=None):
    """
    kind: "float", "int", "float_list", "int_list"
    """
    if qid in answers:
        print(f"[{qid}] Warning: answer already saved before. Overwriting.")

    if kind == "float":
        answers[qid] = _as_float(qid, value)

    elif kind == "int":
        answers[qid] = _as_int(qid, value)

    elif kind == "float_list":
        items = _as_list(qid, value, N)
        answers[qid] = [_as_float(qid, v) for v in items]

    elif kind == "int_list":
        items = _as_list(qid, value, N)
        answers[qid] = [_as_int(qid, v) for v in items]

    else:
        _err(qid, f"unknown kind {kind!r}")

    print(f"[{qid}] Saved.")

    return answers


# -----------------------
# dump (final check + io)
# -----------------------

def dump_answers(answers, *, expected_keys=None, filename="answers_hw6.txt"):
    """
    expected_keys: e.g. ["Q1", "Q2", "Q3"]
    """

    if not isinstance(answers, dict):
        raise AssertionError("answers must be a dict")

    # check keys
    if expected_keys is not None:
        missing = [k for k in expected_keys if k not in answers]
        extra   = [k for k in answers if k not in expected_keys]

        if missing:
            raise AssertionError(f"missing answers: {missing}")
        if extra:
            raise AssertionError(f"unexpected answers: {extra}")

    # stable order for grading
    out = {k: answers[k] for k in sorted(answers)}

    with open(filename, "w") as f:
        f.write(repr(out) + "\n")
