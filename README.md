# Proiect ASP .NET MVC 9.0 — OnlineShop "Stario"               + WebScraper Emag
Un proiect in care am implementat lucrand in echipa  o aplicatie web care implementeaza un magazin online . Pentru baza de date am folosit MySql , impreuna cu un fisier sql de backup (care contine baza de date propriu zisa) + MySqlDump .

## Functionalitati :
Cerintele minime : 

Aplicația web se va realiza în ASP.NET Core MVC și C#, folosind Entity
Framework Core pentru gestionarea datelor și ASP.NET Identity pentru
autentificare și roluri.

### 1) Tipuri de utilizatori și sistem de roluri (0.5p)
Să existe patru tipuri de utilizatori:
- ➢ Vizitator neînregistrat – poate vizualiza produse și review-uri.
Utilizatorul neînregistrat va fi redirecționat să își facă un cont atunci
când încearcă adăugarea unui produs în cos
- ➢ Utilizator înregistrat – poate comanda (să adauge produse în coșul de
cumpărături), adăuga produse în wishlist și scrie review-uri;
-- ➢ Colaborator – poate propune produse spre aprobare;
➢ Administrator – gestionează categoriile, produsele, review-urile și
utilizatorii;
### 2) Gestionarea categoriilor dinamice (1.0p)
Administratorul poate adăuga, edita sau șterge categorii de produse direct
din interfață. Fiecare produs aparține unei categorii.
Explicație:
- ➢ Numele categoriei este unic și obligatoriu;
- ➢ La ștergerea unei categorii se vor șterge toate produsele din acea
categorie;
- ➢ Categoriile sunt afișate în meniu și pot fi folosite pentru filtrare;
### 3) Adăugarea și gestionarea produselor (1.0p)
Un produs conține: titlu, descriere, imagine, preț, stoc, rating (1–5) și
review-uri. Produsele pot fi propuse de colaboratori și aprobate de
administrator. Toate câmpurile sunt obligatorii, mai puțin atributele review si
rating.
Explicație:
- ➢ Câmpurile obligatorii trebuie validate (preț > 0, stoc ≥ 0);
- ➢ Fiecare utilizator acordă un rating de la 1 la 5. Ratingul nu este un
câmp obligatoriu;
- ➢ Produsul are un scor calculat automat din media ratingurilor;
- ➢ Review-ul este un comentariu de tip text lăsat de utilizatori. Acest
camp nu este obligatoriu;
- ➢ Imaginile sunt încărcate cu validări de tip și dimensiune – se poate
restricționa încărcarea imaginii cu o anumită dimensiune sau afișarea
ei într-un anumit format, astfel încât toate imaginile să aibă aceeași
dimensiune;
- ➢ După aprobare de către administrator, produsul devine public;
### 4) Flux colaborator – propuneri și re-aprobări (1.0p)
Colaboratorul poate:
- ➢ Propune produse noi care intră în starea “În așteptare”. Acesta
trimite cereri de adăugare administratorului, iar acesta poate accepta
sau respinge produsele. După aprobare produsele vor putea fi
vizualizate în magazin;
- ➢ Edita și șterge doar produsele propria. După editare, produsul necesită
o nouă aprobare;
Explicație:
- ➢ Starea produsului este afișată clar (“Aprobat”, “În așteptare”,
“Respins”);
- ➢ Adminul decide aprobarea și trimite feedback colaboratorului;
### 5) Vizitatorul și comportamentul la acces restricționat (0.5p)
Vizitatorii pot vizualiza produsele și review-urile, dar nu pot adăuga în coș
sau wishlist. Când încearcă aceste acțiuni, sunt redirecționați către pagina de
autentificare.
Explicație:
- ➢ Mesaj de informare: “Pentru a continua, autentifică-te sau creează un
cont”;
- ➢ Aplicația poate salva intenția utilizatorului și o poate relua după login;

