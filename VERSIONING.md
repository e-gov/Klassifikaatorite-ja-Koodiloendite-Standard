# KLF-standardi draft/stable seadistus

**Olek: rakendusettepanek, mitte GitHubi paigaldatud muudatus.**
Valmistatud 28.09.2026. SKOS/XKOS-vastendust see pakett ei lisa.

## Avaldamismudel

| Allikas | Avaldamine |
| --- | --- |
| `draft`-haru | Iga push uuendab `/draft/` versiooni. |
| `main`-haru | Kinnitatud lähtesisu; tavaline push ei muuda avaldatud stabiilset versiooni. |
| Esmane `bootstrap-stable` main-harust | Loob senise sisu alusversiooni `baseline` ja aliase `stable`. |
| Hilisem heakskiidetud `v*` tähis | Loob eraldi väljalaske ja suunab `stable` sellele. |
| `gh-pages-versioned` | Uus tehniline haru, kuhu salvestatakse kõik ehitatud versioonid. |

Veebi juuraadress suunab `/stable/` alla. Päises on versioonivalik.
`baseline` on tehniline alusversiooni nimi, mitte oletus standardi ametliku versiooninumbri kohta.
Tähistatud väljalaske commit peab kuuluma main-haru ajalukku.

Eeskuju on Andmekirjelduse-Standardi mike-põhine lahendus. Erinevus: mustand
avaldatakse teadlikult eraldi draft-harust, mitte main-harust. Kasutame eraldi
avaldamisajaloo haru ning ametlikku Pages-artifakti avaldamist. Senist
avaldamisväljundit ei kustutata. Mustand on avalik; noindex ei ole juurdepääsukontroll.

## Kontrollimata eeldused

GitHubi kirjutusühendus ei olnud vestluses ühendatud. Repositooriumi kloonimine
ning KLF-i praeguse mkdocs.yml ja avaldamisworkflow allalaadimine ei õnnestunud
selle töökeskkonna kaudu. See ei ole täpne diff olemasoleva commit'i vastu.
Olemasoleva workflow nime ega GitHub Pagesi seadistust ei ole oletatud.

Pakett ei asenda mkdocs.yml faili ega muuda docs/ sisu. Uued konfiguratsioonid
pärivad senise MkDocsi konfiguratsiooni. Enne kasutuselevõttu kontrolli, et uued
failinimed ei kattu olemasolevate kohandustega. Senise workflow vajalikud
lisasõltuvused lisa requirements-versioned.txt faili. Sõltuvuste vahemikud ei
ole lukustatud versioonid; täpsed versioonid saab fikseerida pärast pärisehituse kontrolli.

## Kasutuselevõtt

### 1. Lisa tehnilised failid eraldi pull request'iga

Loo main-harust näiteks setup/versioned-pages. Kopeeri repo-files/ **sisu**
repositooriumi juurkausta, säilitades kaustastruktuuri, kaasa arvatud .github/.
Ära lisa repo-files kausta ennast. Esita PR main-harusse. See PR peab sisaldama
ainult avaldamistaristut, mitte SKOS/XKOS-vastendust ega standardi sisumuudatusi.

Enne ühendamist peab **Check versioned documentation** ehitama mõlemad
konfiguratsioonid. Vajalikud pluginad lisa requirements-versioned.txt faili.
Vaata üle ka MkDocsi hoiatused: kontroll ei kasuta esialgu --strict režiimi.
GitHubi käsitsi käivitatav workflow peab asuma ka vaikeharus; seetõttu läheb
ühine taristu main-harusse. See ei tähenda mustandi sisu kinnitamist.

Vana avaldaja võib selles etapis veel töötada: uus avaldaja ei käivitu
main-haru tavalisest push'ist. Uus versioonitud avaldaja ei tohi siiski pärast
üleminekut vana avaldajaga samal ajal veebilehte muuta.

### 2. Ehita alusversioon avalikku lehte muutmata

Pärast PR-i ühendamist vali **Actions -> Publish versioned documentation -> Run workflow**.

- Branch: main
- operation: bootstrap-stable
- publish: false ehk märkimata

Oodatav tulemus: edukas build, vahele jäetud deploy. Artifaktis github-pages
peavad olema versions.json, baseline/index.html, stable/index.html ja juure
index.html. Allalaaditud ZIP-i sees võib olla omakorda TAR-arhiiv.

Eelvaade **salvestab** ehitusajaloo harusse gh-pages-versioned, kuid **ei avalda**
seda veebilehele. See ei ole täiesti kirjutusvaba dry-run. Teistkordne
bootstrap-stable ei kirjuta olemasolevat stabiilset versiooni üle.

### 3. Vii avaldamine uuele töövoole

Salvesta senine Pagesi avaldamisallikas ja senise avaldaja nimi. Peata muud
avaldamistoimingud ülemineku ajaks. Keela **ainult vana veebilehte avaldav
workflow** (Actions -> vastav workflow -> Disable workflow) ja tühista selle
pooleliolevad/ootel avaldamised. Ära keela muid kontrolltöövooge. Hiljem võib
vana workflow eraldi tehnilise PR-iga eemaldada või asendada.

