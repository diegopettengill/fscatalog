from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, HiddenField, \
    FileField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired
from catalog.models import Category


class ProductForm(FlaskForm):
    class Meta:
        model = Category

    title = StringField('Title', validators=[DataRequired()])
    slug = HiddenField("slug")
    description = TextAreaField('Description', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    category_id = SelectField('Category', coerce=int, validators=[
        DataRequired()])
    user_id = HiddenField("user_id")
    picture = FileField('Picture', validators=[FileAllowed([
        'jpg', 'png'], 'Images only!')])
