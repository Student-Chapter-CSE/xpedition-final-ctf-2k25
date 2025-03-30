# Challenge

## Title

Guess It

## Description

A distress signal has been received from a remote research outpost. Dr. Aris Thorne, a brilliant but eccentric scientist, was working on a groundbreaking project when communication abruptly ceased. The last transmission contained only a garbled message and a single binary file, `guessit`.  
Intelligence suggests Dr. Thorne was researching a containment breach involving a powerful artifact, potentially an Infinity Stone. His outpost may be compromised, and the data within `guessit` is crucial to preventing a catastrophic event. Your mission, agents, is to recover this data. The fate of the world may depend on it.

## Files

- `guessit_linux.out` - The binary file that asks for a password to unlock the flag
- `guessit_windows.exe` - The Windows version of the binary file that asks for a password to unlock the flag

## Solution

The binary file `guessit` is a simple password checker. It checks if the input password matches a hardcoded password. The program will print "Correct Password" and the flag if the password is correct and "Better Luck next time" if it is not.

- You can use the `strings` command to extract the hardcoded password from the binary file.

  ```bash
  strings guessit_linux.out
  ```

- You can even get the flag from the binary file using the `strings` command.

  ```bash
  strings guessit_linux.out | grep "gnosis"
  ```

- Also, you can use hex editor to view the binary file in a more readable format. You can use `xxd` command to convert the binary file to hex format. This will allow you to see the contents of the file in a more readable format. You can find the password and the flag in the dump.

  ```bash
  xxd guessit_linux.out > guessit.hex
  ```

## Flag

```text
gnosis{7h15_15_4_5up3r_53cr37_p455w0rd}
```
