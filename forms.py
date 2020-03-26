from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

#DataRequired = field can not be empty
#Length = field between 2-20 characters only

class registration(FlaskForm):
    uname = StringField('Uname', validators=[DataRequired(),Length(min=2,max=20)])

    email = StringField('Email', validators=[DataRequired(),Email()])

    pwd = PasswordField('Pwd', validators=[DataRequired()])
    c_pwd = PasswordField('C_Pwd', validators=[DataRequired(), EqualTo('pwd')])

    sub = SubmitField('Submit')


class login(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])

    pwd = PasswordField('Pwd', validators=[DataRequired()])

    remb = BooleanField('Remb')

    sub = SubmitField('Login')
