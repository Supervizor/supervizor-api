

# API interface for Supervizor ##

For programmable access to web application Supervizor, API interface is available.


## Supported formats

API interface can output data serialized in JSON, XML or JSONP formats.
JSONP callback function is specified with *callback* GET parameter.
Default function name is *supervizor_callback*.

If the client supports gzip encoding, the data is transferred compressed.


## Calls

Currently API interface consist of three calls. Described below is the structure.

### GET /api/v1/json/company/[tax_id]/

Call returns basic information about business entity and list of financial transactions, monthly sums of transactions and events.

#### Example for a company (Slovenian Postal Services - Pošta Slovenije)

Call:

[/api/v1/json/company/25028022/](http://supervizor.kpk-rs.si/api/v1/json/company/25028022/)

Returns response similar to:

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


Description of individual fields:

 * **status**: Response status; should be "ok".
 * **total_sum**: Total amount of received funds from public sector.
 * **company**: Subobject, containing information about the company.
  * **id**: Registry number of the company.
  * **name**: Short name of the company.
  * **tax_id**: Tax ID number of the company.
 * **transactions**: Object list, containing information about transactions.
  * **amount**: Amount of transaction.
  * **connected**: "true", if transaction is directed to a subsidiary company.
  * **id**: id of transaction,
  * **label**: Name of the recipient of the public funds.
 * **monthly_sums**: List of objects containing monthly sums of funds to be shown in a timeline.
  * **amount**: Total amount of transactions for a given month.
  * **month**: Month in ISO 8601 date format.
 * **events**: List of objects containing information about events regarding a company.
  * **date**: Date of event in ISO 8601 date format.
  * **link**: URL address for event, if present, if not, empty.
  * **description**: Description of event.

### GET /api/v1/json/institution/[pu_id]/

Call returns basic information about public budget users and list of financial transactions, monthly sums of transactions and events.

#### Example for a public budget user (Comission for Prevention of Corruption - Komisija za preprečevanje korupcije)

Call:

[/api/v1/json/institution/13153/](http://supervizor.kpk-rs.si/api/v1/json/institution/13153/)

Returns response similar to:

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


Description of individual fields:

 * **status**: Response status; should be "ok".
 * **total_sum**: Total amount of expenses of public budget user.
 * **gov\_institution**: Subobject containing information about public budget user.
  * **sifra_pu**: Public budget user ID. List of public budget users is accesible on [Public Payments Administration](http://www.ujp.gov.si/dokumenti/dokument.asp?id=316).
  * **name**: Name of a public budget user.
 * **transactions**: Object list, which contains information about transactions.
  * **amount**: Amount of transaction.
  * **connected**: "true", if transaction is directed to a subsidiary company.
  * **id**: id of transaction,
  * **label**: Name of the recipient of the public funds.
  * **skd**: Standard classification of activity.
 * **monthly_sums**: List of objects containing monthly sums of funds to be shown in a timeline.
  * **amount**: Total amount of transactions for a given month.
  * **month**: Month in ISO 8601 date format.
 * **events**: List of objects containing information about events regarding a public budget user.
  * **date**: Date of event in ISO 8601 date format.
  * **link**: URL address for event, if present, if not, empty.
  * **description**: Description of the event.
  * **type**: Category of the event, also the name of the color to use for event display.



### GET /api/v1/json/institution/[pu\_id]/company/[tax_id]/

Call returns basic information about interaction between a company and public budget user. It lists financial transactions, monthly sums of transactions and events.

#### Example (Comission for Prevention of Corruption - Komisija za preprečevanje korupcije and Slovenian Postal Services - Pošta Slovenije)

Call:

[/api/v1/json/institution/13153/company/25028022/](http://supervizor.kpk-rs.si/api/v1/json/institution/13153/company/25028022/)

Returns response similar to:

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


Description of individual fields:

 * **status**: Response status; should be "ok".
 * **total_sum**: Total amount of expenses of public budget user.
  * **company**: Subobject, which contains information about the company.
  * **id**: Registry number of the company.
  * **name**: Short name of the company.
  * **tax_id**: Tax number of the company.
 * **gov\_institution**: Subobject containing information about public budget user.
  * **sifra_pu**: Code of a public budget user. List of a public budget users is accesible on [Public Payments Administration](http://www.ujp.gov.si/dokumenti/dokument.asp?id=316).
  * **name**: Name of a public budget user.
 * **transactions**: Object list, which contains information about transactions.
  * **date**: Date of transaction.
  * **amount**: Amount of transaction.
  * **desc**: Purpose of transaction.
 * **monthly_sums**: List of objects containing monthly sums of funds to be shown in a timeline.
  * **fiduciary**: "true", if transaction was  credited to a [fiduciary bank account](http://www.bsi.si/placilni-sistemi.asp?MapaId=1455), unless "false".
  * **amount**: Total amount of transactions for a given month.
  * **month**: Month in ISO 8601 date format.
 * **events**: List of objects containing information about events regarding a public budget user.
  * **date**: Date of event in ISO 8601 date format.
  * **link**: URL address for event, if present, if not, empty.
  * **description**: Description of the event.