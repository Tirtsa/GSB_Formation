import tkinter as tk
import mysql.connector as mysql
from connexion_root import config_mysql
import requetes as re
from tkinter import ttk

def initialiser_connexion():
    
    global win, accueil, bim, pms, salaries, catalogue, demandes, formations, gestion, liste, login, mdp
    
    #toutes les fenetres

    accueil = tk.Tk()
    accueil.title('accueil')
    accueil.minsize(100, 500)
    accueil.withdraw()
    
    win = tk.Toplevel(accueil)
    win.title('connexion')
    win.minsize(500, 500)
    
    bim = tk.Toplevel(accueil)
    bim.title('budget individuel maximum')
    bim.minsize(500, 500)
    bim.withdraw()

    pms = tk.Toplevel(accueil)
    pms.title('pourcentage masse salariale')
    pms.minsize(500, 500)
    pms.withdraw()

    catalogue = tk.Toplevel(accueil)
    catalogue.title('Catalogue des formations')
    catalogue.minsize(500, 500)
    catalogue.withdraw()

    salaries = tk.Toplevel(accueil)
    salaries.title('Liste des salaries')
    salaries.minsize(500, 500)
    salaries.withdraw()

    demandes = tk.Toplevel(accueil)
    demandes.title('demandes de formations')
    demandes.minsize(500, 500)
    demandes.withdraw()

    formations = tk.Toplevel(accueil)
    formations.title('etats des formations')
    formations.minsize(500, 500)
    formations.withdraw()
    
    gestion = tk.Toplevel(accueil)
    gestion.title('gestion du budget')
    gestion.minsize(500, 500)
    gestion.withdraw()
	
    liste = tk.Toplevel(accueil)
    liste.title('liste des formations de chaque salarie')
    liste.minsize(500, 500)
    liste.withdraw()
    
    #frame un

    frame_un = tk.Frame(win, padx = 10, pady = 10)
    frame_un.pack(side = tk.TOP)

    #affiche identifiant

    tk.Label(frame_un, text = 'identifiant').pack(side = tk.LEFT, padx = 50)

    #cadre pour entrer l'identifiant
    
    login = tk.StringVar()
    ent_login = tk.Entry(frame_un, textvariable = login)
    ent_login.pack(side = tk.LEFT)

    #frame_deux

    frame_deux = tk.Frame(win, padx = 10, pady = 10)
    frame_deux.pack(side = tk.TOP)

    #affiche mdp

    tk.Label(frame_deux, text = 'Mot de passe').pack(side = tk.LEFT, padx = 50)

    #cadre pour le mdp

    mdp = tk.StringVar()
    ent_mdp = tk.Entry(frame_deux, textvariable = mdp)
    ent_mdp.configure(show = '*')
    ent_mdp.pack(side = tk.BOTTOM)

    # affiche le bouton connecter

    btn_connecter = tk.Button(win, text = "connecter", command=page_accueil) 
    btn_connecter.pack(side = tk.BOTTOM, padx = 50, pady=20)

def remplir_pages():

      ## bim

    #menu bim
                
    menu_bim()

    #frames bim

    tk.Label(bim, text = 'Budget individuel maximum').pack(side = tk.TOP, padx = 250, pady=50)

    frame_bim_1 = tk.Frame(bim, padx = 0, pady = 0)
    frame_bim_1.pack(side = tk.TOP)
    
    frame_bim_2 = tk.Frame(bim, padx = 0, pady = 0)
    frame_bim_2.pack(side = tk.TOP)
    
    frame_bim_3 = tk.Frame(bim, padx = 0, pady = 0)
    frame_bim_3.pack(side = tk.TOP)
    
    frame_bim_4 = tk.Frame(bim, padx = 0, pady = 0)
    frame_bim_4.pack(side = tk.TOP)
    
    frame_bim_5 = tk.Frame(bim, padx = 50, pady = 50)
    frame_bim_5.pack(side = tk.TOP)
    
    frame_bim_6 = tk.Frame(bim, padx = 50, pady = 50)
    frame_bim_6.pack(side = tk.TOP)

    #texte bim
                
    tk.Label(frame_bim_1, text = 'Ce budget correspond au plafond annuel que peut se permettre GSB pour chaque salarie.').pack(side = tk.LEFT, padx=5, pady=5)
    tk.Label(frame_bim_2, text = 'Il est modifiable normalement une fois par an.').pack(side = tk.LEFT, padx=5, pady=5)
    tk.Label(frame_bim_3, text = 'Ce montant est theorique, il ne peut en aucun cas interdire une inscription : ').pack(side = tk.LEFT, padx=5, pady=5)
    tk.Label(frame_bim_4, text = 'lavis du Comite dentreprise est obligatoire.').pack(side = tk.LEFT, padx=5, pady=5)
    tk.Label(frame_bim_5, text = 'budget').pack(side = tk.LEFT, padx=5, pady=5)
    valeur_bim = re.budget_ind()
    tk.Label(frame_bim_5, text = valeur_bim ).pack(side = tk.LEFT, padx=5, pady=5)
    tk.Label(frame_bim_5, text = 'E' ).pack(side = tk.LEFT, padx=5, pady=5)
    tk.Button(frame_bim_6, text='Modifier', command=modifier_bim).pack(side = tk.LEFT, padx=5, pady=5);

      ##pms

    #menu pms
     
    menu_pms()

    #frames pms
    
    tk.Label(pms, text = 'Pourcentage masse salariale').pack(side = tk.TOP, padx = 250, pady=50)
    
    frame_pms_1 = tk.Frame(pms, padx = 0, pady = 0)
    frame_pms_1.pack(side = tk.TOP)
    
    frame_pms_2 = tk.Frame(pms, padx = 0, pady = 0)
    frame_pms_2.pack(side = tk.TOP)
    
    frame_pms_3 = tk.Frame(pms, padx = 0, pady = 0)
    frame_pms_3.pack(side = tk.TOP)
    
    frame_pms_4 = tk.Frame(pms, padx = 0, pady = 0)
    frame_pms_4.pack(side = tk.TOP)
    
    frame_pms_5 = tk.Frame(pms, padx = 0, pady = 50)
    frame_pms_5.pack(side = tk.TOP)
    
    frame_pms_6 = tk.Frame(pms, padx = 50, pady = 50)
    frame_pms_6.pack(side = tk.TOP)

    #texte pms
        
    tk.Label(frame_pms_1, text = 'Chaque service de GSB se voit attribuer une enveloppe formation dun certain pourcentage de sa masse salariale.').pack(side = tk.LEFT, padx=5, pady=5)
    tk.Label(frame_pms_2, text = 'Il est modifiable normalement une fois par an.').pack(side = tk.LEFT, padx=5, pady=5)
    tk.Label(frame_pms_3, text = 'Ce montant est theorique, il ne peut en aucun cas interdire une inscription : ').pack(side = tk.LEFT, padx=5, pady=5)
    tk.Label(frame_pms_4, text = 'lavis du Comite dentreprise est obligatoire.').pack(side = tk.LEFT, padx=5, pady=5)
    tk.Label(frame_pms_5, text = 'pourcentage').pack(side = tk.LEFT, padx=5, pady=5)
    valeur_pms = re.pourcentage()
    tk.Label(frame_pms_5, text = valeur_pms ).pack(side = tk.LEFT, padx=5, pady=5)
    tk.Label(frame_pms_5, text = '%' ).pack(side = tk.LEFT, padx=5, pady=5)
    tk.Button(frame_pms_6, text='Modifier', command=modifier_pms).pack(side = tk.LEFT, padx=5, pady=5)

     ##salaries

    menu_salaries()
    tableau_salaries()

     ##catalogue

    menu_catalogue()
    tableau_catalogue()

     ##demandes

    menu_demandes()
    tableau_demandes()

     ##formations

    menu_formations()
    tableau_formations()

    ##gestion

    menu_gestion()
    tableau_gestion()
	
	##liste

    menu_liste()
    tableau_liste()
    

