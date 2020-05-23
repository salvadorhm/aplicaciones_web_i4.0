import web

class Visitas:
    def GET(self, name):
        try:
            cookie = web.cookies()
            print(cookie)
            if cookie.get("visitas"):
                visitas = int(cookie.get("visitas"))
                visitas += 1
                web.setcookie("visitas", str(visitas), expires="", domain=None)
                return "Visitas " + str(visitas)
            else:
                web.setcookie("visitas", str(1), expires="", domain=None)
                return "Visitas " + "1"
        except Exception as e:
            return "Error " + str(e.args)
