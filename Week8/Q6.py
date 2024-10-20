vowels = "AEIOUaeiou"
freq = {}
try:
    f1 = open('file1.txt', 'r')
    for line in f1:
        for char in line:
            if char != " " and char in vowels:
                if char not in freq:
                   freq[char] = 1
                else:
                    freq[char] += 1

    max_vowel = max(freq, key=freq.get)
    print(max_vowel, freq[max_vowel])
except Exception as e:
    print('An error has Occured', e)
finally:
    f1.close()