#create a list
contacts = []

#function add contact
def ajout_contact():
    nom = input("Nom Contact: ")
    for info_contact in contacts:
        if info_contact['nom'] == nom:
            print("Ce nom exite déjà")
            return
        
    tel = input("Numéro de téléphone: ")
    mail = input("Adresse mail: ")

    nouveau_contact = {'nom': nom, 'téléphone': tel, 'adresseMail': mail}
    contacts.append(nouveau_contact)
    print("Le contact est ajouté")

#function search contact by name
def recherche_contact():
    nom_recherche = input("Nom du contact qui doit être recherché: ")
    for info_contact in contacts:
            if info_contact['nom'] == nom_recherche:
                print("Info du contact:")
                print(f"Nom: {info_contact['nom']}")
                print(f"Téléphone: {info_contact['téléphone']}")
                print(f"Email: {info_contact['adresseMail']}")
                return

    print("Pas de contact ou contact non trouvé")

#functon delete contact
def supprimer_contact():
    supp_contact = input("Nom du contact à supprimer : ")
    for info_contact in contacts:
        if info_contact["nom"] == supp_contact:
            contacts.remove(info_contact)
            print("Contact supprimé avec succès!")
            return
        
    print("Pas de contact ou contact non trouvé")

#function view all contact
def afficher_tous_les_contacts():
    if not contacts:
        print("Pas de contact")
        return

    print("Liste des contacts:")
    for info_contact in contacts:
        print(f"Nom: {info_contact['nom']}, Téléphone: {info_contact['téléphone']}, Email: {info_contact['adresseMail']}")



#main loop
while True:
    print("\n1. Ajouter un nouveau contact")
    print("2. Rechercher un contact par son nom")
    print("3. Supprimer un contact par son nom")
    print("4. Afficher tous les contacts")
    print("5. Quitter")

    choix = input("Veuillez choisir une option (1-5) : ")

    if choix == "1":
        ajout_contact()
    elif choix == "2":
        recherche_contact()
    elif choix == "3":
        supprimer_contact()
    elif choix == "4":
        afficher_tous_les_contacts()
    elif choix == "5":
        print("Programme terminé.")
        break
    else:
        print("Option invalide. Veuillez choisir une option valide.")