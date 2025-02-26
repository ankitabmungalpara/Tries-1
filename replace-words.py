"""

In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. 
For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. 
If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

 
Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
 

Constraints:

1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case letters.
1 <= sentence.length <= 106
sentence consists of only lower-case letters and spaces.
The number of words in sentence is in the range [1, 1000]
The length of each word in sentence is in the range [1, 1000]
Every two consecutive words in sentence will be separated by exactly one space.
sentence does not have leading or trailing spaces.


Time Complexity: O(N * M), where N is the number of words in the sentence and M is the number of dictionary roots.  
Space Complexity: O(N), as we store the modified sentence as a list of words.

Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No

"""


# Approach: 
# split the sentence into words and iterate through each word, checking if any root in the dictionary is a prefix of the word.  
# If a root is found and is shorter than the original word, we replace the word with that root.  
# Finally, join the modified words back into a sentence and return it.  


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        sentence = sentence.split()
        for i in range(len(sentence)):
            successor = sentence[i]

            for root in dictionary:
                if successor.startswith(root) and len(root) < len(successor):
                    successor = root

            sentence[i] = successor

        return ' '.join(sentence)

