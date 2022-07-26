def group_anagrams(words): #문자열 배열을 받아 애너그램 단위로 그루핑하는 함수
    sorted_words = []
    for i in range(len(words)):
        sorted_words += sorted(words[i])
        print(words[i])    
    # for i in range(len(words)-1):
    #     for j in range(len(words)-1-i):
    #         if sorted(words[i]) == sorted(words[j]):
    #             sorted_words.append(words[i])
    
    # return sorted_words


print(group_anagrams(['eat','tea','tan','ate','nat','bat']))
