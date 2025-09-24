from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
)
from functools import wraps

web_bp = Blueprint(
    "web_bp", __name__, template_folder="../templates", static_folder="../static"
)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "usuario_id" not in session:
            flash("Por favor, inicia sesión para acceder a esta página.", "warning")
            return redirect(url_for("web_bp.login"))
        return f(*args, **kwargs)

    return decorated_function


@web_bp.route("/", methods=["GET"])
def index():
    return redirect(url_for("web_bp.dashboard"))


@web_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # NOTE: Dummy login for now
        session["usuario_id"] = "dummy_id"
        session["usuario_nombre"] = "Usuario de Prueba"
        flash("Inicio de sesión exitoso!", "success")
        return redirect(url_for("web_bp.dashboard"))

    return render_template("usuarios/login.html")


@web_bp.route("/logout")
def logout():
    session.clear()
    flash("Has cerrado la sesión.", "info")
    return redirect(url_for("web_bp.login"))


@web_bp.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
    # NOTE: Dummy data for now
    estadisticas = {
        "ordenes_en_proceso": 5,
        "ordenes_planificadas": 12,
        "alertas_stock_bajo": 2,
    }
    alertas = [
        {
            "titulo": "Nivel bajo de Harina",
            "mensaje": "Stock actual: 10kg. Stock mínimo: 20kg.",
            "fecha_creacion": "2023-10-27 10:00:00",
        },
        {
            "titulo": "Nivel bajo de Levadura",
            "mensaje": "Stock actual: 2kg. Stock mínimo: 5kg.",
            "fecha_creacion": "2023-10-27 09:30:00",
        },
    ]
    return render_template(
        "dashboard/index.html", estadisticas=estadisticas, alertas=alertas
    )
