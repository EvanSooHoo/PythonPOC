class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mymap = {}
        for x in s:
            #print("add one at " + x)
            mymap[x] = mymap.get(x, 0) + 1
        for x in t:
            #print("subtract one at " + x)
            mymap[x] = mymap.get(x, 0) - 1
        for x in mymap:
            if mymap[x] != 0:
                #print("nope its false theres still " + mymap[x])
                return False
        return True
