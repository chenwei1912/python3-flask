#!/usr/bin/env python3
#encoding=utf-8

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('用户名：', validators=[DataRequired(), Length(1, 45)])
    password = PasswordField('密码：', validators=[DataRequired(), Length(1, 128)])
    submit = SubmitField('登录')

class UserForm(FlaskForm):
    #id = IntegerField('ID：', validators=[DataRequired()])
    username = StringField('用户名：', validators=[DataRequired(), Length(1, 45)])
    password = PasswordField('密码：', validators=[DataRequired(), Length(1, 128)])
    role = IntegerField('角色：', validators=[DataRequired()])
    submit = SubmitField('提交')

class UserForm_Update(FlaskForm):
    #id = IntegerField('ID：', validators=[DataRequired()])
    username = StringField('用户名：', validators=[DataRequired(), Length(1, 45)])
    #password = PasswordField('密码：', validators=[DataRequired(), Length(1, 128)])
    role = IntegerField('角色：', validators=[DataRequired()])
    submit = SubmitField('提交')


if __name__ == '__main__':
    print('forms')
