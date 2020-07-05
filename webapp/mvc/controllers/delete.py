import web

render = web.template.render("mvc/views/")

class Delete():

    def GET(self):
        try:
            return render.delete()
        except Exception as e:
            return "Error"
            