import web

render = web.template.render("mvc/views/")

class Update():

    def GET(self):
        try:
            return render.update() # renderizando formulario.html
        except Exception as e:
            return "Error " + str(e.args)