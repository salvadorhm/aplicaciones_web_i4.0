import web

import mvc.models.personas as personas

model_personas = personas.Personas()

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
            nombre = form.nombre
            email = form.email
            model_personas.insert(nombre, email)
            web.seeother('/personas_list')
        except Exception as e:
            print(e)
            return render.insert()
            