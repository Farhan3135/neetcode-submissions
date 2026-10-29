class Solution:

    def encode(self, strs: List[str]) -> str:
        key = "h"
        string = ""
        finalIdx = -1
        # need to handle the edge case of no length element ""
        for i, s in enumerate(strs):
            if s == "":
                key+= "#"
                continue

            startIdx = finalIdx + 1
            finalIdx = startIdx + (len(s)-1)
            string+= s
            key+= str(startIdx)+":"+str(finalIdx)+","
        print(string+key)
        return string+key
            


    def decode(self, s: str) -> List[str]:
        key = ""
        string =  ""
        for i in range(len(s)-1,-1,-1):
            if s[i] != 'h':
                key+= s[i]
            else:
                break
        string = s[0:i]
        key = key[::-1]
        print(string)
        print(key)

        ogList = []
        p1 = 0
        while p1<len(key):
            if key[p1] =='#':
                ogList.append("")
                p1+=1
                continue

            firstIdx = ""
            secondIdx = ""
            while key[p1]!= ":":
                firstIdx +=key[p1]
                p1+=1
            #skip past sign
            p1+=1
            while key[p1]!= ",":
                secondIdx +=key[p1]
                p1+=1
            #skip past sign
            p1+=1
            # print(key)
            # print(string)
            # print(f"first index: {firstIdx}")
            # print(f"second index: {secondIdx}")
            appending = string[int(firstIdx):int(secondIdx)+1]
            # print(appending)
            ogList.append(appending)
        return ogList
