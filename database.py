import sqlite3

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
                        from Item inner join type on Item.idType=Type.id"""
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

# def insertIntoItems(valeurs):
#     requete= f"""insert into Item (titre, anneeSortie, description, note) values ({titre}, {annee_sortie}, {description}, {note})"""
#     id_type= idItem.idType
#     id_createur= idItem.idCreateur
# def insertIntoType(valeurs2):
#     requete= f"""insert into Type (idType, nomType, nomGenre) values ({id_type}, {nom_type}, {nom_genre})"""
# def insertIntoCreateur(valeurs3):
#     requete= f"""insert into Createur (idCreateur, prenom, nom) values ({id_createur}, {prenom}, {nom}"""

################### FORM ######################

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


# class Questions(FlaskForm):
#     titre = StringField('Titre :', validators=[DataRequired(), Length(1, 20)])
#     genre = StringField('Genre :', validators=[DataRequired(), Length(1, 20)])
#     type = SelectField('Type', choices=[('livre', 'Livre') ('film', 'Film')])
#     createurNom = StringField('Createur nom :', validators=[DataRequired(), Length(1, 20)])
#     createurPrenom = StringField('Createur prenom:', validators=[DataRequired(), Length(1, 20)])
#     description = StringField('Description :', validators=[Length(1, 60)])
#     note = SelectField('Note', choices=[('0', '0') ('1', '1') ('2', '2') ('3', '3') ('4', '4') ('5', '5') ('6', '6') ('7', '7') ('8', '8') ('9', '9') ('10', '10')])
#     anneSortie = StringField('Date de sortie :', validators=[DataRequired(), Length(0, 5)])
#     submit = SubmitField('Submit')


class questions(FlaskForm):
    # pour l'instant on va juste ajouter un createur :
    # on definit les 'questions' : (validators=[DataRequired()  ->  sert a verifier que le champ est pas vide)
    createurNom = StringField('Createur nom :', validators=[DataRequired()])
    createurPrenom = StringField('Createur prenom:', validators=[DataRequired()])
    submit = SubmitField('Submit') # bouton pour submit le form

    # le form va etre sur la page form.html