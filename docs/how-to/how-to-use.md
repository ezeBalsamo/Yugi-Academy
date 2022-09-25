# How to use

Are you ready to become the next generation duelist?
Great, with this guide you'll be more than ready.

Don't forget to read [how to install](how-to-install.md) this application.

You should go to `http://localhost:8000/yugioh/` with your web browser.
This is your application entry point.

---

## Models and their relationship

The main idea behind is that:

- There are cards.

- There are booster packs.

- There are cards belonging to booster packs.

This is a like the so-called 'many-to-many relationship':
a card may belong to many booster packs and a booster pack may have many cards.
A card belonging to a booster pack has an identifier and a rarity.

With all this being said, you can play around registering some spell cards.

---

## Home

Once there, you will see the home page (a video).
Click anywhere to go to the login page.

## Login

### You need to have a registered user to access to yugi academy

You can login to the web page with a previously registered user.
Here, you can also go to sign up page (sign up button) to register a new user.

### Information required for login

- Username

- Password

---

## Sign up

### Information required for sign up

- Username

- Email

- Password

---

## User Profile

You can visit the user profile page from the navigation bar displaying user 
menu (clicking on profile white logo) and clicking on "Profile" option.
Here, you see and update user information and change user password (button).

### Information displayed

- Profile image

- Username

- Full name

- Description

- Social network

- Email

- Password

---

## Change Password

Clicking change password button, you will take you to a change password page.

### Information required to change password

- Current password (need to be the same as current user password)

- New password (need to be different to current user password)

- Confirm password (need to be the same as new password)

---

## Cards

After you logged in, you will see all the cards stored in the system.
They are classified by:

- Monster Cards

- Spell Cards

- Trap Cards

You will also see a navigation bar at the top of the screen.

Currently, you can only register a spell card.
Once you register a spell card, you will see listed all the cards registered.

### Spell Card Model structure

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
There, you will see, of course, the booster packs.
But first, you will need to filter them (by their name).
Here, you can also register a booster pack.
Once you register a booster pack, you won´t see it immediately.
You will have to filter them (again, by name).

Eventually, you will see a message notifying that:

- You have no booster packs registered

- No booster pack has been found

---

### Booster Pack Model structure

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

From the booster packs page, you can see all the cards belonging to one.
You can do this by clicking on the `Cards` link next to that booster pack.

There, you can also register or delete a booster pack card.
After any of those actions, you'll also see listed all the booster pack cards.

Eventually, you will see a message notifying that:

- You have no booster pack cards registered

---

### Booster Pack Card Model structure

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

## About

You can visit the About link from the navigation bar.
Here, you will see the porpuse of this page and all the information 
about the authors of this Yugi Academy World!

---
