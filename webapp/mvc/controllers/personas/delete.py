import web

render = web.template.render("mvc/views/personas/", base="template")

class Delete():

    def GET(self):
        try:
            return render.delete()
        except Exception as e:
            return "Error"
            