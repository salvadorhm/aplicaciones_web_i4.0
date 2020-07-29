import web

import mvc.models.personas as personas

model_personas = personas.Personas()

render = web.template.render("mvc/views/personas/", base="template")

class Update():

    def GET(self, id_persona):
        try:
            result = model_personas.view(id_persona)[0]
            return render.update(result)
        except Exception as e:
            return "Error"

    
    def POST(self, id_persona):
        try:
            form = web.input()
            id_persona = form.id_persona
            nombre = form.nombre
            email = form.email
            result = model_personas.update(id_persona, nombre, email)
            web.seeother('/personas_list')
        except Exception as e:
            print(e)
            return "Error"
   