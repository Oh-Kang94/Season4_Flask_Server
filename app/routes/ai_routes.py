from flask_restx import Resource,fields
from ..services.ai_service import AI_Service
from ..config.Config import api

def ai_routes(ai_ns):
    @ai_ns.route("/ai")
    class aiTest(Resource):
        @ai_ns.expect(api.model('SentimentAnalysis', {
            'new_sentence': fields.String(description='New sentence to analyze')
        }))
        def post(self):
            new_sentence = api.payload['new_sentence']
            result = AI_Service.sentiment_predict(new_sentence)
            return {'sentiment_result': result}