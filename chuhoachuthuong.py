x=str(input())
count_up=0
count_low=0
for c in x:
    if c.isupper():
        count_up+=1
    else:
        count_low+=1
if count_low>=count_up:
    print(x.lower())
else:
    print(x.upper())
            