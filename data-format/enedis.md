# Formats de données accessible par les API Enedis et leur conversion Quoalise

*Document de travail, en cours d’évolution…*

## Data Connect

### API Metering Data v4

Source

```json
{
  "meter_reading": {
    "usage_point_id": "00000000000000",
    "start": "2019-05-06",
    "end": "2020-09-14",
    "quality": "BRUT",
    "reading_type": {
      "measurement_kind": "power",
      "unit": "W",
      "aggregate": "average"
    },
    "interval_reading": [
      {
        "value": "540",
        "date": "2020-09-14 03:00:00",
        "interval_length": "PT30M",
        "measure_type": "B"
      }
    ]
  }
}
```

TODO B?

En quoalise (actuel proxy Data Connect)

```xml
<quoalise xmlns="urn:quoalise:0">
  <data>
    <meta>
      <device type="electricity-meter">
        <identifier authority="enedis" type="prm" value="00000000000000" />
      </device>
      <measurement>
        <physical quantity="power" type="electrical" unit="W" />
        <business graph="load-profile" direction="production" />
        <aggregate type="average" />
        <sampling interval="1800" />
      </measurement>
    </meta>
    <sensml xmlns="urn:ietf:params:xml:ns:senml">
      <senml bn="urn:dev:prm:00000000000000_consumption_load" bt="1600041600" t="0" v="245" bu="W" />
      <senml t="1800" v="420" />
      <senml t="3600" v="367" />
      <senml t="5400" v="377" />
      <!-- … -->
    </sensml>
  </data>
</quoalise>
```

## API Customers V1

TODO

# SGE

## AHC − ConsultationMesuresV1.1

AHC-R1 Accès à l’historique de consommations

Les mesures retournées sont des consommations restituées sur la grille Distributeur et/ou la grille Fournisseur selon le tableau
ci-dessous, sur une profondeur maximale de douze mois limitée par la date de dernière mise en service

Variations:

- TODO point de mesure en production?
- TODO grille distributeur vs grille fournisseur 

### Consommation Energie Active

C5 nouvelle chaine

```python
{
    'grandeurPhysique': {
        'libelle': 'Energie Active',
        'code': 'EA'
    },
    'classeTemporelle': {
        'libelle': 'Heures Creuses Saison Basse',
        'code': 'HCB'
    },
    'calendrier': {
        'libelle': 'Avec différenciation temporelle et saisonnière',
        'code': 'DI000003'
    },
    'unite': 'kWh',
    'mesuresDatees': {
        'mesure': [
            {
                'valeur': 0,
                'dateDebut': datetime.date(2020, 12, 11),
                'dateFin': datetime.date(2021, 1, 11),
                'nature': {
                    'libelle': 'Réelle',
                    'code': 'REEL'
                },
                'declencheur': {
                    'libelle': 'Publication cyclique',
                    'code': 'CYCLIQUE'
                },
                'statut': {
                    'libelle': 'Initiale',
                    'code': 'INITIALE'
                }
            },
            {
                'valeur': 0,
                'dateDebut': datetime.date(2020, 11, 11),
                'dateFin': datetime.date(2020, 12, 11),
                …
            },
            {
                'valeur': 0,
                'dateDebut': datetime.date(2020, 10, 11),
                'dateFin': datetime.date(2020, 11, 11),
                …
            },
            …
            {
                'valeur': 0,
                'dateDebut': datetime.date(2020, 2, 11),
                'dateFin': datetime.date(2020, 3, 11),
                …
            },
            {
                'valeur': 0,
                'dateDebut': datetime.date(2020, 1, 11),
                'dateFin': datetime.date(2020, 2, 11),
                …
            }
        ]
    }
}, {
    'grandeurPhysique': {
        'libelle': 'Energie Active',
        'code': 'EA'
    },
    'classeTemporelle': {
        'libelle': 'Heures Creuses Hiver/Saison Haute',
        'code': 'HCH'
    },
    'calendrier': {
        'libelle': 'Avec différenciation temporelle et saisonnière',
        'code': 'DI000003'
    },
    'unite': 'kWh',
    'mesuresDatees': {
        'mesure': [
            {
                'valeur': 0,
                'dateDebut': datetime.date(2020, 12, 11),
                'dateFin': datetime.date(2021, 1, 11),
                …
            },
            {
                'valeur': 0,
                'dateDebut': datetime.date(2020, 11, 11),
                'dateFin': datetime.date(2020, 12, 11),
                …
            },
            …
            {
                'valeur': 78,
                'dateDebut': datetime.date(2020, 2, 11),
                'dateFin': datetime.date(2020, 3, 11),
                …
            },
            {
                'valeur': 92,
                'dateDebut': datetime.date(2020, 1, 11),
                'dateFin': datetime.date(2020, 2, 11),
                …
            }
        ]
    }
}, {
    'grandeurPhysique': {
        'libelle': 'Energie Active',
        'code': 'EA'
    },
    'classeTemporelle': {
        'libelle': 'Heures Pleines Saison Basse',
        'code': 'HPB'
    },
    'calendrier': {
        'libelle': 'Avec différenciation temporelle et saisonnière',
        'code': 'DI000003'
    },
    'unite': 'kWh',
    'mesuresDatees': {
        'mesure': [
            {
                'valeur': 0,
                'dateDebut': datetime.date(2020, 12, 11),
                'dateFin': datetime.date(2021, 1, 11),
                …
            },
            {
                'valeur': 0,
                'dateDebut': datetime.date(2020, 11, 11),
                'dateFin': datetime.date(2020, 12, 11),
                …
            },
            …
            {
                'valeur': 0,
                'dateDebut': datetime.date(2020, 2, 11),
                'dateFin': datetime.date(2020, 3, 11),
                …
            },
            {
                'valeur': 0,
                'dateDebut': datetime.date(2020, 1, 11),
                'dateFin': datetime.date(2020, 2, 11),
                …
            }
        ]
    }
}, {
    'grandeurPhysique': {
        'libelle': 'Energie Active',
        'code': 'EA'
    },
    'classeTemporelle': {
        'libelle': 'Heures Pleines Hiver/Saison Haute',
        'code': 'HPH'
    },
    'calendrier': {
        'libelle': 'Avec différenciation temporelle et saisonnière',
        'code': 'DI000003'
    },
    'unite': 'kWh',
    'mesuresDatees': {
        'mesure': [
            {
                'valeur': 0,
                'dateDebut': datetime.date(2020, 12, 11),
                'dateFin': datetime.date(2021, 1, 11),
                …
            },
            {
                'valeur': 0,
                'dateDebut': datetime.date(2020, 11, 11),
                'dateFin': datetime.date(2020, 12, 11),
                …
            },
            …
            {
                'valeur': 294,
                'dateDebut': datetime.date(2020, 2, 11),
                'dateFin': datetime.date(2020, 3, 11),
                …
            },
            {
                'valeur': 358,
                'dateDebut': datetime.date(2020, 1, 11),
                'dateFin': datetime.date(2020, 2, 11),
                …
            }
        ]
    }
}
```

