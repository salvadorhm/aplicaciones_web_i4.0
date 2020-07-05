import web

urls = (
    '/', 'mvc.controllers.list.List',
    '/delete','mvc.controllers.delete.Delete',
    '/insert','mvc.controllers.insert.Insert',
    '/update','mvc.controllers.update.Update',
    '/view','mvc.controllers.view.View',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
