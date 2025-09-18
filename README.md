# SAAR Website - Site Web d'Assurances

Site web officiel de SAAR Assurances Côte d'Ivoire, développé avec Django.

## 📋 ANALYSE COMPLÈTE DU PROJET

### 🏗️ **ARCHITECTURE GÉNÉRALE**

**Type de projet :** Site web Django pour SAAR Assurances Côte d'Ivoire  
**Framework :** Django 5.0.4  
**Base de données :** PostgreSQL (production) / SQLite3 (développement)  
**Frontend :** Bootstrap 5 + JavaScript/jQuery + SCSS  

### 📊 **MODÈLES DE DONNÉES**

Le projet utilise 11 modèles principaux dans l'app `administration` :

1. **`Caroussel`** - Bannières défilantes de la page d'accueil
2. **`Actualite`** - Articles et actualités de l'entreprise  
3. **`Categorie`** - Classification des produits (Non-Vie, Vie, Takaful)
4. **`Produit`** - Produits d'assurance avec système de slug
5. **`DetailProduit`** - Informations détaillées des produits
6. **`Formule`** - Formules d'assurance par produit
7. **`Garantie`** - Garanties associées aux produits
8. **`Sinistre`** - Déclarations de sinistres (très détaillé)
9. **`Agence`** - Agences SAAR (Abidjan/Intérieur)
10. **`AgentGeneral`** - Agents généraux
11. **`Temoignage`** - Témoignages clients

### 🎯 **FONCTIONNALITÉS PRINCIPALES**

#### **1. Site Vitrine**
- **Page d'accueil** avec carousel, produits, actualités, témoignages
- **Présentation de l'entreprise** (À propos, Groupe, Valeurs)
- **Catalogue produits** organisé par catégories
- **Localisation des agences** avec cartes interactives

#### **2. Gestion des Produits d'Assurance**
- **3 catégories** : Non-Vie (ID=1), Vie (ID=2), Takaful (ID=3)
- **Système de visibilité** (`is_visible`) pour contrôler l'affichage
- **Pages détaillées** avec garanties et formules
- **Navigation par slug** pour un meilleur SEO

#### **3. Système de Contact & Communication**
- **Formulaire de contact** avec envoi d'emails HTML
- **Double notification** (client + entreprise)
- **Templates email** personnalisés
- **Configuration SMTP Gmail**

#### **4. Déclaration de Sinistres**
- **Formulaire complet** pour sinistres automobiles
- **Génération PDF automatique** avec WeasyPrint
- **Envoi par email** avec pièce jointe
- **Gestion des parties** (assuré + adversaire)

#### **5. Interface d'Administration**
- **Django Admin** personnalisé pour tous les modèles
- **Gestion des médias** (images des produits, agences)
- **Système de fixtures** pour les données initiales

### 🛠️ **ARCHITECTURE TECHNIQUE**

#### **Backend**
- **Django 5.0.4** avec structure MVT classique
- **PostgreSQL** pour la production
- **Gestion des médias** avec upload d'images
- **Envoi d'emails** via SMTP Gmail
- **Génération PDF** avec WeasyPrint

#### **Frontend**
- **Bootstrap 5** pour le responsive design
- **Owl Carousel** pour les diaporamas
- **Font Awesome** pour les icônes
- **SCSS** pour la personnalisation des styles
- **JavaScript/jQuery** pour les interactions

#### **Dépendances Clés**
```
Django==5.0.4
psycopg2-binary==2.9.10
weasyprint==64.0
pillow==11.1.0
pandas==2.2.3
```

### 📁 **STRUCTURE DU PROJET**

```
saar_website/
├── src/
│   ├── administration/          # App principale
│   │   ├── models.py           # 11 modèles
│   │   ├── views.py            # Vues admin
│   │   ├── admin.py            # Interface admin
│   │   ├── forms.py            # Formulaire sinistre
│   │   └── migrations/         # 12 migrations
│   ├── saar_website/           # Configuration
│   │   ├── settings.py         # Config Django
│   │   ├── urls.py            # URLs principales
│   │   ├── views.py           # 8 vues publiques
│   │   ├── templates/         # 39 templates HTML
│   │   └── static/            # CSS, JS, images
│   ├── media/                  # Images uploadées
│   └── manage.py
├── requirements.txt
└── README.md
```

