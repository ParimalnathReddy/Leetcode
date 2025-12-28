def sumOfAllDivisors(n: int) -> int:
    # Write your code here
    def sumofdivisors(num):
        return sum([i for i in range(1,num+1) if num%i==0])
    tsum  = 0
    for i in range(1,n+1):  
        tsum += sumofdivisors(i)
    return tsum
pass

sumOfAllDivisors(10)

sumOfAllDivisors(5) # 21                