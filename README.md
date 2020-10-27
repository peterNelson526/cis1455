# cis1455


from images import Image

def grayscale(image):
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.setPixel(x, y, (lum, lum, lum))
    return image


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

def main():
    image = Image("smokey.gif")
    grayImage = grayscale(image)
    grayImage.draw()
    finalImage = sepia(grayImage)
    finalImage.draw()
    
if __name__ == "__main__":
    main()

