from odoo import models, fields, api
from datetime import date




class fiche(models.Model):

     _inherit='res.partner'

     _description='fichier medical'

     patient_rdv_id = fields.One2many('calendar.event', 'rdv_patient_id', string="rdv_line")
     nomETprenom = fields.Char(string="Nom et Prénom")
     numfiche = fields.Char(string="N° Fiche :")
     assurancemaladie = fields.Char(string="Assurance maladie")
     cin=fields.Integer(string="CIN")
     birthdate_date=fields.Date(string="Date de naissance")
     adresse=fields.Text(string="Adresse")
     notes=fields.Text(string="Notes")
     image=fields.Binary(string="Image")
     antecedants=fields.Text(string="Antecedants")
     observations=fields.Text(string="Observations")
     consultation_id=fields.One2many('consultation.patient','fiche_id',string="consultation_id")
     ordonnnaceligne_id=fields.One2many('ordonnanceligne.patient','patient_id',string="Ordonnance")













