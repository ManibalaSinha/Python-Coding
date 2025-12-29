#def count_word(filename, word):
  # count = 0
with open("large.txt", "r") as f:
      for line in f:
         print(line.strip())
         #count += line.lower().split.count(word.lower())
   #return count
#print(count_word("a.txt", "hen"))        # read entire file
#print(f.read(10))      # read first 10 characters
#print(f.readline())    # read one line
#print(f.readlines())   # read all lines as list