En quoalise

```xml
<!--
'grandeurPhysique': {
    'libelle': 'Energie Active',
    'code': 'EA'
},
'unite': 'kWh',

Energie réactive facturée, aussi pertinente pour la production, on peut demander au fournisseur d’en produire
« énergie consommée mais vraiment utile »

-->

<physical quantity="energy" type="electrical" unit="kWh" />
<business graph="active-energy"
          direction="consumption"
          correction="false"/>
<aggregate type="sum" />

<!--
'classeTemporelle': {
    'libelle': 'Heures Pleines Saison Basse',
    'code': 'HPB'
},
'calendrier': {
    'libelle': 'Avec différenciation temporelle et saisonnière',
    'code': 'DI000003'
},

https://particuliers.engie.fr/en/peak-hours-off-peak-hours.html
Comment ça scale aux autres options de tarification? comme weekend

autre use case

- dépassement
- plage temporelle
- tarifs variables, comme une donnée

EJP rouge / bleu / blanc

Cédric pas forcément besoin du label

Pour rendre générique, une notion d’ordre, plus ou moins cher

=> pas encore prêts à rendre générique

-->

<pricing name="DI000003"
         label="Avec différenciation temporelle et saisonnière"
         range="HPH"
         range-label="Heures Pleines Hiver/Saison Haute"/>

<pricing type="day-peak hour-off-peak"
         code="DI000003/HPH"
         description="Avec différenciation temporelle et saisonnière"
         range-description="Heures Pleines Hiver/Saison Haute"/>

<business … class="month-peak hour-off-peak"/>

=>

<pricing range-code="HPH"
         range-description="Heures Pleines Hiver/Saison Haute"
         type="DI000003"
         type-description="Avec différenciation temporelle et saisonnière"/>

<!--
'nature': {
    'libelle': 'Réelle',
    'code': 'REEL'
},
'declencheur': {
    'libelle': 'Publication cyclique',
    'code': 'CYCLIQUE'
},
'statut': {
    'libelle': 'Initiale',
    'code': 'INITIALE'
}

Utile ?

correction :
- possibilités de données négatives
- toujours réel pour données connectées

TODO vérifier que inverse réel = estimé
business -> nature

name / description, ce qui est affiché sous la courbe
- truc humain, pas forcément à mettre en meta
Mais on doit indique la source, le channel etc

TODO Redondance entre quantity et unit
-->

<business … trigger="periodic"/>
<business … correction="none"/>
<business … nature="real"/>

```

```xml
<quoalise xmlns="urn:quoalise:0">
  <data>
    <meta>
      <device type="electricity-meter">
        <identifier authority="enedis" type="prm" value="00000000000000" />
      </device>
      <measurement
                name="active-energy"
                direction="consumption"
                quantity="energy"
                type="electrical"
                subtype="active"
                unit="kWh"
                estimated="false"
                aggregation="sum"
                sampling-interval="P1D" />
      <pricing range-code="HPH"
               range-description="Heures Pleines Hiver/Saison Haute"
               type="DI000003"
               type-description="Avec différenciation temporelle et saisonnière"/>
    </meta>
    <sensml xmlns="urn:ietf:params:xml:ns:senml">
      <senml bn="urn:dev:prm:00000000000000" n="consumption_load_corrected" bt="1600041600" t="0" v="0" bu="kWh" />
      <senml t="86400" v="0" />
      <senml t="172800" v="0" />
      <senml t="259200" v="0" />
      <!-- … -->
    </sensml>
  </data>
  <!-- repeated for each classe temporelle -->
</quoalise>
```

## CMD2 − ConsultationMesuresDetailleesV2.0

### Puissance active

type: COURBE
grandeur physique: PA

Segment: C5 30M, C1-C4 éventuellement 10M
TODO B?

TODO mesuresCorrigees vs REEL

```python
{
    'pointId': '00000000000000',
    'mesuresCorrigees': 'BRUT',
    'periode': {
        'dateDebut': datetime.date(2020, 3, 1),
        'dateFin': datetime.date(2020, 3, 7)
    },
    'grandeur': [
        {
            'grandeurMetier': 'CONS',
            'grandeurPhysique': 'PA',
            'unite': 'W',
            'mesure': [
                {
                    'v': 100,
                    'd': datetime.datetime(2020, 3, 1, 0, 30, tzinfo=<FixedOffset '+01:00'>),
                    'p': 'PT30M',
                    'n': 'B'
                },
                {
                    'v': 101,
                    'd': datetime.datetime(2020, 3, 1, 1, 0, tzinfo=<FixedOffset '+01:00'>),
                    'p': 'PT30M',
                    'n': 'B'
                },
                …
                {
                    'v': 146,
                    'd': datetime.datetime(2020, 3, 6, 23, 30, tzinfo=<FixedOffset '+01:00'>),
                    'p': 'PT30M',
                    'n': 'B'
                },
                {
                    'v': 147,
                    'd': datetime.datetime(2020, 3, 7, 0, 0, tzinfo=<FixedOffset '+01:00'>),
                    'p': 'PT30M',
                    'n': 'B'
                }
            ]
        }
    ]
}
```

```xml
<quoalise xmlns="urn:quoalise:0">
  <data>
    <meta>
      <device type="electricity-meter">
        <identifier authority="enedis" type="prm" value="00000000000000" />
      </device>
      <measurement>
        <physical quantity="power" type="electrical" unit="W" />
        <business graph="active-power" direction="consumption" />
        <aggregate type="average" />
        <sampling interval="1800" />
      </measurement>
    </meta>
    <sensml xmlns="urn:ietf:params:xml:ns:senml">
      <senml bn="urn:dev:prm:00000000000000_consumption_load" bt="1600041600" t="0" v="0" bu="W" />
      <senml t="1800" v="0" />
      <senml t="3600" v="0" />
      <!-- … -->
    </sensml>
  </data>
  <!-- repeated for each classe temporelle -->
</quoalise>
```