def page_accueil():
    
    reponse = re.connexion(login.get(), mdp.get())
    if reponse:
        win.destroy()
        accueil.deiconify()
        menu_accueil()
        tk.Label(accueil, text = 'Accueil').pack(side = tk.TOP, padx = 250, pady=50)
    else:
        tk.messagebox.showerror('Titre Erreur', "Identifiant ou mot de passe incorrect ")  

def menu_accueil():

    barre_menu_accueil = tk.Menu(accueil)
   
    #menu_chiffres
    
    menu_chiffres_accueil = tk.Menu(barre_menu_accueil, tearoff=0)
    barre_menu_accueil.add_cascade(label="Informations et paramètres",  menu=menu_chiffres_accueil)
    menu_chiffres_accueil.add_command(label="Budget individuel maximum", command=page_bim)
    menu_chiffres_accueil.add_separator()
    menu_chiffres_accueil.add_command(label="Pourcentage de la masse salariale", command=page_pms)
    menu_chiffres_accueil.add_separator()
    menu_chiffres_accueil.add_command(label="Liste des salaries", command=page_salaries)

    #menu_formations
        
    menu_formations_accueil = tk.Menu(barre_menu_accueil, tearoff=0)
    barre_menu_accueil.add_cascade(label="Formations et inscriptions",  menu=menu_formations_accueil)
    menu_formations_accueil.add_command(label="Catalogue", command=page_catalogue)
    menu_formations_accueil.add_separator()
    menu_formations_accueil.add_command(label="Demandes de formations", command=page_demandes)

    #menu_suivi

    menu_suivi_accueil = tk.Menu(barre_menu_accueil, tearoff=0)
    barre_menu_accueil.add_cascade(label="Suivi et budget",  menu=menu_suivi_accueil)
    menu_suivi_accueil.add_command(label="Etats des formations", command=page_formations)
    menu_suivi_accueil.add_separator()
    menu_suivi_accueil.add_command(label="Budget dejà engage", command=page_gestion)
    menu_suivi_accueil.add_separator()
    menu_suivi_accueil.add_command(label="Liste deroulante", command=page_liste)

    accueil.configure(menu=barre_menu_accueil)

def page_bim():
 
    accueil.withdraw()
    pms.withdraw()
    catalogue.withdraw()
    bim.deiconify()
    salaries.withdraw()
    demandes.withdraw()
    formations.withdraw()
    gestion.withdraw()
 
def menu_bim():

    barre_menu_bim = tk.Menu(bim)

    #menu_chiffres
    
    menu_chiffres_bim = tk.Menu(barre_menu_bim, tearoff=0)
    barre_menu_bim.add_cascade(label="Informations et paramètres",  menu=menu_chiffres_bim)
    menu_chiffres_bim.add_command(label="Budget individuel maximum", command=page_bim)
    menu_chiffres_bim.add_separator()
    menu_chiffres_bim.add_command(label="Pourcentage de la masse salariale", command=page_pms)
    menu_chiffres_bim.add_separator()
    menu_chiffres_bim.add_command(label="Liste des salaries", command=page_salaries)

    #menu_formations
        
    menu_formations_bim = tk.Menu(barre_menu_bim, tearoff=0)
    barre_menu_bim.add_cascade(label="Formations et inscriptions",  menu=menu_formations_bim)
    menu_formations_bim.add_command(label="Catalogue", command=page_catalogue)
    menu_formations_bim.add_separator()
    menu_formations_bim.add_command(label="Demandes de formations", command=page_demandes)

    #menu_suivi

    menu_suivi_bim = tk.Menu(barre_menu_bim, tearoff=0)
    barre_menu_bim.add_cascade(label="Suivi et budget",  menu=menu_suivi_bim)
    menu_suivi_bim.add_command(label="Etats des formations", command=page_formations)
    menu_suivi_bim.add_separator()
    menu_suivi_bim.add_command(label="Budget dejà engage", command=page_gestion)
    menu_suivi_bim.add_separator()
    menu_suivi_bim.add_command(label="Liste deroulante", command=page_liste)

    bim.configure(menu=barre_menu_bim)

def modifier_bim():

    global new_valeur_bim, new_bim
    
    new_bim = tk.Toplevel(bim)
    new_bim.minsize(100, 100)
    new_bim.title('modification budget individuel maximum')
    new_valeur_bim = tk.StringVar()
    ent_bim = tk.Entry(new_bim, textvariable = new_valeur_bim)
    ent_bim.pack(side = tk.LEFT)
    tk.Button(new_bim, text='Enregistrer', command=demander_confirmation_bim).pack(side = tk.LEFT, padx=5, pady=5);
    
def demander_confirmation_bim():

    global message_confirmation_bim

    message_confirmation_bim=tk.Toplevel(new_bim)
    message_confirmation_bim.title("confirmer modification")
    tk.Label(message_confirmation_bim, text="Etes vous sur de vouloir proceder à cette modification?").pack(side=tk.TOP)
    tk.Button(message_confirmation_bim, text="Oui", command=enregistrer_bim).pack(side=tk.LEFT)
    tk.Button(message_confirmation_bim, text ="Non", command=annuler_bim).pack(side=tk.RIGHT)

def enregistrer_bim():

    re.enregistrer_bim(new_valeur_bim.get())
    new_bim.destroy()
        
def annuler_bim():

    message_confirmation_bim.destroy()
    new_bim.destroy()
  
def page_pms():

    bim.withdraw()
    catalogue.withdraw()
    pms.deiconify()
    accueil.withdraw()
    salaries.withdraw()
    demandes.withdraw()
    formations.withdraw()
    gestion.withdraw()

def menu_pms():

    barre_menu_pms = tk.Menu(pms)

    #menu_chiffres
    
    menu_chiffres_pms = tk.Menu(barre_menu_pms, tearoff=0)
    barre_menu_pms.add_cascade(label="Informations et paramètres",  menu=menu_chiffres_pms)
    menu_chiffres_pms.add_command(label="Budget individuel maximum", command=page_bim)
    menu_chiffres_pms.add_separator()
    menu_chiffres_pms.add_command(label="Pourcentage de la masse salariale", command=page_pms)
    menu_chiffres_pms.add_separator()
    menu_chiffres_pms.add_command(label="Liste des salaries", command=page_salaries)

    #menu_formations
        
    menu_formations_pms = tk.Menu(barre_menu_pms, tearoff=0)
    barre_menu_pms.add_cascade(label="Formations et inscriptions",  menu=menu_formations_pms)
    menu_formations_pms.add_command(label="Catalogue", command=page_catalogue)
    menu_formations_pms.add_separator()
    menu_formations_pms.add_command(label="Demandes de formations", command=page_demandes)

    #menu_suivi

    menu_suivi_pms = tk.Menu(barre_menu_pms, tearoff=0)
    barre_menu_pms.add_cascade(label="Suivi et budget",  menu=menu_suivi_pms)
    menu_suivi_pms.add_command(label="Etats des formations", command=page_formations)
    menu_suivi_pms.add_separator()
    menu_suivi_pms.add_command(label="Budget dejà engage", command=page_gestion)
    menu_suivi_pms.add_separator()
    menu_suivi_pms.add_command(label="Liste deroulante", command=page_liste)

    pms.configure(menu=barre_menu_pms)

def modifier_pms():

    global new_valeur_pms, new_pms
    
    new_pms = tk.Toplevel(pms)
    new_pms.minsize(100, 100)
    new_pms.title('modification Pourcentage maximum individuel')
    new_valeur_pms = tk.StringVar()
    ent_pms = tk.Entry(new_pms, textvariable = new_valeur_pms)
    ent_pms.pack(side = tk.LEFT)
    tk.Button(new_pms, text='Enregistrer', command=demander_confirmation_pms).pack(side = tk.LEFT, padx=5, pady=5)

