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
    colonnes = db.titreColonne(tableName)
    return render_template("admin.html", items=items, colonnes=colonnes)

@app.route('/liste_livre.html')
def items_livre():
    print()
    items = db.get_all_livre()
    print(items)
    return render_template("liste_livre.html", items=items)

@app.route('/liste_film.html')
def items_film():
    print()
    items = db.get_all_films()
    print(items)
    return render_template("liste_film.html", items=items)

@app.route('/liste_musique.html')
def items_musique():
    print()
    items = db.get_all_musiques()
    print(items)
    return render_template("liste_musique.html", items=items)

@app.route('/liste_items.html')
def items():
    print()
    items = db.get_all_items()
    print(items)
    return render_template("liste_items.html", items=items)

# @app.route('/liste_items.html')
# def items():
#     print()
#     items = db.get_all_items()
#     print(items)
#     return render_template("liste_items.html", items=items)


###################### FORM POUR RENTRER DES DONNEES DANS LA BASE DEPUIS LE SITE ######################

@app.route('/form.html')
def items():
    print()
    items = db.get_all_items()
    print(items)
    return render_template("form.html", items=items)

#######################################################################################################
   
if __name__ == "__main__":
    app.run(debug=True)
