from wand.image import Image

with Image(filename='pdf/2.pdf', resolution=300) as pdf:
    with pdf.convert('jpg') as image:
        image.save(filename='result2.jpg')
