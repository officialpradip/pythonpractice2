'''3.	Write code that will print out the anagrams
 (words that use the same letters) from a paragraph of text. '''
 
from collections import defaultdict 
def Anagrams(words): 
	groupedWords = defaultdict(list) 
	for word in words: 
		groupedWords["".join(sorted(word))].append(word) 
	for group in groupedWords.values(): 
		print(" ".join(group))	 


if __name__ == "__main__": 
	arr = ["cat", "dog", "tac", "god", "act"] 
	Anagrams(arr)	 






