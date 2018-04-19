from base64 import encodebytes


def writePrivateKeyASC(file, data):
    with open(file, "wb") as fh:
        fh.write(b"-----BEGIN PGP PRIVATE KEY BLOCK-----\n")
        fh.write(b"\n")
        fh.write(encodebytes(data))
        fh.write(b"=HFIX\n")
        fh.write(b"-----END PGP PRIVATE KEY BLOCK-----\n")
