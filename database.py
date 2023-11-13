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
    requete = """select Item.titre, Itemm.anneeSortie
                        from Itemm
                        where Itemm.idType=?
                        order by Item.annee desc"""
    return _select(requete, params=(id_Type,))

def get_all_items():
    requete = """select item.titre, item.anneeSortie, Type.nomType
                        from item inner join type on item.idtype=Type.id"""
    return _select(requete)

def admin(poop):
    requete = f"""select * from {poop}"""
    return _select(requete)

