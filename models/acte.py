from odoo import models, fields, api
from datetime import date

class Acte(models.Model):
    _name='acte.patient'
    _description='acte pour patient dans une consultation'
    _rec_name='nomActe'
    nomActe=fields.Char(string="Acte")
    id=fields.Integer(string="idd")