import web

render = web.template.render("mvc/views/personas/", base="template")

class List():

    def GET(self):
        try:
            return render.list()
        except Exception as e:
            print(e)
            return "Error"
   