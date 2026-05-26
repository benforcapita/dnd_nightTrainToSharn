---
tags:
  - night-train-to-sharn
  - encounter
  - statblock
  - combat
  - raiders
---
# Train Raider Statblocks

```statblock
name: Train Raider
size: Medium
type: humanoid
subtype: any race
alignment: neutral
ac: 14
hp: 22
hit_dice: 5d8
speed: 30 ft.
stats: [12, 14, 12, 10, 11, 10]
skillsaves:
  athletics: "+3"
  stealth: "+4"
senses: Passive Perception 10
languages: Common
cr: 1/2
traits:
  - name: Tactics
    desc: "Uses cover in the train cars. Attempts to isolate targets. Retreats if reduced below 8 HP."
actions:
  - name: Shortsword
    desc: "+4 to hit, reach 5 ft., one target. Hit: 5 (1d6+2) piercing damage."
  - name: Hand Crossbow
    desc: "+4 to hit, range 30/120 ft. Hit: 5 (1d6+2) piercing damage."
  - name: Grappling Hook
    desc: "+4 to hit, range 30 ft. On hit, target is pulled 10 feet toward the raider (Strength DC 12 to resist)."
```

> **Hebrew Note:** שודדי רכבת — ותיקי מלחמה שהפכו לשודדים. לא מפלצות. אנשים עם סיבות. תנו לשחקנים לראות את האנושיות שלהם לפני שהקרב מתחיל.

---

```statblock
name: Train Raider Saboteur
size: Medium
type: humanoid
subtype: any race
alignment: neutral
ac: 13 (leather armor)
hp: 19
hit_dice: 4d8+2
speed: 30 ft.
stats: [10, 15, 12, 13, 12, 10]
skillsaves:
  sleight_of_hand: "+4"
  stealth: "+4"
  thieves_tools: "+4"
senses: Passive Perception 11
languages: Common
cr: 1/2
traits:
  - name: Saboteur
    desc: "Advantage on checks to disarm traps, open locks, or disable mechanisms."
  - name: Tactics
    desc: "Stays out of direct combat. Retreats if discovered."
actions:
  - name: Dagger
    desc: "+4 to hit, reach 5 ft. or range 20/60 ft. Hit: 4 (1d4+2) piercing damage."
  - name: Acid Flask
    desc: "Range 20 ft., one object or 5-ft. square. Deals 5 (2d4) acid damage to objects or creatures in contact."
  - name: Smoke Bomb
    desc: "Creates a 10-ft. radius sphere of heavily obscuring smoke that lasts 1 minute or until dispersed by wind."
```

---

```statblock
name: Train Raider Heavy
size: Medium
type: humanoid
subtype: any race
alignment: neutral
ac: 16 (chain shirt + shield)
hp: 38
hit_dice: 7d8+7
speed: 25 ft.
stats: [16, 12, 14, 8, 10, 9]
skillsaves:
  athletics: "+5"
senses: Passive Perception 10
languages: Common
cr: 1
traits:
  - name: Hold the Line
    desc: "When adjacent to an ally, both gain +1 AC."
actions:
  - name: Warhammer
    desc: "+5 to hit, reach 5 ft. Hit: 7 (1d8+3) bludgeoning damage."
  - name: Shield Bash
    desc: "+5 to hit. On hit, target must succeed DC 13 Strength save or be knocked prone."
```
