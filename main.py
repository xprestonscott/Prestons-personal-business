import os
import subprocess

BASE = r"C:\Users\prest\PycharmProjects\PythonProject"

# requirements.txt - tells Render what to install
with open(os.path.join(BASE, "requirements.txt"), "w", encoding="utf-8") as f:
    f.write("flask\ngunicorn\n")
print("requirements.txt created")

# .gitignore - don't upload junk to GitHub
with open(os.path.join(BASE, ".gitignore"), "w", encoding="utf-8") as f:
    f.write(".venv/\n__pycache__/\n*.pyc\nsubmissions.txt\n")
print(".gitignore created")

print("\nNow run these commands one at a time in the terminal:")
print("git init")
print("git add -A")
print('git commit -m "Initial commit"')