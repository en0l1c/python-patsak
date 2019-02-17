
#Author: Konstantinos Gialantzis
#Last update: 17/02/2019



#ο λογος που δεν εγιναν ολοκληρες οι ασκησεις, αλλα οι μισες ειναι ερωτικη απογοητευση. Δεν ειναι οτι βαρεθηκα να τις κανω. Αν δε μου αρεσε δε θα διαλεγα αυτην τη σχολη. Απλα ενημερωνω, για να μην απογοητευσω!

import string
filename = raw_input("Enter your file name (e.x. hello.txt)\n(Make sure the file exists in the same folder with this python file): ")
file = open(filename, "r") #open the file user wants


letters = "abcdefghijklmnopqrstuvwxyz" #initialize and  declare all lower case letters to "letters" variable
for i in file:
  text_lower = i.lower() #convert all letters to lowercase
  text_nospace = text_lower.replace(" ", "") #remove all nospace characters from the text

  text_noPunctuation = text_nospace.strip(string.punctuation) #takes the text with no spaces and remove all punctuation from it
  for a in letters:
    if a in text_noPunctuation: #if there is not punctuation make count for each letter
      num = text_noPunctuation.count(a) #count how many times appears each letter in the main string(the file which contains the text user wants)
      print(a, num)