def demander_confirmation_pms():

    global message_confirmation_pms

    message_confirmation_pms=tk.Toplevel(new_pms)
    message_confirmation_pms.title("confirmer modification")
    tk.Label(message_confirmation_pms, text="Etes vous sur de vouloir proceder à cette modification?").pack(side=tk.TOP)
    tk.Button(message_confirmation_pms, text="Oui", command=enregistrer_pms).pack(side=tk.LEFT)
    tk.Button(message_confirmation_pms, text ="Non", command=annuler_pms).pack(side=tk.RIGHT)

def annuler_pms():

    message_confirmation_pms.destroy()
    new_pms.destroy()
  
def enregistrer_pms():

    re.enregistrer_pms(new_valeur_pms.get())
    new_pms.destroy()

def page_salaries():

    accueil.withdraw()
    salaries.deiconify()
    bim.withdraw()
    pms.withdraw()
    catalogue.withdraw()
    demandes.withdraw()
    formations.withdraw()
    gestion.withdraw()

def menu_salaries() :

    barre_menu_salaries = tk.Menu(salaries)

    #menu_chiffres
    
    menu_chiffres_salaries = tk.Menu(barre_menu_salaries, tearoff=0)
    barre_menu_salaries.add_cascade(label="Informations et paramètres",  menu=menu_chiffres_salaries)
    menu_chiffres_salaries.add_command(label="Budget individuel maximum", command=page_bim)
    menu_chiffres_salaries.add_separator()
    menu_chiffres_salaries.add_command(label="Pourcentage de la masse salariale", command=page_pms)
    menu_chiffres_salaries.add_separator()
    menu_chiffres_salaries.add_command(label="Liste des salaries", command=page_salaries)

    #menu_formations
        
    menu_formations_salaries = tk.Menu(barre_menu_salaries, tearoff=0)
    barre_menu_salaries.add_cascade(label="Formations et inscriptions",  menu=menu_formations_salaries)
    menu_formations_salaries.add_command(label="Catalogue", command=page_catalogue)
    menu_formations_salaries.add_separator()
    menu_formations_salaries.add_command(label="Demandes de formations", command=page_demandes)

    #menu_suivi

    menu_suivi_salaries = tk.Menu(barre_menu_salaries, tearoff=0)
    barre_menu_salaries.add_cascade(label="Suivi et budget",  menu=menu_suivi_salaries)
    menu_suivi_salaries.add_command(label="Etats des formations", command=page_formations)
    menu_suivi_salaries.add_separator()
    menu_suivi_salaries.add_command(label="Budget dejà engage", command=page_gestion)
    menu_suivi_salaries.add_separator()
    menu_suivi_salaries.add_command(label="Liste deroulante", command=page_liste)

    salaries.configure(menu=barre_menu_salaries)
    
def tableau_salaries():

    global tableau_salaries, liste_mat
    
    tk.Label(salaries, text = 'liste des matricules, noms, prenoms et noms de service de chaque salarie par ordre alphabetique').pack(side=tk.TOP, pady=20, padx=5)
    tableau = tk.Frame(salaries)
    tableau.pack(side=tk.TOP, padx=10, pady=10)
    
    scrollv = tk.Scrollbar(tableau, orient=tk.VERTICAL)
    scrollh = tk.Scrollbar(tableau, orient=tk.HORIZONTAL)
    
    scrollv.pack(side=tk.RIGHT, fill=tk.Y)
    scrollh.pack(side=tk.BOTTOM, fill=tk.X)
    
    tableau_salaries = tk.Listbox(tableau, yscrollcommand=scrollv.set, height=80)
    tableau_salaries = tk.Listbox(tableau, xscrollcommand=scrollh.set, height=50)
    tableau_salaries.configure(width=50)
    tableau_salaries.pack(side=tk.LEFT,  fill=tk.BOTH, expand=1)
    
    scrollv.config(command=tableau_salaries.yview)
    scrollh.config(command=tableau_salaries.xview)

    #nb_salaries = {}
    #i=0
    #liste_mat = []
    for une_ligne in re.liste_salaries():
        #nb_salaries[une_ligne['Matricule']] = i
        tableau_salaries.insert(tk.END, str(une_ligne['Matricule']) + ' | ' + une_ligne['Nom'] + ' ' + une_ligne['Prenom'] + ' | ' + str(une_ligne['Nom_service']))
        #liste_mat.append(une_ligne['Matricule'])
        #i += 1

    
def page_catalogue():
    
    accueil.withdraw()
    bim.withdraw()
    pms.withdraw()
    salaries.withdraw()
    catalogue.deiconify()
    demandes.withdraw()
    formations.withdraw()
    gestion.withdraw()
    
def menu_catalogue() :

    barre_menu_catalogue = tk.Menu(catalogue)

    #menu_chiffres
    
    menu_chiffres_catalogue = tk.Menu(barre_menu_catalogue, tearoff=0)
    barre_menu_catalogue.add_cascade(label="Informations et paramètres",  menu=menu_chiffres_catalogue)
    menu_chiffres_catalogue.add_command(label="Budget individuel maximum", command=page_bim)
    menu_chiffres_catalogue.add_separator()
    menu_chiffres_catalogue.add_command(label="Pourcentage de la masse salariale", command=page_pms)
    menu_chiffres_catalogue.add_separator()
    menu_chiffres_catalogue.add_command(label="Liste des salaries", command=page_salaries)

    #menu_formations
        
    menu_formations_catalogue = tk.Menu(barre_menu_catalogue, tearoff=0)
    barre_menu_catalogue.add_cascade(label="Formations et inscriptions",  menu=menu_formations_catalogue)
    menu_formations_catalogue.add_command(label="Catalogue", command=page_catalogue)
    menu_formations_catalogue.add_separator()
    menu_formations_catalogue.add_command(label="Demandes de formations", command=page_demandes)

    #menu_suivi

    menu_suivi_catalogue = tk.Menu(barre_menu_catalogue, tearoff=0)
    barre_menu_catalogue.add_cascade(label="Suivi et budget",  menu=menu_suivi_catalogue)
    menu_suivi_catalogue.add_command(label="Etats des formations", command=page_formations)
    menu_suivi_catalogue.add_separator()
    menu_suivi_catalogue.add_command(label="Budget dejà engage", command=page_gestion)
    menu_suivi_catalogue.add_separator()
    menu_suivi_catalogue.add_command(label="Liste deroulante", command=page_liste)

    catalogue.configure(menu=barre_menu_catalogue)

def tableau_catalogue():

    # tableau

    global liste_formations, liste_ids
    
    tableau = tk.Frame(catalogue)
    tableau.pack(padx=10, pady=20)
    
    scrollv = tk.Scrollbar(tableau, orient=tk.VERTICAL)
    scrollh = tk.Scrollbar(tableau, orient=tk.HORIZONTAL)
    
    scrollv.pack(side=tk.RIGHT, fill=tk.Y)
    scrollh.pack(side=tk.BOTTOM, fill=tk.X)
    
    liste_formations = tk.Listbox(tableau, yscrollcommand=scrollv.set, height=10)
    liste_formations = tk.Listbox(tableau, xscrollcommand=scrollh.set, height=10)
    liste_formations.configure(width=50)
    liste_formations.pack(side=tk.LEFT,  fill=tk.BOTH, expand=1)
    liste_formations.bind('<<ListboxSelect>>', page_formation)
    
    scrollv.config(command=liste_formations.yview)
    scrollh.config(command=liste_formations.xview)

    #liste formations
    
    indexe_formations = {}
    compteur = 0
    liste_ids = []
    for une_formation in re.liste_formations():
        indexe_formations[une_formation['identifiant']] = compteur
        liste_formations.insert(tk.END, 'nom : ' + une_formation['nom'] +  ' \n identifiant : ' + str(une_formation['identifiant']))
        liste_ids.append(une_formation['identifiant'])
        compteur += 1

