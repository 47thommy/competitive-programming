class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first_pointer, second_pointer, output = 0, 0, []
        while first_pointer < len(firstList) and second_pointer < len(secondList) : 
            start = max(firstList[first_pointer][0], secondList[second_pointer][0]) 
            end = min(firstList[first_pointer][1], secondList[second_pointer][1]) 
            if start <= end :
                output.append([start, end]) 

            if firstList[first_pointer][1] < secondList[second_pointer][1] : 
                first_pointer += 1 
            elif firstList[first_pointer][1] >= secondList[second_pointer][1] : 
                second_pointer += 1 

        return output 