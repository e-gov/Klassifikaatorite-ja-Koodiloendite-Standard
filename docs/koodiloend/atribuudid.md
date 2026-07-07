# Koodiloendite kirjeldamine

Koodiloendite kirjeldamisel lähtutakse Statistikaameti koodiloendite kirjeldamise juhistest ning DDI Lifecycle 3.3 koodiloendi mudeli loogikast. Standard kirjeldab, millised koodiloendi ja koodiloendi elemendi atribuudid tuleb esitada.

| Standardi osa | DDI objekt |
|---|---|
| Koodiloend | `CodeList` |
| Koodiloendi element | `CodeType`, `Category` |

## 1. Koodiloend
DDI viide: [CodeList](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/CodeList/)

Koodiloend on piiratud koodide ja kategooriate (koodidele vastavate väärtuste) loend, mis esindavad konkreetse muutuja lubatud väärtusi. Koodiloendid võivad olla nii lineaarsed kui hierarhilised.
- Koodiloendis olevad koodid ja kategooriad ei kuulu lahutamatult kokku. Erinevates koodiloendites võib samal kategoorial olla erinev kood.
- Koodiloendi elemendid ei pea igal tasemel katma nähtust kõikselt ja olema üksteist välistavad.
- Muudatuste korral luuakse uus koodiloend.

| # | Atribuudi nimetus | Määratlus | Kohustuslik | Välja tüüp | Mitmesus | Näide |
|---|---|---|---|---|---|---|
| 1 | Tähis (Name) | Koodiloendi tähis. | **Jah** | [NameType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/NameType/) | 0..n | IK_SUGU |
| 2 | Nimetus (Label) | Koodiloendi nimetus. | **Jah** | [LabelType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/LabelType/) | 0..n | Sugu isikukoodist |
| 3 | Kirjeldus (Description) | Koodiloendi sisu ja eesmärgi kirjeldus. | **Jah** | [StructuredStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/StructuredStringType/) | 0..1 | Isiku sugu, mis on tuletatud isikukoodi esimesest numbrist |
| 4 | Kehtivuse algus (ValidFrom) | Kuupäev, millal koodiloend kehtima hakkas. | Ei | `kuupäev` | 0..1 | 2024-01-01 |
| 5 | Kehtivuse lõpp (ValidTo) | Kuupäev, millal koodiloend muudeti kehtetuks. | Ei | `kuupäev` | 0..1 | 2024-12-31 |
| 6 | Omanik/haldaja (MaintenanceUnitReference) | Organisatsioon või üksus, kes vastutab koodiloendi haldamise (st selle uuendamise ja muutmise) eest. | **Jah** | [Agent](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/Agent/) | 0..n | Statistikaamet |
| 7 | Kontaktandmed (ContactPersonReference) | E-posti aadress või telefon, kust saab täiendavat infot koodiloendi kohta. | **Jah** | [Agent](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/Agent/) | 0..n | klassifikaatorid@stat.ee |

## 2. Koodiloendi element
DDI viide: [Code](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/CodeType/), [Category](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/item-types/Category/)

Koodiloendi element on koodiloendis olev üksik väärtus. Element koosneb koodist ja sellele vastavast kategooriast ehk sisulisest väärtusest. Hierarhilise koodiloendi korral võib elemendil olla ka tase.

| # | Atribuudi nimetus | Määratlus | Kohustuslik | Välja tüüp | Mitmesus | Näide |
|---|---|---|---|---|---|---|
| 1 | Tähis (Name) | Loendi elemendi tähis. | Ei | [NameType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/NameType/) | 0..n |  |
| 2 | Kood (ItemCode) | Loendi elemendi kood. Elemendil võib olla täht-, number- või tähtnumberkood, mis vastab antud taseme koodide struktuurile. Kood on unikaalne selles koodiloendis, kuhu element kuulub. | **Jah** | `string` | 0..1 | M |
| 3 | Nimetus (Label) | Loendi elemendi nimetus. Elemendil on koodiloendi omaniku või haldaja poolt loodud nimetus, mis kirjeldab kategooria sisu. | **Jah** | [LabelType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/LabelType/) | 0..n | Mees |
| 4 | Kirjeldus (Description) | Loendi elemendi sisu kirjeldus. | Ei | [StructuredStringType](https://docs.ddialliance.org/DDI-Lifecycle/3.3/model/composite-types/StructuredStringType/) | 0..1 |  |
| 5 | Tase (Level) | Loendi elemendi tase, kui tegemist on hierarhilise loendiga. | Ei | `string` | 0..1 | 1 |