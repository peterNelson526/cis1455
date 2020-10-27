# cis1455
def main():

def sepia(graypic):
    for y in range(graypic.getHeight()):
        for x in range(graypic.getWidth()):
            (red, green, blue) = graypic.getPixel(x,y)
            if red < 63:
                red = int(red * 1.1)
                blue = int(blue * 0.9)
            elif red < 192:
                red = int(red * 1.15)
                blue = int(blue * 0.85)
            else:
                red = min(int(red * 1.08), 255)
                blue = int(blue * 0.93)
            graypic.setPixel(x,y, (red, green ,blue))
            
    return graypic




if __name__ == '__main__':
    main()
