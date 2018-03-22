import mysql.connector as mysql
from connexion_root import config_mysql
import tkinter as tk

def initialiser():
    global conn, cur
    conn = mysql.connect(**config_mysql)
    cur = conn.cursor()
    cur.execute("USE gsb_formation")

def connexion(un_login, un_mdp):

    cur.execute(
        "SELECT COUNT(*) FROM utilisateurs WHERE login=%s AND mdp=%s",
        (un_login, un_mdp)
    )
    resultat = cur.fetchone()
    if resultat[0] == 1:
        return True
    else:
        return False

def budget_ind() :

    cur.execute("SELECT budget_ind FROM parametres")
    valeur_bim = cur.fetchone()[0]
    return valeur_bim

def enregistrer_bim(new_valeur_bim):

    cur.execute("UPDATE parametres SET budget_ind=%(bud)s",
                {'bud' : new_valeur_bim}
    )
    conn.commit()
    
def pourcentage() :
    
    cur.execute("SELECT PMS FROM parametres")
    valeur_pms = cur.fetchone()[0]
    return valeur_pms

def enregistrer_pms(new_valeur_pms):

    cur.execute("UPDATE parametres SET PMS=%(pms)s",
                {'pms' : new_valeur_pms}
    )
    conn.commit()

def liste_salaries() :

    liste = list()
    cur.execute("SELECT matricule, nom, prénom, nom_service FROM salaries, services WHERE salaries.num_service=services.num_service ORDER BY salaries.nom")
    salaries = cur.fetchall()
    for un_salarie in salaries:
        liste.append({'Matricule' : un_salarie[0], 'Nom' : un_salarie[1], 'Prenom' : un_salarie[2], 'Nom_service' : un_salarie[3]})
    return liste
 
def liste_formations() :

    liste = list()
    cur.execute("SELECT nom_formation, id_formation FROM formations")
    formations = cur.fetchall()
    for une_formation in formations:
        liste.append({'nom': une_formation[0], 'identifiant': une_formation[1]})
    return liste

def description_formation(id_form) :

    cur.execute("SELECT nom_formation, niveau, nature, date_formation, durée, coût FROM formations WHERE id_formation=%(id_form)s",
                {'id_form' : id_form}
    )
    description = cur.fetchall()
    liste = list()
    for une_ligne in description :
        liste.append(une_ligne[0])
        liste.append(une_ligne[1])
        liste.append(une_ligne[2])
        liste.append(une_ligne[3])
        liste.append(une_ligne[4])
        liste.append(une_ligne[5])
    return liste

def confirmation_demande(mat, nom, prenom) :

    cur.execute("SELECT COUNT(*) FROM salaries WHERE matricule=%(mat)s AND nom=%(nom)s AND prénom=%(prenom)s",
                {'mat' : mat, 'nom' : nom, 'prenom' : prenom}
    )
    resultat = cur.fetchone()
    if resultat[0] == 1:
        return True
    else:
        return False
def demande_inexistante(id_form, mat):

    cur.execute("SELECT COUNT(*) FROM demander WHERE matricule=%(mat)s AND id_formation=%(id_form)s",
                {'id_form' : id_form, 'mat' : mat}
    )
    resultat = cur.fetchone()
    if resultat[0] == 0:
        return True
    else:
        return False
    
def envoyer_demande(id_form, mat) :

    cur.execute("INSERT INTO demander (date_demande, id_état, id_formation, matricule, num_service) VALUES (curdate(), '6', %(id_form)s, %(mat)s, (SELECT num_service FROM salaries WHERE matricule=%(mat)s))",
                {'id_form' : id_form, 'mat' : mat}
    )
    conn.commit()
    
def titre_formation(id_form):

    cur.execute("SELECT nom_formation FROM formations WHERE id_formation=%(id)s",
                {'id' : id_form}
    )
    nom_formation = cur.fetchone()[0]
    return nom_formation

def en_cours_vide():

    cur.execute("SELECT COUNT(*) FROM demander WHERE id_état='6'")
    resultat = cur.fetchone()
    if resultat[0] == 0:
        return True
    else:
        return False

def nombre_en_cours():

    cur.execute("SELECT COUNT(*) FROM demander WHERE id_état='6'")
    resultat = cur.fetchone()
    return resultat
    
def demandes_en_cours():

    liste = list()
    cur.execute("SELECT nom, prénom, date_formation, nom_formation, id_demande FROM demander, salaries, formations WHERE salaries.matricule=demander.matricule AND formations.id_formation=demander.id_formation AND demander.id_état='6'")
    demandes = cur.fetchall()
    for une_demande in demandes:
        liste.append({'nom' : une_demande[0], 'prenom' : une_demande[1], 'nom_formation' : une_demande[3], 'date_formation' : une_demande[2], 'id_demande' : une_demande[4]})
    return liste

def confirmation_salarie(mat, nom, prenom):

    cur.execute("SELECT COUNT(*) FROM salaries WHERE matricule=%(mat)s AND nom=%(nom)s AND prénom=%(prenom)s",
                {'mat' : mat, 'nom' : nom, 'prenom' : prenom}
    )
    resultat = cur.fetchone()
    if resultat[0] == 1:
        return True
    else:
        return False
    
def enregistrer_nouveau_salarie(id_demande, mat):

    cur.execute("UPDATE demander SET matricule=%(mat)s WHERE id_demande=%(id)s",
                {'id' : id_demande, 'mat' : mat}
    )
    conn.commit()
    
def confirmation_formation(nom, id_formation):

    cur.execute("SELECT COUNT(*) FROM formations WHERE nom_formation=%(nom)s AND id_formation=%(id)s",
                {'id' : id_formation, 'nom' : nom}
    )
    resultat = cur.fetchone()
    if resultat[0] == 1:
        return True
    else:
        return False
    
def enregistrer_nouvelle_formation(id_formation, id_demande):

    cur.execute("UPDATE demander SET id_formation=%(id_f)s WHERE id_demande=%(id_d)s",
                {'id_f' : id_formation, 'id_d' : id_demande}
    )
    conn.commit()
    
def confirmer_demande(id_demande):

    cur.execute("UPDATE demander SET id_état='2' WHERE id_demande=%(id)s",
                {'id' : id_demande}
    )
    conn.commit()
    
def refuser_demande(id_demande):

    cur.execute("UPDATE demander SET id_état='1' WHERE id_demande=%(id)s",
                {'id' : id_demande}
    )
    conn.commit()
    
def annuler_demande(id_demande):

    cur.execute("UPDATE demander SET id_état='7' WHERE id_demande=%(id)s",
                {'id' : id_demande}
    )
    conn.commit()
    
def acceptees_vide():

    cur.execute("SELECT COUNT(*) FROM demander WHERE id_état='2'")
    resultat = cur.fetchone()
    if resultat[0] == 0:
        return True
    else:
        return False

def nombre_acceptees():

    cur.execute("SELECT COUNT(*) FROM demander WHERE id_état='2'")
    resultat = cur.fetchone()
    return resultat[0]
    
def formations_acceptees():

    liste = list()
    cur.execute("SELECT nom, prénom, date_formation, nom_formation, id_demande FROM demander, salaries, formations WHERE salaries.matricule=demander.matricule AND formations.id_formation=demander.id_formation AND demander.id_état='2'")
    demandes = cur.fetchall()
    for une_demande in demandes:
        liste.append({'nom' : une_demande[0], 'prenom' : une_demande[1], 'nom_formation' : une_demande[2], 'date_formation' : une_demande[3], 'id_demande' : une_demande[4]})
    return liste

def refusees_vide():

    cur.execute("SELECT COUNT(*) FROM demander WHERE id_état='1'")
    resultat = cur.fetchone()
    if resultat[0] == 0:
        return True
    else:
        return False

def nombre_refusees():

    cur.execute("SELECT COUNT(*) FROM demander WHERE id_état='1'")
    resultat = cur.fetchone()
    print(resultat)
    return resultat[0]
    
def formations_refusees():

    liste = list()
    cur.execute("SELECT nom, prénom, date_formation, nom_formation, id_demande FROM demander, salaries, formations WHERE salaries.matricule=demander.matricule AND formations.id_formation=demander.id_formation AND demander.id_état='1'")
    demandes = cur.fetchall()
    for une_demande in demandes:
        liste.append({'nom' : une_demande[0], 'prenom' : une_demande[1], 'nom_formation' : une_demande[2], 'date_formation' : une_demande[3], 'id_demande' : une_demande[4]})
    return liste

def annulees_vide():

    cur.execute("SELECT COUNT(*) FROM demander WHERE id_état='3' OR id_état='4' OR id_état='7'")
    resultat = cur.fetchone()
    if resultat[0] == 0:
        return True
    else:
        return False

def nombre_annulees():

    cur.execute("SELECT COUNT(*) FROM demander WHERE id_état='3' OR id_état='4' OR id_état='7'")
    resultat = cur.fetchone()
    print (resultat)
    return resultat[0]
    
