from odoo import models, fields, api
from datetime import date

class RendesVous(models.Model):

    _inherit ='calendar.event'
    _description ='rendez vous pour un patient'

    motif=fields.Char(string="motif")
    datedebutRDV = fields.Datetime(string="Date debut")
    datefinRDV = fields.Datetime(string="Date fin")
    rdv_patient_id = fields.Many2one('res.partner', string="Nom et Prénom")



