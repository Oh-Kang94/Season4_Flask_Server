from flask_restx import Resource, fields, abort
from ..services.ai_service import AI_Service
from ..config.Config import api


def ai_routes(ai_ns):
    @ai_ns.route("/review")
    class AiTest(Resource):
        @ai_ns.expect(api.model('AITEST', {
            'review': fields.String(description='100자 이내의 문장.', example = '영화가 재미 없습니다.')
        }))
        @ai_ns.doc(
            description = '댓글 분석으로, SCORE를 측정, 긍정 부정 분류',
            responses={
            400: "Bad request. need 'review'",
            500: "Cannot find the AI Model"
        })
        def post(self):
            try:
                review = api.payload['review']
            except KeyError:
                abort(400, error="Bad request. need 'review'")
            try:
                score = AI_Service.AI_predict(review)
            except OSError:
                abort(500, error="Cannot find the AI Model")
            if (score > 0.5):
                return {"results": "{:.2f}% 확률로 긍정 리뷰입니다.".format(score * 100)}
            else:
                return {"results": "{:.2f}% 확률로 부정 리뷰입니다.".format((1 - score) * 100)}
            
    @ai_ns.route("/search/")
    class Test(Resource):
        @ai_ns.expect(api.model('SearchAI', {
            'title': fields.String(description='100자 이내의 문장.', example = '잠')
        }))
        @ai_ns.doc(
            description = '댓글 분석으로, SCORE를 측정, 긍정 부정 분류',
            responses={
            400: "Bad request. need 'new_sentence'",
            500: "Cannot find the AI Model"
        })
        def post(self):
            try:
                title = api.payload['title']
            except KeyError:
                abort(400, error="Bad request. need 'title'")
            try:
                result = AI_Service.get_recommend_movie_list(title)
            except OSError:
                abort(500, error="Cannot find the AI Model")
            return {"results": result}
