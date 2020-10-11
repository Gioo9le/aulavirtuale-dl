# aulavirtuale-dl

Semplice script per fare un dump delle lezioni registrate attualmente condivise su Dolly nel corso di Gestione dell'informazione

- - - -

### Requisiti per il funzionamento

* BeautifulSoup come libreria per python
* ffmpeg chiamato sul terminale

- - - -

### Utilizzo

Basta avviare lo script da terminale senza parametri o opzioni, l’elenco dei link alle lezioni e’ memorizzato su un dizionario all’interno del file, lo aggiornerò’ man mano che le lezioni verranno pubblicate, ma lo si può’ anche aggiornare in locale semplicemente aggiungendo una nuova voce al dizionario con come chiave la data della lezione e come valore il meetingId scritto alla fine del link che si apre quando si visualizza una lezione registrata 

> Es. https://davy04.edunova.it/playback/presentation/2.0/playback.html?meetingId=17d59e4eb742c498e605406fd441c1a2d7eb4bf0-1601628738707 -> MeetingId = 17d59e4eb742c498e605406fd441c1a2d7eb4bf0-1601628738707  
