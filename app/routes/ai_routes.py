from flask_restx import Resource, fields, abort
from ..services.ai_service import AI_Service
from ..config.Config import api


def ai_routes(ai_ns):
    @ai_ns.route("/ai")
    class aiTest(Resource):
        @ai_ns.expect(api.model('SentimentAnalysis', {
            'new_sentence': fields.String(description='100자 이내의 문장.', example = '영화가 재미 없습니다.')
        }))
        @ai_ns.doc(responses={
            400: "Bad request. need 'new_sentence'",
            500: "Cannot find the AI Model"
        })
        def post(self):
            try:
                new_sentence = api.payload['new_sentence']
            except KeyError:
                abort(400, error="Bad request. need 'new_sentence'")
            try:
                score = AI_Service.AI_predict(new_sentence)
            except OSError:
                abort(500, error="Cannot find the AI Model")
            if (score > 0.5):
                return {"results": "{:.2f}% 확률로 긍정 리뷰입니다.".format(score * 100)}
            else:
                return {"results": "{:.2f}% 확률로 부정 리뷰입니다.".format((1 - score) * 100)}
