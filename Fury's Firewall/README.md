# Challenge

## Title

Fury's Firewall

## Description

Nick Fury has hidden classified S.H.I.E.L.D. intelligence in a highly secure Firebase database, accessible only with the correct passphrase. Rumor has it that Hydra agents are desperately trying to break in, but they don’t have the password.

Agent Coulson managed to retrieve an HTML/CSS-based access panel, but there's a catch—he doesn’t know the password! Somewhere within the system lies the key to unlocking the vault, and only the most skilled agents can retrieve it.

## Sites

- [Fury's Firewall](https://nick.ctf.sccseaot.com/)

## Solution

Visiting the site, we are presented with a webpage made in HTML, CSS and JavaScript. The page asks for a password to access the flag. The password is checked against a value stored in the Firebase database. The Firebase database is publicly accessible, so we can check the password stored in the database.

We can solve this challenge in a lot of ways, but the easiest ways are:

1. Use the browser's developer tools to check the network requests and find the password in firebase database websocket request messages.
2. Download the entire HTML page and just add a `console.log` statement to the JavaScript code that gets the password from the database. This way, we can see the password in the console when we load the page.
3. We can get the Firebase database URL from the JavaScript code first and then append `.json` at the end of the URL to get the entire content of the database in JSON format.

## Flag

```text
gnosis{fury_d03snt_tru5t_any0ne_w1th_p455w0rds}
```
