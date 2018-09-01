from flask_restplus import reqparse

translation_arguments = reqparse.RequestParser()
translation_arguments.add_argument('source', type=str, required=True, default='en', help='Source language')
translation_arguments.add_argument('destination', type=str, required=True, default='fr', help='Destination language')
translation_arguments.add_argument('text', type=str, required=True, default='Hello', help='Text tobe convert')
