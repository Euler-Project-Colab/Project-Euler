memo ={}
def fastFib(n,memo):
    """Assumes n is an int >= 0, memo used only by recursive calls
       Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    try: #check if value already calculated
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result #stores result in dict
        return result
    
fastFib(34,memo)
print(memo.values())
sumfib = 0 
for item in memo.values():  #go through sequence and add even numbers until sequence exceeds 4 mil
    if item > 4000000:
        print(item)
        sumfib
        break
    elif item%2 == 0:
        sumfib += item

print(sumfib)
