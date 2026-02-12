# Sesame Auth

*Also known as: Passwordless Authentication*

**Sesame Auth provides a passwordless authentication solution using cryptography, steganography, and biometrics.**

**Category:** authentication_method  
**Maturity:** emerging

## How It Works

Sesame Auth eliminates the need for passwords by combining cryptographic keys with steganography to embed credentials in images. Users register by providing a username and capturing their typing patterns for account recovery. During authentication, users verify their identity through a random string and biometric authentication, ensuring a secure and user-friendly experience.

## Algorithm

**Input:** User's username (string), typing pattern (array), image (binary data)

**Output:** Authentication success (boolean) or failure (boolean)

**Steps:**

1. 1. User installs the Sesame Auth app and registers by providing a username.
2. 2. The app captures the user's typing pattern for account recovery.
3. 3. User uploads an image that will store their account credentials using steganography.
4. 4. The app generates cryptographic keys and securely stores them on the device.
5. 5. During authentication, the user enters their username and receives a random string for verification.
6. 6. The user enters the random string in the app and completes biometric authentication.
7. 7. The server verifies the input and grants access if it matches.

**Core Operation:** `output = verify(username, random_string, biometric_data)`

## Parameters

| Parameter | Typical Value | Effect |
|-----------|--------------|--------|
| `RSA key size` | 2048 bits | Increased security with larger keys, but may affect performance. |
| `Symmetric key size` | 256 bits | Higher key sizes enhance security. |
| `Typing pattern capture` | minimum of three entries | More entries improve accuracy for account recovery. |

## Complexity

- **Time:** Not stated
- **Space:** Not stated
- **In practice:** Authentication time is within 2 seconds, comparable to traditional methods.

## Implementation

```python
def sesame_auth(username: str, random_string: str, biometric_data: Any) -> bool:
    # Step 1: Verify username
    # Step 2: Check random string
    # Step 3: Validate biometric data
    return authentication_success
```

## Common Mistakes

- Neglecting to securely store cryptographic keys.
- Failing to capture sufficient typing patterns for recovery.
- Overlooking the need for user education on biometric usage.

## Use When

- Building applications that require secure user authentication without passwords.
- Developing systems that need to balance security and user experience.
- Implementing authentication methods for mobile applications.

## Avoid When

- The application requires traditional password-based authentication.
- There is a need for immediate account recovery without biometric verification.
- The target user base lacks biometric capabilities.

## Tradeoffs

**Strengths:**

- Eliminates the need for passwords, enhancing user experience.
- Utilizes multiple security layers (cryptography, steganography, biometrics).
- Fast authentication comparable to traditional methods.

**Weaknesses:**

- Requires biometric capabilities, limiting user base.
- Potentially complex implementation compared to simple password systems.
- Dependency on device security for key storage.

**Compared To:**

- **vs Traditional Password Authentication:** Use Sesame Auth for enhanced security and user experience.

## Connects To

- Multi-Factor Authentication
- Biometric Authentication
- Cryptographic Key Management
- Steganography Techniques

## Evidence (Papers)

- **Passwordless Authentication Using a Combination of Cryptography, Steganography, and Biometrics** [6 citations] - [DOI](https://doi.org/10.3390/jcp4020014)
