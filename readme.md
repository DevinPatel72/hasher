## CLI Arguments
Usage: `hasher [-h] [-l] [-n LENGTH] [-f PATH] [-v] <algorithm> ...`

| Argument                  | Description                                                      |
| ------------------------- | ---------------------------------------------------------------- |
| `-l`, `--list-algorithms` | List all supported hashing algorithms.                           |
| `-n`, `--length`          | Output digest length in bytes. Required for SHAKE algorithms.    |
| `-f`, `--file PATH`       | Hash the contents of a file instead of a string preimage.        |
| `-v`, `--verbose`         | Enable verbose output.                                           |
| `algorithm`               | Hashing algorithm to use. Use `-l` to list available options.    |
| `...`                | Remaining arguments joined together to form the digest preimage. |

## Digest Algorithms

| Algorithm   | Digest size              | Notes                                                     |
| ----------- | ------------------------ | --------------------------------------------------------- |
| `md5`       | 128 bits                 | Insecure for collision resistance                         |
| `sha1`      | 160 bits                 | Deprecated for security-sensitive hashing                 |
| `sha224`    | 224 bits                 | SHA-2 family                                              |
| `sha256`    | 256 bits                 | SHA-2 family; widely used                                 |
| `sha384`    | 384 bits                 | SHA-2 family                                              |
| `sha512`    | 512 bits                 | SHA-2 family                                              |
| `sha3_224`  | 224 bits                 | SHA-3 family                                              |
| `sha3_256`  | 256 bits                 | SHA-3 family                                              |
| `sha3_384`  | 384 bits                 | SHA-3 family                                              |
| `sha3_512`  | 512 bits                 | SHA-3 family                                              |
| `shake_128` | Variable                 | Extendable-output function; output length is configurable |
| `shake_256` | Variable                 | Extendable-output function; output length is configurable |
| `blake2b`   | Variable, up to 512 bits | BLAKE2; optimized for 64-bit platforms                    |
| `blake2s`   | Variable, up to 256 bits | BLAKE2; optimized for smaller platforms                   |
