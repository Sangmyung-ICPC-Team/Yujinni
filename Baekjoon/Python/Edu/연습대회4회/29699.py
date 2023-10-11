def solution(n):
    message = 'WelcomeToSMUPC'
    if n < 14:
        result = message[n-1]
    else: 
        find_c = n % 14
        result = message[find_c-1]
    print(result)
n = int(input())
solution(n)