import re


def normalize(cyrillic_string):
    symbols = (u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
           u"abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA") 
    map = {}            
    for a, b in zip(*symbols):
        map.update({ord(a): b})
    translated = cyrillic_string.translate(map)
    new_string = re.sub(r'[^a-zA-Z0-9-]', '_', translated)
    return new_string


def main():
    print(normalize('аомвоалвАААААА555555лллллл;;;>>>>>//////'))
    
if __name__ == "__main__":
        main()   

    