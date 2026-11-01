[← Înapoi la indexul general](../../README.md) | 🇬🇧 English Version TBA

**Acces Rapid:** [📄 Vezi `recombee_items.py`](../recombee_items.py)

---

# Laborator 3: Sistem de recomandare cu Recombee - trimitere items

În cadrul acestui laborator veți continua lucrul cu platforma **Recombee** și cu dataset-ul ales în laboratorul anterior, trecând la popularea efectivă a catalogului cu produse.

- **Link API oficial:** [Recombee API Reference](https://docs.recombee.com/api)
- **Limbajul de programare:** La alegere. *Recombee* pune la dispoziție SDK-uri oficiale în următoarele limbaje: JavaScript, Python, Java, Ruby, PHP, C#, Node.js.

## Cerințe preliminare

1. Asigurați-vă că ați finalizat cu succes *Laboratorul 2* (proprietățile sunt deja definite în Recombee).
2. Asigurați-vă că ați configurat mediul virtual Python conform [Ghidului de instalare din rădăcină](../../README.md).
3. Asigurați-vă că aveți instalate pachetele din `requirements.txt`.
4. Dataset-ul vostru (*CSV*) este curățat și se află în folderul de lucru.

## Cerințe de implementare

### 1. Pregătirea datelor din fișierul CSV

- **Volum:** Minim `100`, maxim `10K` de produse/item-uri (dacă setul inițial este prea mare, veți elimina rânduri).
- **Sursă:** Platforme de date deschise precum [Kaggle](https://www.kaggle.com/), [data.world](https://data.world/) sau site-uri similare.
- **Exemple de domenii:** Cărți, filme, muzică, electronice, produse de supermarket.
- **Coloana de ID:** Identificați coloana care joacă rolul de ID unic pentru fiecare produs, în funcție de dataset-ul vostru (ex.: `product_id`, `id`, `item_id`). Aceasta va fi legată la coloana `itemId` din *Recombee*.

### 2. Cont Recombee

Creați un cont în *Recombee* și oferiți acces profesorului în contul vostru astfel:

1. Intrați în contul vostru pe [Recombee Admin UI](https://admin.recombee.com/).
1. Mergeți în meniul din stânga la *Items*
1. Verificați dacă apar proprietățile definite în *Laboratorul 2*.

### 3. Trimiterea item-urilor în *Recombee*

- Folosind API-ul/SDK-ul oficial, implementați un script care parcurge rândurile din fișierul *CSV* și trimite fiecare produs către *Recombee*.
- **Notă:** Identificatorul unic al produsului îl vom lega la proprietatea `itemId`, pe care *Recombee* ne-o creează implicit.
- **Notă:** Recomandare de optimizare: Pentru a evita trimiterea fiecărui produs printr-un request HTTP separat (ceea ce ar fi foarte lent), puteți folosiți funcționalitatea de *Batch* (cereri batch) oferită de Recombee (*Batch* și *SetItemValues*).

#### Codul de pornire în *Python* (*boilerplate*)

Dacă veți lucra în *Python*, puteți porni  de la script-ul [📄 `recombee_items.py`](../recombee_items.py).

##### Instalare biblioteci

Înainte de a rula codul, trebuie să instalați cele două biblioteci necesare din terminal:
```
pip install recombee-api-client pandas
```

##### Modificare cod

Modificați codul din fișier conform instrucțiunilor din `TODO`-uri, astfel încât să înregistrați în *Recombee* produsele aferente dataset-ului vostru.

### 4. Livrabile obligatorii

- **Repository:** Actualizați repository-ul de *GitHub*/*GitLab* adăugând noul script de trimitere a item-urilor.
- **Documentație:** Actualizați fișierul `README.md` (dacă este nevoie) sau menționați în acesta că datele au fost încărcate cu succes în Recombee.
- **Predare:** Încărcați pe platforma Moodle un fișier cu extensie `.txt` care conține exclusiv link-ul către repository-ul vostru.

## Barem de notare

| Nr. | Criteriu    | Punctaj |
| - | -------- | ------- |
| 1 | Citirea corectă și prelucrarea datelor din fișierul `CSV` (maparea ID-ului unic și a proprietăților) | 30p |
| 2 | Implementarea corectă a scriptului de trimitere folosind SDK-ul Recombee | 30p |
| 3 | Optimizarea trimiterii prin utilizarea cererilor de tip Batch | 20p |
| 4 | Verificarea vizuală în Recombee Admin UI (faptul că item-urile apar în catalog cu atributele completate) | 20p |
