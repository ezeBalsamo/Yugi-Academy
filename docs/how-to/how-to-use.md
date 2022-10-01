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

## Video Introduction Page

Once there, you will see the video introduction page.
Click anywhere to go to the login page.

---

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

- Repeat Password (must be same as password)

---

## User Profile

You can visit the user profile from the navigation bar displaying user menu:

- You have to click on profile white logo and click on "Profile" option.

- Here, you can see and update your profile and your password.

### Information displayed

- Profile image

- Username

- First name

- Last name

- Email

- Description

- Social network

- Update password button (update password)

- Save button (update profile information)

---

## Update Password

You can update your password by clicking the update password button.

### Information required to update the password

- Current password (it needs to be the same as current user password)

- New password (it needs to be different to current user password)

- Repeat password (it needs to be the same as new password)

---

## Home

After you logged in, you will see home page.
There you will see a short description about the page and purpose.

You will also see a navigation bar at the top of the screen.

---

## Cards

You can visit the Cards link from the navigation bar.
In this link you must select a card type.
Card types are classified by:

- Monster Cards

- Spell Cards

- Trap Cards

If you select any of these types you will be redirected to each card type page.

---

### Card Type Page

Whatever type of card you chose you'll see all the cards of the selected type.

Here you can also register, update or delete a card.

If a type does not have any card registered, you will see a message notifying that:

- You have no cards registered yet.

---

### Spell Card Model structure

A Spell Card has:

- A name

- A type

- An image

- A description

### Spell Card Types

- Normal

- Equip

- Continuous

- Quick-Play

- Field

- Ritual

Example

- name: Pot of Greed

- type: Normal

- image: pot-of-greed.png

- description: Draw 2 cards.

---

### Trap Card Model structure

A Trap Card has:

- A name

- A type

- An image

- A description

### Trap Card Types

- Normal

- Equip

- Continuous

- Counter

- Field

Example

- name: Jar of Greed

- type: Normal

- image: jar-of-greed.png

- description: Draw 1 card.

---

### Monster Card Model structure

A Monster Card has:

- A name

- A type

- A race

- An attribute

- A level (between 1 and 12)

- An attack (greater or equal than 0)

- A defense (greater or equal than 0)

- An image

- A description

### Monster Card Type

- Normal

- Effect

- Ritual

- Fusion

- Synchro

- Xyz

- Pendulum

- Link

- Token

### Monster Card Attributes

- Dark

- Divine

- Earth

- Fire

- Light

- Water

- Wind

Example

- name: Dark Magician

- type: Normal

- race: Spellcaster

- attribute: Dark

- level: 7

- attack: 2500

- defense: 2100

- image: dark-magician.png

- description: The ultimate wizard in terms of attack and defense.

---

## Booster packs

You can visit the Booster Packs link from the navigation bar.
There, you will see, of course, the booster packs.
But first, you will need to filter them (by their name).
Here, you can also register a booster pack.
Once you register a booster pack, you won´t see it immediately.
You will have to filter them (again, by name).

In case your filter don't find any booster pack you'll see a message notifying:

- No booster pack has been found or registered yet.

If there's booster packs with name like name of the filter you'll see them.
A table will be displayed and this will show all booster packs found.

Here you can also take some actions like:

- See cards of booster pack (cards icon)

- Update booster pack information (pencil icon)

- Delete booster pack (delete icon)

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
You can do this by clicking on the cards icon in actions of that booster pack.

There, you will see all the booster pack cards from that booster pack.
Here you can also register, update or delete a booster pack card.

If a booster pack doesn't have any card registered, you'll see a message:

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

## Messages

You can visit user messages from the navigation bar displaying user menu:

- You have to click on profile white logo and click on "Messages" option.

Here, you will see:

- An option where you can select a user and search conversation with him.

- A send button message that links to send message page.

### Conversation page

Here you can see all the conversation between user login and selected user.
This conversation has the style of "Whatsapp" where:

- Avatar and username of selected user at the top of conversation.

- Sent messages have a green background, and have been aligned to right.

- Received messages have a gray background, and have been aligned to left.

### Send message page

Here you can select a user of Yugi Academy and send to him a message.

---

## About

You can visit the About page from the navigation bar.
Here, you will see:

- Porpuse of this page.

- Information about the authors of this Yugi Academy World!

---

## Admin

To visit Admin page go to `http://localhost:8000/admin/` with your web browser.

Here, you will see all Apps and models of our project:

- ACCOUNTS

  - User profiles

- MESSAGES

  - Messages

- YUGIOH

  - Booster pack cards

  - Booster packs

  - Monster cards

  - Spell cards

  - Trap cards

You can add, update or delete all models, but you must meet some conditions:

- Messages must have different sender and receiver.

- In booster pack card, the content type must be one of these:

  - YuGiOh | monster card

  - YuGiOh | spell card

  - YuGiOh | trap card

---
