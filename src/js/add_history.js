odoo.define('caravans_history.add_history', function (require) {
    var PublicWidget = require('web.public.widget');
    var AddHistory = PublicWidget.Widget.extend({
        selector: '.add_history_js',
        start: function () {
            const container = this.el
            const form = new Form(container)
            form.onComplete = () => {
                console.log(form.result)
                setTimeout(() => window.location.href = form.result.url,2000)
            }
        }
    })
    PublicWidget.registry.add_history = AddHistory
    return AddHistory
})