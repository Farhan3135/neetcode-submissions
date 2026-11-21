class Solution:

    def encode(self, strs: List[str]) -> str:
        key = "k"
        final = ""
        for s in strs:
            if len(s):
                key+=str(len(s)) + "#"
                final+=s
            else:
                key+="$"
        print(final + key)
        return final + key
    
    def decode(self, s: str) -> List[str]:
        key = ""
        for i in range(len(s)-1, -1,-1):
            if s[i]== "k":
                break
            key+= s[i]
        key = key[::-1]
        s = s[0:i]
        final = []

        run = 0
        end  = 0
        start = 0
        num = ""
        while run < len(key):
            if key[run] == "$":
                final.append("")
            elif key[run] != "#":
                num+=key[run]
            else:
                print(run)
                print(key)
                end = start + int(num)
                final.append(s[start:end])
                start = end
                num = ""
            run+=1
        
        return final 
            
            




