#Jonathan Kelly, lab 5, jonathan.kelly2@marist.edu
# prompts user for sentence and calculates the length of the sentence, length of each word,
# and average word length

def main():
    
    s = str(input("Please enter a sentence: "))
    totalWords = len(s.split(" "))
    average = 0
    
    for x in s:
        average = average + len(x)
        
    average = (average - s.count(" "))/ totalWords
    
    print("Number of characters:", len(s))
    print("Number of words:",  totalWords)
    print("Average word length:", average)
    
main()