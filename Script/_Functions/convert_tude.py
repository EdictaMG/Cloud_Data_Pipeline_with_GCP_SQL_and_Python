#function for converting latitude/longitude to decimals

#must FIRST run latitude or longitude through "standardize_tude" function/module; 
#then can run output as input for function "convert"
#example:
#1st step: munich_lat=standard(48°08′15″N)
#2nd step: convert(munich_lat)

def convert_tude (tude):
  degrees=int(tude[0:3])#assigns slice to degrees (index 0:3)
  minutes=int(tude[4:6])/60 #assigns slice to minutes (index 4:6) and divides by 60
  seconds = int(tude[7:9])/3600 # assings slice to secones (index 7:9) and divides by 3600
  multiplier=1 if tude[-1] in ['N', 'E'] else -1 #results are made negative for west and south directions
  tude_convert=multiplier * (degrees+minutes+seconds)
  return tude_convert
