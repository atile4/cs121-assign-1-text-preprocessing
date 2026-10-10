## UCI COMPSCI 121 Text Preprocessing Homework

### Functions

`tokenize()`: recieving a text file path as an input, outputs a list of the tokens present within the file.

- runs line by line, and for each line, apostrophes are combined and special characters (non alphnum or ascii) and replaced with whitespace, and added to a list.
- by reading line-by-line, the most amount of memory stored would only be the longest line in the text, versus storing the full text file in memory while processing.
- O(n \* m) time, where n is the number of lines in the file and m is the average character count in each line.

`computeWordFrequencies()`:

- Runs token by token
- runs in O(n + m log m), where:
  - n is the length of tokens
  - k is the number of unique tokens, and k <= n.
- In the worst case, where all tokens are unique, k would equal n. In that case, the runtime would be O(n + n log n).

`print_map()`:

- Outputs each item in the dictionary
- Runs in O(n) time, where n is the number of key value pairs in the dictionary. This also means that n is the number of unique tokens present in the file path text.

`compare_token()`

- Runs in O(n + m), where n is the number of characters in
  the first file after it's inputted and m is the number of characters in the second file.
- The function inside `compare_tokens()`, `tokenize()`, runs in linear time (runtime scales linearly to line count). Converting a list to a set and intersecting it with another set also occurs in linear time and are considered negligible to the overall runtime.

- Across all of this, it's O(# of chararcters in file) complexity. tokenize() is called twice, so it would be the count of characters for both files.

### How to run

```
python PartB.py <sample1.txt> <sample2.txt>
```

### Zip Command

```
tar.exe -a -c -f Assignment1.zip .git PartA.py PartB.py
```
