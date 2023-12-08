from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        check = defaultdict(list)
        
        for path in paths:
            files = path.split(' ')
            directory = files[0]
            
            for file in files[1:]:
                name, c = file.split('(')
                check[c[:-1]].append(directory + '/' + name)
                
        return [check[c] for c in check if len(check[c]) > 1]

            
            
            