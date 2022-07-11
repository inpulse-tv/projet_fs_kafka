from storage import connexion
from storage import celebrity_schema
import pysolr


def NotExistInSolr(url):
    """
        Cette fonstion sert à la verification si une image existe dans Solr ou pas,
    en utiisant url.
    :param url: le lien de l'image.
    :return: false si l'image existe déjà dans la base de donnée.
    """
    try :
        solr = pysolr.Solr('http://localhost:8983/solr/core_2')
        result = solr.search('urlImage:"' + url + '"')
        if result.docs:
            print('[STOP] Image already exists in Solr.')
            return False
        else:
            return True
    except Exception as e:
        print('[ERROR] There is an exception : ',e)

def NotExistInMongodb(url):
    """
            Cette fonstion sert à la verification si une image existe dans Mongodb ou pas,
        en utiisant url.
    :param url: le lien de l'image.
    :return: false si l'image existe déjà dans la base de donnée.
    """
    try:
        connexion.get_connexion()
        nmbr_image = celebrity_schema.Image.objects(url=url).count()
        if nmbr_image == 0:
            return True
        else:
            print('[STOP] Image already exists in Mongodb.')
            return False
    except Exception as e:
        print(str(e))

def NotExistInMongodbByFileName(filename):
    """
    cette fonction permet de savoir si une image contient déjà le nom donné en argument
    :param filename: le nom de l'image à chercher
    :return: True si aucune image ne contient ce nom, sinon elle retourne False.
    """
    image = celebrity_schema.Image.objects(name=filename).first()
    if image is not None:
        return False
    else:
        return True


