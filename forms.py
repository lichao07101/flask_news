#!/usr/bin/python
#coding=utf-8

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, RadioField
from wtforms.validators import DataRequired

class NewsForm(FlaskForm):
    """ 新闻表单 """
    title = StringField(label='新闻标题', validators=[DataRequired("请输入标题")],
        description="请输入标题",
        render_kw={"required": "required", "class": "form-control"})
    body = TextAreaField(label='新闻内容', validators=[DataRequired("请输入内容")],
        description="请输入内容",
        render_kw={"required": "required", "class": "form-control"})
    submit = SubmitField('提交')

