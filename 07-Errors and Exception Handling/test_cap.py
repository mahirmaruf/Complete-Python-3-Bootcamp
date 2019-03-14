import unittest #First need to import the unittest (inbuilt)
import cap # imports the py script that we are testting

class TestCap(unittest.TestCase): #inherit from unittest.TestCase, inheritence of OOP
    
    # Number your tests
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text) # Call the function from your text
        self.assertEqual(result, 'Python') # Expectation, you need the result to equal your expected output
        
    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')
        
if __name__ == '__main__': # 
    unittest.main()