def page_formation(event):

    global nom_formation, formation, id_form

    # ouverture page

    id_form = liste_ids[liste_formations.curselection()[0]]
    nom_formation=re.titre_formation(id_form)
    formation = tk.Toplevel(catalogue)
    formation.title(nom_formation)
    formation.minsize(500, 500)

    #grand frame
    
    frame_description = tk.LabelFrame(formation, height=200, width=400)
    frame_description.pack(pady=30)

    #petits frames 
    
    frame_nom = tk.Frame(frame_description)
    frame_nom.pack(side=tk.TOP)
    
    frame_niveau = tk.Frame(frame_description)
    frame_niveau.pack(side=tk.TOP)
    
    frame_nature = tk.Frame(frame_description)
    frame_nature.pack(side=tk.TOP)
    
    frame_date = tk.Frame(frame_description)
    frame_date.pack(side=tk.TOP)
    
    frame_duree = tk.Frame(frame_description)
    frame_duree.pack(side=tk.TOP)
    
    frame_coût = tk.Frame(frame_description)
    frame_coût.pack(side=tk.TOP)

    #remplissage
   
    description=re.description_formation(id_form)
    
    tk.Label(frame_nom, text = 'nom: %s' % str(description[0])).pack(side=tk.LEFT, pady=5, padx=5)
    tk.Label(frame_niveau, text = 'niveau: %s' % str(description[1])).pack(side=tk.LEFT, pady=5, padx=5)                    
    tk.Label(frame_nature, text = 'nature: %s' % str(description[2])).pack(side=tk.LEFT, pady=5, padx=5)
    tk.Label(frame_date, text = 'date: %s' % str(description[3])).pack(side=tk.LEFT, pady=5, padx=5)
    tk.Label(frame_duree, text = 'duree: %s jours' % str(description[4])).pack(side=tk.LEFT, pady=5, padx=5)               
    tk.Label(frame_coût, text = 'coût: %s E' % str(description[5])).pack(side=tk.LEFT, pady=5, padx=5)

    tk.Button(formation, text='Proceder à une demande', command=proceder_demande).pack(side = tk.BOTTOM, pady=50)

def proceder_demande():

    global demande_formation, matricule_entre, nom_salarie_entre, prenom_salarie_entre

    # ouverture page

    demande_formation = tk.Toplevel(formation)
    demande_formation.title(nom_formation)
    demande_formation.minsize(500, 500)

    #frames salaries

    info_salarie = tk.Frame(demande_formation)
    info_salarie.pack(side=tk.TOP)
    
    frame_nom_salarie = tk.Frame(demande_formation)
    frame_nom_salarie.pack(side=tk.TOP)

    frame_prenom_salarie = tk.Frame(demande_formation)
    frame_prenom_salarie.pack(side=tk.TOP)
    
    frame_id_salarie = tk.Frame(demande_formation)
    frame_id_salarie.pack(side=tk.TOP)

    #remplissage

    tk.Label(info_salarie, text = 'informations sur le salarie à inscrire').pack(side=tk.LEFT, pady=5, padx=20)
    
    tk.Label(frame_nom_salarie, text = 'nom').pack(side=tk.LEFT, pady=5, padx=5)
    nom_salarie_entre = tk.StringVar()
    ent_nom= tk.Entry(frame_nom_salarie, textvariable = nom_salarie_entre)
    ent_nom.pack(side = tk.LEFT)

    tk.Label(frame_prenom_salarie, text = 'prenom').pack(side=tk.LEFT, pady=5, padx=5)
    prenom_salarie_entre= tk.StringVar()
    ent_prenom= tk.Entry(frame_prenom_salarie, textvariable = prenom_salarie_entre)
    ent_prenom.pack(side = tk.LEFT)

    tk.Label(frame_id_salarie, text = 'identifiant (se referer à la page salaries du menu)').pack(side=tk.LEFT, pady=5, padx=5)
    matricule_entre = tk.StringVar()
    ent_id= tk.Entry(frame_id_salarie, textvariable = matricule_entre)
    ent_id.pack(side = tk.LEFT)

    tk.Button(demande_formation, text='Envoyer la demande', command=demander_confirmation).pack(side = tk.BOTTOM, pady=50)

def demander_confirmation():

    global message_confirmation_demande

    confirmation = re.confirmation_demande(matricule_entre.get(), nom_salarie_entre.get(), prenom_salarie_entre.get())
    if confirmation:
        message_confirmation_demande=tk.Toplevel(demande_formation)
        message_confirmation_demande.title("confirmer demande")
        tk.Label(message_confirmation_demande, text="Etes vous sur de vouloir proceder à cette inscription?").pack(side=tk.TOP)
        tk.Button(message_confirmation_demande, text="Oui", command=envoyer_demande).pack(side=tk.LEFT)
        tk.Button(message_confirmation_demande, text ="Non", command=annuler_non).pack(side=tk.RIGHT)
    else:
        tk.messagebox.showerror('Titre Erreur', "Ces informations ne correspondent à aucun salarie")  
    
def envoyer_demande():

    demande_inexistante=re.demande_inexistante(id_form, matricule_entre.get())
    if demande_inexistante:
        re.envoyer_demande(id_form, matricule_entre.get())
        annuler_non()
    else:
        tk.messagebox.showerror('Titre Erreur', "Demande dejà traitee")

def annuler_non():

    message_confirmation_demande.destroy()
    demande_formation.destroy()

def page_demandes():
    
    accueil.withdraw()
    bim.withdraw()
    pms.withdraw()
    salaries.withdraw()
    catalogue.withdraw()
    demandes.deiconify()
    formations.withdraw()
    gestion.withdraw()

def menu_demandes() :

    barre_menu_demandes = tk.Menu(demandes)

    #menu_chiffres
    
    menu_chiffres_demandes = tk.Menu(barre_menu_demandes, tearoff=0)
    barre_menu_demandes.add_cascade(label="Informations et paramètres",  menu=menu_chiffres_demandes)
    menu_chiffres_demandes.add_command(label="Budget individuel maximum", command=page_bim)
    menu_chiffres_demandes.add_separator()
    menu_chiffres_demandes.add_command(label="Pourcentage de la masse salariale", command=page_pms)
    menu_chiffres_demandes.add_separator()
    menu_chiffres_demandes.add_command(label="Liste des salaries", command=page_salaries)

    #menu_formations
        
    menu_formations_demandes = tk.Menu(barre_menu_demandes, tearoff=0)
    barre_menu_demandes.add_cascade(label="Formations et inscriptions",  menu=menu_formations_demandes)
    menu_formations_demandes.add_command(label="Catalogue", command=page_catalogue)
    menu_formations_demandes.add_separator()
    menu_formations_demandes.add_command(label="Demandes de formations", command=page_demandes)

    #menu_suivi

    menu_suivi_demandes = tk.Menu(barre_menu_demandes, tearoff=0)
    barre_menu_demandes.add_cascade(label="Suivi et budget",  menu=menu_suivi_demandes)
    menu_suivi_demandes.add_command(label="Etats des formations", command=page_formations)
    menu_suivi_demandes.add_separator()
    menu_suivi_demandes.add_command(label="Budget dejà engage", command=page_gestion)
    menu_suivi_demandes.add_separator()
    menu_suivi_demandes.add_command(label="Liste deroulante", command=page_liste)

    demandes.configure(menu=barre_menu_demandes)

def tableau_demandes():

    global liste_demandes, liste_id_demandes

    # tableau
    
    tableau = tk.Frame(demandes)
    tableau.pack(padx=10, pady=20)
    
    scrollv = tk.Scrollbar(tableau, orient=tk.VERTICAL)
    scrollh = tk.Scrollbar(tableau, orient=tk.HORIZONTAL)
    
    scrollv.pack(side=tk.RIGHT, fill=tk.Y)
    scrollh.pack(side=tk.BOTTOM, fill=tk.X)
    
    liste_demandes = tk.Listbox(tableau, yscrollcommand=scrollv.set, height=10)
    liste_demandes = tk.Listbox(tableau, xscrollcommand=scrollh.set, height=10)
    liste_demandes.configure(width=50)
    liste_demandes.pack(side=tk.LEFT,  fill=tk.BOTH, expand=1)
    liste_demandes.bind('<<ListboxSelect>>', page_en_cours)
    
    scrollv.config(command=liste_demandes.yview)
    scrollh.config(command=liste_demandes.xview)

    # liste des demandes

    liste_id_demandes = []
    en_cours_vide=re.en_cours_vide()
    
    if en_cours_vide:
        tk.Label(liste_demandes, text="Il n'y a aucune demande de formation en cours").pack(side=tk.TOP)
    else:
        for une_ligne in re.demandes_en_cours():
            liste_demandes.insert(tk.END, str(une_ligne['nom']) + ' ' + str(une_ligne['prenom']) + ' | ' + str(une_ligne['nom_formation']) + ' | ' + str(une_ligne['date_formation']))
            liste_id_demandes.append(une_ligne['id_demande'])

