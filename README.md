# Lens vs Lille Match Tracker 🏆

Un bot Twitter qui suit et partage les victoires de Lens contre Lille. Le projet analyse automatiquement les résultats des matchs et publie des mises à jour sur Twitter concernant le temps écoulé depuis la dernière victoire de Lens.

## Fonctionnalités ✨

- 📊 **Extraction de données de matchs** : Interrogation automatique d'API pour les résultats de matchs
- ⏱ **Calcul de différence de dates** : Suivi précis du temps écoulé depuis la dernière victoire
- 🐦 **Publication Twitter** : Tweets automatiques pour informer la communauté
- 🔐 **Sécurisé avec .env** : Gestion sécurisée des clés d'API

## Prérequis 🛠

- Python 3.7 ou supérieur
- Compte RapidAPI pour les données de matchs
- Compte Twitter Developer avec les accès API

## Installation 🚀

1. Clonez le projet
```bash
git clone https://github.com/votre_nom_d_utilisateur/nom_du_projet.git
cd nom_du_projet
```

2. Installez les dépendances
```bash
pip install -r requirements.txt
```

3. Configurez votre fichier `.env`
```env
# API Keys
API_KEY=your_api_key_here
API_URL=your_api_url_here

# Twitter Credentials
X_API_KEY=your_twitter_api_key_here
X_API_SECRET_KEY=your_twitter_api_secret_key_here
X_ACCESS_TOKEN=your_twitter_access_token_here
X_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret_here
```

## Utilisation 📝

Exécutez le script principal :
```bash
python main_script.py
```

### Exemple de Tweet
> "Lens n'a pas gagné de match contre Lille depuis le 12 février 2023, soit 1 année, 2 mois et 5 jours."

## Dépendances 📦

- `requests` - Requêtes HTTP
- `python-dateutil` - Calculs de dates
- `tweepy` - API Twitter
- `python-dotenv` - Gestion des variables d'environnement

## Contribuer 🤝

Les contributions sont bienvenues ! Voici comment participer :

1. Forkez le projet
2. Créez votre branche (`git checkout -b feature/nouvelle-fonctionnalite`)
3. Committez vos changements (`git commit -m 'Ajout nouvelle fonctionnalite'`)
4. Pushez vers la branche (`git push origin feature/nouvelle-fonctionnalite`)
5. Ouvrez une Pull Request

## Licence 📜

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.