Seejärel kontrolli seadistusi:

- Settings -> Pages -> Build and deployment -> Source: **GitHub Actions**.
- Settings -> Environments -> github-pages: avaldamisreeglid lubavad harud
  main ja draft. Hilisemate väljalasete jaoks lisa eraldi tag-reegel v*.
  Säilita olemasolevad vajalikud heakskiidureeglid.
- Organisatsioon lubab kasutatavaid GitHub Actionsi toiminguid ja töövoos
  deklareeritud õigusi. Isiklikku tokenit see lahendus ei vaja.

Käivita **Publish versioned documentation**: branch main, operation republish,
publish true. See avaldab varem valmis ehitatud versioonid. Kontrolli /stable/
lehte ja juuraadressi suunamist enne draft-haru avaldamist.

### 4. Loo draft-haru

Loo draft **uuendatud main-harust**, et ka mustandil oleks avaldamistaristu.
Kui draft juba eksisteerib, ära kustuta ega kirjuta seda üle: kanna sinna
tehnilised muudatused eraldi PR-iga.

Uue draft-haru push käivitab avaldamise. Alternatiivina vali Actionsis branch
draft, operation draft, publish true. Esimeseks draft-eelvaateks saab kasutada
sama käsitsi käivitust publish=false valikuga; tavaline push on avaldav toiming.

Git-i kaudu, ainult siis, kui draft-haru veel ei ole:

```sh
git fetch origin
git switch -c draft origin/main
git commit --allow-empty -m "Start draft publication"
git push -u origin draft
```

Kui draft-ehitus käivitatakse enne alusversiooni loomist, peatub see veaga.
Mustandit ei valita kunagi stabiilse versiooni asemel vaikimisi versiooniks.

### 5. Kontrolli tulemust

Oodatavad aadressid **pärast edukat avaldamist**, mitte selle paketi loomisel:

- https://e-gov.github.io/Klassifikaatorite-ja-Koodiloendite-Standard/
- https://e-gov.github.io/Klassifikaatorite-ja-Koodiloendite-Standard/stable/
- https://e-gov.github.io/Klassifikaatorite-ja-Koodiloendite-Standard/draft/

Kontrolli versioonivalikut, draft-päise MUSTAND-teksti, mõlema versiooni otsingut,
pilte ja skeeme. Kontrolli vana süvalinki, näiteks /klassifikaator/atribuudid/:
see peaks suunduma sama lehe /stable/ versioonile, säilitades ankru ja päringu.
Kui vana fail puudub uuest stabiilsest ehitusest, ei saa skript seda taastada;
sellisele teele tuleb vajaduse korral lisada eraldi suunamine.

Kontrolli docs/ sisu absoluutlinke: käsitsi vanale juuraadressile kirjutatud
link võib ka draft-lehelt stabiilsesse versiooni viia. Vajaduse korral muuda
need versioonisisesteks suhtelisteks linkideks. Alles seejärel lisa vastendus draft-harusse.

## Edasine kasutus ja taastamine

Mustandi sisu muuda draft-harus. Kinnitatud väljalase eeldab kontrollitud PR-i
main-harusse ja seejärel kokkulepitud uut v* tähist sellel commit'il.
Lihtne main-push ei avalda uut stabiilset versiooni.

Avaldatud tähist ei kirjutata üle. Ebaõnnestunud avaldamise kordamiseks ilma
uuesti ehitamata kasuta main / republish / publish=true. Kui GitHubi concurrency
jättis mõne ootel töövoo vahele, kontrolli selle run'i olekut ning käivita
vajalik toiming uuesti: ühist aktiivset avaldamist ei katkestata, kuid see ei
ole kõigi sündmuste FIFO-järjekord.

Tagasipöördumiseks peata uus avaldaja, taasta salvestatud Pagesi allikas ning
luba ja käivita vana avaldaja uuesti. Vana avaldamisharu ja docs/ sisu ei ole
kustutatud. Uus gh-pages-versioned võib jääda alles vea uurimiseks.

## Allikad

- Eeskuju workflow: https://github.com/e-gov/Andmekirjelduse-Standard/blob/main/.github/workflows/deploy-mkdocs.yml
- Eeskuju konfiguratsioon: https://github.com/e-gov/Andmekirjelduse-Standard/blob/main/mkdocs.yml
- mike: https://github.com/jimporter/mike
- Materiali versioonivalik: https://squidfunk.github.io/mkdocs-material/setup/setting-up-versioning/
- MkDocsi konfiguratsiooni pärimine: https://www.mkdocs.org/user-guide/configuration/#configuration-inheritance
- GitHub Pagesi workflow: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
- Pagesi avaldamisallikas: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- Käsitsi käivitamine: https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow
