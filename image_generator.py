# source: https://pythonprogramming.altervista.org/make-an-image-with-text-with-python/
# how to send image to Flask: https://stackoverflow.com/questions/7877282/how-to-send-image-generated-by-pil-to-browser
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import os
from flask import send_file


def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

def make_pil_image(person, plan, date, time, location):
    fnt = ImageFont.truetype(font='Avenir', size=35)
    image = Image.new(mode='L', size=(1080, 1080), color=255)
    draw = ImageDraw.Draw(image)
    confirmation_string = make_confirmation_string(person, plan, date, time, location)
    draw.multiline_text((250, 250), confirmation_string, font=fnt, fill='black', align='center')
    return image

def make_confirmation_string(person, plan="[to be decided]", date="[to be decided]", time="[to be decided]", location="[to be decided]"):
    return "{}\n" \
           "proposes that we shall go for {}\n" \
           "{}, {}\n" \
           "at {}".format(person, plan, date, time, location)