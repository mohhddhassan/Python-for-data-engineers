import re

text = "Contact me at user@example.com"
email = re.findall(r"[a-zA-Z0-9._]+@[a-z]+\.[a-z]+", text)
print(email)
