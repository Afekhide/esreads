from flask.blueprints import Blueprint
from esreads.schemas import roles_schema, role_schema
from esreads.models.role import Role

role_blueprint = Blueprint('role', __name__, url_prefix='/api/roles')


@role_blueprint.route('/', methods=['GET'])
def all_roles():
    roles = Role.query.all()
    print('/roles/all called...')
    return roles_schema.dumps(roles)