### 6) Coș de cumpărături, comenzi și wishlist (1.0p)
Utilizatorii înregistrați pot:
- ➢ Adăuga produse în coș, seta cantitatea dorită și plasa comenzi
(fictive);
- ➢ Stocul produsului scade automat după plasarea comenzii;
- ➢ Adăuga produse într-un wishlist personal, fără duplicare;
- ➢ Muta produse rapid din wishlist în coș;
Explicație:
- ➢ Coșul și wishlist-ul se salvează per utilizator;
- ➢ Se validează stocul la fiecare achiziție;
- ➢ Aplicația afișează mesaj dacă stocul este epuizat;
### 7) Review-uri și rating (0.5p)
Utilizatorii înregistrați pot:
- ➢ Adăuga, edita și șterge review-uri (text și/sau rating 1–5);
- ➢ Vedea scorul mediu al fiecărui produs;
Explicație:
- ➢ Ștergerea unui review duce la recalcularea scorului produsului;
- ➢ Validări clare: textul review-ului este opțional, rating-ul este opțional,
dar trebuie să aibă valoarea între 1–5 în cazul în care este completat;
### 8) Căutare, filtrare și sortare produse (1.0p)
Utilizatorii pot:
- ➢ Căuta produse după denumire. De asemenea, produsele nu trebuie
căutate după tot numele. Ele trebuie să fie găsite și în cazul în care un
utilizator caută doar anumite părți care compun denumirea
(“lapto” → “laptop”);
- ➢ Filtra după categorie – pot căuta după numele categoriei;
- ➢ Rezultatele motorului de căutare pot fi sortate crescător, respectiv
descrescător, în funcție de preț și numărul de stele (se vor implementa
filtre din care un utilizator poate să aleagă);

### 9) Componentă AI – Întrebări & răspunsuri “Product Assistant” (1.0p)
Pe pagina fiecărui produs există un chat lateral AI care răspunde la întrebări
despre produs, folosind date din descriere și FAQ (logare întrebări frecvente).
Explicație:
- ➢ Utilizatorul poate întreba: “Are garanție?” / “Este potrivit pentru
copii?”;
- ➢ Companionul AI caută informațiile relevante și oferă răspunsuri clare;
- ➢ Întrebările frecvente sunt salvate în baza de date;
- ➢ Dacă nu există informații, AI-ul răspunde politicos (“Momentan nu
avem detalii despre acest aspect.”).

### 10) Administrare platformă (0.5p)
Administratorul are control complet asupra aplicației și poate:
- ➢ Gestiona produse, categorii, review-uri și utilizatori. Acesta poate
șterge sau edita produse, șterge review-uri, activa sau revoca
drepturilor utilizatorilor;

### 11) Calitatea proiectului și integrarea AI companion (1.0p)
Se punctează:
- ➢ Organizarea corectă a aplicației MVC (Models, Views, Controllers);
- ➢ Validări de date și mesaje de eroare clare;
- ➢ Seed de date realist (minim 3 utilizatori, 3 categorii, 5 produse cu
review-uri);
- ➢ Integrarea corectă a companionului AI și documentarea modului de
funcționare;
- ➢ README complet – adică acel raport pe care trebuie să-l redactați;

Se acorda 1 punct din oficiu. Punctul se acordă integral pentru proiectele
complete, funcționale și documentate conform cerințelor.

## Implementare:

Pentru a gestiona cat mai bine tasku-urile am folosit Trello + git.


## Cum rulezi proiectul:
Terminal MySql:
```
create database OnlineShopDb;
CREATE USER root IDENTIFIED WITH mysql_native_password BY 't1234578!';
grant all privileges on OnlineShopDb.* to root;

--aici se poate schimba cu orice alt user VEZI appsettings.json
--"DefaultConnection": "Server=localhost;Database=OnlineShopDb;User=root;Password=t1234578!"
--modifica conform user-ului tau pentru a rula
```
Terminal Linux/PWD:
```
mysql -u root -p OnlineShopDb < /home/mario/my_backup.sql

--modifica conform PATH-ului my_backup.sql
--/home/mario/my_backup.sql
```

Din IDE-ul preferat (Rider(Linux) / Visual Studio Code 2022(Windows)):
```
dotnet build
dotnet run
```

## Web-Scraper 

- Pentru a popula baza de date mai eficient am memorat produsele intr-un fisier JSON
- Ne-am gandit la JSON pentru ca majoritatea magazinelor online au codul HTML cu datele produselor public ( click dreapta si view-source code) si pot fi vulnerabile unui scraper
### Cum functioneaza ?
Implementarea a fost facuta folosind Python, BeautifulSoup si Regex. 
- Pe scurt , ii dat link-ul unui pagini de la Emag si acesta iti returneaza toate produsele in formatul JSON corespunzator proiectului.

## Dificultati intalnite:

## Cum arata ?
- Landing Page utilizator nelogat (Vizitator)
  ![Landing Page](docs_github/Screenshot from 2026-01-07 04-01-38.png)





