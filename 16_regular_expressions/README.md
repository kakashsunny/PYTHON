# Regular Expressions in Python

## Definitions & Concepts
Regular expressions (regex) are sequences of characters defining a search pattern. Python handles regex through the built-in `re` module.

## Common Regex Metacharacters
- `.` : Any character except newline.
- `^` : Start of string.
- `$` : End of string.
- `*` : Zero or more repetitions.
- `+` : One or more repetitions.
- `?` : Zero or one repetition.
- `\d` : Any digit.
- `\w` : Any alphanumeric character.
- `\s` : Any whitespace character.

## Core `re` Functions
1. **`re.match(pattern, string)`**: Checks if the pattern matches at the beginning of the string.
2. **`re.search(pattern, string)`**: Searches the entire string for a match.
3. **`re.findall(pattern, string)`**: Returns a list of all matches.
4. **`re.finditer(pattern, string)`**: Returns an iterator of match objects.
5. **`re.sub(pattern, replacement, string)`**: Replaces matches with replacement text.

## Syntax & Examples
```python
import re

text = "Call 555-0199 or 555-0100"
pattern = r"\d{3}-\d{4}"

# Find all matches
matches = re.findall(pattern, text)
print(matches) # ['555-0199', '555-0100']
```

## Best Practices
- Always prefix regex patterns with `r` (raw string) to prevent Python from parsing backslashes.
- Compile regular expressions using `re.compile()` if they are used repeatedly inside loops to improve performance.

## Common Mistakes
- Using `re.match` when `re.search` is needed (since `match` only looks at the start of the string).
- Not escaping metacharacters like dots or question marks (e.g. searching for a dot literal using `.` instead of `\.`).

## Interview Tips
- **Q**: What is the difference between greedy and non-greedy matching?
- **A**: Greedy operators (`*`, `+`) match as much text as possible. Adding a `?` after them (e.g., `*?`, `+?`) makes them non-greedy (lazy), matching the minimum text required.
