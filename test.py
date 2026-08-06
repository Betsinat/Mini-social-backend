from auth.hash import hash_password, verify_password

# Test password
my_password = "securepassword123"

# 1. Hash the same password twice
hash_one = hash_password(my_password)
hash_two = hash_password(my_password)

print(f"Hash 1: {hash_one}")
print(f"Hash 2: {hash_two}")

print(f"Are the hashes identical? {hash_one == hash_two}")

print(f"Verify hash 1: {verify_password(my_password, hash_one)}")
print(f"Verify hash 2: {verify_password(my_password, hash_two)}")