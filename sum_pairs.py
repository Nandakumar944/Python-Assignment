def find_unique_pairs(arr,target):
    s = set()
    p = set()

    for num in arr:
        c = target - num

        if c in s:
            a=tuple(sorted((num,c)))
            p.add(a)

        s.add(num)

    return [list(a) for a in p]

print(find_unique_pairs([1, 2, 3, 4, 5],5))
print(find_unique_pairs([2, 7, 11, 15],9)) 
print(find_unique_pairs([1, 1, 2, 3],4)) 
print(find_unique_pairs([3, 3, 3],6))  
print(find_unique_pairs([1, 2, 3],10))
























