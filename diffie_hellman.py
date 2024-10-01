import random

def generate_private_key(prime):
    """Generate a random private key."""
    return random.randint(2, prime - 2)

def generate_public_key(prime, base, private_key):
    """Generate the public key using the formula: (base ^ private_key) % prime."""
    return pow(base, private_key, prime)

def calculate_shared_secret(prime, public_key_other, private_key):
    """Calculate the shared secret using the formula: (public_key_other ^ private_key) % prime."""
    return pow(public_key_other, private_key, prime)

def diffie_hellman_key_exchange(prime=23, base=5, private_key_a=None, private_key_b=None):
    """
    Perform Diffie-Hellman Key Exchange and return the public keys and shared secret.
    
    Parameters:
    - prime (int): The prime number P.
    - base (int): The base G (primitive root modulo P).
    - private_key_a (int): Alice's private key. If None, generate randomly.
    - private_key_b (int): Bob's private key. If None, generate randomly.
    
    Returns:
    - dict: Contains public and private keys for Alice and Bob, and the shared secret.
    """
    # Generate private keys if not provided
    private_key_a = generate_private_key(prime) if private_key_a is None else private_key_a
    private_key_b = generate_private_key(prime) if private_key_b is None else private_key_b

    # Generate public keys
    public_key_a = generate_public_key(prime, base, private_key_a)
    public_key_b = generate_public_key(prime, base, private_key_b)

    # Calculate shared secrets
    shared_secret_a = calculate_shared_secret(prime, public_key_b, private_key_a)
    shared_secret_b = calculate_shared_secret(prime, public_key_a, private_key_b)

    # Ensure both shared secrets match
    if shared_secret_a != shared_secret_b:
        raise ValueError("Shared secrets do not match!")

    return {
        "private_key_a": private_key_a,
        "public_key_a": public_key_a,
        "private_key_b": private_key_b,
        "public_key_b": public_key_b,
        "shared_secret": shared_secret_a
    }
