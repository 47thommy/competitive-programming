class Solution:
    def printVertically(self, s: str) -> List[str]:
        l = s.split(' ')
        mlength = max(l, key=len)
        retval = []
        
        for i in range(len(mlength)):   
            temp_arr = []
            for word in l: 
                if i < len(word): 
                    temp_arr.append(word[i])
                else:
                    temp_arr.append(' ')
                    
            for letter in temp_arr[::-1]:
                if letter == ' ':
                    temp_arr.pop()
                else:
                    break
					
            temp_word = ''.join(temp_arr) 
            retval.append(temp_word)
            
        return retval 
            
            
            
            