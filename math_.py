from typing import List, Any

def sum_(a: int, b: int) -> int:
    return a+b

def list_sum(a: List, b: List) -> List:
    assert len(a)==len(b), "len(a) != len(b)"
    return [i+j for i, j in zip(a,b)]

def substract(a: int, b: int) -> int:
    return a-b

def list_substract(a: List, b: List) -> List:
    assert len(a)==len(b), "len(a) != len(b)"
    return [i-j for i, j in zip(a,b)]

def isnum(a: Any):
    if isinstance(a, int):
        return True
    elif isinstance(a, str):
        try:
            _ = int(a)
            return True
        except Exception:
            pass
    return False