def page_en_cours(event):

    global en_cours, id_demande
    
    #ouverture page
    
    id_demande = liste_id_demandes[liste_demandes.curselection()[0]]
    en_cours = tk.Toplevel(demandes)
    en_cours.title("demande en cours")
    en_cours.minsize(500, 500)

    tk.Label(en_cours, text="Vous pouvez :").pack(side=tk.TOP)

    #petits frames 
    
    frame_en_cours_1 = tk.Frame(en_cours)
    frame_en_cours_1.pack(side=tk.TOP)
    
    frame_en_cours_2 = tk.Frame(en_cours)
    frame_en_cours_2.pack(side=tk.TOP)
    
    frame_en_cours_3 = tk.Frame(en_cours)
    frame_en_cours_3.pack(side=tk.TOP)
    
    frame_en_cours_4 = tk.Frame(en_cours)
    frame_en_cours_4.pack(side=tk.TOP)

   
    #remplissage
    
    tk.Button(frame_en_cours_1, text="Modifier", command=commande_confirmation_1).pack(side=tk.LEFT)
    tk.Label(frame_en_cours_1, text="Si vous voulez modifier un paramètre de la demande").pack(side=tk.LEFT)

    tk.Button(frame_en_cours_2, text="Confirmer", command=commande_confirmation_2).pack(side=tk.LEFT)
    tk.Label(frame_en_cours_2, text="Si votre demande a ete acceptee").pack(side=tk.LEFT)
    tk.Label(en_cours, text="Attention ! Confirmer une demande est irreversible et genère quoi qu'il arrive des frais").pack(side=tk.TOP)

    tk.Button(frame_en_cours_3, text="Refuser", command=commande_confirmation_3).pack(side=tk.LEFT)
    tk.Label(frame_en_cours_3, text="Si votre demande a ete refusee").pack(side=tk.LEFT)

    tk.Button(frame_en_cours_4, text="Annuler", command=commande_confirmation_4).pack(side=tk.LEFT)
    tk.Label(frame_en_cours_4, text="Si vous souhaitez annuler cette demande de formation").pack(side=tk.LEFT)

    tk.Button(en_cours, text="Retour", command=fermer_en_cours).pack(side=tk.TOP)

def fermer_en_cours():

    en_cours.destroy()

def commande_confirmation_1():

    global message_confirmation_1

    message_confirmation_1=tk.Toplevel(en_cours)
    message_confirmation_1.title("modifier demande")
    tk.Label(message_confirmation_1, text="Quel(s) parametre(s) souhaitez vous modifier?").pack(side=tk.TOP)
    tk.Button(message_confirmation_1, text="Salarie", command=modifier_salarie).pack(side=tk.LEFT, padx=10)
    tk.Button(message_confirmation_1, text ="Formation", command=modifier_formation).pack(side=tk.LEFT, padx=10)
    tk.Button(message_confirmation_1, text ="Les deux", command=modifier_les_deux).pack(side=tk.LEFT, padx=10)
    tk.Button(message_confirmation_1, text ="Retour", command=fermer_message_confirmation_1).pack(side=tk.LEFT, padx=10)

def fermer_message_confirmation_1():
    
    message_confirmation_1.destroy()
    
def modifier_salarie():

    global page_modifier_salarie, nouveau_matricule_entre, nouveau_nom_salarie_entre, nouveau_prenom_salarie_entre

    page_modifier_salarie=tk.Toplevel(message_confirmation_1)
    page_modifier_salarie.title("modifier salarie")
    
    tk.Label(page_modifier_salarie, text = 'informations sur le salarie à inscrire').pack(side=tk.TOP, pady=5, padx=20)

    frame_1 = tk.Frame(page_modifier_salarie)
    frame_1.pack(side=tk.TOP)
    
    frame_2 = tk.Frame(page_modifier_salarie)
    frame_2.pack(side=tk.TOP)
    
    frame_3 = tk.Frame(page_modifier_salarie)
    frame_3.pack(side=tk.TOP)
    
    frame_4 = tk.Frame(page_modifier_salarie)
    frame_4.pack(side=tk.TOP)
    
    tk.Label(frame_1, text="Nouveau nom salarie").pack(side=tk.LEFT)
    nouveau_nom_salarie_entre = tk.StringVar()
    ent_nvx_nom= tk.Entry(frame_1, textvariable = nouveau_nom_salarie_entre)
    ent_nvx_nom.pack(side = tk.LEFT)
    
    tk.Label(frame_2, text="Nouveau prenom salarie").pack(side=tk.LEFT)
    nouveau_prenom_salarie_entre= tk.StringVar()
    ent_nvx_prenom= tk.Entry(frame_2, textvariable = nouveau_prenom_salarie_entre)
    ent_nvx_prenom.pack(side = tk.LEFT)
    
    tk.Label(frame_3, text="Nouvel identifiant salarie").pack(side=tk.LEFT)
    nouveau_matricule_entre = tk.StringVar()
    ent_nvx_mat= tk.Entry(frame_3, textvariable = nouveau_matricule_entre)
    ent_nvx_mat.pack(side = tk.LEFT)
    
    tk.Button(frame_4, text="Enregistrer", command=demander_confirmation_salarie).pack(side=tk.LEFT)
    tk.Button(frame_4, text="Retour", command=fermer_page_modifier_salarie).pack(side=tk.LEFT)

def fermer_page_modifier_salarie():

    page_modifier_salarie.destroy()

def demander_confirmation_salarie():

    confirmation = re.confirmation_salarie(nouveau_matricule_entre.get(), nouveau_nom_salarie_entre.get(), nouveau_prenom_salarie_entre.get())
    if confirmation:
        message_confirmation_salarie=tk.Toplevel(page_modifier_salarie)
        message_confirmation_salarie.title("confirmer modification salarie")
        tk.Label(message_confirmation_salarie, text="Etes vous sur de vouloir modifier ce salarie?").pack(side=tk.TOP)
        tk.Button(message_confirmation_salarie, text="Oui", command=enregistrer_nouveau_salarie).pack(side=tk.LEFT)
        tk.Button(message_confirmation_salarie, text ="Non", command=fermer_message_confirmation_salarie).pack(side=tk.RIGHT) 
    else:
        tk.messagebox.showerror('Titre Erreur', "Ces informations ne correspondent à aucun salarie")

def fermer_message_confirmation_salarie():

    message_confirmation_salarie.destroy()

def enregistrer_nouveau_salarie():

    re.enregistrer_nouveau_salarie(nouveau_matricule_entre.get(), id_demande)
    fermer_en_cours()
              
