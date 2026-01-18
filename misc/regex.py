'''
Docstring for misc.regex
In Python regular expressions (regex), metacharacters are special characters that do not match themselves but instead indicate rules for pattern matching,
 serving as the building blocks for search criteria. 
Key metacharacters and their functions in Python regex include:

Quantifiers
These modify the number of occurrences of the preceding character or group. 
*: Matches zero or more occurrences (e.g., s* matches "", "s", "ss", etc.).
+: Matches one or more occurrences (e.g., s+ matches "s", "ss", etc., but not "").
?: Matches zero or one occurrence (e.g., s? matches "" or "s").
{m}: Matches exactly m occurrences (e.g., d{3} matches "123" but not "12" or "1234").
{m,n}: Matches between m and n occurrences (e.g., d{2,4} matches "12", "123", or "1234"). 

Anchors
These specify the position of a match within a string. 
^: Matches the start of the string or line (e.g., ^hello matches "hello world" but not "world hello").
$: Matches the end of the string or line (e.g., world$ matches "hello world" but not "hello world!").
\b: Matches a word boundary.
\B: Matches a non-word boundary. 

Character Classes and Alternation
These define sets of characters or alternatives. 
.: Matches any single character except a newline (unless a specific flag is set).
[]: Defines a set of characters to match a single character from (e.g., [abc] matches "a", "b", or "c"; [a-z] matches any lowercase letter).
|: Acts as an OR operator (e.g., cat|dog matches either "cat" or "dog"). 

Predefined Special Sequences
These are shorthand for common character sets, typically using a backslash \ followed by a letter. 
\d: Matches any digit (0-9).
\D: Matches any non-digit character.
\w: Matches any word character (alphanumeric and underscore: [a-zA-Z0-9_]).
\W: Matches any non-word character.
\s: Matches any whitespace character (space, tab, newline, etc.).
\S: Matches any non-whitespace character.

Escaping Metacharacters
To match a metacharacter as a literal character, you must escape it with a backslash (\). 
For instance, \. matches a literal period, and \\ matches a literal backslash. 
Using Python raw strings (prefixing the string literal with r, e.g., r'\.') is highly recommended to avoid conflicts with Python's own string escaping rules. 
'''

import re
def find_metacharacters(pattern, string):
    """
    Finds all occurrences of the given regex pattern in the provided string.

    Args:
        pattern (str): The regex pattern to search for.
        string (str): The string to search within.
    Returns:
        list: A list of all matches found.
    """
    return re.findall(pattern, string)

# Example usage:
if __name__ == "__main__":
    test_string = "The price is $100. Contact us at 123-456-7890."
    test_pattern = r'\$\d+'  # Pattern to find dollar amounts
    matches = find_metacharacters(test_pattern, test_string)
    print("Matches found:", matches) # Output: Matches found: ['$100']

# Demonstrating span() method
text = "The quick brown fox jumps over the lazy dog"
pattern = re.compile(r'fox')
match = pattern.search(text)

if match:
    start_pos, end_pos = match.span()
    print(f"Found 'fox' from position {start_pos} to {end_pos}")
    # Output: Found 'fox' from position 16 to 19

    matched_substring = text[start_pos:end_pos]
    print(f"Matched text: '{matched_substring}'")
    # Output: Matched text: 'fox'

else:
    print("No match found")