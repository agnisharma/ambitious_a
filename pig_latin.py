original = input("Type in a sentence: ").strip().lower()

words = original.split()

new_words = []

for w in words:
    if w[0] in "aeiou":
        new_w = w + "yay"
        new_words.append(new_w)
    else:
        vowel_loc = 0
        for l in w:
            if l not in "aeiou":
                vowel_loc = vowel_loc + 1
            else:
                break
        con = w[:vowel_loc]
        remaining = w[vowel_loc:]
        new_w = remaining+con+"ay"
        new_words.append(new_w)

output = " ".join(new_words)
print(output)
        


