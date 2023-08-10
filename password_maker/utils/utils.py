import random, string

def randomChars(n):
   return ''.join(random.choices(string.ascii_letters + string.digits, k=n))