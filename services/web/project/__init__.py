import logging

from flask import redirect
from project.server import server, User, login_manager, api

from project.ac_dash.ac_dash.api.routes import register_api, auth_bp
from project.ac_dash.ac_dash import mk_ac_plot
from project.ac_dash.ac_dash.ac_depth import mk_ac_depth
from project.ac_dash.ac_dash.views.login import mk_login_page
from project.ac_dash.ac_dash.views.success import mk_success
from project.ac_dash.ac_dash.views.logout import mk_logout_page


logger = logging.getLogger("defaultLogger")


ac_plot_route = "/dashing/"

mk_ac_depth(server, "/ac_depth/")
mk_ac_plot(server, ac_plot_route)
register_api(api)


login = mk_login_page(server, "/auth/login/")
logout = mk_logout_page(server, "/logout/")
success = mk_success(server, "/success/")

server.register_blueprint(auth_bp)


@server.route("/")
def root():
    return redirect(ac_plot_route)


@login_manager.user_loader
def user_loader(user_id):
    print(user_id)
    return User.query.get(user_id)


if __name__ == "__main__":
    server.run(host="0.0.0.0", debug=True)
