# Challenge

## Title

HydraCryption

## Description

In an attempt to secure their secret communications, Hydra encrypted a classified message using their own special method. They believe their encryption is unbreakable, trusting that no one—not even S.H.I.E.L.D.—can undo their work.

Your mission should you choose to accept it is to analyze Hydra’s encryption, and recover the secret before it’s too late!

## Files

- `privkey.pem`: A private key that can be used to decrypt the message.
- `secret.bin`: The encrypted message.

## Solution

We can use a python script to decrypt the message using the private key. The script will read the private key from `privkey.pem` and the encrypted message from `secret.bin`, then use the RSA algorithm to decrypt the message.
The decrypted message will be in bytes, so we will convert it to a string and print it.

We can also use CyberChef to decrypt the message. CyberChef is a web application that allows you to perform various operations on data, including encryption and decryption.

### CyberChef Recipe

[Click Here](https://gchq.github.io/CyberChef/#recipe=RSA_Decrypt('-----BEGIN%20RSA%20PRIVATE%20KEY-----%5CnMIICWwIBAAKBgQCWNKW9Czd5DWViQdfUbvMGQjcbyhCS/MfbED9NJI1zFHjG/bd5%5CnGMlIkBWRqmWmfDRxsIYk1cTgKyZj2/ldvtThI0FaD3/NnJoLlOmvKu8AAvsI/HEo%5CnjF3DKC5N4qCg5LBVaVSym9knhWwRn3K%2BUZsMBBgEYUfYWHz/D3rcgean4QIDAQAB%5CnAoGACAPytToYQXo0xw/G7fPmvZaCfNXlWQaqvpapHht9fd7hjBLle82WDix8LiwG%5Cn5SG7Jbb7DZOnwCOlVo5aSgWhM/aA%2BlPjf01qWC4EV7/hDbS1TR0sDaLU2YX4GYBX%5CnUGSV8XWMAxZ%2BllSO6oGzMdDhWoq6EIAOXP6TZaHBVMHc0d0CQQDF32hdC3gFhl31%5CnIVixB9JWR2dH0WssmF6mkKf2%2B7LRkTXj2p40EO8KpLyB63iivr/bL34oD/tX7eGV%5CnziAyFzRFAkEAwlSK4O5hyM5G/TPw7le3v3ogow/cMyy%2BbYzHEPi%2B3iehH5WFHX09%5CnWuZwGXgnuGaY1M/EFlklv%2BBMJc7h9Yx07QJAV3b2YdKU/hQz6gwQcUhc0GiFnbhT%5CnIIZFqGje5gzCMWJ3qL1VGvy1PUYuUVttmrqogdGPeVP/LRHomlhf4ORi5QJABMw1%5CniYwZGe4Nzp6Dqj68KJwJRj1UAGdwZB//oimh/LYZwj/cw3eeFipuRhKzWFggGdDv%5CnVGXrCqus9Zn/9iH7mQJAMsJeiK1XTjaJe1zz6mpKcEB1AXQza8hmPGHctHbBfZTg%5CnnZbkx2imxcAtvL0hGf5xNavLFoMbX1ZefPu3Gx/S9w%3D%3D%5Cn-----END%20RSA%20PRIVATE%20KEY-----%5Cn','','RSA-OAEP','SHA-1')&input=MG8CShMxOuTqEQBzU2ioz/Hq4787IIqKyKorn%2B08l92idCVgU/wbP1M5o3VVrWgXKEr3shXPDZEtgwzWmxXmRmk1ZkbPwa4UxyDLul3BSSXRTQuI/geykk8f7qgS0pB0e/75WevBuYHsfbvqr4oK5XzTg2wNctA6PO7f4ZOxi/A)

## Flag

```text
gnosis{h4il_hydr4_but_n0t_th31r_crypt0_sk1lls}
```
