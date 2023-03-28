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

            if(count not in table):
                table[num] = count

            return count

        if(n == 2):
            return 2
        elif(n == 1):
            return 1

        output = recursive(n, 0)

        return output
