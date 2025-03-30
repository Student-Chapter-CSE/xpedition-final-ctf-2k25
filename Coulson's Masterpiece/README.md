# Challenge

## Title

Coulson's Masterpiece

## Description

Agent Coulson has always been a man of many talents—strategizing, espionage, even taking down Hydra agents. But as it turns out, art isn't one of them.

In his attempt to conceal classified information, Coulson hastily sketched something that was supposed to be a masterpiece. Unfortunately, it's such a mess that even Hydra couldn't decipher it.

Your mission should you choose to accept it is to unravel Coulson’s questionable drawing skills, and retrieve the secret before Hydra does!

## Files

- `Coulson.svg` - A bad drawing

## Solution

The flag is hidden in the form of a QR code beneath the top layers of the SVG image. Keep removing the top layers until you reach the QR code. You can achieve this by opening the SVG file in the browser and using the developer tools to inspect the elements. The QR code is located at the bottom of the SVG file.

## Flag

```text
gnosis{c0u1s0n5_4r7_sk1ll5_4r3_w0rs3_th4n_hydr4s_d3c3pt10n} 
```
