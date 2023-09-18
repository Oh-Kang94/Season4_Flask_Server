from flask_restx import Namespace

from ..routes.user_routes import user_routes
from ..routes.ai_routes import ai_routes

def register_namespaces(api):
    user_ns = Namespace("user")
    ai_ns = Namespace("ai")

    user_routes(user_ns)
    ai_routes(ai_ns)

    api.add_namespace(user_ns)
    api.add_namespace(ai_ns)
