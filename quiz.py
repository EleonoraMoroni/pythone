class Student :
    def __init__(self, nome, cognome):
        self._nome = nome
        self._cognome = cognome
        self._totScore = 0.0
        self._nOfQuiz = 0
    
    def getName(self):
        return f"{self._nome} {self._cognome}"

    def addQuiz(self, score) :
        self._totScore += score
        self._nOfQuiz += 1
        
   
    def getTotalScore(self) :
        return self._totScore
   
    def getAverageScore(self) :
        raise ValueError(f"Lo studente {self._nome}{self._cognome} non ha ")
        return self._totScore / self._nOfQuiz
    
eleonora = Student("Eleonora","Moroni") 
davide = Student("Davide","Sambughi")

davide.addQuiz(19)
davide.addQuiz(17)
davide.addQuiz(18)

davide.getAverageScore()

edoardo = Student("Edoardo","Caprini")
edoardo.getAverageScore()
try:
    edoardo.getAverageScore()
except ValueError as e:
    print(e)