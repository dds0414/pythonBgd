from wand.image import Image

with Image(filename='pdf/1.pdf', width=2480, height=3509, resolution=300) as pdf:
    with pdf.convert('jpg') as image:
        print('format =', image.format)
        print('width =', image.width)
        print('height =', image.height)
        image.save(filename='result1.jpg')
