# Challenge

## Title

Hail Hydra

## Description

J.A.R.V.I.S., has intercepted multiple encrypted transmissions from Hydra. Each message comes with a decryption program, but there's a catch—each program is designed for a different operating system, and only one will work on your machine. Your mission is to identify the correct decryption program, execute it with the provided encrypted message, and unveil Hydra's hidden secrets before it's too late.

## Files

- `executables.zip`: A zip file containing multiple executables for different operating systems.
- `secret.txt`: A text file containing an encrypted message from Hydra.

## Solution

1. **Unzip the `executables.zip` file**: Extract the contents of the zip file to access the executables.
2. **Identify your operating system**: Determine which operating system you are using (Windows, Linux, macOS, etc.).
3. **Run the appropriate executable**: Execute the program that matches your operating system. If you are using Windows, run the Windows executable; if you are on Linux, run the Linux executable, and so on.
4. **Decrypt the message**: You can decode the encrypted message using the decryption program. The command is `./encoder_decoder-linux-amd64 -d -t "<THE SECRET FROM secret.txt>"` for Linux and `.\encoded_decoder-windows.exe -d -t "<THE SECRET FROM secret.txt>"` for Windows. This will reveal the flag.

## Flag

```text
gnosis{h41l_hydr4_th3_k3y_t0_unl0ck1ng_s3cr375}
```
