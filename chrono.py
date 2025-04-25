from datetime import datetime, timedelta
import csv

class Chrono:
    def __init__(self, time=None):
        self.start_time = time
        self.end_time = None

    def start(self):
        self.start_time = datetime.now()
        self.end_time = None



    def stop(self):
        self.end_time = datetime.now()
        elapsed = self.end_time - self.start_time
        print("Temps :", elapsed)
        return elapsed

class ClassementCSV:
    def __init__(self, chemin_csv):
        self.chemin = chemin_csv
        self.donnees = []
        self._lire_csv()

    def _str_to_time(self, time_str):
        """Convertit une chaîne HH:MM:SS en timedelta."""
        return timedelta(
            hours=int(time_str.split(":")[0]),
            minutes=int(time_str.split(":")[1]),
            seconds=int(time_str.split(":")[2])
        )

    def _time_to_str(self, delta):
        """Convertit un timedelta en HH:MM:SS."""
        total_seconds = int(delta.total_seconds())
        return str(timedelta(seconds=total_seconds))

    def _lire_csv(self):
        try:
            with open(self.chemin, mode="r", newline='') as fichier:
                reader = csv.DictReader(fichier)
                self.donnees = [
                    {"nom": row["nom"], "temps": self._str_to_time(row["temps"])}
                    for row in reader
                ]
        except FileNotFoundError:
            self.donnees = []

    def ajouter_score(self, nom, temps_str):
        nouveau_temps = self._str_to_time(temps_str)
        trouve = False
        score_modifie = False

        for entry in self.donnees:
            if entry["nom"] == nom:
                trouve = True
                if nouveau_temps < entry["temps"]:
                    entry["temps"] = nouveau_temps
                    score_modifie = True
                break

        if not trouve:
            self.donnees.append({"nom": nom, "temps": nouveau_temps})
            score_modifie = True

        if score_modifie:
            self.donnees.sort(key=lambda x: x["temps"])
            self._sauver_csv()

    def _sauver_csv(self):
        with open(self.chemin, mode="w", newline='') as fichier:
            writer = csv.DictWriter(fichier, fieldnames=["nom", "temps"])
            writer.writeheader()
            for entree in self.donnees:
                writer.writerow({
                    "nom": entree["nom"],
                    "temps": self._time_to_str(entree["temps"])
                })

    def top_5(self):
        noms = [entry["nom"] for entry in self.donnees[:5]]
        temps = [self._time_to_str(entry["temps"]) for entry in self.donnees[:5]]

        # Compléter avec des chaînes vides si nécessaire
        while len(noms) < 5:
            noms.append("")
            temps.append("")

        return noms, temps

