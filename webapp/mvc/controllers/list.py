import web

render = web.template.render("mvc/views/")

class List():

    def GET(self):
        try:
            return render.list()
        except Exception as e:
            return "Error"
   