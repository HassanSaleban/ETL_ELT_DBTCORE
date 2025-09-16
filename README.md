# 🚀 ETL\_ELT\_DBTCORE_INITIATION

Ce projet a été réalisé dans le cadre d'une prise en main de l'outil **DBT (Data Build Tool)**. Il combine l’utilisation de DBT pour la transformation des données avec **Python** et **SQLAlchemy** pour la phase de chargement initial dans la base de données.

## 📚 Sommaire

- [Objectifs](#objectifs)
- [Structure du projet](#structure-du-projet)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Chargement avec SQLAlchemy](#chargement-avec-sqlalchemy)
- [Contenu DBT](#contenu-dbt)
- [Auteur](#auteur)

---

## 🌟 Objectifs

- Comprendre les concepts **ETL/ELT** et **Data Warehousing**.
- Se familiariser avec **DBT** : structure de projet, modèles, tests, seeds, documentation.
- Charger des données brutes via Python avec **SQLAlchemy**.
- Appliquer des tests de qualité des données (`not_null`, `unique`, `relationship`).

---

## 🗂 Structure du projet

```bash
ETL_ELT_DBTORE/
│
├── logs/
├── projet_dbt_one/
│   ├── models/
│   ├── seeds/
│   └── ...
├── drop_db.py
├── load_data.py        # ← Script de chargement utilisant SQLAlchemy
├── notebook.ipynb
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Installation

```bash
git clone https://github.com/HassanSaleban/ETL_ELT_DBTORE.git
cd ETL_ELT_DBTORE
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## ▶️ Utilisation

1. **Charger les seeds avec DBT**

   ```bash
   dbt seed
   ```

2. **Exécuter les transformations**

   ```bash
   dbt run
   ```

3. **Tester les modèles**

   ```bash
   dbt test
   ```

4. **Générer et consulter la documentation**

   ```bash
   dbt docs generate
   dbt docs serve
   ```

---

##  Chargement avec SQLAlchemy

Le script [`load_data.py`](load_data.py) permet de charger des données CSV dans une base MySQL via **SQLAlchemy**. Voici ses fonctionnalités principales :

- Chargement sécurisé via des **variables d’environnement** (.env\_pass)
- Connexion à la base via une **URL SQLAlchemy**
- Création automatique de la base si elle n'existe pas (`create_database`)
- Chargement de plusieurs fichiers `.csv` depuis un répertoire `seeds/`
- Insertion directe dans des tables nommées `customers`, `orders`, etc.

### Exemple d'utilisation

```bash
python load_data.py
```

Assurez-vous que le fichier `.env_pass` contient :

```
DB_USER=root
DB_PASSWORD= un_mot_de_passe_qui_n_est_pas_celui_ci
DB_HOST=localhost
DB_PORT=3306
DB_NAME=ma_base_de_donnees
```

---

## 🧐 Contenu DBT

| Élément           | Description                             |
| ----------------- | --------------------------------------- |
| `models/staging`  | Modèles de transformation (`stg_*.sql`) |
| `tests/`          | Tests de validation DBT                 |
| `seeds/`          | Données sources                         |
| `dbt_project.yml` | Configuration DBT                       |
| `snapshots/`      | Prévus pour le versioning               |

---

## 👤 Auteur

- **Hassan Saleban**

Prise en main de l'outil réalisé dans le cadre d'une formation à la WildcodeSchool.

