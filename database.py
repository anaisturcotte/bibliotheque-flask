import sqlite3

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

DBNAME = "bibliotheque.db"

def _select(requete, params=None):
    """ Exécute une requête type select"""
    with sqlite3.connect(DBNAME) as db:
        c = db.cursor()
        if params is None:
            c.execute(requete)
        else:
            c.execute(requete, params)
        res = c.fetchall()
    return res


def get_item_by(id_Createur):
    requete = """select Item.titre, Item.anneeSortie
                    from Item
                    where Item.idCreateur=?
                    order by Item.annee desc"""
    return _select(requete, params=(id_Createur))

def get_all_items():
    requete = """select Item.image, Item.titre, Item.anneeSortie, Type.nomType
                        from Item inner join type on Item.idType=Type.id
                        order by Item.titre asc;"""
    return _select(requete)

def get_all_films():
    requete = """select Item.image, Item.titre, Item.anneeSortie, Type.nomType 
                        from Item inner join type on Item.idType=Type.id 
                        where Type.nomType = 'Film'"""
    return _select(requete)

def get_all_livre():
    requete = """select Item.image, Item.titre, Item.anneeSortie, Type.nomType 
                        from Item inner join type on Item.idType=Type.id 
                        where Type.nomType = 'Livre'"""
    return _select(requete)

def get_all_musiques():
    requete = """select titre, anneeSortie from Item inner join type on Item.idType=Type.id where Type.nomType = 'Musique'"""
    return _select(requete)

def admin(tableName): 
    requete = f"""select * from {tableName}"""
    return _select(requete)

def titreColonne(tableName):
    requete= f"""PRAGMA table_info({tableName});"""
    return _select(requete)


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ajoutCreateur(FlaskForm):
    Qprenom = StringField("Prenom: ")
    Qnom = StringField("Nom: ")
    submit = SubmitField("Submit")

def ajoutCreateurRequete(Nom,Prenom):
    requete= f"""insert into createur (nom, prenom)
                    values ({Nom}, {Prenom})"""

# from:
# https://overiq.com/flask-101/form-handling-in-flask/