import datetime
import logging
import json
from odoo import http
from odoo.http import request, Controller
from werkzeug.utils import redirect
from odoo.tools.translate import _
from odoo.exceptions import UserError, AccessDenied

class CaravanForum(http.Controller):
    @http.route('/history/add', type='http', auth='user', website=True, method="POST")
    def index(self, **kw):
        blog_ids = request.env["blog.blog"].sudo().search([])
        return request.render('caravans_history.history_add',{
            "blog_ids": blog_ids
        })
    
    @http.route('/create/history', type='json', auth='user', website=True)
    def create_history(self, **post):
        values = {"blog_id": int(post['history-category']), 'name':post['history-title'], 'subtitle':post['history-description'],'content':post['history-content'],'cover_image':post['image'], 'is_published': True}
        newHistory = request.env['blog.post'].sudo().create(values)
        data = newHistory.cover_properties
        dataJson = json.loads(data)
        dataJson['background-image'] = f'url(/web/image?model=blog.post&id={newHistory.id}&field=cover_image)'
        newHistory.cover_properties = json.dumps(dataJson)

        return {'id': newHistory.id,
                'url': f"/blog/{newHistory.blog_id.id}/{newHistory.id}"
                }
    

class CaravanForumEdit(http.Controller):
    @http.route('/edit/history/<id>', type='http', auth='user', website=True, method="GET")
    def index(self, id):
        editCurrentHistory = request.env['blog.post'].sudo().browse(int(id))
        data = editCurrentHistory.cover_properties
        dataJson = json.loads(data)
        imageUrl = dataJson['background-image']
        newUrl = imageUrl.split("(")[1][:-1]
        blog_ids = request.env["blog.blog"].sudo().search([])
        return request.render('caravans_history.history_edit',{
            "editCurrentHistory": editCurrentHistory,
            "blog_ids": blog_ids,
            "newUrl": newUrl,
        })
    
    @http.route('/edit/history/successful/<id>', type='json', auth='user', website=True)
    def edit_history(self,id,**post):
        editedHistory = request.env['blog.post'].sudo().browse(int(id))
        values = {"blog_id": int(post['history-category']), 'name':post['history-title'], 'subtitle':post['history-description'],'content':post['history-content'],'cover_image':post['image'] if post.get('image') else editedHistory.cover_image, 'is_published': True}
        editedHistory.write(values)
        data = editedHistory.cover_properties
        dataJson = json.loads(data)
        dataJson['background-image'] = f'url(/web/image?model=blog.post&id={editedHistory.id}&field=cover_image)'
        editedHistory.cover_properties = json.dumps(dataJson)
        
        return {'id': editedHistory.id,
                'url': f"/blog/{editedHistory.blog_id.id}/{editedHistory.id}"
                }