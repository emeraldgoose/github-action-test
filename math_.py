from typing import List

def sum_(a: int, b: int) -> int:
    return a+b

def list_sum(a: list, b: list) -> list:
    assert len(a)==len(b), "len(a) != len(b)"
    return [i+j for i, j in zip(a,b)]
