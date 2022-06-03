class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        finalAns = []
        for x in range (1,n+1):
            #finalStr = ""
            print (x)
            if x % 3 is 0 and x % 5 != 0:
                finalAns.append("Fizz")
            elif x % 5 is 0 and x % 3 != 0:
                finalAns.append("Buzz")
            elif x % 3 is 0 and x % 5 is 0:
                finalAns.append("FizzBuzz")
            else:
                finalAns.append(str(x))
        return finalAns
