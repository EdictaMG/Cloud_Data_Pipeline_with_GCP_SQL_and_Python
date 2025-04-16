import re

#function to extract year from timestamp
def extract_year (date):
  pattern = r'\b\d{4}\b' # Regular expression pattern to match a four-digit year
  matches = re.findall(pattern, date)# Find all matches of the pattern in the input string
  if matches:# Extract the first match if available
      year = matches[0]
  else:
      print("No year found")
  return (year)