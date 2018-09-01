import logging
from flask_restplus import Api
import settings

log = logging.getLogger(__name__)

api = Api(version='1.0', title='Text Translation APIs', description='Text translation API can dynamically translate text '
                                                                    'between language pairs (English - en, Chinese Simplified - zh-CN, '
                                                                    'Chinese Traditional - zh-TW, '
                                                                    'Hindi - hi, French - fr, Spanish - es, Welsh - cy, Portuguese - pt).')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500

