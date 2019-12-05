from odoo import models, fields, api
from datetime import date

class RendesVous(models.Model):

    _inherit ='calendar.event'
    _description ='rendez vous pour un patient'


    rdv_patient_id = fields.Many2one('res.partner', string="Nom et Prénom")



