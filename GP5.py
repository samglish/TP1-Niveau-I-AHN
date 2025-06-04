class Noeud:
    def __init__(self, valeur, gauche=None, droite=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droite = droite

    def __repr__(self):
        return str(self.valeur)

class ArbreBinaireExpression:
    def __init__(self, expression):
        self.expression = expression
        self.index = 0
        self.racine = self._construire_arbre()

    def _construire_arbre(self):
        # Expression formatée : ((2+3)*4)/5
        # On ignore les espaces
        def parse():
            if self.index >= len(self.expression):
                return None

            if self.expression[self.index] == '(':
                self.index += 1
                gauche = parse()
                operateur = self.expression[self.index]
                self.index += 1
                droite = parse()
                self.index += 1  # pour ')'
                return Noeud(operateur, gauche, droite)
            else:
                # chiffre (nombre)
                val = ""
                while self.index < len(self.expression) and self.expression[self.index].isdigit():
                    val += self.expression[self.index]
                    self.index += 1
                return Noeud(int(val))

        return parse()

    def evaluer(self, noeud=None):
        if noeud is None:
            noeud = self.racine
        if isinstance(noeud.valeur, int):
            return noeud.valeur
        gauche = self.evaluer(noeud.gauche)
        droite = self.evaluer(noeud.droite)
        if noeud.valeur == '+':
            return gauche + droite
        elif noeud.valeur == '-':
            return gauche - droite
        elif noeud.valeur == '*':
            return gauche * droite
        elif noeud.valeur == '/':
            return gauche / droite
        else:
            raise ValueError(f"Opérateur inconnu {noeud.valeur}")

    def afficher_infixe(self, noeud=None):
        if noeud is None:
            noeud = self.racine
        if isinstance(noeud.valeur, int):
            return str(noeud.valeur)
        return f"({self.afficher_infixe(noeud.gauche)} {noeud.valeur} {self.afficher_infixe(noeud.droite)})"

if __name__ == "__main__":
    print("\nExpression: ((2+3)*4)/5")
    expr = "((2+3)*4)/5"
    arbre = ArbreBinaireExpression(expr)

    print("Expression infixe reconstruite :")
    print(arbre.afficher_infixe())

    print("\nÉvaluation de l'expression :")
    print(arbre.evaluer())

