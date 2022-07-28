# PROJET QUESTIONNAIRE V3 : POO
#
# - Pratiquer sur la POO
# - Travailler sur du code existant
# - Mener un raisonnement
#
# -> Définir les entitées (données, actions)
#
# Question
#    - titre       - str
#    - choix       - (str)
#    - bonne_reponse   - str
#
#    - poser()  -> bool
#
# Questionnaire
#    - questions      - (Question)
#
#    - lancer()
#

import json
from operator import le
from turtle import st

import unicodedata

from numpy import diff

X =0
class Question:
    def __init__(self, categorie, titre, difficulte):
        self.titre = titre
        self.categorie = categorie
        self.difficulte = difficulte
        

    def FromData(data):
        # ....
        q = Question(data[2], data[0], data[1])
        return q

    def strip_accents(self, s):
        return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

    def get_quizz_filename(self, categorie, titre, difficulte):
        return self.strip_accents(categorie).lower().replace(" ", "") + "_" + self.strip_accents(titre).lower().replace(" ", "") + "_" + self.strip_accents(difficulte).lower().replace(" ", "") + ".json"
    def afficher_choix(self, choix):
        for i in range(0, len(choix)):
            print(str(i+1), '-', choix[i][0])
    def poser(self):
        f = open(self.get_quizz_filename(self.categorie, self.titre, self.difficulte), 'r')
        self.file_des = json.load(f)
        f.close
        print("QUESTION")
        print("  " + self.titre)
        for i in range(len(self.file_des["questions"])):
            print("  ", i+1, "-", self.file_des["questions"][i]["titre"])

            print()
            self.afficher_choix(self.file_des["questions"][i]["choix"])
            resultat_response_correcte = False
            reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.file_des["questions"][i]["choix"]))
            if self.file_des["questions"][i]["choix"][reponse_int-1][1] == True:
                print("Bonne réponse")
                resultat_response_correcte = True
            else:
                print("Mauvaise réponse")
            
        print()
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
        return Question.demander_reponse_numerique_utlisateur(min, max)
    
class Questionnaire:
    def __init__(self, questions):
        self.questions = questions

    def lancer(self):
        score = 0
        
        for question in self.questions:
            if question.poser():
                score += 1
        print("Score final :", score, "sur", len(self.file_des["questions"]))
        #for question in file_des["questions"]:
        #    if question.poser():
        #        score += 1
        #print("Score final :", score, "sur", len(self.questions))
        return score


"""questionnaire = (
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    ("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
                )

lancer_questionnaire(questionnaire)"""

# q1 = Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris")
# q1.poser()

# data = (("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris", "Quelle est la capitale de la France ?")
# q = Question.FromData(data)
# print(q.__dict__)

Questionnaire(
    (
    Question("animaux", "les chats", "confirme"),
    Question("animaux", "les chats", "confirme")
    )
).lancer()

# animaux_leschats_confirme