### Puissance réactive inductive

type: COURBE
grandeur physique: PRI

Segment C1-C4
TODO pas dispo en C5?

```python
{
    'pointId': '00000000000000',
    'mesuresCorrigees': 'BRUT',
    'periode': {
        'dateDebut': datetime.date(2020, 3, 1),
        'dateFin': datetime.date(2020, 3, 7)
    },
    'grandeur': [
        {
            'grandeurMetier': 'CONS',
            'grandeurPhysique': 'PRI',
            'unite': 'VAr',
            'mesure': [
                {
                    'v': 100,
                    'd': datetime.datetime(2020, 3, 1, 0, 0, tzinfo=<FixedOffset '+01:00'>),
                    'p': 'PT10M',
                    'n': 'B'
                },
                {
                    'v': 101,
                    'd': datetime.datetime(2020, 3, 1, 0, 10, tzinfo=<FixedOffset '+01:00'>),
                    'p': 'PT10M',
                    'n': 'B'
                },
                …
                {
                    'v': 242,
                    'd': datetime.datetime(2020, 3, 6, 23, 40, tzinfo=<FixedOffset '+01:00'>),
                    'p': 'PT10M',
                    'n': 'B'
                },
                {
                    'v': 243,
                    'd': datetime.datetime(2020, 3, 6, 23, 50, tzinfo=<FixedOffset '+01:00'>),
                    'p': 'PT10M',
                    'n': 'B'
                }
            ]
        }
    ]
}
```

TODO 'mesuresCorrigees': 'BRUT', ?

```xml
<!--
'grandeurMetier': 'CONS',
'grandeurPhysique': 'PRI',
'unite': 'VAr',

power vs reactive power?
https://en.wikipedia.org/wiki/AC_power
var (wikipedia) vs VAr (enedis)
-->

<physical quantity="power" type="electrical" unit="var" />
<business graph="reactive-power"
          direction="consumption"
          correction="false"/>
<aggregate type="average" />
```

### Historique énergie globales quotidiennes

type: ENERGIE
grandeur physique: EA

Segment: C5
TODO autres segments?

```python
{
    'pointId': '00000000000000',
    'mesuresCorrigees': 'BRUT',
    'periode': {
        'dateDebut': datetime.date(2020, 3, 1),
        'dateFin': datetime.date(2020, 3, 7)
    },
    'grandeur': [
        {
            'grandeurMetier': 'CONS',
            'grandeurPhysique': 'EA',
            'unite': 'Wh',
            'mesure': [
                {
                    'v': 800,
                    'd': datetime.datetime(2020, 3, 1, 0, 0, tzinfo=<FixedOffset '+01:00'>),
                    'p': None,
                    'n': None
                },
                {
                    'v': 801,
                    'd': datetime.datetime(2020, 3, 2, 0, 0, tzinfo=<FixedOffset '+01:00'>),
                    'p': None,
                    'n': None
                },
                {
                    'v': 802,
                    'd': datetime.datetime(2020, 3, 3, 0, 0, tzinfo=<FixedOffset '+01:00'>),
                    'p': None,
                    'n': None
                },
                {
                    'v': 803,
                    'd': datetime.datetime(2020, 3, 4, 0, 0, tzinfo=<FixedOffset '+01:00'>),
                    'p': None,
                    'n': None
                },
                {
                    'v': 804,
                    'd': datetime.datetime(2020, 3, 5, 0, 0, tzinfo=<FixedOffset '+01:00'>),
                    'p': None,
                    'n': None
                },
                {
                    'v': 805,
                    'd': datetime.datetime(2020, 3, 6, 0, 0, tzinfo=<FixedOffset '+01:00'>),
                    'p': None,
                    'n': None
                }
            ]
        }
    ]
}
```

```xml
<!--
'grandeurMetier': 'CONS',
'grandeurPhysique': 'PRI',
'unite': 'VAr',

power vs reactive power?
https://en.wikipedia.org/wiki/AC_power
-->

<physical quantity="power" type="electrical" unit="Wh" />
<business graph="reactive-power"
          direction="consumption"/>
<aggregate type="sum" />
```

### Historique de puissances max

type: PMAX
grandeur: PMA

Segment C5
TODO autres segments?

```python
{'code': None, 'message': None, 'data': {
    'pointId': '00000000000000',
    'mesuresCorrigees': 'BRUT',
    'periode': {
        'dateDebut': datetime.date(2020, 1, 1),
        'dateFin': datetime.date(2020, 2, 1)
    },
    'grandeur': [
        {
            'grandeurMetier': 'CONS',
            'grandeurPhysique': 'PMA',
            'unite': 'VA',
            'mesure': [
                {
                    'v': 800,
                    'd': datetime.datetime(2020, 1, 1, 22, 0, 22, tzinfo=<FixedOffset '+01:00'>),
                    'p': None,
                    'n': None
                },
                {
                    'v': 801,
                    'd': datetime.datetime(2020, 1, 2, 22, 0, 22, tzinfo=<FixedOffset '+01:00'>),
                    'p': None,
                    'n': None
                },
                …
                {
                    'v': 829,
                    'd': datetime.datetime(2020, 1, 30, 22, 0, 22, tzinfo=<FixedOffset '+01:00'>),
                    'p': None,
                    'n': None
                },
                {
                    'v': 830,
                    'd': datetime.datetime(2020, 1, 31, 22, 0, 22, tzinfo=<FixedOffset '+01:00'>),
                    'p': None,
                    'n': None
                }
            ]
        }
    ]
}}
```

```xml
<!--
'grandeurMetier': 'CONS',
'grandeurPhysique': 'PMA',
'unite': 'VA',
-->

<physical quantity="power" type="electrical" unit="VA" />
<business graph="max-power"
          direction="consumption"/>
<aggregate type="max" />
```

# Flux historique mail / ftp

F1 - F10 = 10 compteurs dispo dans le linky pour compter de l’énergie (dont 1 en injection)

TODO, est-ce qu’on peut avoir ces données avec API

