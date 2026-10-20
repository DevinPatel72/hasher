#!/usr/bin/env python3

if __name__ == "__main__":
    import argparse
    import hashlib
    import sys
    import os
    
    help_text = "Hash generator script. The first argument is the hashing algorithm. All remaining arguments are joined together into a single string with a NULL byte (\\0) separating each argument. A file argument can be passed instead of string arguments."
    
    digest_list = """
Algorithm       Digest size                 Notes
————————————————————————————————————————————————————————————————————————————————————————
md5             128 bits                    Insecure for collision resistance
sha1            160 bits                    Deprecated for security-sensitive hashing
sha224          224 bits                    SHA-2 family
sha256          256 bits                    SHA-2 family; widely used
sha384          384 bits                    SHA-2 family
sha512          512 bits                    SHA-2 family
sha3_224        224 bits                    SHA-3 family
sha3_256        256 bits                    SHA-3 family
sha3_384        384 bits                    SHA-3 family
sha3_512        512 bits                    SHA-3 family
shake_128       Variable                    Extendable-output function
shake_256       Variable                    Extendable-output function
blake2b         Variable, up to 512 bits    BLAKE2, optimized for 64-bit platforms
blake2s         Variable, up to 256 bits    BLAKE2, optimized for smaller platforms"""

    def print_digest_list():
        print(digest_list)
    
    argparser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, description=help_text)
    argparser.add_argument('-l', '--list-algorithms', action='store_true', dest='list', help="List all of the possible hashing algorithms")
    argparser.add_argument("-n", "--length", type=int, help="Output length in bytes (required for SHAKE algorithms)")
    argparser.add_argument("-f", "--file", metavar="PATH", help="File to hash instead of a string")
    argparser.add_argument('-v', '--verbose', action='store_true', dest='verbose', help="Verbose output")
    argparser.add_argument("algorithm", nargs="?", help="Hashing algorithm to use. Use -l to see options.")
    argparser.add_argument("preimage", nargs=argparse.REMAINDER, help="Remaining arguments to join together into a digest preimage.")
    args = argparser.parse_args()
    
    if args.list:
        print_digest_list()
        sys.exit(0)
    elif args.algorithm is None:
        argparser.error("algorithm is required unless -l is specified")
    elif args.algorithm.lower() in ("shake_128", "shake_256"):
        if args.length is None:
            argparser.error("SHAKE algorithms require an output length -n <NumberOfBytes>")

        if args.length <= 0:
            argparser.error("Output length must be positive")

        length = args.length
    elif args.file is not None and not os.path.isfile(args.file):
        argparser.error(f'Argument \"{args.file}\" does not exist or is not a file')
    elif args.file is None and len(args.preimage) <= 0:
        argparser.error('No preimage arguments passed')
    else:
        length = None
    
    algorithm = args.algorithm
    verbose = args.verbose
    
    try:
        hasher = hashlib.new(algorithm)
        
        if args.file is not None:
            with open(args.file, "rb") as file:
                for chunk in iter(lambda: file.read(1024 * 1024), b""):
                    hasher.update(chunk)
            verbose_text = args.file
        else:
            preimage_list = args.preimage
            preimage_text = "\0".join(preimage_list).encode('utf-8')
            hasher.update(preimage_text)
            verbose_text = preimage_text

        # SHAKE algorithms require an explicit output length.
        if algorithm.lower() in ("shake_128", "shake_256") and length is not None:
            digest = hasher.hexdigest(length)
        else:
            digest = hasher.hexdigest()

        if verbose:
            print(verbose_text, '->', end='\n')
        print(digest)

    except (ValueError, TypeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)

