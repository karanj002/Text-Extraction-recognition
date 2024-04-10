user_inputa=input("Enter the Text to be searched:")
file=open("C:\\ShareholderText.txt",'r')

for line in file:
    if user_input in line:
        print(line)

################################################

f=open("c:\\ShareholderText.txt","r")
user_inputa=input("Enter the Text to be searched:")
s=" "
count=1

L=f.readlines()

for i L:
    L2=i.split()
    if user input in L2:
        print("Line no. :",count,":",i)

    count+=1


######################################################


from rake_nltk import rake

r=Rake()
r.extract_keywords_from_text(extract_text())
for rating, keyword in r.get_ranked_phrases_with_scores():
    if rating>5:
        print(rating, keyword)

##########################################################


def read_line(fname, lnum):
  
  try:

    file = open(fname, "r")
    lines = file.readlines()
    file.close()
  # if an except occurs when attempting to read from the file, print an error
  # message  and terminate the function
  except:
    print("Error reading file.")
    return 
    total_lines = len(lines)
    
  if (lnum > total_lines):
    print(str(total_lines) + " file lines.")
    print("Can't read line " + str(lnum) + "!")
  
  else:
    line = lines[lnum - 1].rstrip('\n')
    print(line)

read_line("file.txt", 1)
filename = input("File: ")
line_number = int(input("Line: "))
read_line(filename, line_number)
