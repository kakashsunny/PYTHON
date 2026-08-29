# Regular Expressions Examples and Practice
import re

# 1. Matching and Searching
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
test_string = "My emails are bob@test.com and alice.jones@work.org"

# Find all emails
emails = re.findall(email_pattern, test_string)
print("Emails found:", emails)

# 2. String substitution (sub)
# Mask credit card digits
card_text = "My account numbers are 1234-5678-9012 and 9876-5432-1098"
masked_text = re.sub(r"\d{4}-\d{4}-\d{4}", "XXXX-XXXX-XXXX", card_text)
print("Masked:", masked_text)

# 3. Match Groups
date_pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
match = re.search(date_pattern, "Today is 2026-08-05")
if match:
    print("Match dict:", match.groupdict())
    print("Year:", match.group("year"))

# Practice: Check if string is a valid phone number (Format: XXX-XXX-XXXX)
def is_valid_phone(phone):
    pattern = r"^\d{3}-\d{3}-\d{4}$"
    return bool(re.match(pattern, phone))

print("Is 123-456-7890 valid?", is_valid_phone("123-456-7890"))
print("Is 12-456-7890 valid?", is_valid_phone("12-456-7890"))
