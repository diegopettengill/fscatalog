from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    category = SelectField('Category', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])