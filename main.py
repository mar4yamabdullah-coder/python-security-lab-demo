import hashlib
 password = "secret123"
 hashed = 
hashlib.md5(password.encode()).hexdigest()
 print(f"MD5 hash: {hashed}")
