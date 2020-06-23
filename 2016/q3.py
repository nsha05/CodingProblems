def palindromeDetector(string: str) -> bool:
     n = len(string)

     for i in range(n):
          if string[i] != string[n - 1 - i]:
               return False
     return True

word = input()

maxlen = 1

for i in range(len(word)):
     for j in range(len(word) - i):
          tump = word[i:i + j + 1]
          if palindromeDetector(tump) == True:
               maxlen = max(len(tump), maxlen)

print(maxlen)
