from odoo import models, fields, api
from datetime import date


class consultation(models.Model):
    _name='consultation.patient'
    _description='la consultation pour un patient'
    dateConsulation=fields.Datetime(string="Date", default=fields.Datetime.now(), readonly=True,)
    fiche_id=fields.Many2one('res.partner',string="fiche_id",readonly=True,)
    diadnostique=fields.Char(string="diagnostique")
    examenClinique=fields.Text(string="Examen Clinique")
    ordonnanceligne_consultation_id = fields.One2many('ordonnanceligne.patient','consultation_ordonnanceligne_id',string="Ordonnance")
    acte_id=fields.Many2many('acte.patient',string="Acte")
    radio_id=fields.Many2many('ir.attachment',string="Radio")
