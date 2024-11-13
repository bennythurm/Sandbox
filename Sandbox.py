"""Restricted environment"""
#Create a restricted environment
#which limits the built in functions (whitelist)
restricted_env = {'__builtins__':{"print": print}}

#Safe code
CODE = 'print("Hello, world!")'

#Dangerous code
DANGEROUS_CODE = 'open("credentials.txt", "r")'

#Try to execute safe code
exec(CODE, restricted_env)

#Try to execute dangerous code
try:
    exec(DANGEROUS_CODE, restricted_env)
except NameError as e:
    print(f"Error: {e}")
