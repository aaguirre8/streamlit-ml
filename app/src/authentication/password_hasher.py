from typing import List

import streamlit_authenticator as stauth


def encrypt_passwords(plain_passwords: List[str]) -> None:
    """
    Encrypts a list of plain passwords and writes the hashed passwords to a file.

    Args:
        plain_passwords (List[str]): A list of plain passwords to be hashed.

    Returns:
        None
    """

    hashed_passwords = stauth.Hasher(plain_passwords).generate()
    FILE_NAME = "src/authentication/hashed_passwords.txt"
    file_content = "\n".join(hashed_passwords)

    with open(FILE_NAME, "w") as file:
        file.write(file_content)

    return print("Successfully hashed passwords")


def main():

    try:

        plain_passwords = ["welcome123"]
        encrypt_passwords(plain_passwords)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
