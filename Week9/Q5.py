try:
    f1 = open('file1.txt', 'r+')
    content = f1.read().lower()
    
    freq = {}
    for word in content:
        for char in word:
            if char != " ":
                if char not in freq:
                    freq[char] = 1
                else:
                    freq[char] += 1
    max_count = max(freq.values())
    max_alphabets = [char for char, count in freq.items() if count == max_count]

    print(max_alphabets, max_count)
    
except Exception as e:
    print('An Error has Occured:', e)
finally:
    f1.close()