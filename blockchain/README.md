# Projekti Blockchain

Një zbatim i thjeshtë i blockchain-it në Python që demonstron konceptet bazë të teknologjisë blockchain, përfshirë krijimin e blloqeve, gjenerimin e hash-eve, mekanizmin Proof of Work dhe validimin e zinxhirit.


## Hyrje
Ky projekt implementon një blockchain të thjeshtë në Python. Ai ju lejon të:
- Krijoni një **Genesis Block** (blloku i parë në zinxhir)
- Shtoni blloqe të reja me të dhëna dhe një hash të vlefshëm përmes një mekanizmi të thjeshtë **Proof of Work**
- Validoni integritetin e të gjithë zinxhirit të blloqeve


## Karakteristikat
- **Krijimi i Blloqeve:** Secili bllok përfshin një indeks, kohëzgjatje (timestamp), të dhëna, hash-in e bllokut të mëparshëm, një nonce dhe hash-in e vet.
- **Hash-i:** Përdor algoritmin SHA-256 për të krijuar hash-e unike për secilin bllok, duke siguruar integritetin e të dhënave.
- **Proof of Work:** Implementon një algoritëm minimi që rrit `nonce` derisa të gjendet një hash me një numër të caktuar zero-ve në fillim.
- **Validimi i Blockchain-it:** Përfshin funksionalitet për të verifikuar që secili bllok ka një hash të saktë dhe është i lidhur në mënyrë korrekte me bllokun e mëparshëm.

## Instalimi

### Hapat
1. **Klono depozitën nga GitHub:**
   ```bash
   git clone https://github.com/amoreldmija/blockchain.git
   cd blockchain-project
