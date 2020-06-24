import web

urls = (
    '/', 'mvc.controllers.formulario.Formulario'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