```
Identifiant PRM;Type de donnees;Date de debut;Date de fin;Grandeur physique;Grandeur metier;Etape metier;Unite;Pas en minutes
00000000000000;Courbe de charge;01/09/2018;21/08/2020;Energie active;Consommation;Comptage Brut;W;

Horodate;Valeur
2018-12-07T00:00:00+01:00;
2018-12-07T01:00:00+01:00;
…
2020-08-20T23:40:00+02:00;270
2020-08-20T23:50:00+02:00;264
```

=> ouvrir en libre office
```
Identifiant PRM;Type de donnees;Date de debut;Date de fin;Grandeur physique;Grandeur metier;Etape metier;Unite
00000000000000;Index;01/09/2019;21/08/2020;Energie active;Consommation;Comptage Brut;Wh

Horodate;Type de releve;EAS F1;EAS F2;EAS F3;EAS F4;EAS F5;EAS F6;EAS F7;EAS F8;EAS F9;EAS F10;EAS D1;EAS D2;EAS D3;EAS D4;EAS T
2019-09-02T00:00:00+02:00;Arrêté quotidien;1009905;819074;2679;2747;;;;;;;1012584;821821;;;1834405
2019-09-03T00:00:00+02:00;Arrêté quotidien;1009905;819074;5185;6747;;;;;;;1015090;825821;;;1840911
2019-09-04T00:00:00+02:00;Arrêté
…
quotidien;2641025;3347317;3622954;5549142;;;;;;;6263979;8896459;;;15160438
2020-08-21T00:00:00+02:00;Arrêté quotidien;2641025;3347317;3628251;5556478;;;;;;;6269276;8903795;;;15173071

Periode;Identifiant calendrier fournisseur;Libelle calendrier fournisseur;Identifiant classe temporelle 1;Libelle classe temporelle 1;Cadran classe temporelle 1;Identifiant classe temporelle 2;Libelle classe temporelle 2;Cadran classe temporelle 2;Identifiant classe temporelle 3;Libelle classe temporelle 3;Cadran classe temporelle 3;Identifiant classe temporelle 4;Libelle classe temporelle 4;Cadran classe temporelle 4;Identifiant classe temporelle 5;Libelle classe temporelle 5;Cadran classe temporelle 5;Identifiant classe temporelle 6;Libelle classe temporelle 6;Cadran classe temporelle 6;Identifiant classe temporelle 7;Libelle classe temporelle 7;Cadran classe temporelle 7;Identifiant classe temporelle 8;Libelle classe temporelle 8;Cadran classe temporelle 8;Identifiant classe temporelle 9;Libelle classe temporelle 9;Cadran classe temporelle 9;Identifiant classe temporelle 10;Libelle classe temporelle 10;Cadran classe temporelle 10;Identifiant calendrier distributeur;Libelle calendrier distributeur;Identifiant classe temporelle distributeur 1;Libelle classe temporelle distributeur 1;Cadran classe temporelle distributeur 1;Identifiant classe temporelle distributeur 2;Libelle classe temporelle distributeur 2;Cadran classe temporelle distributeur 2;Identifiant classe temporelle distributeur 3;Libelle classe temporelle distributeur 3;Cadran classe temporelle distributeur 3;Identifiant classe temporelle distributeur 4;Libelle classe temporelle distributeur 4;Cadran classe temporelle distributeur 4
Du 2019-09-02T00:00:00+02:00 au 2019-10-22T00:00:00+02:00;FC011827;HC Semaine et HC Week-End;HCWE;Heures Creuses Week-end;EAS F1;HPWE;Heures Pleines Week-end;EAS F2;HCSEM;Heures Creuses Semaine;EAS F3;HPSEM;Heures Pleines Semaine;EAS F4;;;EAS F5;;;EAS F6;;;EAS F7;;;EAS F8;;;EAS F9;;;EAS F10;DI000002;Avec différenciation temporelle;HC;Heures Creuses;EAS D1;HP;Heures Pleines;EAS D2;;;EAS D3;;;EAS D4
Du 2019-10-22T00:00:00+02:00 au 2019-10-23T00:00:00+02:00;INCONNU;INCONNU;;;EAS F1;;;EAS F2;;;EAS F3;;;EAS F4;;;EAS F5;;;EAS F6;;;EAS F7;;;EAS F8;;;EAS F9;;;EAS F10;INCONNU;INCONNU;;;EAS D1;;;EAS D2;;;EAS D3;;;EAS D4
Du 2019-10-23T00:00:00+02:00 au 2019-11-02T23:00:00+01:00;FC011827;HC Semaine et HC Week-End;HCWE;Heures Creuses Week-end;EAS F1;HPWE;Heures Pleines Week-end;EAS F2;HCSEM;Heures Creuses Semaine;EAS F3;HPSEM;Heures Pleines Semaine;EAS F4;;;EAS F5;;;EAS F6;;;EAS F7;;;EAS F8;;;EAS F9;;;EAS F10;DI000002;Avec différenciation temporelle;HC;Heures Creuses;EAS D1;HP;Heures Pleines;EAS D2;;;EAS D3;;;EAS D4
Du 2019-11-02T23:00:00+01:00 au 2019-11-03T23:00:00+01:00;INCONNU;INCONNU;;;EAS F1;;;EAS F2;;;EAS F3;;;EAS F4;;;EAS F5;;;EAS F6;;;EAS F7;;;EAS F8;;;EAS F9;;;EAS F10;INCONNU;INCONNU;;;EAS D1;;;EAS D2;;;EAS D3;;;EAS D4
Du 2019-11-03T23:00:00+01:00 au 2019-11-09T23:00:00+01:00;FC011827;HC Semaine et HC Week-End;HCWE;Heures Creuses Week-end;EAS F1;HPWE;Heures Pleines Week-end;EAS F2;HCSEM;Heures Creuses Semaine;EAS F3;HPSEM;Heures Pleines Semaine;EAS F4;;;EAS F5;;;EAS F6;;;EAS F7;;;EAS F8;;;EAS F9;;;EAS F10;DI000002;Avec différenciation temporelle;HC;Heures Creuses;EAS D1;HP;Heures Pleines;EAS D2;;;EAS D3;;;EAS D4
Du 2019-11-09T23:00:00+01:00 au 2019-11-13T23:00:00+01:00;INCONNU;INCONNU;;;EAS F1;;;EAS F2;;;EAS F3;;;EAS F4;;;EAS F5;;;EAS F6;;;EAS F7;;;EAS F8;;;EAS F9;;;EAS F10;INCONNU;INCONNU;;;EAS D1;;;EAS D2;;;EAS D3;;;EAS D4
Du 2019-11-13T23:00:00+01:00 au 2019-12-01T23:00:00+01:00;FC011827;HC Semaine et HC Week-End;HCWE;Heures Creuses Week-end;EAS F1;HPWE;Heures Pleines Week-end;EAS F2;HCSEM;Heures Creuses Semaine;EAS F3;HPSEM;Heures Pleines Semaine;EAS F4;;;EAS F5;;;EAS F6;;;EAS F7;;;EAS F8;;;EAS F9;;;EAS F10;DI000002;Avec différenciation temporelle;HC;Heures Creuses;EAS D1;HP;Heures Pleines;EAS D2;;;EAS D3;;;EAS D4
Du 2019-12-01T23:00:00+01:00 au 2019-12-03T23:00:00+01:00;INCONNU;INCONNU;;;EAS F1;;;EAS F2;;;EAS F3;;;EAS F4;;;EAS F5;;;EAS F6;;;EAS F7;;;EAS F8;;;EAS F9;;;EAS F10;INCONNU;INCONNU;;;EAS D1;;;EAS D2;;;EAS D3;;;EAS D4
Du 2019-12-03T23:00:00+01:00 au 2019-12-08T23:00:00+01:00;FC011827;HC Semaine et HC Week-End;HCWE;Heures Creuses Week-end;EAS F1;HPWE;Heures Pleines Week-end;EAS F2;HCSEM;Heures Creuses Semaine;EAS F3;HPSEM;Heures Pleines Semaine;EAS F4;;;EAS F5;;;EAS F6;;;EAS F7;;;EAS F8;;;EAS F9;;;EAS F10;DI000002;Avec différenciation temporelle;HC;Heures Creuses;EAS D1;HP;Heures Pleines;EAS D2;;;EAS D3;;;EAS D4
Du 2019-12-08T23:00:00+01:00 au 2019-12-09T23:00:00+01:00;INCONNU;INCONNU;;;EAS F1;;;EAS F2;;;EAS F3;;;EAS F4;;;EAS F5;;;EAS F6;;;EAS F7;;;EAS F8;;;EAS F9;;;EAS F10;INCONNU;INCONNU;;;EAS D1;;;EAS D2;;;EAS D3;;;EAS D4
Du 2019-12-09T23:00:00+01:00 au 2019-12-14T23:00:00+01:00;FC011827;HC Semaine et HC Week-End;HCWE;Heures Creuses Week-end;EAS F1;HPWE;Heures Pleines Week-end;EAS F2;HCSEM;Heures Creuses Semaine;EAS F3;HPSEM;Heures Pleines Semaine;EAS F4;;;EAS F5;;;EAS F6;;;EAS F7;;;EAS F8;;;EAS F9;;;EAS F10;DI000002;Avec différenciation temporelle;HC;Heures Creuses;EAS D1;HP;Heures Pleines;EAS D2;;;EAS D3;;;EAS D4
Du 2019-12-14T23:00:00+01:00 au 2019-12-15T23:00:00+01:00;INCONNU;INCONNU;;;EAS F1;;;EAS F2;;;EAS F3;;;EAS F4;;;EAS F5;;;EAS F6;;;EAS F7;;;EAS F8;;;EAS F9;;;EAS F10;INCONNU;INCONNU;;;EAS D1;;;EAS D2;;;EAS D3;;;EAS D4
Du 2019-12-15T23:00:00+01:00 au 2019-12-25T23:00:00+01:00;FC011827;HC Semaine et HC Week-End;HCWE;Heures Creuses Week-end;EAS F1;HPWE;Heures Pleines Week-end;EAS F2;HCSEM;Heures Creuses Semaine;EAS F3;HPSEM;Heures Pleines Semaine;EAS F4;;;EAS F5;;;EAS F6;;;EAS F7;;;EAS F8;;;EAS F9;;;EAS F10;DI000002;Avec différenciation temporelle;HC;Heures Creuses;EAS D1;HP;Heures Pleines;EAS D2;;;EAS D3;;;EAS D4
Du 2019-12-25T23:00:00+01:00 au 2019-12-26T23:00:00+01:00;INCONNU;INCONNU;;;EAS F1;;;EAS F2;;;EAS F3;;;EAS F4;;;EAS F5;;;EAS F6;;;EAS F7;;;EAS F8;;;EAS F9;;;EAS F10;INCONNU;INCONNU;;;EAS D1;;;EAS D2;;;EAS D3;;;EAS D4
Du 2019-12-26T23:00:00+01:00 au 2020-01-05T23:00:00+01:00;FC011827;HC Semaine et HC Week-End;HCWE;Heures Creuses Week-end;EAS F1;HPWE;Heures Pleines Week-end;EAS F2;HCSEM;Heures Creuses Semaine;EAS F3;HPSEM;Heures Pleines Semaine;EAS F4;;;EAS F5;;;EAS F6;;;EAS F7;;;EAS F8;;;EAS F9;;;EAS F10;DI000002;Avec différenciation temporelle;HC;Heures Creuses;EAS D1;HP;Heures Pleines;EAS D2;;;EAS D3;;;EAS D4
Du 2020-01-05T23:00:00+01:00 au 2020-01-06T23:00:00+01:00;INCONNU;INCONNU;;;EAS F1;;;EAS F2;;;EAS F3;;;EAS F4;;;EAS F5;;;EAS F6;;;EAS F7;;;EAS F8;;;EAS F9;;;EAS F10;INCONNU;INCONNU;;;EAS D1;;;EAS D2;;;EAS D3;;;EAS D4
Du 2020-01-06T23:00:00+01:00 au 2020-03-02T23:00:00+01:00;FC011827;HC Semaine et HC Week-End;HCWE;Heures Creuses Week-end;EAS F1;HPWE;Heures Pleines Week-end;EAS F2;HCSEM;Heures Creuses Semaine;EAS F3;HPSEM;Heures Pleines Semaine;EAS F4;;;EAS F5;;;EAS F6;;;EAS F7;;;EAS F8;;;EAS F9;;;EAS F10;DI000002;Avec différenciation temporelle;HC;Heures Creuses;EAS D1;HP;Heures Pleines;EAS D2;;;EAS D3;;;EAS D4
Du 2020-03-02T23:00:00+01:00 au 2020-03-04T23:00:00+01:00;INCONNU;INCONNU;;;EAS F1;;;EAS F2;;;EAS F3;;;EAS F4;;;EAS F5;;;EAS F6;;;EAS F7;;;EAS F8;;;EAS F9;;;EAS F10;INCONNU;INCONNU;;;EAS D1;;;EAS D2;;;EAS D3;;;EAS D4
Du 2020-03-04T23:00:00+01:00 au 2020-03-10T23:00:00+01:00;FC011827;HC Semaine et HC Week-End;HCWE;Heures Creuses Week-end;EAS F1;HPWE;Heures Pleines Week-end;EAS F2;HCSEM;Heures Creuses Semaine;EAS F3;HPSEM;Heures Pleines Semaine;EAS F4;;;EAS F5;;;EAS F6;;;EAS F7;;;EAS F8;;;EAS F9;;;EAS F10;DI000002;Avec différenciation temporelle;HC;Heures Creuses;EAS D1;HP;Heures Pleines;EAS D2;;;EAS D3;;;EAS D4
Du 2020-03-10T23:00:00+01:00 au 2020-03-11T23:00:00+01:00;INCONNU;INCONNU;;;EAS F1;;;EAS F2;;;EAS F3;;;EAS F4;;;EAS F5;;;EAS F6;;;EAS F7;;;EAS F8;;;EAS F9;;;EAS F10;INCONNU;INCONNU;;;EAS D1;;;EAS D2;;;EAS D3;;;EAS D4
Du 2020-03-11T23:00:00+01:00 au 2020-05-02T00:00:00+02:00;FC011827;HC Semaine et HC Week-End;HCWE;Heures Creuses Week-end;EAS F1;HPWE;Heures Pleines Week-end;EAS F2;HCSEM;Heures Creuses Semaine;EAS F3;HPSEM;Heures Pleines Semaine;EAS F4;;;EAS F5;;;EAS F6;;;EAS F7;;;EAS F8;;;EAS F9;;;EAS F10;DI000002;Avec différenciation temporelle;HC;Heures Creuses;EAS D1;HP;Heures Pleines;EAS D2;;;EAS D3;;;EAS D4
Du 2020-05-02T00:00:00+02:00 au 2020-05-03T00:00:00+02:00;INCONNU;INCONNU;;;EAS F1;;;EAS F2;;;EAS F3;;;EAS F4;;;EAS F5;;;EAS F6;;;EAS F7;;;EAS F8;;;EAS F9;;;EAS F10;INCONNU;INCONNU;;;EAS D1;;;EAS D2;;;EAS D3;;;EAS D4
Du 2020-05-03T00:00:00+02:00 au;FC011827;HC Semaine et HC Week-End;HCWE;Heures Creuses Week-end;EAS F1;HPWE;Heures Pleines Week-end;EAS F2;HCSEM;Heures Creuses Semaine;EAS F3;HPSEM;Heures Pleines Semaine;EAS F4;;;EAS F5;;;EAS F6;;;EAS F7;;;EAS F8;;;EAS F9;;;EAS F10;DI000002;Avec différenciation temporelle;HC;Heures Creuses;EAS D1;HP;Heures Pleines;EAS D2;;;EAS D3;;;EAS D4
Identifiant PRM;Type de donnees;Date de debut;Date de fin;Grandeur physique;Grandeur metier;Etape metier;Unite
00000000000000;Puissance maximale quotidienne;01/09/2019;21/08/2020;Puissance maximale atteinte;Consommation;Comptage Brut;W
Horodate;Valeur
2019-09-01T15:17:24+02:00;3695
2019-09-02T01:34:50+02:00;2345
…
2020-08-19T16:00:02+02:00;3699
2020-08-20T08:15:08+02:00;3608
```

