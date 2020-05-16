import web

urls = (
    '/(.*)', 'mvc.controllers.hello.Hello'
)
app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()
