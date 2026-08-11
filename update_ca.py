import os
import re

filepath = r'C:\Tools\heteroagent\assets\index-DSB1OGKv.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'"coming soon on pons family"', '"0x99e353ffe80ae434f7d16c0428788B628EbcB5B2"', content, flags=re.IGNORECASE)
content = re.sub(r'coming soon on pons family', '0x99e353ffe80ae434f7d16c0428788B628EbcB5B2', content, flags=re.IGNORECASE)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully.")
