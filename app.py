import sys

print(sys.path)

from flask import Flask
from flask_smorest import Api

from controller.bank_account import blp as BankAccountBlueprint
from controller.budget_group import blp as BudgetGroupBlueprint
from controller.budget_category import blp as BudgetCategoryBlueprint


app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "La French Enveloppe - API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(BankAccountBlueprint)
api.register_blueprint(BudgetGroupBlueprint)
api.register_blueprint(BudgetCategoryBlueprint)
