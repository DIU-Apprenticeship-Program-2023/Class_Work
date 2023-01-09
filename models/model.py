# -*- coding: utf-8 -*-

from odoo import fields, models


class StudentResult(models.Model):
  _name ="student.result"
  _description="student result"

  name=fields.Char(string="name",required=True)
  description=fields.Char(string="description",required=True)

  