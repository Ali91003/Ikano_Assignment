def calculate_fibonacci(n:int) -> int:
    if not isinstance(n,int):
        raise ValueError("n must be an integer")
    if n<0:
        raise ValueError("n must be greater than or equal to 0")
    if n==0:
        return 0
    if n==1:
        return 1
    prev=0
    curr=1
    for _ in range(2,n+1):
        prev, curr = curr, prev+curr
    return curr