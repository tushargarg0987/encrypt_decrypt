# File and Folder Encryption/Decryption Tool

## Introduction

This project provides a simple and secure way to encrypt and decrypt files and folders, making it ideal for safe data transfer and storage. It consists of two main components:

1. **File Encryption/Decryption**: This component allows you to encrypt and decrypt individual files, ensuring the confidentiality and security of your data.

2. **Folder Encryption/Decryption**: This component enables you to encrypt and decrypt entire folders, making it easy to secure and transfer multiple files and directories.

## Features

- Strong encryption: Utilizes robust encryption algorithms to protect your data.
- User-friendly interface: Easy-to-use command-line interface for both file and folder operations.
- Cross-platform: Compatible with Windows, macOS, and Linux.
- Secure key management: Supports password-based encryption, ensuring only authorized users can access the data.
- Fast and efficient: Optimized for performance to handle large files and folders.

## Prerequisites

Before using this tool, you need to have the following prerequisites installed on your system:

- Python 3.x: Ensure Python 3.x is installed on your system.
- Additional Python Libraries: Install the required libraries using the following command:
  ```
  pip install cryptography
  ```

## Usage

### File Encryption/Decryption

#### Encrypt a File

To encrypt a file, use the following command:

```bash
python safe_file.py encrypt -i input_file -o encrypted_file
```

- `-i` or `--input`: Specify the path to the input file you want to encrypt.
- `-o` or `--output`: Specify the path where the encrypted file will be saved.

#### Decrypt a File

To decrypt a file, use the following command:

```bash
python safe_file.py decrypt -i encrypted_file -o decrypted_file -k secret_key
```

- `-i` or `--input`: Specify the path to the encrypted file you want to decrypt.
- `-o` or `--output`: Specify the path where the decrypted file will be saved.
- `-k` or `--key`: Specify the key generated during the encryption.

### Folder Encryption/Decryption 

#### Encrypt a Folder

To encrypt a folder, use the following command:

```bash
python safe_dir.py encrypt
```


#### Decrypt a Folder

To decrypt a folder, use the following command:

```bash
python safe_dir.py decrypt 
```

- folder should contain `thekey.key` file generated during encryption

## Security

- Ensure that you keep your encryption keys and passwords safe. Losing them may result in data loss.

## License

This project is licensed under the [MIT License](LICENSE.md).

## Acknowledgments

Special thanks to the [Cryptography](https://cryptography.io/en/latest/) library for providing encryption support.

Enjoy secure data transfer and storage with our encryption tool!