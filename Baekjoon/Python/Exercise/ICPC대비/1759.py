from itertools import combinations
def password(L, C, char_list):
    diction_1, diction_2 = list(), list()
    can_password = list()
    for i in range(C):
        if char_list[i] in ['a','e','i','o','u']:
            diction_1.append(char_list[i])
        else:
            diction_2.append(char_list[i])
    diction_1.sort()
    diction_2.sort()
    plus, minus = 1, L-1
    while True:
        #print(plus, minus)
        if minus < 2:
            break
        if len(diction_1) < plus or len(diction_2) < minus:
            pass
        else:
            can_dict1 = list(combinations(diction_1, plus))
            can_dict2 = list(combinations(diction_2, minus))
            for i in range(len(can_dict1)):
                for j in range(len(can_dict2)):
                    combine = list(can_dict1[i] + can_dict2[j])
                    combine.sort()
                    combine_result = ''.join(combine)
                    can_password.append(combine_result)
        plus += 1
        minus -=1
    can_password.sort()
    for i in range(len(can_password)):
        print(can_password[i])
L, C = map(int,input().split())
char_list = list(input().split())
password(L, C, char_list)