import logging
from api.restplus import api
from flask import request
from flask_restplus import Resource,abort
from api.translator.serializers import translation_model,goslate_translation_model
import goslate
from googletrans import Translator


log = logging.getLogger(__name__)
ns = api.namespace('trans', description='Dynamically translate text')
gs = goslate.Goslate()
translator = Translator()

supported_languages = {
    'en': 'English',
    'hi': 'Hindi',
    'fr': 'French',
    'es': 'Spanish',
    'cy': 'Welsh',
    'pt': 'Portuguese',
    'zh-CN':'Chinese Simplified',
    'zh-TW':'Chinese Traditional'
}


@ns.route('/translate')
class Translation(Resource):
    @api.response(200, 'Text translated successfully.')
    @api.expect(translation_model, validate=True)
    def post(self):
        """
        Dynamically translate text. Supported language set {en, zh-CN, zh-TW, hi, fr, es, cy, pt}
        """
        data = request.json
        source = data.get('source')
        destination = data.get('destination')
        text = data.get('text')

        if not source or source.isspace():
            abort(401, error='Source language code is required')
        if not destination or destination.isspace():
            abort(401, error='Destination language code is required')
        if not text or text.isspace():
            abort(401, error='Text is required')
        if source and not source.isspace():
            if source not in supported_languages:
                abort(401, error='Please select a supported language source - ' + getSupportedLanguage())

        if destination and not destination.isspace():
            if destination not in supported_languages:
                abort(401, error='Please select a supported language destination - ' + getSupportedLanguage())

        print("\n\nTranslating text, Source: " + source + " --> Dest: " + destination)
        print("Source Text : " + text)


        t = translator.translate(text, src=source, dest=destination)
        print("Destination Text : " + t.text)

        return {'source': source + ' - ' + supported_languages[source],
                'destination': destination + ' - ' + supported_languages[destination],
                'translated_text': t.text}, 200


@ns.route('/translate_goslate')
class TranslationGoslate(Resource):
    @api.response(200, 'Text translated successfully.')
    @api.expect(goslate_translation_model, validate=True)
    def post(self):
        """
        Dynamically translate text. Supported language set {en, zh-CN, zh-TW, hi, fr, es, cy, pt}
        """
        data = request.json
        destination = data.get('destination')
        text = data.get('text')

        if not destination or destination.isspace():
            abort(401, error='Destination language code is required')
        if not text or text.isspace():
            abort(401, error='Text is required')

        if destination and not destination.isspace():
            if destination not in supported_languages:
                abort(401, error='Please select a supported language destination - ' + getSupportedLanguage())

        print("\n\nTranslating text  --> Dest: " + destination)
        print("Source Text : " + text)
        dest_text = gs.translate('hello world', 'de')
        print("Destination Text : " + dest_text)

        return {'destination': destination + ' - ' + supported_languages[destination],
                'translated_text': dest_text}, 200





def getSupportedLanguage():
    res = ""
    for x in supported_languages:
        res = res +(x+':'+supported_languages[x])+" , "
    return res
