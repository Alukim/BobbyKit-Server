from app import toolsCategoryControllerNamespace
from flask_restplus import fields

toolCategoriesResponseModel = toolsCategoryControllerNamespace.model('Tool categories response model', {
    'categories': fields.List(fields.String)
})