def modifier_formation():

    global page_modifier_formation, nouveau_nom_formation_entre, nouvel_identifiant_formation_entre

    page_modifier_formation=tk.Toplevel(message_confirmation_1)
    page_modifier_formation.title("modifier formation")
    
    tk.Label(page_modifier_formation, text = 'informations sur la formation à inscrire').pack(side=tk.TOP, pady=5, padx=20)

    frame_1 = tk.Frame(page_modifier_formation)
    frame_1.pack(side=tk.TOP)
    
    frame_2 = tk.Frame(page_modifier_formation)
    frame_2.pack(side=tk.TOP)
    
    frame_3 = tk.Frame(page_modifier_formation)
    frame_3.pack(side=tk.TOP)
    
    tk.Label(frame_1, text="Nouveau nom formation").pack(side=tk.LEFT)
    nouveau_nom_formation_entre = tk.StringVar()
    ent_nvx_nom_form= tk.Entry(frame_1, textvariable = nouveau_nom_formation_entre)
    ent_nvx_nom_form.pack(side = tk.LEFT)
    
    tk.Label(frame_2, text="Nouvel identifiant formation").pack(side=tk.LEFT)
    nouvel_identifiant_formation_entre = tk.StringVar()
    ent_nvx_id_form= tk.Entry(frame_2, textvariable = nouvel_identifiant_formation_entre)
    ent_nvx_id_form.pack(side = tk.LEFT)
    
    tk.Button(frame_3, text="Enregistrer", command=demander_confirmation_formation).pack(side=tk.LEFT)
    tk.Button(frame_3, text="Retour", command=fermer_page_modifier_formation).pack(side=tk.LEFT)

def fermer_page_modifier_formation():

    page_modifier_formation.destroy()

def demander_confirmation_formation():

    confirmation = re.confirmation_formation(nouveau_nom_formation_entre.get(), nouvel_identifiant_formation_entre.get())
    if confirmation:
        message_confirmation_formation=tk.Toplevel(page_modifier_formation)
        message_confirmation_formation.title("confirmer modification formation")
        tk.Label(message_confirmation_formation, text="Etes vous sur de vouloir modifier cette formation?").pack(side=tk.TOP)
        tk.Button(message_confirmation_formation, text="Oui", command=enregistrer_nouvelle_formation).pack(side=tk.LEFT)
        tk.Button(message_confirmation_formation, text ="Non", command=fermer_message_confirmation_formation).pack(side=tk.RIGHT) 
    else:
        tk.messagebox.showerror('Titre Erreur', "Ces informations ne correspondent à aucune formation")

def fermer_message_confirmation_formation():

    message_confirmation_formation.destroy()

def enregistrer_nouvelle_formation():

    re.enregistrer_nouvelle_formation(nouvel_identifiant_formation_entre.get(), id_demande)
    fermer_en_cours()
              
def modifier_les_deux():

    global page_modifier_les_deux, nouveau_matricule_entre, nouveau_nom_salarie_entre, nouveau_prenom_salarie_entre, nouveau_nom_formation_entre, nouvel_identifiant_formation_entre

    page_modifier_les_deux=tk.Toplevel(message_confirmation_1)
    page_modifier_les_deux.title("modifier salarie et formation")
    
    tk.Label(page_modifier_les_deux, text="informations sur le salarie à inscrire").pack(side=tk.TOP, pady=5, padx=20)
    
    frame_1 = tk.Frame(page_modifier_les_deux)
    frame_1.pack(side=tk.TOP)
    
    frame_2 = tk.Frame(page_modifier_les_deux)
    frame_2.pack(side=tk.TOP)
    
    frame_3 = tk.Frame(page_modifier_les_deux)
    frame_3.pack(side=tk.TOP)
    
    tk.Label(frame_1, text="Nouveau nom salarie").pack(side=tk.LEFT)
    nouveau_nom_salarie_entre = tk.StringVar()
    ent_nvx_nom= tk.Entry(frame_1, textvariable = nouveau_nom_salarie_entre)
    ent_nvx_nom.pack(side = tk.LEFT)
    
    tk.Label(frame_2, text="Nouveau prenom salarie").pack(side=tk.LEFT)
    nouveau_prenom_salarie_entre= tk.StringVar()
    ent_nvx_prenom= tk.Entry(frame_2, textvariable = nouveau_prenom_salarie_entre)
    ent_nvx_prenom.pack(side = tk.LEFT)
    
    tk.Label(frame_3, text="Nouvel identifiant salarie").pack(side=tk.LEFT)
    nouveau_matricule_entre = tk.StringVar()
    ent_nvx_mat= tk.Entry(frame_3, textvariable = nouveau_matricule_entre)
    ent_nvx_mat.pack(side = tk.LEFT)
    
    tk.Button(page_modifier_les_deux, text="Enregistrer", command=demander_confirmation_salarie).pack(side=tk.TOP, pady=5)

    tk.Label(page_modifier_les_deux, text ="informations sur la formation à inscrire").pack(side=tk.TOP, pady=5, padx=20)

    frame_4 = tk.Frame(page_modifier_les_deux)
    frame_4.pack(side=tk.TOP)

    frame_5 = tk.Frame(page_modifier_les_deux)
    frame_5.pack(side=tk.TOP)
    
    frame_6 = tk.Frame(page_modifier_les_deux)
    frame_6.pack(side=tk.TOP)
    
    tk.Label(frame_4, text="Nouveau nom formation").pack(side=tk.LEFT)
    nouveau_nom_formation_entre = tk.StringVar()
    ent_nvx_nom_form= tk.Entry(frame_4, textvariable = nouveau_nom_formation_entre)
    ent_nvx_nom_form.pack(side = tk.LEFT)
    
    tk.Label(frame_5, text="Nouvel identifiant formation").pack(side=tk.LEFT)
    nouvel_identifiant_formation_entre = tk.StringVar()
    ent_nvx_id_form= tk.Entry(frame_5, textvariable = nouvel_identifiant_formation_entre)
    ent_nvx_id_form.pack(side = tk.LEFT)
    
    tk.Button(page_modifier_les_deux, text="Enregistrer", command=demander_confirmation_formation).pack(side=tk.TOP, pady=5)
    tk.Button(page_modifier_les_deux, text="Retour", command=fermer_page_modifier_les_deux).pack(side=tk.TOP, pady=10)

def fermer_page_modifier_les_deux():

    page_modifier_les_deux.destroy()

def commande_confirmation_2():

    global message_confirmation_2

    message_confirmation_2=tk.Toplevel(en_cours)
    message_confirmation_2.title("confirmer demande")
    tk.Label(message_confirmation_2, text="Etes vous sur de vouloir confirmer?").pack(side=tk.TOP)
    tk.Label(message_confirmation_2, text="Attention ! Confirmer une demande est irreversible et genère quoi qu'il arrive des frais").pack(side=tk.TOP)
    tk.Button(message_confirmation_2, text="Oui", command=confirmer_demande).pack(side=tk.LEFT)
    tk.Button(message_confirmation_2, text ="Non", command=fermer_message_confirmation_2).pack(side=tk.RIGHT)

def fermer_message_confirmation_2():

    message_confirmation_2.destroy()

def confirmer_demande():

    re.confirmer_demande(id_demande) 
    fermer_en_cours()

def commande_confirmation_3():

    global message_confirmation_3

    message_confirmation_3=tk.Toplevel(en_cours)
    message_confirmation_3.title("refuser demande")
    tk.Label(message_confirmation_3, text="Etes vous sûr de vouloir refuser?").pack(side=tk.TOP)
    tk.Button(message_confirmation_3, text="Oui", command=refuser_demande).pack(side=tk.LEFT)
    tk.Button(message_confirmation_3, text ="Non", command=fermer_message_confirmation_3).pack(side=tk.RIGHT)

def fermer_message_confirmation_3():

    message_confirmation_3.destroy()

def refuser_demande():

    re.refuser_demande(id_demande)
    fermer_en_cours()
    
def commande_confirmation_4():

    global message_confirmation_4

    message_confirmation_4=tk.Toplevel(en_cours)
    message_confirmation_4.title("annuler demande")
    tk.Label(message_confirmation_4, text="Etes vous sur de vouloir annuler?").pack(side=tk.TOP)
    tk.Button(message_confirmation_4, text="Oui", command=annuler_demande).pack(side=tk.LEFT)
    tk.Button(message_confirmation_4, text ="Non", command=fermer_message_confirmation_4).pack(side=tk.RIGHT)

def fermer_message_confirmation_4():

    message_confirmation_4.destroy()

def annuler_demande():
    
    re.annuler_demande(id_demande)
    fermer_en_cours()

def page_formations():

    accueil.withdraw()
    bim.withdraw()
    pms.withdraw()
    salaries.withdraw()
    catalogue.withdraw()
    demandes.withdraw()
    formations.deiconify()
    gestion.withdraw()

