class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0 or len(words[0]) == 0: 
            return []
        result = []
        word_freq = {}
        for w in words:
            if w not in word_freq:
                word_freq[w] = 0
            word_freq[w] += 1 
        count = len(words)
        length = len(words[0])
        for i in range((len(s) - count * length)+1):
            seen = {}
            for j in range(count):
                next_index = i + j * length 
                word = s[next_index: next_index + length]
                
                if word not in word_freq: break 
                if word not in seen:
                    seen[word] = 0 
                seen[word] += 1 
                if seen[word] > word_freq.get(word, 0): break 
                if j+1 == count: result.append(i)
                    
            
        return result 