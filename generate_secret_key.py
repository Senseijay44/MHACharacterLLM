import secrets

# Generate a secure secret key
secret_key = secrets.token_hex(32)
print(f"Your generated secret key is: {secret_key}")
