from odoo import api, fields, models

class BlogPost(models.Model):
    _inherit = "blog.post"

    cover_image = fields.Binary()
    filename = fields.Char("Filename")
    post_image_ids = fields.One2many(
        string="Post Images", comodel_name="product.image", inverse_name="blog_post_id"
    )

    @api.model
    def get_data(self, id=None, json_data=None):
        domain = []
        if id:
            domain.append(("id", "=", int(id)))
        posts = self.search(domain)
        if json_data:
            return list(map(lambda f: f._get_forum_data(), posts))
        return posts

    def _get_forum_data(self):
        return {
            "id": self.id,
            "name": self.name or "",
            "subtitle": self.subtitle or "",
            "content": self.content or "",
            "tags": list(map(lambda t: {"id": t.id, "name": t.name}, self.tag_ids)),
            "author": {"id": self.id, "name": self.name},
            "create_date": self.create_date,
        }
