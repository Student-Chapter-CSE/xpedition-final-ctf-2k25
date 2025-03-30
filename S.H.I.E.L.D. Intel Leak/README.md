# Challenge

## Title

S.H.I.E.L.D. Intel Leak

## Description

Agent Coulson's been compromised! His encrypted message to Director Fury was intercepted by a Hydra mole. We believe it contains the location of a hidden S.H.I.E.L.D. base. Can you decode the message and help the Avengers find it before Hydra does?

## Files

- `secret.txt` - The encrypted message from Agent Coulson.

## Solution

The coded message is encoded using Base64 encoding. To decode it, we can use the `base64` command-line utility or a programming language like Python.

- Using the command line, we can decode the message with the following command:

  ```bash
  base64 -d secret.txt
  ```

- Alternatively, we can use Python to decode the message:

  ```python
  import base64
  with open('secret.txt', 'r') as file:
      encoded_message = file.read()
  decoded_message = base64.b64decode(encoded_message).decode('utf-8')
  print(decoded_message)
  ```

### CyberChef Recipe

<https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=WjI1dmMybHplMnd3WXpRM01UQnVYekUxWHpRM2JEUnVOekZqWHpCak16UnVmUT09>

## Flag

```text
gnosis{l0c4710n_15_47l4n71c_0c34n}
```
