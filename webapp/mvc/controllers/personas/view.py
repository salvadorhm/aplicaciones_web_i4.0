import web

import mvc.models.personas as personas

model_personas = personas.Personas()

render = web.template.render("mvc/views/personas/", base="template")

class View():

    def GET(self, id_persona):
        try:
            result = model_personas.view(id_persona)[0]
            return render.view(result)
        except Exception as e:
            return "Error"
   