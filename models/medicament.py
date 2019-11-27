from odoo import models, fields, api
from datetime import date


class Medicament(models.Model):
    _name = 'medicament.patient'
    _rec_name = 'nom'

    ordonnance_medicament_id = fields.One2many('ordonnance.patient', 'medicament_ordonnance_id', string="ord_med_id",
                                               readonly=True, invisible=True)
    nom = fields.Char(string="Medicament")


