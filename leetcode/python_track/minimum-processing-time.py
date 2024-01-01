class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()
        p=3
        eachProcessorTime=[]
        for i in range(len(processorTime)):
            eachProcessorTime.append((tasks[p]+processorTime[i]))
            p+=4
        minimumTime=max(eachProcessorTime)
        return minimumTime