from odoo import api, fields, models

class BlogBlog(models.Model):
    _inherit = "blog.blog"

    @api.model
    def get_data(self, id=None, json_data=None):
        domain = []
        if id:
            domain.append(("id", "=", int(id)))
        blogs = self.search(domain)
        if json_data:
            return list(map(lambda f: f._get_forum_data(), blogs))
        return blogs

    def _get_forum_data(self):
        return {"id": self.id, "name": self.name or ""}
