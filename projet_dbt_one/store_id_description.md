{% docs store_id_description %}

**store_id** représente l'identifiant unique de chaque magasin dans le modèle de données.

### Détails :

- Il s'agit d'une **clé étrangère** (foreign key) qui fait référence à la colonne `id` de la table `stores`.
- Cette colonne permet de **lier les ventes ou commandes** à un magasin spécifique dans l'entreprise.
- Elle est utilisée dans les jointures pour enrichir les données transactionnelles avec des informations sur les magasins (nom, localisation, etc.).

### Exemple d'utilisation :

```sql
select
  o.order_id,
  s.store_name
from {{ ref('fct_sales') }} o
left join {{ ref('stg_stores') }} s
  on o.store_id = s.id
