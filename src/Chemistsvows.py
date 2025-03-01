elements = {'h', 'he', 'li', 'be', 'b', 'c', 'n', 'o', 'f', 'ne', 'na', 'mg', 'al', 'si', 'p', 's', 'cl', 'ar', 'k',
            'ca', 'sc', 'ti', 'v', 'cr', 'mn', 'fe', 'co', 'ni', 'cu', 'zn', 'ga', 'ge', 'as', 'se', 'br', 'kr', 'rb',
            'sr', 'y', 'zr', 'nb', 'mo', 'tc', 'ru', 'rh', 'pd', 'ag', 'cd', 'in', 'sn', 'sb', 'te', 'i', 'xe', 'cs',
            'ba', 'hf', 'ta', 'w', 're', 'os', 'ir', 'pt', 'au', 'hg', 'tl', 'pb', 'bi', 'po', 'at', 'rn', 'fr', 'ra',
            'rf', 'db', 'sg', 'bh', 'hs', 'mt', 'ds', 'rg', 'cn', 'fl', 'lv', 'la', 'ce', 'pr', 'nd', 'pm', 'sm', 'eu',
            'gd', 'tb', 'dy', 'ho', 'er', 'tm', 'yb', 'lu', 'ac', 'th', 'pa', 'u', 'np', 'pu', 'am', 'cm', 'bk', 'cf',
            'es', 'fm', 'md', 'no', 'lr'}

for _ in range(int(input())):
    find_str = input()
    found = {0}
    for i in range(len(find_str)):
        if i in found:
            if find_str[i] in elements:
                found.add(i+1)
            if find_str[i:i+2] in elements:
                found.add(i+2)
    if len(find_str) in found:
        print("YES")
    else:
        print("NO")
