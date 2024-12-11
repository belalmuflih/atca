import argparse
import json
import os
import requests
import base64
from . import schema
from .constants.endpoints import URLs
from colorama import Fore


def create_parser():
    parser = argparse.ArgumentParser(description="ZATCA Phase 2")
    parser.add_argument(
        "-t",
        "--test",
        metavar="",
        help="Test CSR",
    )
    parser.add_argument(
        "-c",
        "--create",
        action="store_true",
        help="Create a new CSR and test it.",
    )
    return parser


def test_csr(csr_path="./keys/taxpayer.csr") -> schema.SandboxTestCSR | None:
    with open(csr_path) as f:
        csr = f.read()
    headers = {
        "accept": "application/json",  # Not to be changed
        "OTP": "123345",  # To be changed
        "Accept-Version": "V2",  # Not to be changed
        "Content-Type": "application/json",  # Not to be changed
    }

    csr_encoded = base64.b64encode(csr.encode()).decode()
    json_data = {
        "csr": csr_encoded,
    }

    response = requests.post(
        URLs.sandbox_compliance,
        headers=headers,
        json=json_data,
    )
    text = f"{Fore.RED}Invalid CSR.{Fore.RESET}"
    if response.status_code == 200:
        text = f"{Fore.GREEN}Valid CSR.{Fore.RESET}"
        response_json = response.json()
        with open("keys/CSID.json", "w") as f:
            json.dump(response_json, f, indent=4)
        with open("keys/cert.txt", "w") as f:
            cert = base64.b64decode(response_json['binarySecurityToken']).decode()
            f.write(cert)
    print(text)


def create_csr():
    os.system("openssl ecparam -name secp256k1 -genkey -noout -out keys/PrivateKey.pem")
    os.system("openssl ec -in keys/PrivateKey.pem -pubout -out keys/publickey.pem")
    os.system(
        "openssl req -new -sha256 -key keys/PrivateKey.pem -extensions v3_req -config Configuration.cnf -out keys/taxpayer.csr"
    )


def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.create:
        create_csr()
        test_csr()
    if args.test:
        test_csr(args.test)


if __name__ == "__main__":
    main()
