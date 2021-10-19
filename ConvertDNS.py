#converts a list of domains to Microsoft DNS debug log format: https://serverfault.com/questions/513538/what-do-the-numbers-in-parentheses-mean-in-my-windows-dns-debug-log
import io
import re
import csv
outputEncoding = "utf-8"
strinputFile = "g:\\test\dga.txt" #Input file to process
strOutPath = "g:\\test\\dga_formatted.txt" #output file
boolQuoteOutput = False #add quotes around each field
boolAddEscape = False #add escape character
domainLoc = 0

def writeCSV(fHandle, rowOut):
  if boolQuoteOutput == True:
    fHandle.write("\"" + rowOut.replace("|", "\",\"") + "\"\n")
  else:
    fHandle.write(rowOut.replace("|", ",") + "\n")

with io.open(strOutPath, "w", encoding=outputEncoding) as f:
  intRowCount = 0;
  with open(strinputFile, "rt", encoding="utf-8") as csvfile: #, encoding="utf-16"
      reader = csv.reader(csvfile, delimiter=',', quotechar='\"')
      for row in reader:
        tmpDomain = row[domainLoc]
        arrayDomain = re.split("\.", tmpDomain)
        outdomain = ""
        for subdomain in arrayDomain:
          if outdomain == "":
            outdomain = "(" + str(len(subdomain)) + ")" + subdomain
          else:
            outdomain = outdomain + "(" + str(len(subdomain)) + ")" + subdomain
        if boolAddEscape == True:
          outdomain= outdomain.replace("(","\\(").replace(")","\\)")
          writeCSV(f,outdomain + "\(0\)")
        else:
          writeCSV(f,outdomain + "(0)")