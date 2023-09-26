from flask_restx import Namespace

from ..routes.user_routes import user_routes
from ..routes.ai_routes import ai_routes
from ..routes.auth_routes import auth_routes
from ..routes.movie_routes import movie_routes
from ..routes.review_routes import review_routes
from ..routes.map_routes import map_routes

authorizations = {"Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}}

def register_namespaces(api):
    user_ns = Namespace("user", description= '유저 관련 정보')
    auth_ns = Namespace("auth", authorizations= authorizations, description="로그인 및 인증 관련")
    ai_ns = Namespace("ai", description= 'AI MODEL TEST용')
    movie_ns = Namespace('movie', description='Movie 관련 CRUD')
    review_ns = Namespace('review', description='Review 관련 CRUD')
    map_ns = Namespace('map', description='MAP 검색')

    user_routes(user_ns)
    auth_routes(auth_ns)
    ai_routes(ai_ns)
    movie_routes(movie_ns)
    review_routes(review_ns, auth_ns)
    map_routes(map_ns)

    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(ai_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(review_ns)
    api.add_namespace(map_ns)
