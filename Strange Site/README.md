# Challenge

## Title

Strange Site

## Description

Agent Coulson has left a cryptic message for the Avengers: "The key to unlocking this digital vault lies hidden in plain sight."  
A web interface has been provided to access this vault. Your mission, should you choose to accept it, is to find the password and help the Avengers assemble.

## Sites

- [Strange Site](https://coulson.ctf.sccseaot.com/)

## Solution

1. Open the Strange Site link in a web browser.
2. Inspect the page source code to find `getCorrectPassword()` function in the JavaScript code.
3. You can run the function in the browser console to get the password.
4. Or you can get the endpoint of fetching the password by decoding base64 string in the `getCorrectPassword()` function and then visiting the endpoint in the browser.

## Flag

```text
gnosis{n33d_70_f1nd_d0c70r_57r4n63}
```
