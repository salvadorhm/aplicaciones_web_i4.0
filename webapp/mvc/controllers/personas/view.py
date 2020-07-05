import web

render = web.template.render("mvc/views/personas/", base="template")

class View():

    def GET(self):
        try:
            return render.view()
        except Exception as e:
            return "Error"
   