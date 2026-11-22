s=input('enter string:')
count=0
for i in s:
    if i in 'aeiouAEIOU':
        count=count+1
print('Number of vowels:', count)