# https://www.codewars.com/kata/596fba44963025c878000039

def contamination(text, char):
    return "" if not text or not char else char * len(text)
