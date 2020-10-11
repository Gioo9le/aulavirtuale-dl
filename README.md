# aulavirtuale-dl

Semplice script per fare un dump delle lezioni registrate attualmente condivise su Dolly nel corso di Gestione dell'informazione

- - - -

### Prerequisiti

* [ffmpeg](https://ffmpeg.org/download.html) presente nel PATH

- - - -

### Installazione

Per installare aulavirtuale-dl:

1. Clona (scarica) questo repository:
   ```bash
   git clone https://github.com/Gioo9le/aulavirtuale-dl
   ```

2. Entra nella directory che si è creata:
   ```bash
   cd aulavirtuale-dl
   ```

3. Crea e attiva un nuovo `venv`:
   
   - su Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
  
   - su Windows:
     ```bat
     py -m venv venv
     venv\Scripts\activate.bat
     ```

4. Installa BeautifulSoup4 per il parsing di pagine web:
   ```bash
   pip install beautifulsoup4
   ```

- - - -

### Utilizzo

Per scaricare tutte le lezioni attualmente conosciute:

1. Attiva il `venv` creato in precedenza:

   - su Linux:
     ```bash
     source venv/bin/activate
     ```
     
   - su Windows:
     ```bat
     venv\Scripts\activate.bat
     ```

2. Avvia lo script di download:
   ```
   python aulavirtuale-dl
   ```
  
> Nota: il download e la combinazione delle lezioni potrebbe richiedere molto tempo!
> Si consiglia di farlo nelle ore di inattività del computer.

- - - -

### Aggiornamento

Per aggiornare `aulavirtuale-dl` all'ultima versione:

1. Se hai modificato in precedenza dei file del progetto:
   
   - Per eliminare le tue modifiche:
     ```
     git stash
     ```
     
   - Per mantenere le tue modifiche (e in seguito effettuare il merge con quelle remote):
     ```
     git add "*"
     git commit
     ```

2. Scarica tutti i nuovi commit dal repository GitHub:
  ```
  git pull
  ```

- - - -

### Aggiungere nuove lezioni

I link a tutte le lezioni conosciute sono memorizzati in `aulavirtuale-dl.py`, nel dizionario `meetingsID` che
 associa il nome del file che verrà creato all'meetingID di BBB.

> ##### Come trovare il meetingID  
> ```
> https://davy04.edunova.it/playback/presentation/2.0/playback.html?meetingId=17d59e4eb742c498e605406fd441c1a2d7eb4bf0-1601628738707
>                                                                             ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑↑ 
> ```

Esso sarà aggiornato man mano che le lezioni verranno pubblicate, ma lo si può anche aggiornare manualmente aggiungendo
 nuove voci al dizionario.
