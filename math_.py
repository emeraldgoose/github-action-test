from typing import List

def sum_(a: int, b: int) -> int:
    return a+b

def List_sum(a: List, b: List) -> List:
    assert len(a)==len(b), "len(a) != len(b)"
    return [i+j for i, j in zip(a,b)]

def substract(a: int, b: int) -> int:
    return a-b

def List_substract(a: List, b: List) -> List:
    assert len(a)==len(b), "len(a) != len(b)"
    return [i-j for i, j in zip(a,b)]