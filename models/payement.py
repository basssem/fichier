from odoo import models, fields, api
from datetime import date



class Payement(models.Model):

     _inherit='account.invoice'
     _description='facturation et payement'




