def calculate_factorial(n:int) -> int:
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    if n<0:
        raise ValueError("n must be greater than or equal to 0")
    result=1
    for number in range(2, n+1):
        result *=number

    return result