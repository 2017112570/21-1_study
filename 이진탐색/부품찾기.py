''' 이진 탐색 이용 X '''
# n = int(input())
# n_list = list(map(int,input().split()))

# m = int(input())
# m_list = list(map(int,input().split()))

# result = []

# for i in m_list:
#     if i in n_list:
#         result.append('yes')
#     else:
#         result.append('no')

# for i in result:
#     print(i,end=' ')


''' 이진 탐색 풀이 '''
def binary_search(arr,target,start,end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
arr = list(map(int,input().split()))
arr.sort()

m = int(input())
m_list = list(map(int,input().split()))

for i in m_list:
    result = binary_search(arr,i,0,n-1)
    
    if result != None:
        print('yes',end=' ')
    else:
        print('no',end=' ')