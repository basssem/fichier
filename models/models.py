from odoo import models, fields, api
from datetime import date




class fiche(models.Model):
     _name = 'fiche.patient'

     _description='fichier medical'
     _rec_name='nomETprenom'


     nomETprenom = fields.Char(string="Nom et Prénom")
     assurancemaladie = fields.Char(string="Assurance maladie")
     email = fields.Char(string="Email")
     phone = fields.Integer(string="Phone")
     mobile = fields.Integer(string="Mobile")
     function = fields.Char(string="Fonction")

     cin=fields.Integer(string="CIN")
     birthdate_date=fields.Date(string="Date de naissance")
     adresse=fields.Text(string="Adresse")
     notes=fields.Text(string="Notes")
     image=fields.Binary(string="Image")
     #email=fields.email(string="Email")
     antecedants=fields.Text(string="Antecedants")
     observations=fields.Text(string="Observations")
     consultation_id=fields.One2many('consultation.patient','fiche_id',string="consultation_id")
     registre_id=fields.One2many('registre.patient','patient_id',string="registre_id")
     rendezvous_line =fields.One2many('rendezvous.patient','patient_id', string="rendezvous_line")
     rdvpatient_id =fields.One2many('rdv.patient','patientrdv_id', string="rdv_line")
