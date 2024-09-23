import re
from collections import Counter
import textstat  # Optional: Install using 'pip install textstat' for readability analysis

def text_analysis(text):
    #Word Count
    words = re.findall(r'\b\w+\b', text.lower())  # Split text into words (case-insensitive)
    word_count = len(words)

    #Character Count
    total_chars = len(text)
    total_chars_no_spaces = len(text.replace(" ", ""))

    # Sentence Count
    sentences = re.split(r'[.!?]+', text.strip())
    sentence_count = len([s for s in sentences if s])

    #Word Frequency
    word_freq = Counter(words)
    most_common_word = word_freq.most_common(1)

    #Longest Word
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]

    #Most Common Word
    common_word = word_freq.most_common(1)[0][0]

    #Readability (Optional)
    readability_score = textstat.flesch_reading_ease(text)
    readability_grade = textstat.flesch_kincaid_grade(text)

    # Output results
    print("\nText Analysis Results")
    print(f"Total Words: {word_count}")
    print(f"Total Characters (including spaces): {total_chars}")
    print(f"Total Characters (excluding spaces): {total_chars_no_spaces}")
    print(f"Total Sentences: {sentence_count}")
    
    print("\nWord Frequency:")
    for word, freq in word_freq.most_common(5):  # Show top 5 most common words
        print(f" - {word}: {freq}")
    
    print(f"\nLongest Word(s): {' '.join(longest_words)} ({max_length} characters)")
    print(f"Most Common Word(s): {common_word} ({most_common_word[0][1]} occurrences)")

    print(f"\nReadability Analysis (Flesch Reading Ease): {readability_score}")
    print(f"Readability Grade Level (Flesch-Kincaid): {readability_grade}")

# User Input
def main():
    print("Enter the text for analysis (multiple lines allowed, type 'done' when finished):")
    lines = []
    while True:
        line = input()
        if line.lower() == "done":
            break
        lines.append(line)
    text = "\n".join(lines)
    
    if text.strip():  # Check if input is valid
        text_analysis(text)
    else:
        print("Error: No text provided for analysis.")

if __name__ == "__main__":
    main()
