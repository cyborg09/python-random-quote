import random
def primary():
  print("Keep it logically awesome.")
  lst = 13
  rnd = random.randint(0,lst)
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes)
  print(quotes[rnd])

if __name__== "__main__":
  primary()
