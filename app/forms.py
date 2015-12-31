from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class LoginForm(Form):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
    submit = SubmitField('Login')


class AddServer(Form):
    server_name = StringField('name', validators=None)
    server_API_key = StringField('API key', validators=[DataRequired()])
    server_API_hash = StringField('API hash', validators=[DataRequired()])
    server_location = StringField('server location', validators=None)
    server_API_url = StringField('Solus VM client API URL', validators=[DataRequired()])
    server_description = TextAreaField('Server description', validators=None)
    server_submit = SubmitField('Add server')
    server_edit = SubmitField('Submit Changes')




