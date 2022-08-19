from flask import Flask, request, render_template

appr = Flask(__name__)
appr.config.from_pyfile("config.py")


@appr.route('/')
def page_index():
    title = appr.config.get("PROJECT_NAME")
    description = appr.config.get("PROJECT_DESCRIPTION")
    return f"<h1>{ title }</h1><p>{ description }</p>"


appr.run()
