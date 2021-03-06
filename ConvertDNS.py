#converts a list of domains to Microsoft DNS debug log format: https://serverfault.com/questions/513538/what-do-the-numbers-in-parentheses-mean-in-my-windows-dns-debug-log
import io
import re
import csv
outputEncoding = "utf-8"
strinputFile = "c:\\test\\domains.txt" #Input file to process
strOutPath = "c:\\test\\domains_formatted.txt" #output file
boolQuoteOutput = False #add quotes around each field
boolAddEscape = False #add escape character
domainLoc = 0

def writeCSV(fHandle, rowOut):
  if boolQuoteOutput == True:
    fHandle.write("\"" + rowOut.replace("|", "\",\"") + "\"\n")
  else:
    fHandle.write(rowOut.replace("|", ",") + "\n")

def dnsConvert(strDomainName, boolAddEscapeChar):
  arrayDomain = re.split("\.", strDomainName)
  outdomain = ""
  for subdomain in arrayDomain:
    if outdomain == "":
      outdomain = "(" + str(len(subdomain)) + ")" + subdomain
    else:
      outdomain = outdomain + "(" + str(len(subdomain)) + ")" + subdomain
  if boolAddEscapeChar == True:
    outdomain= outdomain.replace("(","\\(").replace(")","\\)")
    outdomain= outdomain + "\(0\)"
  else:
    outdomain= outdomain + "(0)"
  return outdomain
  
with io.open(strOutPath, "w", encoding=outputEncoding) as f:
  intRowCount = 0;
  with open(strinputFile, "rt", encoding="utf-8") as csvfile: #, encoding="utf-16"
      reader = csv.reader(csvfile, delimiter=',', quotechar='\"')
      for row in reader:
        if len(row) > domainLoc:
          tmpDomain = row[domainLoc]
          tmpDomain = dnsConvert(tmpDomain, boolAddEscape)
          writeCSV(f,tmpDomain)
