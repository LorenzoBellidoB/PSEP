from clases import Voluntario, Gestor

if __name__ == "__main__":

# Solo me a dado tiempo a comprobar que con 4 Voluntarios y 8 Gestores los gestores se quedan esperando.
    NUM_VOLUNTARIOS = 200

    NUM_GESTORES = 4

# Bucles para nombrar e inicializar los hilos
    for i in range(NUM_VOLUNTARIOS):
        voluntario = Voluntario(i + 1)
        voluntario.start()

    for i in range(NUM_GESTORES):
        voluntario = Gestor(i + 1)
        voluntario.start()
   