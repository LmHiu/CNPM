import math

from flask import render_template, request
import dao
from app import app


@app.route("/")
def index():
    cates = dao.load_categories()

    cate_id = request.args.get('category_id')
    page_num = request.args.get('page', 1)
    kw = request.args.get('kw')
    prods = dao.load_products(cate_id=cate_id, kw=kw, page_num=int(page_num))
    num_of_prod = dao.count_query()
    page_size = app.config['PAGE_SIZE']

    return render_template('index.html', categories=cates, products=prods, num_of_prod=math.ceil(num_of_prod/page_size))


if __name__ == '__main__':
    app.run(debug=True)
