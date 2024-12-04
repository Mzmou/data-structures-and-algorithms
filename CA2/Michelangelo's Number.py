n = int(input())
nums =list(map(int,input().split()))
loc = [0] * (n+1)
answer = 0
for i in range(n):
    loc[nums[i]] = i
first_stack =[]
second_stack = []
previous_nums = [-1] * (n+1)
for i in range(n,0,-1):
    while len(first_stack)>0  and loc[i] < loc[first_stack[-1]]:
        first_stack.pop()     
    if len(first_stack)>0:
        previous_nums[i] = loc[first_stack[-1]]
    first_stack.append(i)


print(0)
for i in range(1,n+1):
    while len(second_stack)>0  and loc[i] < loc[second_stack[-1]]:
        second_stack.pop()
        answer -= 1

    if previous_nums[i] != -1 and len(second_stack)==0 or(len(second_stack)>0 and previous_nums[second_stack[-1]] != previous_nums[i]):
            second_stack.append(i)
            answer += 1
    print(answer)