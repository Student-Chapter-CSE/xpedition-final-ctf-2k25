# Challenge

## Title

Help Agent Coulson

## Description

Agent Coulson intercepted a coded message from a Hydra agent before his capture. He believes it contains the location of a hidden Hydra base. The message is encrypted with a certain cipher, and Agent Coulson needs your help to decode it.

## Files

- `secret.txt` - The coded message from the Hydra agent.

## Solution

The coded message is encrypted using a simple Caesar cipher. The key to the cipher is the number of positions each letter in the plaintext is shifted to create the ciphertext. In this case, the key is 5 characters backward.

The Caesar cipher works by shifting each letter in the plaintext by a fixed number of positions down the alphabet. For example, if the key is 5 characters backward, the letter 'A' would be shifted to 'V', 'B' to 'W', and so on. The alphabet wraps around, so after 'Z', it goes back to 'A'.

### CyberChef Recipe

<https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,false,-5)&input=bHN0eG54e3EzNzVfcjMzNzVfNDdfN20zX3Z6MXNvMzd9>

## Flag

```text
gnosis{l375_m3375_47_7h3_qu1nj37}
```
