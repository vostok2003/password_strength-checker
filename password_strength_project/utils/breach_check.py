import hashlib


def check_password_breach(password):
    
   
    common_breached_passwords = [
    
    "7c4a8d09ca3762af61e59520943dc26494f8941b",  # 123456
    "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8",  # password
    "b1b3773a05c0ed0176787a4f1574ff0075f7521e",  # qwerty
    "e5e9fa1ba31ecd1ae84f75caaa474f3a663f05f4",  # secret
    "5ebe2294ecd0e0f08eab7690d2a6ee69a2138e0f",  # admin
    "f7c3bc1d808e04732adf679965ccc34ca7ae3441",  # admin123
    "ef92b778bafe771e89245b89ecbc08a44a4e166c",  # password123
    "b9c950640e1b3740e98acb93e669c65766f6670dd1609ba91ff41052ba48c6f3",  # letmein
    

    "356a192b7913b04c54574d18c28d46e6395428ab",  # 1
    "da4b9237bacccdf19c0760cab7aec4a8359010b0",  # 12
    "77de68daecd823babbb58edb1c8e14d7106e83bb",  # 123
    "6b3a55a3948031e518f2bc3b16ad26e02c5a34b7",  # 123123123
    "827ccb0eea8a706c4c34a16891f84e7b",  # 1234567
    "12dada6c449a1e55d299b423cbbdd7f796f11d68",  # 12345678!
    "6cf61523d04d53565c89e899ebd3f898b5fce048",  # 987654
    "3d4f2ad86b2e8936a2995b72a97f9f8e47a1fada",  # qazwsxedc
    "e99a18c428cb38d5f260853678922e03",  # abc123!
    "700be43b6234f7057c659eb275b3f9f90b049f29",  # princess
    "1532f1db95306a1c3d7c5cfd46eb3f8c",  # welcome2
    "57d9366f88e14b433a52d2c070c14fc0b6fa1c65",  # football1
    "5df5396c64f94a95e9c418dd06c6439e",  # qwerty1
    "f5a7924e621e84c9280a9a27e1bcb7f6",  # 1111111
    "66a2c8f4f24f4a3d36b54a2f0dfc4f4f",  # iloveyou1
    "a697fa83b98e83bba432a45df5b2dbf3",  # baseball12
    "d077f244def8a70e5ea758bd8352fcd8",  # asdf
    "69691c7bdcc3ce6d5d8a1361f22d04ac",  # test
    "eb61eead90e3b899c6bcbe27ac581660c7d48180",  # 123qwe123
    "02aa629c8b16cd18d796b8dca072d5aa",  # iloveu
    "bfcfd9f68a199fd96609839653fbc1fa",  # password321
    "da4b9237bacccdf19c0760cab7aec4a8359010b0",  # 12
    "6606f6f8ea62a6aab0c2a4c2d6275b5e",  # asdasd
    "eeaee137d710b3bb5a74fdf75e99de30",  # 12345678910
    "f8984a00c11d3d57f5e3b58b690e96a4",  # qwerty12
    "4cb76b09a7c891578b296fef2aa17767",  # passw0rd
    "4a7d1ed414474e4033ac29ccb8653d9b",  # letmein!
    "bde1fdefe5dd177b1a59c26224fdf29a",  # monkey1
    "3bc15c8aae3e4124dd409035f32ea2fd",  # 999999
    "16e699c18f135df3ae89adff0b7fe1b1",  # changeme
    "5d5e96fb8da4a92c7d76379dbfdd4436",  # dragon12
    "b2a033239b8e2495cf14fb0b6e164561",  # freedom1
    "202cb962ac59075b964b07152d234b70",  # 123
    "5f4dcc3b5aa765d61d8327deb882cf99",  # password (MD5)
    "d8578edf8458ce06fbc5bb76a58c5ca4",  # qwerty (MD5)
    "25d55ad283aa400af464c76d713c07ad",  # 1234567890
    "6c569aabbf7775ef8fc570e228c16b98",  # 1234 (MD5)
    "5d93ceb70e2bf5daa84ec3d0cd2c731a",  # letmein123
    "e2ef524fbf3d9fe611d5a8e90fefdc9c",  # abcdef
    "25d55ad283aa400af464c76d713c07ad",  # 1234567890
    "4297f44b13955235245b2497399d7a93",  # p@ssw0rd
    "7c222fb2927d828af22f592134e8932480637c0d",  # 1234
    "7c6a180b36896a0a8c02787eeafb0e4c",  # password1
    "9a0b93e5fa12d3347f1d393dc85a8746",  # welcome!
    "71c3c54c8bc35049c2f89c57eb46de47",  # letmein123
    "1532f1db95306a1c3d7c5cfd46eb3f8c",  # welcome2
    "1ee1569a02f169d92c4b8199c4767ef3",  # qwertyuiop
    "c8837b23ff8aaa8a2dde915473ce099f",  # dragon!
]

    
    # Calculate SHA-1 hash of the password
    sha1_hash = hashlib.sha1(password.encode()).hexdigest()
    
    # Check if the hash is in the list of breached passwords
    if sha1_hash in common_breached_passwords:
        return True
    
    # Also check SHA-256 for demonstration purposes
    sha256_hash = hashlib.sha256(password.encode()).hexdigest()
    if sha256_hash in common_breached_passwords:
        return True
    
    return False

def get_breach_details(password):
    """
    Get details about breaches where the password was found.
    
    In a real application, this would return information about which breaches
    contained the password, when they occurred, etc.
    
    Args:
        password (str): Password to check
        
    Returns:
        list: List of breach details (empty if no breaches)
    """
    is_breached = check_password_breach(password)
    
    if is_breached:
        # This is simulated data
        return [
            {
                "name": "Example Breach",
                "date": "2023-01-15",
                "records_affected": "10,000,000"
            }
        ]
    
    return []