# CHIUDI.

**Follow-up operativo per aziende che lavorano a preventivo.**

CHIUDI parte da una domanda semplice: prima di comprare nuovi lead, quanti preventivi già emessi sono ancora recuperabili?

Il repository contiene una prima versione funzionante e deliberatamente leggera:

- landing pubblica orientata al cliente;
- Recovery Desk locale;
- import/export CSV;
- pipeline, stati e date di follow-up;
- sequenze di messaggi modificabili e copiabili;
- campo esplicito per verificare la base di contatto;
- persistenza nel browser con `localStorage`;
- deploy statico su Cloudflare Workers.

## Avvio locale

Non serve installare dipendenze.

```bash
python3 -m http.server 8787 --directory public
```

Poi apri:

- `http://localhost:8787/`
- `http://localhost:8787/desk.html`

## Deploy Cloudflare

Il progetto usa Workers Static Assets.

```bash
npx wrangler@latest deploy
```

Configurazione: `wrangler.jsonc`.

## Principio di prodotto

Questa versione **non invia messaggi automaticamente**. Serve prima a validare tre cose:

1. che le aziende percepiscano il problema come economicamente importante;
2. che paghino per riordinare e riaprire la pipeline esistente;
3. che il workflow migliori davvero il tasso di follow-up e generi opportunità riaperte.

Automazioni, API WhatsApp/email, AI autonoma e integrazioni CRM entrano solo dopo la prova commerciale.

## Documentazione canonica

- [`docs/PRODUCT.md`](docs/PRODUCT.md) — cosa stiamo costruendo e per chi;
- [`docs/GTM.md`](docs/GTM.md) — primo esperimento commerciale;
- [`docs/COMPLIANCE.md`](docs/COMPLIANCE.md) — vincoli operativi e sicurezza del pilot;
- [`docs/STATUS.md`](docs/STATUS.md) — stato reale del progetto;
- [`docs/NEXT.md`](docs/NEXT.md) — prossime mosse;
- [`docs/DECISIONS.md`](docs/DECISIONS.md) — decisioni già prese.

## CSV

È incluso `public/sample-leads.csv`.

Header consigliato:

```text
nome;lavoro;valore;data_preventivo;prossimo_followup;contatto;base_di_contatto;stato;note
```

L'importer accetta anche virgola e tab come delimitatori e riconosce alcuni alias comuni dei campi.