# Dataconsoelec

# Bouchage de trous

utilisation de null, comme ici
https://core-wg.github.io/senml-etch/iesg-adam/draft-ietf-core-senml-etch.html
pas cherché plus loin

```xml
<quoalise xmlns="urn:quoalise:0">
  <data>
    <meta>
      <device type="electricity-meter">
        <identifier authority="enedis" type="prm" value="00000000000000" />
      </device>
      <measurement>
        <physical quantity="power" type="electrical" unit="W" />
        <business graph="load-profile" direction="production" />
        <aggregate type="average" />
        <sampling interval="1800" />
      </measurement>
    </meta>
    <sensml xmlns="urn:ietf:params:xml:ns:senml">
      <senml bn="urn:dev:prm:00000000000000_consumption_load" bt="1600041600" t="0" v="245" bu="W" />
      <senml t="1800" v="420" />
      <senml t="3600" v="null" />
      <senml t="5400" v="377" />
      <!-- … -->
    </sensml>
  </data>
</quoalise>
```


# API

Original enedis

```
ConsulterMesuresDetaillees(
    initiateurLogin,
    pointId,
    mesuresTypeCode,
    grandeurPhysique,
    soutirage,
    injection,
    dateDebut,
    dateFin,
    mesuresPas,
    mesuresCorrigees,
    accordClient
)
```

