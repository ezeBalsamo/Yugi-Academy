# How to use

Are you ready to become the next generation duelist? Great, with this guide you'll be more than ready.

Don't forget to read [how to install](how-to-install.md) this application.

So, assuming that you have already installed and started the game, you should go to `http://localhost:8000/yugioh/` with your favourite web browser.
This is your application entry point.

---
### Model structure

The main idea behind is that:
- There are cards.
- There are booster packs.
- There are cards belonging to booster packs. 

This is a like the so-called 'many-to-many relationship', in which a card may belong to many booster packs and therefore, booster packs may have many cards.
When a card belongs to a booster pack, it has additional information, like an identifier and a rarity.

With all this being said, you can play around registering some spell cards.

---

## Home

Once there, you will see the home page (a video).
Click anywhere to go to the login page.

## Login

For this moment, you can log in with any credentials, since the logic is not developed yet.

## Cards

After you successfully logged in, you will see all the cards stored in the system, classified by:
- Monster Cards
- Spell Cards
- Trap Cards

You will also see a navigation bar at the top of the screen.

Currently, you can only register a spell card.
Once you register a spell card, you will see listed all the cards registered.

### Model structure

A Spell Card has:
- A name
- A type
- A description

Example

- name: Pot of Greed
- type: Normal
- description: Draw 2 cards.

---

## Booster packs

You can visit the Booster Packs link from the navigation bar.
There, you will see, of course, the booster packs. But first, you will need to filter them (by their name).

Here, you can also register a booster pack.
Once you register a booster pack, you won´t see it immediately. You will have to filter them (again, by name).
If you have no booster packs registered or if no one was found, you will see a message notifying that.

---

### Model structure

A Booster Pack has:
- A name
- A code
- A release date (mm/dd/yyyy format)

Example

- name: Zombie Madness
- code: SD2
- release date: 01/01/2005

---

## Booster pack cards

From the booster packs page, you can see all the cards belonging to a specific booster pack by clicking on the `Cards` link next to that booster pack.

There, you can also register or delete a booster pack card.

Once you register or delete a booster pack card, you will see listed all the booster pack cards for that specific booster pack.
If you have no booster pack cards registered, you will see a message notifying that.

---

### Model structure

A Booster Pack card has:
- A card (previously stored)
- A booster pack (previously stored)
- An identifier
- A rarity

Example

- card: Pot of Greed
- booster pack: Zombie Madness
- identifier: SD2-EN017
- rarity: Common

---