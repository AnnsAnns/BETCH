# [Click for Bot Invite](https://discordapp.com/api/oauth2/authorize?client_id=520331685104189452&permissions=0&scope=bot)

# [Discord Client Plugin for Goose Mod](https://github.com/GooseMod-Modules/SwitchErrorLookup)

### Donations to keep the bot running: https://ko-fi.com/tomger

---

# What is this?

This is a rewrite of the error code module that I maintained for [Robocop/Komet](https://github.com/reswitched/robocop-ng).

This rewrite features automatic scrapping of error codes, a better format for error codes and much more. It'll always only focus on error codes and on nothing else.

---

# API

There are 3 requests you can set to the server @ err.tomger.eu!

A. ```err.tomger.eu/api/betch/all``` -> Sends every single error code in a huge dictionary

B. ```err.tomger.eu/api/betch/<module_int>/<description_int>``` -> Sends the info related to that error code

C. ```err.tomger.eu/api/betch/reload/<token>``` -> Reloads the error list

---

# Manual Installation

**This bot is hosted freely [HERE](https://discordapp.com/api/oauth2/authorize?client_id=520331685104189452&permissions=0&scope=bot), feel free to use it instead**

```pip install -r requirements.py```

and then ```token = "YOUR-TOKEN"``` in "config.py" to your discord token.

---

# License

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
repository, You can obtain one at https://mozilla.org/MPL/2.0/.
