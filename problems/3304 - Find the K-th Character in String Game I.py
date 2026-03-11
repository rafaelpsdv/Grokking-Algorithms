def findKthCharacter(k, word):
    new_word = ''
    for letter in word:
        asc = ord(letter)
        if asc == 122:
            asc = asc - 25
        else:
            asc += 1    

        new_word += (chr(asc))

    word += new_word

    # Base case
    if len(word) >= k:
        return word[k - 1]
    
    return findKthCharacter(k, word)


print(findKthCharacter(500, 'z'))



class Solution:
    def kthCharacter(self, k, word=['a']):
        # Base case
        if len(word) >= k:
            return word[k - 1]

        new_word = []
        for letter in word:
            asc = ord(letter)
            if asc == 122:
                asc = asc - 25
            else:
                asc += 1

            new_word.append(chr(asc))

        word += new_word

        return self.kthCharacter(k, word)