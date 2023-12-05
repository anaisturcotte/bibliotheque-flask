from wtforms import SubmitField
import database as db

from flask import render_template, request, Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
# page de presentation renvoie a page index
def index():
    items = db.get_all_items()
    return render_template("index.html", items=items)

@app.route('/admin/<tableName>')
# route pour toutes les vues admin
def admin(tableName):
    items = db.admin(tableName)
    colonnes = db.titreColonne(tableName)
    return render_template("admin.html", items=items, colonnes=colonnes)
    
@app.route('/liste_livre.html')
# voir tous les livres
def items_livre():
    print()
    items = db.get_all_livre()
    print(items)
    return render_template("liste_livre.html", items=items)

@app.route('/liste_film.html')
# voir tous les films
def items_film():
    print()
    items = db.get_all_films()
    print(items)
    return render_template("liste_film.html", items=items)


@app.route('/liste_createur.html')
def createurs_film():
    print()
    createurs = db.get_all_createur()
    print(createurs)
    return render_template("liste_createur.html", createurs=createurs)

# originalemwenr musique mais abandonné
@app.route('/liste_musique.html')
def items_musique():
    print()
    items = db.get_all_musiques()
    print(items)
    return render_template("liste_musique.html", items=items)

@app.route('/liste_items.html')
# liste de tous les items films+livre
def items():
    print()
    items = db.get_all_items()
    print(items)
    return render_template("liste_items.html", items=items)

@app.route('/form.html', methods=['GET', 'POST'])
def ajoutCreateur():
    if SubmitField=="yes":
        return redirect(url_for('success'))
    return render_template('form.html')


@app.route('/success')
# page succes du formulaire
def success():
    db.ajoutCreateurRequete(
    request.args.get('createurNom'),
    request.args.get('createurPrenom'),
    request.args.get('typeType'),
    request.args.get('typeGenre'),
    request.args.get('itemImage'),
    request.args.get('itemTitre'),
    request.args.get('itemAnneeSortie'),
    request.args.get('itemDescription'),
    request.args.get('itemNote'),)
    return render_template('success.html')

# from:
# https://overiq.com/flask-101/form-handling-in-flask/

   
if __name__ == "__main__":
    app.run(debug=True)