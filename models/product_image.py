from odoo import fields, models


class ProductImage(models.Model):
    _inherit = "product.image"

    blog_post_id = fields.Many2one(
        string="Blog post", comodel_name="blog.post", ondelete="restrict"
    )
