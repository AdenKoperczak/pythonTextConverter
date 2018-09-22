import binascii
import re
import string
digs = string.digits + string.ascii_letters
asciToMorse={"a":".-",
           "b":"-...","c":"-.-.",
           "d":"-..","e":".",
           "f":"..-.","g":"--.",
           "h":"....","i":"..",
           "j":".---","k":"-.-",
           "l":".-..","m":"--",
           "n":"-.","o":"---",
           "p":".--.","q":"--.-",
           "r":".-.","s":"...",
           "t":"-","u":"..-",
           "v":"...-","w":".--",
           "x":"-..-","y":"-.--",
           "z":"--..","0":"-----",
           "1":".----","2":"..---",
           "3":"...--","4":"....-",
           "5":".....","6":"-....",
           "7":"--...","8":"---..",
           "9":"----."}
morseToAsci=dict(zip(asciToMorse.values(),asciToMorse.keys()))
def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)

def textCon(text, tFrom, tTo):
    types=["asci","binary","decimal","hex","morse"]
    if(tFrom in types and tTo in types):
        if(tFrom=="asci"):
            asc = text
        elif(tFrom=="binary"):
             asc = ""
             for ch in re.split(r' ',text):
                 asc=asc+chr(int(ch,2))
        elif(tFrom=="decimal"):
            asc = ""
            for ch in re.split(r' ',text):
                asc=asc+chr(int(ch,10))
        elif(tFrom=="hex"):
            asc = ""
            for ch in re.split(r' ',text):
                asc=asc+chr(int(ch,16))
        elif(tFrom=="morse"):
            asc=""
            for ch in re.split(r' ',text):
                asc=asc+morseToAsci[ch]
#==============================================================================================
        if(tTo=="asci"):
            return(asc)
        elif(tTo=="binary"):
            out=""
            for ch in asc:
                out=out+str(int2base(int(binascii.hexlify(bytearray(ch,"utf-8")),16),2))+" "
            return(out)
        elif(tTo=="decimal"):
            out=""
            for ch in asc:
                out=out+str(int(binascii.hexlify(bytearray(ch,"utf-8")),16))+" "
            return(out)
        elif(tTo=="hex"):
            out=""
            for ch in asc:
                out=out+str(binascii.hexlify(bytearray(ch,"utf-8"))).replace("b'","").replace("'","")+" "
            return(out)
        elif(tTo=="morse"):
            out=""
            for ch in asc:
                out=out+asciToMorse[ch]+" "
            return(out)
    else:
        return("type not found")

