def solution(s):
    new_list = []
    word_list = s.split(" ")
    for word in words_list:
        new_words = ""
        for i in range(len(word)):
            if i % 2:
                new_words += word[i].lower()
            else:
                new_words += word[i].upper()
        new_list.append(new_words)
    return ' '.join(new_list)