des paramètres inter dépendants, vraiment pas facile de savoir quelles valeures sont possibles dans quelles conditions

vs

Séparé par fonctions en fonction des paramètres possibles (pas de paramètre requis uniquement quand un autre est présent)

```
get_active_power(
    usage_point_id,
    direction,
    corrected,
    start_date,
    end_date
)

get_energy(
    usage_point_id,
    direction,
    corrected,
    period,
    start_date,
    end_date,
)

…
```

vs

Générique, chaque série temporelle dispose de sa propre clé, un mécanisme pour les lister / découvrir par la suite

```
get('consumption_active_power_raw', usage_point_id, start_date, end_date)
get('consumption_active_power_corrected', …)
get('production_active_power_raw', …)
get('production_active_power_corrected', …)
…
get('consumption_energy_daily_raw', …)
get('consumption_energy_monthly_raw', …)
get('consumption_energy_daily_corrected', …)
get('consumption_energy_monthly_corrected', …)
get('consumption_energy_daily_raw', …)
get('consumption_energy_monthly_raw', …)
get('consumption_energy_daily_corrected', …)
get('consumption_energy_monthly_corrected', …)
```

API Enedis vs conversion plus générique

```
MesuresDetaillees/injection/COURBE/E/BRUT
vs
production_voltage_corrected
```

