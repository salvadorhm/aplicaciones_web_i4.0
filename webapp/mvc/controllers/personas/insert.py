import web

render = web.template.render("mvc/views/personas/", base="template")

class Insert():

    def GET(self):
        try:
            return render.insert()
        except Exception as e:
            return "Error"

    def POST(self):
        try:
            form = web.input()
            print(form)
            print(form.nombre)
            print(form.email)
        except Exception as e:
            return "Error"