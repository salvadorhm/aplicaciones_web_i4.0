import web

urls = (
    '/', 'mvc.controllers.index.Index',
    
    '/personas_list', 'mvc.controllers.personas.list.List',
    '/personas_delete/(.*)','mvc.controllers.personas.delete.Delete',
    '/personas_insert','mvc.controllers.personas.insert.Insert',
    '/personas_update/(.*)','mvc.controllers.personas.update.Update',
    '/personas_view/(.*)','mvc.controllers.personas.view.View',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
