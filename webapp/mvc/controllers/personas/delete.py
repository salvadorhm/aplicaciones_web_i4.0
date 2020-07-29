import web

import mvc.models.personas as personas

model_personas = personas.Personas()

render = web.template.render("mvc/views/personas/", base="template")

class Delete():

    def GET(self, id_persona):
        try:
            result = model_personas.view(id_persona)[0]
            return render.delete(result)
        except Exception as e:
            print(e)
            return "Error"

    def POST(self, id_persona):
        try:
            form = web.input()
            id_persona = form.id_persona # hidden
            result = model_personas.delete(id_persona)
            web.seeother('/personas_list')
        except Exception as e:
            print(e)
            return "Error"
            