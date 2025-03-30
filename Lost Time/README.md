# Challenge

## Title

Lost Time

## Description

The Avengers successfully retrieved the Time Stone, but now they face an even greater challenge—returning it to the exact moment it was taken. If they fail, the timeline will collapse, and the world as we know it will be destroyed!

Your task is to ensure the Time Stone is returned at the correct time. However, the authentication system seems... flawed. Perhaps there's a way to convince the system that the stone was returned on time?

## Sites

- [Lost Time](https://lost-time.ctf.sccseaot.com/): A web application that simulates the process of returning the Time Stone. It asks for the username and redirects it to a page that checks the JWT auth token of the user and returns the flag if the date in the JWT auth token is before the specified date.

## Files

- `app.py`: The main application file that contains the logic for the web application.
- `requirements.txt`: A file that lists the required Python packages for the application.

## Solution

- The web app is vulnerable to SSTI (Server-Side Template Injection) and JWT (JSON Web Token) manipulation. The application uses the `jwt` library to encode and decode JWT tokens, and it also uses the `jinja2` library for rendering templates.
- The application does have some checks to prevent direct leaking of the flag and private key, but it does not have a check for the public key used to sign the JWT token.
- The application uses the `jwt.encode` method to create a JWT token with a payload that contains the username and the date when the Time Stone was returned. It uses the `EdDSA` algorithm to sign the token with a private key.
- When checking the token, the application decodes it using the `jwt.decode` method and checks if the date in the token is before the specified date. If it is, it returns the flag. It uses the default algorithms for decoding the token, which can be any of the following: `HS256`, `RS256`, `ES256`, `EdDSA`, etc.
- Since `HS256` is a symmetric algorithm, it uses the same key for signing and verifying the token. The application does not check if the token is signed with the correct algorithm, so it is possible to use a different algorithm to sign the token.

1. Leak the public key used to sign the JWT token by injecting a payload that contains the public key. This can be done by using the `{{ PUBLIC_KEY }}` variable in the Jinja2 template, which contains the configuration of the Flask application.
2. Use the leaked public key to create a JWT token from [JWT.io](https://jwt.io) with a payload that contains the username and the date when the Time Stone was returned. The date should be set to a date before the specified date in the application.
3. Use the leaked public key to sign the JWT token with the `HS256` algorithm.
4. Modify the cookies in the web application to include the JWT token with the signed payload.
5. Access the web application with the modified cookies to retrieve the flag.

## Flag

```text
gnosis{l0k1_h1j4ck3d_th3_t1m3st0n3_w1th_jwt_m4g1c}
```
