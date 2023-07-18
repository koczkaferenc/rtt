from flask import Blueprint, render_template, current_app

stat_page = Blueprint('stat_page', __name__,
                      template_folder='templates',
                      static_folder=None)


@stat_page.route("/<page>")
def print_page(page):
    try:
        print(page)
        return render_template(page + '.html', config=current_app.config)
    except Exception as e:
        return render_template('notfound.html', config=current_app.config, page=page), 404
