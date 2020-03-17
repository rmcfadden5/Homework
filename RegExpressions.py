import urllib.request
from urllib.request import urlopen
import re

#      Regular Expressions

regex = 'N'
regex2 = 'C'
regex3 = 'D'

regexvalid = '\|([0-9]{2}|-[0-9]{2}|[0-9]{2}\.[0-9]{2}|-[0-9]{2}\.[0-9]{2}|[0-9]{2}\.)\|\s\|\s\|'
regex2valid = '\|\s\|([a-z]{1})\|\s\|'
regex3valid = '\|\s\|\s\|(([0]{1}[1-9]{1}|[1]{1}[0-2]{1})/([1-2]{1}[0-9]{1}|[3]{1}[0-1]{1})/[1-2]{1}[0-9]{3})\|'

regexnonumber = '\|\s\|.\|.\|'
regexnochar = '\|.\|\s\|.\|'
regexbaddate = '\|[0-9]{1}\.[0-9]{1} \|\s\|(([0]{1}[1-9]{1}|[1]{1}[0-2]{1})/([1-2]{1}[0-9]{1}|[3]{1}[0-1]{1})/[1-2]{1}[0-9]{3})\|'


text_file = open("data.txt", "r")

#text_string = text_file.read()
line = text_file.readline()
cnt = -1

while line:
 
 line = text_file.readline()
 cnt += 1
#Need to use an if statement here. To check if regular expression is true
#if true then a second regular expression to check for the validity of the line is needed
#May need to make three seperate findit variables for each field type

#   Patterns Compile

 pattern = re.compile(regex)
 pattern2 = re.compile(regex2)
 pattern3 = re.compile(regex3)
 
 patternvalid = re.compile(regexvalid)
 pattern2valid = re.compile(regex2valid)
 pattern3valid = re.compile(regex3valid)

 patternnonumber = re.compile(regexnonumber)
 patternnochar = re.compile(regexnochar)
 patternbaddate = re.compile(regexbaddate)

#   Findits
 findit = re.findall(pattern, line)
 findit2 = re.findall(pattern2, line)
 findit3 = re.findall(pattern3, line)

 finditvalid = re.findall(patternvalid, line)
 findit2valid = re.findall(pattern2valid, line)
 findit3valid = re.findall(pattern3valid, line)

 finditnonumber = re.findall(patternnonumber, line)
 finditnochar = re.findall(patternnochar, line)
 finditbaddate = re.findall(patternbaddate, line)

#   IF statements

 if findit:
  
  if finditvalid:
   print("Line", cnt, "OK---", line)
  else:
   if finditnonumber:
    print("Line", cnt, "NO---No number in field---", line)
   else:
    print("Line", cnt, "NO---Invalid number---", line)
    
 
 if findit2:
  
  if findit2valid:
   print("Line", cnt, "OK---", line)
  else:
   if finditnochar:
    print("Line", cnt, "NO---No char in field---", line)
   else:
    print("Line", cnt, "NO---Invalid char---", line)
   
   
 if findit3:
  

  if findit3valid:
   print("Line", cnt, "OK---", line)
  else:
   if finditbaddate:
    print("Line", cnt, "NO---Only date should be in field---", line)
   else:
    print("Line", cnt, "NO---Invalid date---", line)
   
