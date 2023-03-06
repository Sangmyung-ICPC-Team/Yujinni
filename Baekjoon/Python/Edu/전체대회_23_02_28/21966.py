n=int(input())
s=input()
if len(s)<=25:
    print(s)
else:
    get=s[11:-11]
    if '.' in get[:-1]:
        print(s[:9]+'......'+s[-10:])
    else:
        print(s[:11]+'...'+s[-11:])
            