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


def get_item_by(id_Type):
    requete = """select Item.titre, Item.anneeSortie
                    from Item
                    where Item.idType=?
                    order by Item.annee desc"""
    return _select(requete, params=(id_Type,))

def get_all_items():
    requete = """select Item.titre, Item.anneeSortie, Type.nomType
                        from Item inner join type on Item.idType=Type.id"""
    return _select(requete)

def admin(tableName): 
    requete = f"""select * from {tableName}"""
    return _select(requete)

def titreColonne(tableName):
    requete= f"""PRAGMA table_info({tableName});"""
    return _select(requete)