import sys
from collections import Counter

def analyze_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        words = []
        for line in lines:
            words.extend(line.strip().split())

        word_count = len(words)
        char_count = sum(len(word) for word in words)
        line_count = len(lines)
        most_common = Counter(words).most_common(5)

        print(f"Lines: {line_count}")
        print(f"Words: {word_count}")
        print(f"Characters: {char_count}")
        print("Top 5 Most Common Words:")
        for word, count in most_common:
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyzer.py <filename.txt>")
    else:
        analyze_file(sys.argv[1])