def menu_formations():

    barre_menu_formations = tk.Menu(formations)
   
    #menu_chiffres
    
    menu_chiffres_formations = tk.Menu(barre_menu_formations, tearoff=0)
    barre_menu_formations.add_cascade(label="Informations et paramètres",  menu=menu_chiffres_formations)
    menu_chiffres_formations.add_command(label="Budget individuel maximum", command=page_bim)
    menu_chiffres_formations.add_separator()
    menu_chiffres_formations.add_command(label="Pourcentage de la masse salariale", command=page_pms)
    menu_chiffres_formations.add_separator()
    menu_chiffres_formations.add_command(label="Liste des salaries", command=page_salaries)

    #menu_formations
        
    menu_formations_formations = tk.Menu(barre_menu_formations, tearoff=0)
    barre_menu_formations.add_cascade(label="Formations et inscriptions",  menu=menu_formations_formations)
    menu_formations_formations.add_command(label="Catalogue", command=page_catalogue)
    menu_formations_formations.add_separator()
    menu_formations_formations.add_command(label="Demandes de formations", command=page_demandes)

    #menu_suivi

    menu_suivi_formations = tk.Menu(barre_menu_formations, tearoff=0)
    barre_menu_formations.add_cascade(label="Suivi et budget",  menu=menu_suivi_formations)
    menu_suivi_formations.add_command(label="Etats des formations", command=page_formations)
    menu_suivi_formations.add_separator()
    menu_suivi_formations.add_command(label="Budget dejà engage", command=page_gestion)
    menu_suivi_formations.add_separator()
    menu_suivi_formations.add_command(label="Liste deroulante", command=page_liste)

    formations.configure(menu=barre_menu_formations)

def tableau_formations():

    global liste_id_acceptees, tableau_acceptees

    Onglets = ttk.Notebook(formations)

    #onglet un

    ongletUn = ttk.Frame(Onglets)
    Onglets.add(ongletUn, text='formations_acceptees %s' % str(re.nombre_acceptees()))

    tableau1 = tk.Frame(ongletUn)
    tableau1.pack(side=tk.TOP, padx=10, pady=10)
    
    scrollv = tk.Scrollbar(tableau1, orient=tk.VERTICAL)
    scrollh = tk.Scrollbar(tableau1, orient=tk.HORIZONTAL)
    
    scrollv.pack(side=tk.RIGHT, fill=tk.Y)
    scrollh.pack(side=tk.BOTTOM, fill=tk.X)
    
    tableau_acceptees = tk.Listbox(tableau1, yscrollcommand=scrollv.set, height=80)
    tableau_acceptees = tk.Listbox(tableau1, xscrollcommand=scrollh.set, height=50)
    tableau_acceptees.configure(width=50)
    tableau_acceptees.pack(side=tk.LEFT,  fill=tk.BOTH, expand=1)
    tableau_acceptees.bind('<<ListboxSelect>>', page_annuler)
    
    scrollv.config(command=tableau_acceptees.yview)
    scrollh.config(command=tableau_acceptees.xview)

    liste_id_acceptees = []

    acceptees_vide=re.acceptees_vide()
    if acceptees_vide:
        tk.Label(tableau_acceptees, text="Il n'y a aucune formation acceptee").pack(side=tk.TOP)
    else: 
        for une_ligne in re.formations_acceptees():
            tableau_acceptees.insert(tk.END, str(une_ligne['nom']) + ' ' + str(une_ligne['prenom']) + ' | ' + str(une_ligne['nom_formation']) + ' | ' + str(une_ligne['date_formation']))
            liste_id_acceptees.append(une_ligne['id_demande'])

     #onglet deux
        
    ongletDeux = ttk.Frame(Onglets)
    Onglets.add(ongletDeux, text='formations_refusees %s' % str(re.nombre_refusees()))

    tableau2 = tk.Frame(ongletDeux)
    tableau2.pack(side=tk.TOP, padx=10, pady=10)
    
    scrollv = tk.Scrollbar(tableau2, orient=tk.VERTICAL)
    scrollh = tk.Scrollbar(tableau2, orient=tk.HORIZONTAL)
    
    scrollv.pack(side=tk.RIGHT, fill=tk.Y)
    scrollh.pack(side=tk.BOTTOM, fill=tk.X)
    
    tableau_refusees = tk.Listbox(tableau2, yscrollcommand=scrollv.set, height=80)
    tableau_refusees = tk.Listbox(tableau2, xscrollcommand=scrollh.set, height=50)
    tableau_refusees.configure(width=50)
    tableau_refusees.pack(side=tk.LEFT,  fill=tk.BOTH, expand=1)
    
    scrollv.config(command=tableau_refusees.yview)
    scrollh.config(command=tableau_refusees.xview)
    
    liste_id_refusees = []
    refusees_vide=re.refusees_vide()
    
    if refusees_vide:
        tk.Label(tableau_refusees, text="Il n'y a aucune formation refusee").pack(side=tk.TOP)
    else:
        for une_ligne in re.formations_refusees():
            tableau_refusees.insert(tk.END, str(une_ligne['nom']) + ' ' + str(une_ligne['prenom']) + ' | ' + str(une_ligne['nom_formation']) + ' | ' + str(une_ligne['date_formation']))
            liste_id_refusees.append(une_ligne['id_demande'])

     #onglet trois
    
    ongletTrois = ttk.Frame(Onglets)
    Onglets.add(ongletTrois, text='formations_annulees %s' % str(re.nombre_annulees()))

    tableau3 = tk.Frame(ongletTrois)
    tableau3.pack(side=tk.TOP, padx=10, pady=10)
    
    scrollv = tk.Scrollbar(tableau3, orient=tk.VERTICAL)
    scrollh = tk.Scrollbar(tableau3, orient=tk.HORIZONTAL)
    
    scrollv.pack(side=tk.RIGHT, fill=tk.Y)
    scrollh.pack(side=tk.BOTTOM, fill=tk.X)
    
    tableau_annulees = tk.Listbox(tableau3, yscrollcommand=scrollv.set, height=80)
    tableau_annulees = tk.Listbox(tableau3, xscrollcommand=scrollh.set, height=50)
    tableau_annulees.configure(width=50)
    tableau_annulees.pack(side=tk.LEFT,  fill=tk.BOTH, expand=1)
    
    scrollv.config(command=tableau_annulees.yview)
    scrollh.config(command=tableau_annulees.xview)
    
    liste_id_annulees = []
    annulees_vide=re.annulees_vide()
    
    if annulees_vide:
        tk.Label(tableau_annulees, text="Il n'y a aucune formation annulee").pack(side=tk.TOP)
    else:
        for une_ligne in re.formations_annulees():
            tableau_annulees.insert(tk.END, str(une_ligne['nom']) + ' ' + str(une_ligne['prenom']) + ' | ' + str(une_ligne['nom_formation']) + ' | ' + str(une_ligne['date_formation']))
            liste_id_annulees.append(une_ligne['id_demande'])

     #onglet quatre
    
    ongletQuatre = ttk.Frame(Onglets)
    Onglets.add(ongletQuatre, text='formations_effectuees %s' % str(re.nombre_effectuees()))

    tableau4 = tk.Frame(ongletQuatre)
    tableau4.pack(side=tk.TOP, padx=10, pady=10)
    
    scrollv = tk.Scrollbar(tableau4, orient=tk.VERTICAL)
    scrollh = tk.Scrollbar(tableau4, orient=tk.HORIZONTAL)
    
    scrollv.pack(side=tk.RIGHT, fill=tk.Y)
    scrollh.pack(side=tk.BOTTOM, fill=tk.X)
    
    tableau_effectuees = tk.Listbox(tableau4, yscrollcommand=scrollv.set, height=80)
    tableau_effectuees = tk.Listbox(tableau4, xscrollcommand=scrollh.set, height=50)
    tableau_effectuees.configure(width=50)
    tableau_effectuees.pack(side=tk.LEFT,  fill=tk.BOTH, expand=1)
    
    scrollv.config(command=tableau_effectuees.yview)
    scrollh.config(command=tableau_effectuees.xview)
    
    liste_id_effectuees = []
    effectuees_vide=re.effectuees_vide()
    
    if effectuees_vide:
        tk.Label(tableau_effectuees, text="Il n'y a aucune formation effectuee").pack(side=tk.TOP)
    else:
        for une_ligne in re.formations_effectuees():
            tableau_effectuees.insert(tk.END, str(une_ligne['nom']) + ' ' + str(une_ligne['prenom']) + ' | ' + str(une_ligne['nom_formation']) + ' | ' + str(une_ligne['date_formation']))
            liste_id_effectuees.append(une_ligne['id_demande'])

    Onglets.pack(expand=1, fill="both")

