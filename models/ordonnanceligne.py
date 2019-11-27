from odoo import models, fields, api
from datetime import date
class Ordonnaceligne(models.Model):

    _name ='ordonnanceligne.patient'
    _description='ligne -medicament- ordonnace pour un patient'

    ordonnance_ordonnanceligne_id = fields.One2many('ordonnance.patient', 'ordonnanceligne_ordonnance_id',
                                                   string="Ordonnance")
    consultation_ordonnanceligne_id = fields.Many2one('consultation.patient', string="consultation_ordonnanceligne_id")