def formations_annulees():

    liste = list()
    cur.execute("SELECT nom, prénom, date_formation, nom_formation, id_demande FROM demander, salaries, formations WHERE salaries.matricule=demander.matricule AND formations.id_formation=demander.id_formation AND (demander.id_état='7' OR demander.id_état='3' OR demander.id_état='4')")
    demandes = cur.fetchall()
    for une_demande in demandes:
        liste.append({'nom' : une_demande[0], 'prenom' : une_demande[1], 'nom_formation' : une_demande[2], 'date_formation' : une_demande[3], 'id_demande' : une_demande[4]})
    return liste

def effectuees_vide():

    cur.execute("SELECT COUNT(*) FROM demander WHERE id_état='5'")
    resultat = cur.fetchone()
    if resultat[0] == 0:
        return True
    else:
        return False

def nombre_effectuees():

    cur.execute("SELECT COUNT(*) FROM demander WHERE id_état='5'")
    resultat = cur.fetchone()
    return resultat[0]

def formations_effectuees():

    liste = list()
    cur.execute("SELECT nom, prénom, date_formation, nom_formation, id_demande FROM demander, salaries, formations WHERE salaries.matricule=demander.matricule AND formations.id_formation=demander.id_formation AND demander.id_état='5'")
    demandes = cur.fetchall()
    for une_demande in demandes:
        liste.append({'nom' : une_demande[0], 'prenom' : une_demande[1], 'nom_formation' : une_demande[2], 'date_formation' : une_demande[3], 'id_demande' : une_demande[4]})
    return liste

def annuler_formation(id_acceptee):

    cur.execute("UPDATE demander SET id_état='3' WHERE id_demande=%(id)s AND curdate()<echeance_annulation.date_annulation",
               {'id' : id_acceptee}
    )
    cur.execute("UPDATE demander SET id_état='4' WHERE id_demande=%(id)s AND curdate()>(date_formation-30)",
               {'id' : id_acceptee}
    )
    conn.commit()

def budget1():

    cur.execute("SELECT sum(coût*pourcentage_engagé/100) FROM formations, etats_formations, demander  WHERE etats_formations.id_état=demander.id_état AND formations.id_formation=demander.id_formation AND demander.num_service='s01'")
    result=cur.fetchone()
    if result[0]:
        return result[0]
    else :
        return 0

def budget2():

    cur.execute("SELECT sum(coût*pourcentage_engagé/100) FROM formations, etats_formations, demander  WHERE etats_formations.id_état=demander.id_état AND formations.id_formation=demander.id_formation AND demander.num_service='s02'")
    result=cur.fetchone()
    if result[0]:
        return result[0]
    else :
        return 0
    
def budget3():

    cur.execute("SELECT sum(coût*pourcentage_engagé/100) FROM formations, etats_formations, demander  WHERE etats_formations.id_état=demander.id_état AND formations.id_formation=demander.id_formation AND demander.num_service='s03'")
    result=cur.fetchone()
    if result[0]:
        return result[0]
    else :
        return 0
    
def budget4():

    cur.execute("SELECT sum(coût*pourcentage_engagé/100) FROM formations, etats_formations, demander  WHERE etats_formations.id_état=demander.id_état AND formations.id_formation=demander.id_formation AND demander.num_service='s04'")
    result=cur.fetchone()
    if result[0]:
        return result[0]
    else :
        return 0

def budget5():

    cur.execute("SELECT sum(coût*pourcentage_engagé/100) FROM formations, etats_formations, demander  WHERE etats_formations.id_état=demander.id_état AND formations.id_formation=demander.id_formation AND demander.num_service='s05'")
    result=cur.fetchone()
    if result[0]:
        return result[0]
    else :
        return 0

def budget6():

    cur.execute("SELECT sum(coût*pourcentage_engagé/100) FROM formations, etats_formations, demander  WHERE etats_formations.id_état=demander.id_état AND formations.id_formation=demander.id_formation AND demander.num_service='s06'")
    result=cur.fetchone()
    if result[0]:
        return result[0]
    else :
        return 0

def budget7():

    cur.execute("SELECT sum(coût*pourcentage_engagé/100) FROM formations, etats_formations, demander  WHERE etats_formations.id_état=demander.id_état AND formations.id_formation=demander.id_formation AND demander.num_service='s07'")
    result=cur.fetchone()
    if result[0]:
        return result[0]
    else :
        return 0

def liste_salar():
    
    liste = list()
    cur.execute("SELECT salaries.nom, salaries.prénom FROM salaries, demander WHERE demander.matricule=salaries.matricule AND demander.id_état='5'")
    salaries = cur.fetchall()
    for un_salarie in salaries:
        liste.append({'Nom' : un_salarie[0], 'Prenom' : un_salarie[1]})
    return liste
 
    











    
