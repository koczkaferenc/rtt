from flask import Blueprint, render_template, current_app
from .model import Animal

bp1 = Blueprint('bp1', __name__,
                url_prefix='/bp1',
                template_folder='templates',
                static_folder='static')


@bp1.route('/about')
def about():
    '''' an about page '''
    animal = Animal('Rabbit')
    return render_template('about.html', config=current_app.config, animal=animal)
