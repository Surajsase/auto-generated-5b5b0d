import json
import os
import sys
import subprocess

def count_vowels(text):
    """Count the total number of vowels in the given text."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

def count_words(text):
    """Count the total number of words in the given text."""
    return len(re.findall(r'\b\w+\b', text))

def print_statistics(email, feedback):
    """Print the statistics of the given email and feedback."""
    text = email + feedback
    words = count_words(text)
    vowels = count_vowels(text)
    print(f"{'Word Count':<20} | {words:>10}")
    print(f"{'Vowel Count':<20} | {vowels:>10}")

def main():
    # Read the context from the JSON file
    with open('context.json', 'r') as f:
        upstream_data = json.load(f)
    
    # Extract the email from the upstream data
    email = upstream_data.get('email', '')
    
    # Read the feedback from the file
    feedback_file_path = r'outputs\documents\5e982450-07a1-4d8a-acf2-3faef24997b8\feedback.txt'
    if os.path.exists(feedback_file_path):
        with open(feedback_file_path, 'r') as f:
            feedback = f.read()
    else:
        print("Feedback file not found.")
        return
    
    # Print the statistics
    print_statistics(email, feedback)

if __name__ == "__main__":
    main()