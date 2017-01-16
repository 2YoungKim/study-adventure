num_list = ['일', '이', '삼', '사', '오', '오', '오']
num_list.reverse()
'''
tmp_list = list()
new_list = list()

if (len(num_list) > 1) : # 일의 자리 수가 아니라면,
    for i in range(1,len(num_list)+1) :
        if(( i % 4 ) != 0) :
            tmp_list.append(num_list[i - 1])
        else :
            tmp_list.append(num_list[i - 1])
            new_list.append(tmp_list)
            break

print(new_list)
'''
for i in range(1, len(num_list)+1) :
    if ((i % 4) == 1) :
        pass
    elif ((i % 4) == 2) :
        num_list[i-1] = num_list[i-1] + '십'
    elif ((i % 4) == 3) :
        num_list[i-1] = num_list[i-1] + '백'
    elif ((i % 4) == 0) :
        num_list[i-1] = num_list[i-1] + '천'
if(len(num_list) > 4) :
    num_list.insert(4,'만')
num_list.reverse()

#new list 만들기 4단위로 묶기



print(num_list)

# [ [1일 2십 3백 4천] 억 [5일 6십 7백 8천]만 [9일 9십 9백 9천] ]
