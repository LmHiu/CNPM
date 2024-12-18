from app.models import Category, Product
from app import app


def load_categories():
    return Category.query.order_by("id").all()


def load_products(cate_id=None, kw=None, page_num=1):
    query = Product.query

    if cate_id:
        query = query.filter(Product.category_id == cate_id)

    if kw:
        query = query.filter(Product.name.contains(kw))

    page_size = app.config['PAGE_SIZE']
    start = (page_num - 1) * page_size
    query = query.slice(start, start + page_size)

    return query.all()

def count_query():
    return Product.query.count()
