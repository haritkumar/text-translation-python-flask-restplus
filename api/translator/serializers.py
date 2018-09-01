from flask_restplus import fields
from api.restplus import api

translation_model = api.model('Translation payload', {
    'source': fields.String(required=True,defaut='en', description='Source language, Default is en'),
    'destination': fields.String(required=True, description='Destination language, Default is en'),
    'text': fields.String(required=True, description='Text to be convert')
})


goslate_translation_model = api.model('Goslate Translation payload', {
    'destination': fields.String(required=True, description='Destination language, Default is en'),
    'text': fields.String(required=True, description='Text to be convert')
})