def page_annuler(event):

    global message_annulation

    message_annulation=tk.Toplevel(formations)
    message_annulation.title("annuler formation")
    tk.Label(message_annulation, text="Voulez-vous annuler cette formation?").pack(side=tk.TOP)
    tk.Button(message_annulation, text="Oui", command=annuler_formation).pack(side=tk.LEFT)
    tk.Button(message_annulation, text="Non", command=fermer_la_page).pack(side=tk.RIGHT)
    
def annuler_formation():

    id_acceptee = liste_id_acceptees[tableau_acceptees.curselection()[0]]
    re.annuler_formation(id_acceptee)
    fermer_la_page()
    
def fermer_la_page():

    message_annulation.destroy()

def page_gestion():

    accueil.withdraw()
    pms.withdraw()
    catalogue.withdraw()
    bim.withdraw()
    salaries.withdraw()
    demandes.withdraw()
    formations.withdraw()
    gestion.deiconify()

def menu_gestion():

    barre_menu_gestion = tk.Menu(gestion)

    #menu_chiffres
    
    menu_chiffres_gestion = tk.Menu(barre_menu_gestion, tearoff=0)
    barre_menu_gestion.add_cascade(label="Informations et paramètres",  menu=menu_chiffres_gestion)
    menu_chiffres_gestion.add_command(label="Budget individuel maximum", command=page_bim)
    menu_chiffres_gestion.add_separator()
    menu_chiffres_gestion.add_command(label="Pourcentage de la masse salariale", command=page_pms)
    menu_chiffres_gestion.add_separator()
    menu_chiffres_gestion.add_command(label="Liste des salaries", command=page_salaries)

    #menu_formations
        
    menu_formations_gestion = tk.Menu(barre_menu_gestion, tearoff=0)
    barre_menu_gestion.add_cascade(label="Formations et inscriptions",  menu=menu_chiffres_gestion)
    menu_formations_gestion.add_command(label="Catalogue", command=page_catalogue)
    menu_formations_gestion.add_separator()
    menu_formations_gestion.add_command(label="Demandes de formations", command=page_demandes)

    #menu_suivi

    menu_suivi_gestion = tk.Menu(barre_menu_gestion, tearoff=0)
    barre_menu_gestion.add_cascade(label="Suivi et budget",  menu=menu_chiffres_gestion)
    menu_suivi_gestion.add_command(label="Etats des formations", command=page_formations)
    menu_suivi_gestion.add_separator()
    menu_suivi_gestion.add_command(label="Budget dejà engage", command=page_gestion)
    menu_suivi_gestion.add_separator()
    menu_suivi_gestion.add_command(label="Liste deroulante", command=page_liste)

    gestion.configure(menu=barre_menu_gestion)

def tableau_gestion():

    service1=re.budget1()
    service2=re.budget2()
    service3=re.budget3()
    service4=re.budget4()
    service5=re.budget5()
    service6=re.budget6()
    service7=re.budget7()

    tk.Label(gestion, text="Budget engage pour chaque service :").pack(side=tk.TOP, pady=100, padx=100)
    tk.Label(gestion, text="Communication : %s E" % str(service1)).pack(side=tk.TOP, padx=5)
    tk.Label(gestion, text="Comptabilite : %s E" % str(service2)).pack(side=tk.TOP, padx=5)
    tk.Label(gestion, text="RH : %s E" % str(service3)).pack(side=tk.TOP, padx=5)
    tk.Label(gestion, text="Production : %s E" % str(service4)).pack(side=tk.TOP, padx=5)
    tk.Label(gestion, text="Visiteurs : %s E" % str(service5)).pack(side=tk.TOP, padx=5)
    tk.Label(gestion, text="Recherche : %s E" % str(service6)).pack(side=tk.TOP, padx=5)
    tk.Label(gestion, text="Client : %s E" % str(service7)).pack(side=tk.TOP, padx=5)

def menu_liste() :

    barre_menu_liste = tk.Menu(liste)

    #menu_chiffres
    
    menu_chiffres_liste = tk.Menu(barre_menu_liste, tearoff=0)
    barre_menu_liste.add_cascade(label="Informations et paramètres",  menu=menu_chiffres_liste)
    menu_chiffres_liste.add_command(label="Budget individuel maximum", command=page_bim)
    menu_chiffres_liste.add_separator()
    menu_chiffres_liste.add_command(label="Pourcentage de la masse salariale", command=page_pms)
    menu_chiffres_liste.add_separator()
    menu_chiffres_liste.add_command(label="Liste des salaries", command=page_salaries)

    #menu_formations
        
    menu_formations_liste = tk.Menu(barre_menu_liste, tearoff=0)
    barre_menu_liste.add_cascade(label="Formations et inscriptions",  menu=menu_formations_liste)
    menu_formations_liste.add_command(label="Catalogue", command=page_catalogue)
    menu_formations_liste.add_separator()
    menu_formations_liste.add_command(label="Demandes de formations", command=page_demandes)

    #menu_suivi

    menu_suivi_liste = tk.Menu(barre_menu_liste, tearoff=0)
    barre_menu_liste.add_cascade(label="Suivi et budget",  menu=menu_suivi_liste)
    menu_suivi_liste.add_command(label="Etats des formations", command=page_formations)
    menu_suivi_liste.add_separator()
    menu_suivi_liste.add_command(label="Budget dejà engage", command=page_gestion)

    liste.configure(menu=barre_menu_liste)
    
def page_liste():

    bim.withdraw()
    catalogue.withdraw()
    pms.withdraw()
    accueil.withdraw()
    salaries.withdraw()
    demandes.withdraw()
    formations.withdraw()
    gestion.withdraw()
    liste.deiconify()


def tableau_liste():
        
    tk.Label(liste, text="Liste des salaries inscrits à une formation").pack(side=tk.TOP, pady=100, padx=100)

    global liste_liste, liste_forma
    
    tableau = tk.Frame(liste)
    tableau.pack(padx=10, pady=20)
    
    scrollv = tk.Scrollbar(tableau, orient=tk.VERTICAL)
    scrollh = tk.Scrollbar(tableau, orient=tk.HORIZONTAL)
    
    scrollv.pack(side=tk.RIGHT, fill=tk.Y)
    scrollh.pack(side=tk.BOTTOM, fill=tk.X)
    
    liste_liste = tk.Listbox(tableau, yscrollcommand=scrollv.set, height=10)
    liste_liste = tk.Listbox(tableau, xscrollcommand=scrollh.set, height=10)
    liste_liste.configure(width=50)
    liste_liste.pack(side=tk.LEFT,  fill=tk.BOTH, expand=1)
    liste_liste.bind('<<ListboxSelect>>', page_listforma)
    
    scrollv.config(command=liste_liste.yview)
    scrollh.config(command=liste_liste.xview)
    
    for une_ligne in re.liste_salar():
        liste_liste.insert(tk.END, str(une_ligne['Nom'] + ' ' + une_ligne['Prenom']))

        
def page_listforma(event):

    liste2=tk.Toplevel(liste)
    tk.Label(liste2, text="Liste des formations").pack(side=tk.TOP, pady=100, padx=100)
    


def mainloop_fin():

    accueil.mainloop()





