Mais pas tout à fait générique au final (on doit donner le point et la date)

Propostion Gautier

Tu arrives sur le système, tu donne

- dans le get la même chose que tu récupère au niveau de l’id du SENML
    + juste les dates à rajouter
    + séparation host (genre prm, pas forcément accessible) et série temporelle (courbe de charge)

URN vs URI

- URN plus récent, RFC à lire
- on peut dire que le host contient les :, après le dernier : le nom de la série


{"bn":"urn:dev:ow:10e2073a01080063:id_serie/sdfsd/sdfsdf","bt":1.320067464e+09
     {"u":"lon","v":24.30621},
     {"u":"lat","v":60.07965},
     {"t":60,"v":20.3},


type de requete données technique contractuelle
dans tous les cas on veut pouvoir demander juste technique


TODO quantité energie, comment exprimer les types / formes

- electrique, thermique, cinétique etc.
- puissance active / reactive
- puissance active / reactive inductive / reactive capacitive
- etc.
- Déjà une onthologie existante?

### Changement : _

Dans la spec SENML
https://datatracker.ietf.org/doc/html/rfc8428#page-15

```json
[
     {"bn":"urn:dev:ow:10e2073a0108006:","bt":1.276020076001e+09,
      "bu":"A","bver":5,
      "n":"voltage","u":"V","v":120.1},
     {"n":"current","t":-5,"v":1.2},
]
```

Mais dans la spec URN dev
https://datatracker.ietf.org/doc/html/draft-ietf-core-dev-urn-11#page-11

```
urn:dev:ow:264437f5000000ed_humidity    # The humidity
                                        # part of a multi-sensor
                                        # device

urn:dev:ow:264437f5000000ed_temperature # The temperature
                                        # part of a multi-sensor
                                        # device
```

```
  devurn = "urn:dev:" body componentpart
  body = macbody / owbody / orgbody / osbody / opsbody / otherbody
  macbody = %s"mac:" hexstring
  owbody = %s"ow:" hexstring
  orgbody = %s"org:" posnumber "-" identifier *( ":"  identifier )
  osbody = %s"os:" posnumber "-" serial *( ":"  identifier )
  opsbody = %s"ops:" posnumber "-" product "-" serial *( ":"  identifier )
  otherbody = subtype ":" identifier *( ":"  identifier )
  subtype = LALPHA *(DIGIT / LALPHA)
  identifier = 1*devunreserved
  identifiernodash = 1*devunreservednodash
  product = identifiernodash
  serial = identifier
  componentpart = *( "_" identifier )
  devunreservednodash = ALPHA / DIGIT / "."
  devunreserved = devunreservednodash / "-"
  hexstring = 1*(hexdigit hexdigit)
  hexdigit = DIGIT / "a" / "b" / "c" / "d" / "e" / "f"
  posnumber = NZDIGIT *DIGIT
  ALPHA =  %x41-5A / %x61-7A
  LALPHA =  %x41-5A
  NZDIGIT = %x31-39
  DIGIT =  %x30-39
  ```

plus facile à parser, il ne peut y avoir de _ avant une « part »

=> plutôt utiliser _
   ex. urn:dev:prm:30001610071843_consumption/active_power/raw
=> on ne respecte pas le standard urn:dev da.s tous les cas on fait ce qu’on veut
   ex. urn:dev:prm:30001610071843/consumption/active_power/raw
   ex. urn:dev:prm:30001610071843:consumption/active_power/raw

### Données techniques métier

#### ex. donnée "structurées" en SENML

```json
[
     {"bn":"urn:dev:ow:10e2073a01080063","bt":1.320067464e+09,
      "bu":"%RH","v":20},
     {"u":"lon","v":24.30621},
     {"u":"lat","v":60.07965},
     {"t":60,"v":20.3},
     {"u":"lon","t":60,"v":24.30622},
     {"u":"lat","t":60,"v":60.07965},
     {"t":120,"v":20.7},
     {"u":"lon","t":120,"v":24.30623},
     {"u":"lat","t":120,"v":60.07966},
     {"u":"%EL","t":150,"v":98},
     {"t":180,"v":21.2},
     {"u":"lon","t":180,"v":24.30628},
     {"u":"lat","t":180,"v":60.07967}
   ]
```

```json
  [
    {"bn":"urn:dev:ow:10e2073a01080063:","n":"temp","u":"Cel","v":23.1},
    {"n":"label","vs":"Machine Room"},
    {"n":"open","vb":false},
    {"n":"nfc-reader","vd":"aGkgCg"}
  ]
```

=> value typée semble assez chiant à parser, le lecteur doit connaître le type, on peut mettre des vs partout

#### ex. données Enedis

```python
{
    'donneesGenerales': {
        'etatContractuel': {
            'libelle': 'En service',
            'code': 'SERVC'
        },
        'adresseInstallation': {
            'escalierEtEtageEtAppartement': 'B3 RC 01   ',
            'batiment': 'GOYA BAT B3',
            'numeroEtNomVoie': '736 CH DES AMES DU PURGATOIRE',
            'lieuDit': None,
            'codePostal': '06600',
            'commune': {
                'libelle': 'ANTIBES',
                'code': '06004'
            }
        },
        'dateDerniereModificationFormuleTarifaireAcheminement': None,
        'dateDerniereAugmentationPuissanceSouscrite': None,
        'dateDerniereDiminutionPuissanceSouscrite': None,
        'segment': None,
        'niveauOuvertureServices': '2'
    },
    'situationAlimentation': {
        'alimentationPrincipale': {
            'domaineTension': {
                'libelle': 'BT<=36kVA',
                'code': 'BTINF'
            },
            'tensionLivraison': None,
            'modeApresCompteur': None,
            'puissanceRaccordementSoutirage': {
                'valeur': Decimal('9'),
                'unite': 'kVA'
            }
        }
    },
    'situationComptage': {
        'dispositifComptage': {
            'typeComptage': {
                'libelle': 'Compteur Linky',
                'code': 'LINKY'
            },
            'compteurs': {
                'compteur': [
                    {
                        'localisation': {
                            'libelle': 'Gaine',
                            'code': 'GAINE'
                        },
                        'matricule': '782',
                        'ticActivee': True,
                        'ticStandard': False,
                        'ticActivable': True,
                        'plagesHeuresCreuses': None,
                        'parametresTeleAcces': None,
                        'programmationHoraire': None
                    }
                ]
            },
            'disjoncteur': {
                'calibre': {
                    'libelle': '15-45 A',
                    'code': '15-45'
                }
            },
            'relais': None,
            'transformateurCourant': None,
            'transformateurTension': None
        },
        'caracteristiquesReleve': {
            'modeTraitement': None,
            'periodicite': {
                'libelle': 'Mensuelle',
                'code': 'MENSU'
            },
            'plageReleve': None
        },
        'modeReleve': None,
        'mediaReleve': None,
        'futuresPlagesHeuresCreuses': {
            'libelle': 'HC (22H56-6H56)',
            'code': '440'
        },
        'futuresProgrammationsHoraires': None
    },
    'situationContractuelle': None,
    'id': '25946599093143'
}
```

get(urn:dev:prm:30001610071843/technical)

```xml
    <quoalise xmlns="urn:quoalise:0">
      <data>
        <meta>
          <device type="electricity-meter">
            <identifier authority="enedis" type="prm" value="30001610071843"/>
          </device>
        </meta>
        <sensml xmlns="urn:ietf:params:xml:ns:senml">
          <senml bn="urn:dev:prm:30001610071843_technical/"
                 bt="1583016600"
                 n="donneesGenerales/etatContractuel/libelle"
                 vs="En service"/>
          <senml n="donneesGenerales/etatContractuel/code"
                 vs="SERVC"/>
          <senml n="donneesGenerales/adresseInstallation/escalierEtEtageEtAppartement"
                 vs="B3 RC 01" />
          <senml n="donneesGenerales/adresseInstallation/batiment"
                 vs="GOYA BAT B3" />
          <senml n="donneesGenerales/adresseInstallation/numeroEtNomVoie"
                 vs="736 CH DES AMES DU PURGATOIRE" />
          <senml n="donneesGenerales/adresseInstallation/lieuDit"
                 vs="" />
          <senml n="donneesGenerales/adresseInstallation/codePostal"
                 vs="06600" />
          <senml n="donneesGenerales/adresseInstallation/commune/libelle"
                 vs="ANTIBES" />
          <senml n="donneesGenerales/adresseInstallation/commune/code"
                 vs="06004" />
          <!-- … -->
        </sensml>
      </data>
    </quoalise>
```

TODO données non présente, ex lieu dit

```xml
    <senml n="donneesGenerales/adresseInstallation/lieuDit" vs="" />
    <!-- ou carrément ignorer cette données -->
```

Pourrait aussi être utilisé pour demander juste une valeur

get(urn:dev:prm:30001610071843_technical/donneesGenerales/etatContractuel/code)

get(urn:dev:prm:30001610071843_technical/donneesGenerales/etatContractuel/code)

```xml
    <quoalise xmlns="urn:quoalise:0">
      <data>
        <meta>
          <device type="electricity-meter">
            <identifier authority="enedis" type="prm" value="30001610071843"/>
          </device>
        </meta>
        <sensml xmlns="urn:ietf:params:xml:ns:senml">
          <senml bn="urn:dev:prm:30001610071843_technical/"
                 bt="1583016600"
                 n="donneesGenerales/etatContractuel/code"
                 vs="SERVC"/>
          <!-- … -->
        </sensml>
      </data>
    </quoalise>
```

Mais complique dans le cas d’un tableau, il semble y avoir une liste de compteurs.

```python
'situationComptage': {
    'compteurs': {
        'compteur': [
            {
                'localisation': {
                    'libelle': 'Gaine',
                    'code': 'GAINE'
                },
                'matricule': '782',
                'ticActivee': True,
                'ticStandard': False,
                'ticActivable': True,
                'plagesHeuresCreuses': None,
                'parametresTeleAcces': None,
                'programmationHoraire': None
            },
            {…}
        ]
    },
}
```

```xml
    <quoalise xmlns="urn:quoalise:0">
      <data>
        <meta>
          <device type="electricity-meter">
            <identifier authority="enedis" type="prm" value="30001610071843"/>
          </device>
        </meta>
        <sensml xmlns="urn:ietf:params:xml:ns:senml">
          <senml bn="urn:dev:prm:30001610071843_technical/"
                 bt="1583016600"
                 n="situationComptage/compteur[0]/matricule"
                 vs="782"/>
          <!-- … -->
        </sensml>
      </data>
    </quoalise>
```

=> Est-ce que un compteur n’est pas un device propre
urn:dev:prm:30001610071843:0/technical/donneesGenerales/situationComptage/compteur/matricule

ou / dans un autre cas arbitraire

situationComptage/compteur[0]/matricule => [ interdit normalement
situationComptage/compteur/0/matricule => [ interdit normalement

on pourrrait demander situationComptage/compteur pour avoir la liste

Non présent

          <senml n="donneesGenerales/adresseInstallation/lieuDit"
                 vs="" />
=> pas possible de faire la différence entre vide et pas renseigné
          <senml n="donneesGenerales/adresseInstallation/lieuDit"
                 v="null" />
=> comme pour les séries temporelle
          <senml n="donneesGenerales/adresseInstallation/lieuDit" />
=> autorisé ? c’est le plus propre, on part là dessus

#### En version non senml

donner directement la réponse Enedis avec son propre namespace déjà défini

#### Si on veut standardiser une partie?

Dans les deux cas on peut donner toutes les données brutes et dupliquer les informations dans les metadonnées :

```xml
    <quoalise xmlns="urn:quoalise:0">
      <data>
        <meta>
          <device type="electricity-meter">
            <identifier authority="enedis" type="prm" value="30001610071843"/>
          </device>
          <address>
                <firstname>Christiane</firstname>
                <lastname>Gellesch</lastname>
                <address>
                    <line>Avon House</line>
                    <line>23 David Place. St. Helier</line>
                </address>
                <city>Jersey</city>
                <postcode>JE2 2TE</postcode>
          </address>
        </meta>
        <sensml xmlns="urn:ietf:params:xml:ns:senml">
          <!-- … -->
        </sensml>
      </data>
    </quoalise>
```