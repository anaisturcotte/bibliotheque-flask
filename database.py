import sqlite3

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField

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

def get_all_createur():
    requete = """select nom, prenom from Createur"""
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


class ajoutCreateur(FlaskForm):
    QCreateurPrenom = StringField("Prenom: ")
    QCreateurNom = StringField("Nom: ")
    QTypeType = SelectField("Type: ", choices= [ ('livre', 'Livre'), ('film', 'Film') ])
    QTypeGenre = StringField("Genre: ")
    QItemTitre = StringField("Titre: ")
    QItemAnneeSortie = StringField("Année de sortie: ")
    QItemDescription = StringField("Description: ")
    QItemNote = SelectField("Note sur 10", choices= [ ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),])
    QImage = StringField("Lien pour une image: ")
    submit = SubmitField("Submit")

def ajoutCreateurRequete(Nom,Prenom,Type,Genre,Image,Titre,AnneeSortie,Description,Note,):
    requete= f"""insert into Createur (nom, prenom)
                    values ('{Nom}', '{Prenom}')"""
    requete= f"""insert into Type (nomType, nomGenre)
                    values ('{Type}', '{Genre}')"""
    requete= f"""select idCreateur from Createur where Createur.nom = '{Nom}' and Createur.prenom = '{Prenom}' as 'IdCreateur'"""
    requete= f"""select idType from Type where Type.nomType = '{Type}' and Type.nomGenre = '{Genre}' as 'IdType'"""
    requete= f"""insert into Item (image, titre, anneeSortie, description, note, idCreateur, idType, idDisponibilite)
                    values ('{Image}', '{Titre}', {AnneeSortie}, '{Description}', '{Note}', 'IdCreateur', 'IdType', 0)"""
    print(requete)
    return _select(requete)

# from:
# https://overiq.com/flask-101/form-handling-in-flask/