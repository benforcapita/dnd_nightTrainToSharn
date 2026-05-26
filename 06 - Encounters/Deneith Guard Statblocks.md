---
tags:
  - night-train-to-sharn
  - encounter
  - statblock
  - house-deneith
---
# Deneith Guard Statblocks

```statblock
name: Deneith Guard
size: Medium
type: humanoid
subtype: any race
alignment: lawful neutral
ac: 16 (chain shirt + shield)
hp: 26
hit_dice: 4d8+8
speed: 30 ft.
stats: [14, 12, 14, 10, 12, 10]
skillsaves:
  athletics: "+4"
  perception: "+3"
senses: Passive Perception 13
languages: Common
cr: 1/2
traits:
  - name: Sentinel
    desc: "When the guard hits a creature with an opportunity attack, that creature's speed becomes 0 for the rest of the turn."
  - name: Hold Position
    desc: "If the guard has not moved this turn, it gains +1 AC."
actions:
  - name: Longsword
    desc: "+4 to hit, reach 5 ft. Hit: 6 (1d8+2) slashing damage."
  - name: Spear
    desc: "+4 to hit, reach 5 ft. or range 20/60 ft. Hit: 5 (1d6+2) piercing damage."
```

---

```statblock
name: Deneith Elite Guard
size: Medium
type: humanoid
subtype: any race
alignment: lawful neutral
ac: 17 (half plate + shield)
hp: 45
hit_dice: 6d8+18
speed: 30 ft.
stats: [16, 14, 16, 10, 12, 10]
skillsaves:
  athletics: "+5"
  intimidation: "+2"
  perception: "+3"
senses: Passive Perception 13
languages: Common
cr: 2
traits:
  - name: Sentinel
    desc: "When the guard hits a creature with an opportunity attack, that creature's speed becomes 0 for the rest of the turn."
  - name: Protection
    desc: "When a creature the guard can see attacks a target other than the guard within 5 ft., the guard can use its reaction to impose disadvantage on the attack roll."
  - name: Veteran Discipline
    desc: "The guard has advantage on saving throws against being frightened."
actions:
  - name: Multiattack
    desc: "The guard makes two longsword attacks."
  - name: Longsword
    desc: "+5 to hit, reach 5 ft. Hit: 7 (1d8+3) slashing damage."
  - name: Shield Bash
    desc: "+5 to hit, reach 5 ft. Hit: 5 (1d4+3) bludgeoning damage. If the target is Large or smaller, it must succeed a DC 13 Strength save or be knocked prone."
reactions:
  - name: Parry
    desc: "The guard adds 2 to its AC against one melee attack that would hit it."
```
