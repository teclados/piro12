'''1번
num = int(input())
answer = 0

for i in range(1, num+1):
    coef_num_list = list(map(int, str(i)))
    answer = i + sum(coef_num_list)
    if answer == num:
        print(i)
        break
    if i == num:
        print(0)

'''


'''2번
a = int(input())
count = 0
minimum=[a]
def cal(a):
    list = []
    for i in a:
        list.append(i-1)
        if i%3 == 0:
            list.append(i/3)
        if i%2 == 0:
            list.append(i/2)
    return list
 
while True:
    if a == 1:
        print(count)
        break
    temp = minimum[:]
    minimum = []
    minimum = cal(temp)
    count +=1
    if min(minimum) == 1:
        print(count)
        break
'''


'''3번
num = int(input())
lst = []
for i in range(num):
    lst.append(input())

for elm in lst:
    count = 0
    for j in elm:
        if j == '(':
            count += 1
        elif j == ')':
            count -= 1
        if count < 0:
            break
    if count == 0:
        print('YES')
    else:
        print('NO')
'''


'''카카오 1번
s = input()
half = len(s)//2
length_lst = []

for i in range(1, half+1):
    lst = [s[j:j+i] for j in range(0, len(s), i)]
    temp = lst[0]
    count = 0
    count_lst = []
    for k in range(1, len(lst)):
        if temp == lst[k]:
            count += 1
        else:
            temp = lst[k]
            count_lst.append(count)
            count = 0
    if count != 0:
        count_lst.append(count)
    length = len(s)
    for l in count_lst:
        if l != 0:
            length = length - l*i + 1
    length_lst.append(length)

if len(s) == 1:#길이가 1일때, 예외처리
    print(1)
else:
    print(min(length_lst))

'''


