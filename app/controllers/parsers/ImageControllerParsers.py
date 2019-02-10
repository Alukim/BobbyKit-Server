from app import imageControllerNamespace
from werkzeug.datastructures import FileStorage

fileParser = imageControllerNamespace.parser()
fileParser.add_argument('image', location = 'files', type = FileStorage, required = True)