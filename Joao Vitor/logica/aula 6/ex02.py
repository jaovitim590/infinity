def fibonacci(n):
    fib_seq = [0,1]
    for i in range(2,n):
        next_termo = fib_seq[i-1] + fib_seq[i-2]
        fib_seq.append(next_termo)
    return ' '.join(str(x) for x in fib_seq[:n]) 

n = int(input("digite um numero: "))

print(fibonacci(n))