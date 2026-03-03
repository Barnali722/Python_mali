sentence = input("Enter the sentence (Capital letters): ").strip()

if sentence[-1] not in ['.', '?', '!']:
    print("Incomplete Sentence")
else:
    clean_sentence = sentence.replace('.', '').replace('?', '').replace('!', '').strip()
    words = clean_sentence.split()

    vowel_words = list(filter(
        lambda w: True if (w[0] in "AEIOU" or w[-1] in "AEIOU") else False,
        words
    ))

    other_words = list(filter(
        lambda w: False if (w[0] in "AEIOU" or w[-1] in "AEIOU") else True,
        words
    ))

    print("Starting and ending with vowels:", "".join(vowel_words))
    print("Frequency =", len(vowel_words)) #len is used to find total number of items
    print("Words without vowels:", "".join(other_words))