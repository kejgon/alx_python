def fibonacci_sequence(n):
    if n < 0:
        return []

    result = []
    a = 0
    b = 1

    for _ in range(n):
        result.append(a)
        a, b = b, a + b

    return result



fibonacci_sequence(6)
fibonacci_sequence(1)
fibonacci_sequence(0)
fibonacci_sequence(20)