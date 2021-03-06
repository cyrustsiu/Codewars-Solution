def decipher_this(string):
    
    import re
    code = re.findall(r'(\d+)',string)
    initial = [chr(int(i)) for i in code]
    
    remainder = re.sub(r'\d+','',string).split(' ')
    word = [r[-1] + r[1:-1] + r[0] if len(r) >= 2 else r for r in remainder]
    
    return ' '.join(map(lambda a,b: a+b, initial,word))
