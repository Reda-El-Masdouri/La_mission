
#

import json


import unicodedata


class Quizz:
    def __init__(self, categorie, titre, difficulte):
        self.titre = titre
        self.categorie = categorie
        self.difficulte = difficulte
        

    #def FromData(data):
        # ....
    #    q = Quizz(data[2], data[0], data[1])
    #    return q

    def strip_accents(self, s):
        return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

    def get_quizz_filename(self, categorie, titre, difficulte):
        return self.strip_accents(categorie).lower().replace(" ", "") + "_" + self.strip_accents(titre).lower().replace(" ", "") + "_" + self.strip_accents(difficulte).lower().replace(" ", "") + ".json"
    def afficher_choix(self, choix):
        for i in range(0, len(choix)):
            print(str(i+1), '-', choix[i][0])
    def lancer(self):
        score = 0
        f = open(self.get_quizz_filename(self.categorie, self.titre, self.difficulte), 'r')
        data = f.read()
        f.close()
        self.file_des = json.loads(data)
        
        print("Début de Quizz")
        print("  Questionnaire: " + self.titre)
        print("   Catégorie: "+ self.categorie)
        print("    Difficulté:" + self.difficulte)
        print("     Nombre de questions: "+ str(len(self.file_des["questions"])))
        for i in range(len(self.file_des["questions"])):
            print(" Question ", i+1, "/", len(self.file_des["questions"]), ":", self.file_des["questions"][i]["titre"])

            print()
            self.afficher_choix(self.file_des["questions"][i]["choix"])
            resultat_response_correcte = False
            reponse_int = Quizz.demander_reponse_numerique_utlisateur(1, len(self.file_des["questions"][i]["choix"]))
            if self.file_des["questions"][i]["choix"][reponse_int-1][1] == True:
                print("Bonne réponse")
                resultat_response_correcte = True
                score += 1
            else:
                print("Mauvaise réponse")
            
        print()
        print("Score final :", score, "sur", len(self.file_des["questions"]))
        return resultat_response_correcte

    def demander_reponse_numerique_utlisateur(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Quizz.demander_reponse_numerique_utlisateur(min, max)
    
class Questionnaire:
    def __init__(self, quizzs):
        self.quizzs = quizzs

    def commencer(self):      
        for quizz in self.quizzs:
            quizz.lancer()
                

Questionnaire(
    [
    Quizz("animaux", "les chats", "confirme"),
    Quizz("animaux", "les chats", "confirme")    
    ]
).commencer()


