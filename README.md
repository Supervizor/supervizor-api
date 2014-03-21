

# Programski vmesnik do spletne aplikacije Supervizor ##

Za dostop do spletne aplikacije Supervizor je na voljo tudi programski vmesnik.


## Podprti formati zapisa

Programski vmesnik za serializacijo podpira zapise JSON, JSONP ali XML.
JSONP pokliče funkcijo, katere ime je podano v *callback* GET parametru.
Če ime ni podano, se pokliče funkcija *supervizor_callback*.

Če odjemalec podpira kodiranje gzip, se podatki prenašajo kompresirano.


## Klici

Trenutno je programski vmesnik sestavljen iz treh klicev. Opisana je struktura za JSON, XML 

### GET /api/v1/json/company/[tax_id]/

Klic vrne osnovne podatke o podjetju in sezname transakcij, mesečnih zneskov in dogodkov.

#### Primer za podjetje (na primeru Pošte Slovenije)

Klic:

[/api/v1/json/company/25028022/](http://supervizor.kpk-rs.si/api/v1/json/company/25028022/)

Vrne odgovor, podoben:

    {

        "status": "ok",
        "total_sum": 494675665.8,
        "company": {
            "id": "5881447000",
            "name": "POŠTA SLOVENIJE d.o.o.",
            "tax_id": 25028022
        },
        "transactions": [
            {
                "amount": 27468006.63,
                "connected": false,
                "id": 42188,
                "label": "OKROŽNO SODIŠČE V LJUBLJANI"
            },
            …
        ],
        "monthly_sums": [
            {
                "amount": 3578502.14,
                "month": "2003-01-01"
            },
            …
        ],
        "events": [
            {
                "date": "2003-02-06",
                "link": "",
                "description": "Vpis v register"
            },
            …
        ]

    }

Pomen posameznih polj:

 * **status**: stanje odgovora; mora biti "ok", da je z odgovorom vse v redu.
 * **total_sum**: Skupna vsota prejemkov podjetja iz javnega sektorja.
 * **company**: Podobjekt, ki združuje informacije o podjetju.
  * **id**: Matična številka podjetja.
  * **name**: Kratko ime podjetja.
  * **tax_id**: Davčna številka podjetja.
 * **transactions**: Seznam z objekti, ki vsebujejo informacije o transakcijah.
  * **amount**: Znesek transakcije.
  * **connected**: "true", če gre za nakazilo hčerinskemu podjetju.
  * **id**: id transakcije,
  * **label**: Oznaka naslovnika transakcije.
 * **monthly_sums**: Seznam objektov, ki vsebujejo mesečne vsote za prikaz na časovnici.
  * **amount**: Skupna vsota zneskov transakcij za dani mesec.
  * **month**: Mesec v obliki datuma po zapisu ISO 8601.
 * **events**: Seznam objektov, ki vsebujejo informacije o dogodkih pri podjetju.
  * **date**: datum dogodka v zapisu ISO 8601.
  * **link**: URL naslov, če ima dogodek povezavo, sicer prazno.
  * **description**: Opis dogodka.

### GET /api/v1/json/institution/[pu_id]/

Klic vrne osnovne podatke o proračunskem uporabniku in sezname transakcij, mesečnih zneskov in dogodkov.

#### Primer za proračunskega uporabnika (na primeru Komisije za preprečevanje korupcije)

Klic:

[/api/v1/json/institution/13153/](http://supervizor.kpk-rs.si/api/v1/json/institution/13153/)

Vrne odgovor, podoben:

    {
        "status": "ok",
        "transactions": [ 
            {
                "skd": "61.100",
                "amount": 91076.55,
                "connected": false,
                "id": 98511734,
                "label": "TELEKOM SLOVENIJE, d.d."
            },
            …
        ],
        "total_sum": 2892476.14,
        "gov_institution": {
            "sifra_pu": 13153,
            "name": "KOMISIJA ZA PREPREČEVANJE KORUPCIJE"
        },
        "monthly_sums": [ 
            {
                "amount": 34493.71,
                "month": "2012-01-01"
            },
            …
        ],
        "events": [
            {
                "date": "2004-10-01",
                "link": "",
                "description": "PU: Vpis v register",
                "type": "blue"
            },
            …
        ]
    }

Pomen posameznih polj:

 * **status**: stanje odgovora; mora biti "ok", da je z odgovorom vse v redu.
 * **total_sum**: Skupni znesek odhodkov proračunskega uporabnika.
 * **gov\_institution**: Podobjekt, ki združuje informacije o proračunskem uporabniku.
  * **sifra_pu**: Šifra proračunskega uporabnika. Iskalnik in celoten seznam proračunskih uporabnikov je na voljo na [Upravi za javna plačila](http://www.ujp.gov.si/dokumenti/dokument.asp?id=316).
  * **name**: Ime proračunskega uporabnika.
 * **transactions**: Seznam z objekti, ki vsebujejo informacije o transakcijah.
  * **amount**: Znesek transakcije.
  * **connected**: "true", če gre za nakazilo hčerinskemu podjetju.
  * **id**: id transakcije,
  * **label**: Oznaka naslovnika transakcije.
 * **monthly_sums**: Seznam objektov, ki vsebujejo mesečne vsote za prikaz na časovnici.
  * **amount**: Skupna vsota zneskov transakcij za dani mesec.
  * **month**: Mesec v obliki datuma po zapisu ISO 8601.
 * **events**: Seznam objektov, ki vsebujejo informacije o dogodkih pri podjetju.
  * **date**: datum dogodka v zapisu ISO 8601.
  * **link**: URL naslov, če ima dogodek povezavo, sicer prazno.
  * **description**: Opis dogodka.
  * **type**: Kategorija dogodka.



### GET /api/v1/json/institution/[pu\_id]/company/[tax_id]/

Klic vrne osnovne podatke o poslovanju podjetja z izbranim proračunskim uporabnikom in sezname transakcij, mesečnih zneskov in dogodkov.

#### Primer (na primeru Komisije za preprečevanje korupcije in Pošte Slovenije)

Klic:

[/api/v1/json/institution/13153/company/25028022/](http://supervizor.kpk-rs.si/api/v1/json/institution/13153/company/25028022/)

Vrne odgovor, podoben:

    {
        "status": "ok",
        "company": {
            "id": "5881447000",
            "name": "POŠTA SLOVENIJE d.o.o.",
            "tax_id": 25028022
        },
        "transactions": [
            {
                "date": "2006-02-13",
                "amount": 45.28,
                "desc": "5870018 FRANKIRANJE, POŠTNINA"
            },
            …
        ],
        "gov_institution": {
            "sifra_pu": 13153,
            "name": "KOMISIJA ZA PREPREČEVANJE KORUPCIJE"
        },
        "monthly_sums": [
            {
                "fiduciary": false,
                "amount": 437.18,
                "month": "2013-03-01"
            },
            …
        ],
        "total_sum": 30625.03,
        "events": [
            {
                "date": "2003-02-06",
                "link": "",
                "description": "Vpis v register"
            },
            …
        ]
    }

Pomen posameznih polj:

 * **status**: stanje odgovora; mora biti "ok", da je z odgovorom vse v redu.
 * **total_sum**: Skupni znesek odhodkov proračunskega uporabnika.
 * **company**: Podobjekt, ki združuje informacije o podjetju.
  * **id**: Matična številka podjetja.
  * **name**: Kratko ime podjetja.
  * **tax_id**: Davčna številka podjetja.
 * **gov\_institution**: Podobjekt, ki združuje informacije o proračunskem uporabniku.
  * **sifra_pu**: Šifra proračunskega uporabnika. Iskalnik in celoten seznam proračunskih uporabnikov je na voljo na [Upravi za javna plačila](http://www.ujp.gov.si/dokumenti/dokument.asp?id=316).
  * **name**: Ime proračunskega uporabnika.
 * **transactions**: Seznam z objekti, ki vsebujejo informacije o transakcijah.
  * **date**: Datum transakcije.
  * **amount**: Znesek transakcije.
  * **desc**: Namen transakcije.
 * **monthly_sums**: Seznam objektov, ki vsebujejo mesečne vsote za prikaz na časovnici.
  * **fiduciary**: "true", če gre za vsoto nakazil na [fiduciarni transakcijski račun](http://www.bsi.si/placilni-sistemi.asp?MapaId=1455), sicer "false".
  * **amount**: Skupna vsota zneskov transakcij za dani mesec.
  * **month**: Mesec v obliki datuma v zapisu ISO 8601.
 * **events**: Seznam objektov, ki vsebujejo informacije o dogodkih pri podjetju.
  * **date**: datum dogodka v zapisu ISO 8601.
  * **link**: URL naslov, če ima dogodek povezavo, sicer prazno.
  * **description**: Opis dogodka.


