
def fib(n,memo):
    if n<=1:
        return n
    if memo[n]!=-1:
        return memo[n]
    memo[n]=fib(n-1,memo)+fib(n-2,memo)
    return memo[n]
n=int(input("Enter"))
memo=[-1]*(n+1)
#memo[0]=0
#memo[1]=1
res=fib(n,memo)
print("fib is",res)
#top down