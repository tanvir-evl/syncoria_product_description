
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class ProductTemplateWebsiteDescription(models.Model):
    _inherit = 'product.template'

    
    web_description = fields.Text('Website Description', help="This description will show up on website as product description.")
    

