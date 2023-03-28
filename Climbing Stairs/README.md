# 70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

> Example 1:  
> **Input: n = 2**  
> **Output: 2**  
> **Explanation: There are two ways to climb to the top.**  
> **1. 1 step + 1 step**  
> **2. 2 steps**  

> Example 2:  
> **Input: n = 3**  
> **Output: 3**  
> **Explanation: There are three ways to climb to the top.**  
> **1. 1 step + 1 step + 1 step**  
> **2. 1 step + 2 steps**  
> **3. 2 steps + 1 step**  
 
When n=1 and 2, we can know that the output is 1 and 2.  
So let's look to the second example, when n = 3 the answer we get is 3.  

1 step + 1 step + 1 step  
1 step + 2 steps  
2 steps + 1 step  

Two of these methods are the same as the answer for n = 2, but with one more method.  

This way we know that the calculated numbers can be reused, and when I want to know the result for n = 3, I just need to keep calculating until n = 2 to solve it.  
 
So our first step is to declare a variable that is used to store the calculated number of moves.  
```
table = {}
```
When I need n=2, I can call table[2] and get 2, when I need n=3, I can call table[3] and get 3, and so on.  

Second step, we need a function to calculate the number of steps required for each n to be executed(output)  

```
def recursive(num: int, count: int):
    if(num - 1 == 0):
        count += 1
    elif(num - 2 == 0):
        count += 1
        count += recursive(num - 1, 0)
    elif(num in table):
        return table[num]
    else:
        count += recursive(num - 1, 0)
        count += recursive(num - 2, 0)

    if(num not in table):
        table[num] = count

    return count
```

In this function, We can break it down to explain  

```
if(num - 1 == 0):
    count += 1
```

When num is 1, it means that there is only one step left to choose, so when n = 1, output(count) is 1.  

```
elif(num - 2 == 0):
    count += 1
    count += recursive(num - 1, 0)
```

When num is 2, we can choose to take one step forward (1+1) or two steps forward.   
So when n=2, count will add 1 (representing two steps forward at n=2 ), then call the function again and n-1 (representing one step forward and only one step left).  

```
elif(num in table):
    return table[num]
```
skip this step, come back to explain later.  

```
else:
    count += recursive(num - 1, 0)
    count += recursive(num - 2, 0)
```

When n is not 1 or 2, it means he has more steps to choose from, but it is always one step forward or two steps forward, so we need to add up the two different ways to go.  


```
if(num not in table):
    table[num] = count
```

skip this step again,come back to explain later.  

```
return count
```

get our output!  

So, as soon as we call this function, we get the output:  
↓↓
```
if(n == 2):
    return 2
elif(n == 1):
    return 1

output = recursive(n, 0)
```

When n=1 or 2, we already know the result so we just return
When n>2, then the recursive function is called.  

Now we can assume that n is 4, into the recursive(4, 0) function.  

function step:  

recursive(4, 0) -> recursive(3, 0) -> recursive(2, 0) -> recursive(1, 0)  
　　　　　　　-> recursive(2, 0) -> recursive(1, 0)  

From this example, we can find that recursive(2, 0) and recursive(1, 0) are recalculated, and as n gets larger, the number of recalculations (like recursive(3, 0), recursive(4, 0)...) will become more and more.  
       
When the counting is done once, we can know "n=?" so that it can be recorded and ignored when the same n is encountered again late.  

```
if(num not in table):
    table[num] = count
```

When n is not in the table, it saves the steps needed for n.  

```
elif(num in table):
    return table[num]
```

When n is in the table, it skips the subsequent steps of calculating n.  

Finally, we can look at the complete code as follows  

```
class Solution:
    def climbStairs(self, n: int) -> int:
        table = {}
        def recursive(num: int, count: int):
            if(num - 1 == 0):
                count += 1
            elif(num - 2 == 0):
                count += 1
                count += recursive(num - 1, 0)
            elif(num in table):
                return table[num]
            else:
                count += recursive(num - 1, 0)
                count += recursive(num - 2, 0)

            if(num not in table):
                table[num] = count

            return count

        if(n == 2):
            return 2
        elif(n == 1):
            return 1

        output = recursive(n, 0)

        return output
```

This may not be the best solution, just provide a direction to solve the problem, thanks for watching!  