from jinja2 import Enviroment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader("test"),
    autoescape=select_autoescape()
)
template = env.get_template("saludo.html")
datos