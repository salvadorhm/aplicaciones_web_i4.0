import web

import mvc.models.personas as personas

model_personas = personas.Personas()

render = web.template.render("mvc/views/personas/", base="template")

class List():

    def GET(self):
        try:
            result = model_personas.select()
            return render.list(result)
        except Exception as e:
            print(e)
            return "Error"
   