### 🎨 **INTERFACE UTILISATEUR**

#### **Design**
- **Thème moderne** avec couleurs corporate SAAR
- **Responsive design** adapté mobile/desktop  
- **Navigation intuitive** avec menus déroulants
- **Carousels animés** pour les produits et témoignages

#### **Pages Principales**
1. **Accueil** (`index.html`) - Carousel, produits, actualités
2. **Produits** (`produit-{id}.html`) - Pages spécifiques par produit
3. **Détail produit** (`detail.html`) - Garanties et formules
4. **À propos** - Présentation entreprise
5. **Agences** - Localisation avec cartes
6. **Contact** - Formulaire avec envoi email
7. **Réclamations** - Déclaration sinistres

### 🔧 **CONFIGURATION**

#### **Base de Données**
- **Production :** PostgreSQL (localhost:5432)
- **Développement :** SQLite3
- **Utilisateur :** postgres / root

#### **Email**
- **SMTP Gmail** configuré
- **Templates HTML** pour les notifications
- **Double envoi** (accusé réception client)

#### **Sécurité**
- **DEBUG=True** (⚠️ à désactiver en production)
- **SECRET_KEY** exposée (⚠️ à sécuriser)
- **ALLOWED_HOSTS** configurés pour local

### 📈 **POINTS FORTS**

✅ **Architecture Django solide** avec bonnes pratiques  
✅ **Interface utilisateur moderne** et responsive  
✅ **Système complet de gestion des produits**  
✅ **Fonctionnalité sinistres très détaillée**  
✅ **Intégration email fonctionnelle**  
✅ **Administration complète via Django Admin**  

### ⚠️ **POINTS D'AMÉLIORATION**

🔸 **Sécurité** - Masquer SECRET_KEY et désactiver DEBUG  
🔸 **Performance** - Optimiser les requêtes base de données  
🔸 **SEO** - Améliorer les métadonnées et structure  
🔸 **Tests** - Ajouter une suite de tests automatisés  
🔸 **Monitoring** - Implémenter logs et monitoring  

---

## 🚀 Installation et Configuration

### Prérequis
- Python 3.12+
- PostgreSQL
- Git

### Installation

1. **Cloner le projet**
```bash
git clone <repository-url>
cd saar_website
```

2. **Créer l'environnement virtuel**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Configuration base de données**
```bash
# Créer la base PostgreSQL
createdb saar_website

# Appliquer les migrations
cd src
python manage.py migrate
```

5. **Charger les données initiales**
```bash
python manage.py loaddata administration/fixtures/data_admin.json
python manage.py loaddata administration/fixtures/users.json
```

6. **Créer un superutilisateur**
```bash
python manage.py createsuperuser
```

7. **Lancer le serveur**
```bash
python manage.py runserver
```

### URLs Principales
- **Site public :** http://127.0.0.1:8000/
- **Administration :** http://127.0.0.1:8000/admin/

---

## 📚 Notes Techniques

### Upload d'images Django
https://codinggear.org/how-to-upload-images-in-django/

### Gestion des données initiales
https://docs.djangoproject.com/fr/1.8/howto/initial-data/

**Commandes utiles :**
```bash
# Exporter les données
python -Xutf8 manage.py dumpdata administration > data_admin.json
python -Xutf8 manage.py dumpdata auth.user > users.json

# Importer les données
python manage.py loaddata initial_data.json
```

### Personnalisation Bootstrap
**Éléments impactés par la modification des couleurs :**
- `.btn-primary` (background-color ; border-color)
- `.dropdown-item.active,.dropdown-item:active` (background-color)
- `.bg-primary` (background-color)

### Ressources Images
- https://www.shutterstock.com/fr/search/assurance-voiture-africain
- https://stock.adobe.com/search?k=pattern+background