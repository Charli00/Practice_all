import sys
import os

name = sys.argv[1]
print(f"Hello, {name}!")




user = os.getenv("PASSWORD")
print(f"Logged in as: {user}")

print(os.getenv("API_KEY"))
