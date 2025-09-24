from flask import Blueprint, render_template

orden_produccion_bp = Blueprint('orden_produccion', __name__, url_prefix='/ordenes-produccion')

@orden_produccion_bp.route('/')
def listar():
    """
    Muestra la lista de órdenes de producción.
    NOTE: Esta es una implementación placeholder.
    """
    # Se pasa una lista vacía por ahora
    return render_template('ordenes_produccion/listar.html', ordenes=[])
