from app import toolsCategoryControllerNamespace
from app.controllers.documentationModels.ToolCategoryControllerDocumentationModels import toolCategoriesResponseModel
from flask_restplus import Resource, marshal_with

class ToolCategoryController(Resource):

    @toolsCategoryControllerNamespace.marshal_with(toolCategoriesResponseModel)
    def get(self):
        return {
            'categories': [
                'Wiertarki',
                'Młotki',
                'Odkurzacze',
                'Frezarki',
                'Imadła',
                'Lutownice',
                'Myjki Ciśnieniowe',
                'Klucze',
                'Młoty udarowe',
                'Nożyce do blachy',
                'Opalarki',
                'Spawarki',
                'Pistolety do kleju',
                'Szczypce, nożyce, obcęgi',
                'Szlifierki, polerki',
                'Wkrętarki' 
            ] 
        }, 200