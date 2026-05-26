---
tags:
  - night-train-to-sharn
  - location
  - map
  - eberron
---
# Khorvaire Interactive Map

*An interactive map of the continent and [[The Firefly]]'s maiden voyage route.*

## The Continent of Khorvaire

```leaflet
id: khorvaire-map
image: Khorvaire Map.png
height: 700px
width: 100%
lat: 50
long: 50
minZoom: 1
maxZoom: 8
defaultZoom: 4
unit: miles
scale: 10
marker: default, 52, 18, Thronehold, Thronehold
marker: default, 58, 38, Starilaskur, Starilaskur
marker: default, 50, 50, Vathirond, Vathirond
marker: default, 38, 56, Aruldusk, Aruldusk
marker: default, 42, 72, Passage, Passage
marker: default, 36, 82, Sharn, Sharn
marker: default, 36, 82, Terminus Station, Terminus Station
```

## [[The Firefly]]'s Journey

The **[[The Firefly|Firefly]]** travels the primary lightning rail artery connecting **[[Thronehold]]** to **[[Sharn]]** — the two most important cities in post-war Khorvaire.

### Route Overview
- **Origin:** [[Thronehold|Thronehold Station]] — the fractured capital, city of ghosts and crowns
- **Destination:** [[Terminus Station|Terminus Station]] — [[Sharn]]'s cathedral of glass, brass, and controlled chaos
- **Duration:** ~8 hours at [[The Firefly|Firefly]]'s enhanced speed
- **Stops:** Starilaskur, Vathirond, Aruldusk, Passage (brief halts for conductor stone alignment)

### Key Locations

#### [[Thronehold]]
The departure point. A city occupied by soldiers from all Five Nations who patrol the same streets but refuse to acknowledge each other. The Treaty of [[Thronehold]] was signed here. So was the [[Timeline|Mourning]] born.

#### Starilaskur
A Brelish trade hub on the shore of Lake Brey. [[House Orien]] maintains a major conductor stone array here.

#### Vathirond
Border town between Breland and Thrane. Tensions remain high despite the Treaty.

#### Aruldusk
Aundairan city known for its arcane universities and crystal production.

#### Passage
The last major stop before [[Sharn]]. A city built around the lightning rail itself — transfer point for routes to the Eldeen Reaches and beyond.

#### [[Sharn]] — The City of Towers
The journey's end. A vertical city of impossible architecture, where the wealthy live in towers that pierce the clouds and the poor toil in [[Sharn|The Cogs]] below. [[The Firefly]] arrives at [[Terminus Station|Terminus Station]], where Inspector Varn of the City Watch waits with too many questions.

---

## For the DM

### The Heist Location
The attack on [[The Firefly]] occurs approximately **4 hours into the journey**, somewhere between **Vathirond** and **Aruldusk** — the most remote stretch of the Brelish countryside. [[Captain Ash]] chose this location because:
- It's far from any major [[House Orien]] response base
- The terrain is flat enough for his crew's skycoach to approach
- The conductor stones are oldest here — easier to disrupt

### Future Expansion
As the campaign unfolds, add markers for:
- The Mournland (Cyre's grave)
- The Mror Holds
- The Talenta Plains
- Xen'drik (if the shard's origin leads there)
- Any locations the party visits in future sessions

To add a new marker, edit the leaflet code block above and add a line like:
```
marker: default, [latitude], [longitude], Note Name, Display Name
```

---

*Map style: [[House Orien]] industrial schematic · 998 YK*
