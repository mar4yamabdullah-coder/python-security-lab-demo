import os
 password = "12345" # hardcoded password
 def insecure_func(user_input):
 eval("print(user_input)") # dangerous use of eval
 insecure_func("Hello, Bandit!"
