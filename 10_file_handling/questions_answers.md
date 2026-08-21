# Questions & Answers: File Handling

## MCQs
1. **What happens if you open a non-existent file in `'a'` mode?**
   - A) Raises `FileNotFoundError`
   - B) Creates a new file
   - C) Returns `None`
   - D) Hangs execution
   - **Answer**: B
   - **Explanation**: Append (`'a'`) and Write (`'w'`) modes will create the file if it does not exist.

2. **Which method is used to move the file cursor to a specific position?**
   - A) `tell()`
   - B) `seek()`
   - C) `move()`
   - D) `reset()`
   - **Answer**: B
   - **Explanation**: `seek(offset, whence)` changes the file cursor position. `tell()` returns the current position.

## Beginner & Intermediate Questions
### Q1: What is the benefit of opening a file in binary mode (`'rb'` or `'wb'`)?
**Answer**: Binary mode reads/writes raw bytes without translating newlines (`\n` to platform-specific endings) or encoding characters. It is required for media files (images, audio, zip files).

### Q2: What does `f.flush()` do?
**Answer**: It forces the buffer's write contents to be written to the disk immediately without waiting for the file to be closed.

## Coding Practice & Solutions
### Problem: Write a Python program to count the number of words in a text file.
**Solution**:
```python
def count_words_in_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return len(f.read().split())
    except FileNotFoundError:
        return 0
```
