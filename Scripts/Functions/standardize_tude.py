import re

#function for standardizing length of lon/lat ('dms'=degrees, minutes, seconds)
def standardize_tude (dms): 

    # regular expression to parse DMS components
    pattern = r'^\s*(\d{1,3})°\s*(\d{1,2})′?\s*(\d{1,2}(?:\.\d+)?)?″?\s*([NSEW])\s*$'
    match = re.match(pattern, dms)
    degrees, minutes, seconds, direction = match.groups()

    # convert to integers or floats as appropriate
    degrees = int(degrees)
    minutes = int(minutes) if minutes else 0
    seconds = float(seconds) if seconds else 0.0

    # padding degrees and minutes with zeros to make up the necesarry standard length
    degrees_str = f'{degrees:03d}'
    minutes_str = f'{minutes:02d}'
    seconds_str = f'{int(seconds):02d}'

    # construct standardized DMS string
    standardized_dms = f'{degrees_str}°{minutes_str}′{seconds_str}″{direction}'
    return standardized_dms