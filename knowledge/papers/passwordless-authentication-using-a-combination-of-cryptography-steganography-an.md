# Passwordless Authentication Using a Combination of Cryptography, Steganography, and Biometrics

## Access

| Field | Value |
|-------|-------|
| DOI | `10.3390/jcp4020014` |
| Full Paper | [https://doi.org/10.3390/jcp4020014](https://doi.org/10.3390/jcp4020014) |
| Semantic Scholar | [https://www.semanticscholar.org/paper/362509194df2c5cc13c0e7025e56cc0df017a239](https://www.semanticscholar.org/paper/362509194df2c5cc13c0e7025e56cc0df017a239) |
| Source | [https://journalclub.io/episodes/passwordless-authentication-using-a-combination-of-cryptography-steganography-and-biometrics](https://journalclub.io/episodes/passwordless-authentication-using-a-combination-of-cryptography-steganography-and-biometrics) |
| Source | [https://www.semanticscholar.org/paper/362509194df2c5cc13c0e7025e56cc0df017a239](https://www.semanticscholar.org/paper/362509194df2c5cc13c0e7025e56cc0df017a239) |
| Year | 2026 |
| Citations | 6 |
| Authors | Tunde Oduguwa, A. Arabo |
| Paper ID | `eda44c35-b0a6-4f28-aa70-2b0ca289550e` |

## Classification

- **Problem Type:** passwordless authentication
- **Domain:** Cybersecurity
- **Sub-domain:** Passwordless Authentication
- **Technique:** Sesame Auth
- **Technique Category:** framework
- **Type:** novel

## Summary

The paper presents a passwordless authentication system called Sesame Auth, which integrates cryptography, steganography, and biometrics to enhance security while maintaining user-friendliness. Engineers should care because it offers a scalable alternative to traditional password-based systems, eliminating the need for shared secrets and reducing the risk of breaches.

## Key Contribution

**Introduction of a passwordless authentication system that balances security and usability using a combination of cryptographic, steganographic, and biometric techniques.**

## Problem

The need for a secure and user-friendly alternative to traditional password-based authentication systems due to their vulnerabilities and user dissatisfaction.

## Method

**Approach:** Sesame Auth eliminates the need for passwords by using a combination of cryptographic keys, steganography to embed credentials in images, and biometric authentication. The system captures user typing patterns for account recovery and uses secure communication protocols to ensure data integrity.

**Algorithm:**

1. 1. User installs the Sesame Auth app and registers by providing a username.
2. 2. The app captures the user's typing pattern for account recovery.
3. 3. User uploads an image that will store their account credentials using steganography.
4. 4. The app generates cryptographic keys and securely stores them on the device.
5. 5. During authentication, the user enters their username and receives a random string for verification.
6. 6. The user enters the random string in the app and completes biometric authentication.
7. 7. The server verifies the input and grants access if it matches.

**Input:** User's username, typing pattern, and an image for steganography.

**Output:** Authentication success or failure.

**Key Parameters:**

- `RSA key size: 2048 bits`
- `Symmetric key size: 256 bits`
- `Typing pattern capture: minimum of three entries`

**Complexity:** Not stated

## Benchmarks

**Tested on:** User typing patterns and images for steganography

**Results:**

- Authentication time: within 2 seconds

**Compared against:** Traditional password-based authentication systems

**Improvement:** Demonstrated comparable authentication speed to passwords without the need for shared secrets.

## Implementation Guide

**Data Structures:** User accounts database, Image storage for steganography, Cryptographic key storage

**Dependencies:** React Native, Node.js, TypingDNA API, Jimp library for image processing

**Core Operation:**

```python
if user_authentication_successful: grant_access() else: deny_access()
```

**Watch Out For:**

- Ensure biometric authentication is supported on user devices.
- Handle potential issues with image size for steganography.
- Capture sufficient typing patterns to create a reliable model.

## Use This When

- Building applications that require secure user authentication without passwords.
- Developing systems that need to balance security and user experience.
- Implementing authentication methods for mobile applications.

## Don't Use When

- The application requires traditional password-based authentication.
- There is a need for immediate account recovery without biometric verification.
- The target user base lacks biometric capabilities.

## Key Concepts

cryptography, steganography, biometrics, typing dynamics, secure communication, user experience

## Connects To

- FIDO2
- biometric authentication systems
- cryptographic protocols
- steganography techniques

## Prerequisites

- Understanding of cryptographic principles
- Familiarity with biometric systems
- Knowledge of steganography

## Limitations

- Requires biometric-capable devices
- Initial setup may be complex for users
- Dependent on user compliance for typing pattern capture

## Open Questions

- How to improve user adoption of passwordless systems?
- What are the long-term security implications of this approach?

## Abstract

Remember a year or two ago when “passwordless” authentication for websites was all the rage? News articles from the time proclaimed that passwords were dead and that passkeys (and related technologies) were clearly the future. Well…what happened? From what I can tell, a lot of people gave passkeys a try, hated them, and went right back to using passwords. To be fair, passwordless authentication for mobile lock-screens and mobile payments did become a reality (in the form of biometrics) but passwordless authentication on the web never really caught-on (outside of Oauth). It turns out, if you want to disrupt something as ubiquitous as passwords you need to offer a solution that is waaaay better. Not just a slight improvement, but a full step-function better. And in the minds of many users, passkeys didn't reach that bar.
