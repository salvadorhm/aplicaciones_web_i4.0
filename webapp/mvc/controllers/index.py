import web

render = web.template.render("mvc/views/", base="template")

class Index():

    def GET(self):
        try:
            return render.index()
        except Exception as e:
            return "Error"
            