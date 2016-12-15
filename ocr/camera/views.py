from flask import Blueprint, request, jsonify
from . import camera
from . import ocr
import logging
from logging import Formatter, FileHandler
from ..decorators import templated
from werkzeug.datastructures import FileStorage

import os
import pytesseract
from PIL import Image, ImageFilter, ImageEnhance
from ocr import process_image

_VERSION = 1  # API version

@camera.route("/v{}/ocr".format(_VERSION), methods=["POST"])
def ocr():
    FileStorage(stream=request.files['data']).save(os.path.join('/Users/pdm640/workspaces/git/ocr/ocr/imgs','input.png'))

    image = Image.open('/Users/pdm640/workspaces/git/ocr/ocr/imgs/input.png')

    grayscale = image.convert('L')
    sharpen = ImageEnhance.Sharpness(grayscale).enhance(20)

    sharpen.save('/Users/pdm640/workspaces/git/ocr/ocr/imgs/sharpen.png')


    # crop = sharpen.crop((0, 90, 320, 150))
    # crop.save('/Users/pdm640/workspaces/git/ocr/ocr/imgs/crop.jpg')

    # edge_crop = image.filter(ImageFilter.FIND_EDGES).crop((0, 90, 320, 150))
    # edge_crop = ImageEnhance.Contrast(edge_crop).enhance(15)
    # edge_crop = ImageEnhance.Sharpness(edge_crop).enhance(20)
    # edge_crop.save('/Users/pdm640/workspaces/git/ocr/ocr/imgs/edges.jpg')

    text = pytesseract.image_to_string(sharpen, config='digits')
    print(text)

    # for string in text.split('\n'):
    #     if len(string.split(' ')) > 4:
    #         print(string)

    # ID card
    for string in text.split('\n'):
        for number in string.split(' '):
            if len(number) == 9:
                print(number)

    return jsonify(())

@camera.route("/", methods=["GET"])
@templated('camera.html')
def camera():
    return dict()

