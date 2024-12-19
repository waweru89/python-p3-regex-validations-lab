import re

# Updated Name regex with negative lookahead to disallow multiple spaces
name = r"^(?!.*\s{2,})[A-Z][a-zA-Z' -]*(?: [A-Z][a-zA-Z' -]*)*$"
name_regex = re.compile(name)

# Phone number regex: Various formats of 10-digit phone numbers
phone_number = r"^(?:\(?\d{3}\)?[-.\s]?|\d{3}[-.\s]?)?\d{3}[-.\s]?\d{4}$"
phone_regex = re.compile(phone_number)

# Email address regex: Standard email formats starting with an alphabet
email_address = r"^[a-zA-Z][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
email_regex = re.compile(email_address)
