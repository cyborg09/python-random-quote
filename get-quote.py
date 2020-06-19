import random
def primary():
  #print("Keep it logically awesome.")
  lst = 13
  rnd = random.randint(0,lst)
  rnd1 = random.randint(0,lst)
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes)
  print(quotes[rnd]+quotes[rnd1])
  with open("quotes.txt",'a') as q:
  	q.write("\nFlyhigh in the sky\n")
  print("")

if __name__== "__main__":
  primary()
