import unittest
import os
import sys
import subprocess

class TestStatistics(unittest.TestCase):
    def test_vowels(self):
        self.assertEqual(count_vowels('Hello World'), 3)
        self.assertEqual(count_vowels('AEIOU'), 5)
        self.assertEqual(count_vowels('bcdfg'), 0)

    def test_words(self):
        self.assertEqual(count_words('Hello World'), 2)
        self.assertEqual(count_words('This is a test'), 4)
        self.assertEqual(count_words(''), 0)

    def test_print_statistics(self):
        email = 'Hello World'
        feedback = 'This is a test'
        capturedOutput = ''
        def capture_output(*args, **kwargs):
            capturedOutput += args[0]
        import sys
        sys.stdout = open('capture.txt', 'w')
        print_statistics(email, feedback)
        sys.stdout.close()
        sys.stdout = sys.__stdout__
        with open('capture.txt', 'r') as f:
            capturedOutput = f.read()
        self.assertIn('Word Count', capturedOutput)
        self.assertIn('Vowel Count', capturedOutput)

if __name__ == "__main__":
    unittest.main()