# -*- coding: utf-8 -*-
from odoo import http

# class Fichier(http.Controller):
#     @http.route('/fichier/fichier/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fichier/fichier/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fichier.listing', {
#             'root': '/fichier/fichier',
#             'objects': http.request.env['fichier.fichier'].search([]),
#         })

#     @http.route('/fichier/fichier/objects/<model("fichier.fichier"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fichier.object', {
#             'object': obj
#         })