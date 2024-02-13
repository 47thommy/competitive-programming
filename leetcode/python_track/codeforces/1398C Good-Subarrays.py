from collections import defaultdict
t=int(input())
for _ in range(t):
  n=int(input())
  nums=input()
  prefix_sum=[]
  running_sum=0
  for i in range(n):
    running_sum+=int(nums[i])
    prefix_sum.append(running_sum)
  count=0
  visited={0:1}
  
  for j in range(len(prefix_sum)):
    if prefix_sum[j]-j-1 in visited:
      count+=visited[prefix_sum[j]-j-1]
    visited[prefix_sum[j]-j-1]=visited.get(prefix_sum[j]-j-1,0)+1
  print(count)
  
