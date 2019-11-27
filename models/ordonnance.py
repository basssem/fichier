from odoo import models, fields, api
from datetime import date

class Ordonnance(models.Model):
    _name = 'ordonnance.patient'
    _description='ordonnance pour un patient'

    dateOrdonnce = fields.Datetime(string="Date", default=fields.Datetime.now(), readonly=True,)
    ordonnanceligne_ordonnance_id = fields.Many2one('ordonnanceligne.patient',string="Ordonnance")
    medicament_ordonnance_id = fields.Many2one('medicament.patient',string="Medicaments")
   # medecin_id=fields.Many2one(comodel_name='hr.employee',string="Medecin")
    dosage = fields.Char(string="Dosage")
    duree = fields.Integer(string="Durée en jours")

