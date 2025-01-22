import os
import logging
from flask import Flask
from flask_restful import Api
from flask_login import UserMixin, LoginManager
from sqlalchemy.exc import IntegrityError


from project.ac_dash.ac_dash.users_mgt.users_mgt import (
    db,
    User as base,
    mk_user_table,
    add_user,
    show_users,
)

from project.ac_dash.ac_dash.data_mgt import (
    mk_flux_table,
    mk_gas_table,
    mk_cycle_table,
    mk_volume_table,
    apply_volume_table_trigger,
)

from project.temp_users import users as init_users

logger = logging.getLogger("defaultLogger")

# initiate flask server
server = Flask(__name__, static_folder="static")
server.config.from_object(os.getenv("FLASK_CONFIG", "default_config_module"))
api = Api(server)

# initiate DB
db.init_app(server)


# usermixin adds default methods that flask_login expects users to have
class User(UserMixin, base):
    pass


mk_user_table()
mk_flux_table()
mk_gas_table()
mk_cycle_table()
mk_volume_table()
apply_volume_table_trigger()

for user in init_users:
    add_user(user["username"], user["password"], user["email"], user["role"])

# initiate login manager
server.config["SECRET_KEY"] = "my_secret_key"
login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = "auth.login_route"
