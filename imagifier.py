from PIL import Image

#It'd be so nice if python supported enums, oh well.
DECODE = 0
ENCODE = 1

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

def chToPix(char):
    if char == "\n":
        return 0
    asNum = ord(char)
    pixels = asNum - 31
    return pixels

def pixToCh(pixels):
    if pixels == 0:
        return "\n"
    ch = pixels + 31
    return chr(ch)

mode = None

while True:
    selec = int(input("modes:\n1. Encode\n2. Decode\nselection: "))
    if selec == 1:
        mode = ENCODE
        break
    elif selec == 2:
        mode = DECODE
        break
    else:
        print("invalid input")

if mode == ENCODE:
    fileName = input("in file name: ")
    textFile = open(fileName, "r")
    text = textFile.read()
    textFile.close()
    im = Image.new("RGB", (91, len(text)))

    for y in range(im.size[1]):
        numPix = chToPix(text[y])
        for x in range(numPix):
            im.putpixel((x, y), WHITE)
        #im.putpixel((y, numPix), RED)
    
    im.save("out.png")

elif mode == DECODE:
    fileName = input("in file name: ")
    im = Image.open(fileName)
    outFile = open("out.txt", "w")

    for y in range(im.size[1]):
        pixels = 0
        for x in range(im.size[0]):
            if im.getpixel((x, y)) == WHITE:
                pixels += 1
            else:
                break
        outFile.write(pixToCh(pixels))

    outFile.close()
