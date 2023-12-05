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
        c.close()
    return res

def _update(requete, params=None):
    """ Exécute une requête type insert/update"""
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()

    try:
        # Assuming you have a table named 'createur'
        cursor.execute(requete, params)
        conn.commit()
    finally:
        conn.close()

def get_item_by(id_Createur):
    requete = """select Item.titre, Item.anneeSortie
                    from Item
                    where Item.idCreateur=?
                    order by Item.annee desc"""
    return _select(requete, params=(id_Createur))

def get_all_items():
    requete = """select Item.image, Item.titre, Item.anneeSortie, Item.description, Type.nomType, Type.nomGenre
                        from Item inner join type on Item.idType=Type.id
                        order by Item.titre asc;"""
    return _select(requete)

def get_all_films():
    requete = """select Item.image, Item.titre, Item.anneeSortie,Item.description, Type.nomGenre 
                        from Item inner join type on Item.idType=Type.id 
                        where Type.nomType = 'Film'"""
    return _select(requete)

def get_all_livre():
    requete = """select Item.image, Item.titre, Item.anneeSortie,Item.description, Type.nomGenre 
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

def ajoutCreateurRequete(Nom, Prenom, Type, Genre, Image, Titre, AnneeSortie, Description, Note):
    ajoutDeCreateur = f"""INSERT INTO Createur (nom, prenom)
                                VALUES (?, ?)"""
    print(Nom, Prenom)
    _update(ajoutDeCreateur, (Nom, Prenom))

    ajoutDeType = f"""INSERT INTO Type (nomType, nomGenre)
                            VALUES (?, ?)"""
    print(Type, Genre)
    _update(ajoutDeType, (Type, Genre))

    createur_id_query = f"""SELECT id
                           FROM Createur
                           WHERE nom = ? AND prenom = ?"""
    print(createur_id_query)
    createur_id = _select(createur_id_query, (Nom, Prenom))
    print(f"createur_id = {createur_id}")
    createur_id = createur_id[0][0]

    type_id_query = f"""SELECT id
                       FROM Type
                       WHERE nomType = ? AND nomGenre = ?"""
    print(type_id_query)
    type_id = _select(type_id_query, (Type, Genre))    
    print(f"type_id = {type_id}")
    type_id = type_id[0][0]

    insertionFinale = f"""INSERT INTO Item (image, titre, anneeSortie, description, note, idCreateur, idType, idDisponibilite)
                            VALUES (?, ?, ?, ?, ?, ?, ?, 0)"""
    _update(insertionFinale, (Image, Titre, AnneeSortie, Description, Note, createur_id, type_id))

# from:
# https://overiq.com/flask-101/form-handling-in-flask/