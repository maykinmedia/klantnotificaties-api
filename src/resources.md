# Resources

Dit document beschrijft de (RGBZ-)objecttypen die als resources ontsloten
worden met de beschikbare attributen.


## KlantNotificatie

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_1.0/doc/objecttype/klantnotificatie)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| url | URL-referentie naar dit object. Dit is de unieke identificatie en locatie van dit object. | string | nee | ~~C~~​R​~~U~~​~~D~~ |
| klant | URL-referentie naar de KLANT (in de Klanten API) | string | ja | C​R​U​D |
| productaanvraag | URL-referentie naar de ProductAanvraag (in de Objecten API) van de KLANT | string | ja | C​R​U​D |
| bericht | Het bericht voor de klant | string | ja | C​R​U​D |


* Create, Read, Update, Delete
