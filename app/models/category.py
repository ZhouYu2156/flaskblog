from app import db
from slugify import slugify

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    slug = db.Column(db.String(100), unique=True)
    posts = db.relationship('Post', backref='category', lazy='dynamic')

    def __init__(self, **kwargs):
        super(Category, self).__init__(**kwargs)
        if self.name and not self.slug:
            self.slug = slugify(self.name)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    @staticmethod
    def init_slugs():
        """为所有没有slug的分类生成slug"""
        categories = Category.query.filter_by(slug=None).all()
        for category in categories:
            category.slug = slugify(category.name)
        db.session.commit() 