import cv2
import time
from ultralytics import YOLO
from collections import defaultdict

# Charger le modèle YOLOv8
model = YOLO("best_base_AmeliorerV21_V2.pt")  # Remplacez "votre_modele.pt" par le chemin vers votre fichier modèle.

# Ouvrir la caméra
cap = cv2.VideoCapture(0)  # Utilise la caméra par défaut (index 0)

if not cap.isOpened():
    print("Erreur : Impossible d'accéder à la caméra.")
    exit()

# Initialiser les variables
last_time = time.time()
detections = defaultdict(list)  # Stocker les fréquences et les scores des cartes détectées
output_file = "Sortie.txt"

# Effacer le fichier de sortie précédent
with open(output_file, "w") as f:
    f.write("Détections filtrées des cartes:\n")

# Paramètre de seuil de confiance
confidence_threshold = 0.9  
frequency_threshold = 30 # Une carte doit apparaître au moins 5 fois consécutives

# Boucle pour traiter le flux vidéo
while True:
    # Lire une image de la caméra
    ret, frame = cap.read()
    if not ret:
        print("Erreur : Impossible de lire l'image de la caméra.")
        break

    # Effectuer la détection
    results = model(frame)

    # Filtrer les prédictions avec un seuil de confiance
    filtered_results = [r for r in results[0].boxes if r.conf >= confidence_threshold]
    for box in filtered_results:
        # Extraire les coordonnées, la classe, et la confiance
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        confidence = float(box.conf)  # Conversion en flottant
        class_id = int(box.cls)  # Conversion en entier
        label = model.names[class_id]

        # Ajouter la détection avec sa confiance
        detections[label].append(confidence)

        # Dessiner les résultats filtrés sur l'image
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"{label} {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Filtrer les cartes validées par fréquence
    validated_detections = {card: scores for card, scores in detections.items() if len(scores) >= frequency_threshold}

    # Calculer les FPS
    current_time = time.time()
    fps = 1 / (current_time - last_time)
    last_time = current_time
    print(f"FPS: {fps:.2f}")

    # Écrire les détections validées dans un fichier
    with open(output_file, "w") as f:
        for card, scores in validated_detections.items():
            avg_confidence = sum(scores) / len(scores)  # Confiance moyenne
            f.write(f"Carte détectée : {card}, Fréquence : {len(scores)}, Confiance moyenne : {avg_confidence:.2f}\n")

    # Afficher le flux vidéo avec les détections
    cv2.imshow("Détection YOLOv8", frame)

    # Quitter avec la touche 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer les ressources
cap.release()
cv2.destroyAllWindows()

# Sauvegarder les détections finales
with open(output_file, "a") as f:
    f.write("\nDétections finales:\n")
    for card, scores in validated_detections.items():
        avg_confidence = sum(scores) / len(scores)
        f.write(f"Carte détectée : {card}, Fréquence : {len(scores)}, Confiance moyenne : {avg_confidence:.2f}\n")
