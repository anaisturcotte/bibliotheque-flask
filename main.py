from flask import render_template, request, Flask
import database as db

app = Flask(__name__)

@app.route('/')
def index():
    items = db.get_all_items()
    return render_template("liste_all_items.html", items=items)

@app.route('/admin/<tableName>')
def admin(tableName):
    items = db.admin(tableName)
    return render_template("admin.html", items=items)


#essayez d'appeler cette route avec par exemple l'URL : http://127.0.0.1:5000/films_de/13848
#13848 est l'id de Charles Chaplin
@app.route('/Items_de/<int:id_Createur>')
def items_de(id_Createur):
    print(id_Createur)
    items = db.get_items_by(id_Createur)
    print(items)
    return render_template("liste_Items.html", items=items)


   
if __name__ == "__main__":
    app.run()
