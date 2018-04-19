# netsec_exercise
some exercises concerning network security


> ###### pgpExtract_r_s.py
> Extracts the signature (r,s) from AliceMsgtxt.asc.
> You are able to see the values also with pgpdump -i command.
> Printed values are modulo 0xb0b!

> ###### pgpManipulateKeyfile.py
> Extracts Key-Packets and manipulates the private Key.
> Generates new file with manipulated key and Checksum.
> The new file should be readable via pgpdump -i command.

> ###### rsaFaultAttackCalcParameters.py
> Calculates rsa Fault Attack with given parameters.
> Look at the file for the parameters.