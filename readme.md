> [!CAUTION]
> Due to massive changes in the Discord API, deprecated libraries and a personal lack of interest in Switch homebrew this repository has been archived.
> [Robocop](https://github.com/reswitched/robocop-ng) offers the initial version of the error code module, still maintained by the Reswitched Team and should cover the most common errors.

---

# [Click for Bot Invite](#)

# [Discord Client Plugin for Goose Mod](https://github.com/GooseMod-Modules/SwitchErrorLookup)

---

# What is this?

This is a rewrite of the error code module that I maintained for [Robocop/Komet](https://github.com/reswitched/robocop-ng).

This rewrite features automatic scrapping of error codes, a better format for error codes and much more. It'll always only focus on error codes and on nothing else.

---

# API

v1 of the API ran on a dedicated webserver at [DEPRECATED]. Sadly servers are expensive and as such the "API" was re-engineered to be be a fully static file that gets updated through Github Actions at https://raw.githubusercontent.com/tumGER/BETCH/actions/api.json.

[That static file](https://raw.githubusercontent.com/AnnsAnns/BETCH/actions/api.json) will always have the most updated version of the BETCH error codes.

---

# Manual Installation

**This bot is hosted freely [HERE](#), feel free to use it instead**

```pip install -r requirements.py```

and then ```token = "YOUR-TOKEN"``` in "config.py" to your discord token.

---

# License

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
repository, You can obtain one at https://mozilla.org/MPL/2.0/.
