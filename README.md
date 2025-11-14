# TP Docker Networks - Flask + MariaDB + Nginx

> **Auteur** : corentin lecoq 
> **Objectif** : Mettre en place une infrastructure Docker avec 3 services sur 2 réseaux isolés  
> **Bonus** : `db` inaccessible depuis l’hôte, `app` accessible uniquement via proxy

---

## Fonctionnalités

- **3 services** :
  - `db` → MariaDB (base de données)
  - `app` → Application Flask (Python + `pymysql`)
  - `proxy` → Nginx (reverse proxy)

- **2 réseaux Docker** :
  - `backend_net` → `app` + `db`
  - `frontend_net` → `proxy` (aussi dans `backend_net` pour parler à `app`)

- **Bonus respectés** :
  - `db` → **aucun port exposé**
  - `app` → **inaccessible en direct** (`curl localhost:5000` → refusé)
  - Accès uniquement via `http://localhost:8080`

---

## Structure du projet

<img width="228" height="266" alt="image" src="https://github.com/user-attachments/assets/7cf6cd81-1d65-4803-a646-7e4aaafbc748" />

---

## Lancement

# Cloner le repo
git clone https://github.com/tonpseudo/tp-networks.git
cd tp-networks

# Lancer
docker-compose up --build

> Attendre ~30s (MariaDB démarre lentement)

---

## Tests

# Page d'accueil
curl http://localhost:8080
# → "Hello from app!"

# Liste des users
curl http://localhost:8080/users
# → [{"id":1,"name":"Tien",...}]

### Bonus : Sécurité

# App inaccessible en direct
curl http://localhost:5000
# → Connection refused

# DB inaccessible depuis l'hôte
mysql -h localhost -u root -p
# → Refusé (pas de port 3306)

---

## Images DockerHub

| Service | Lien DockerHub |
|--------|----------------|
| App    | https://hub.docker.com/r/cocorentindocker/app-vodka38 |
| Proxy  | https://hub.docker.com/r/cocorentindocker/proxy-vodka38 |

> Images buildées avec `docker-compose build` puis poussées avec `docker push`

---

## Détails techniques

### `docker-compose.yml`
- `healthcheck` sur `db` → `app` attend que MariaDB soit prête
- `depends_on` + `service_healthy` → évite les erreurs de connexion
- 2 réseaux isolés avec `driver: bridge`

### `init.sql`
- Crée la base `mydb` et la table `users`
- Insère 3 utilisateurs de test

### `app.py`
- Connexion à MariaDB via `pymysql`
- Retry automatique si la DB n’est pas prête

### `nginx.conf`
- Reverse proxy vers `app:5000`
- Headers de sécurité ajoutés

---

## Vérification des réseaux

docker network inspect tp-networks_backend_net
# → app + db + proxy

docker network inspect tp-networks_frontend_net
# → seulement proxy

---
