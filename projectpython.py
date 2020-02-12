from google.cloud import vision
from google.cloud.vision import types

image_uri = 'gs://cloud-vision-codelab/otter_crossing.jpg'

client = vision.ImageAnnotatorClient()
image = types.Image()
image.source.image_uri = image_uri

response = client.text_detection(image=image)

for text in response.text_annotations:
    print('=' * 79)
    print('"{}"'.format(text.description))

    vertices = (['({},{})'.format(v.x, v.y)
                 for v in text.bounding_poly.vertices])

    print('bounds: {}'.format(','.join(vertices)))