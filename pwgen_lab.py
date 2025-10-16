#!/usr/bin/env python3
"""
pwgen_lab.py (v9 - clean build)

Educational password-pattern generator for authorized testing only.
Max passwords: 1,500,000
"""

import itertools
import sys

CONSENT_PHRASE = "I HAVE AUTHORIZATION"
MAX_DEFAULT = 1500000


def normalize_tokens(raw):
    seen = set()
    out = []
    for t in (x.strip() for x in raw.split(',')):
        if t and t not in seen:
            seen.add(t)
            out.append(t)
    return out


def get_cap_variants(token):
    variants = []
    if len(token) > 0:
        variants.append(token[0].upper() + token[1:].lower())
    if len(token) > 0:
        variants.append(token[:-1].lower() + token[-1].upper())
    if len(token) > 1:
        variants.append(token[0].upper() + token[1:-1].lower() + token[-1].upper())
    elif len(token) == 1:
        variants.append(token.upper())
    return list(dict.fromkeys(variants))


def generate_preferred_numbers():
    return ['123', '321']


def generate_same_digit_numbers():
    numbers = []
    for digit in range(1, 10):
        numbers.append(str(digit) * 3)
    numbers.append('000')
    return numbers


def generate_100_to_999_numbers():
    return [str(i) for i in range(100, 1000)]


def generate_extended_numbers():
    priority = []
    priority.extend(['123', '321'])
    for digit in range(1, 10):
        priority.append(str(digit) * 3)
    priority.append('000')
    for i in range(100, 1000):
        num_str = str(i)
        if num_str not in priority:
            priority.append(num_str)
    for digit in range(1, 10):
        priority.append(str(digit) * 4)
    priority.append('0000')
    for i in range(1, 10000):
        num_str = str(i)
        if num_str not in priority:
            priority.append(num_str)
    return priority


def generate_patterns(tokens, name_tokens, birth_year, include_extra_numbers, cap_mode, max_passwords):
    passwords = []
    seen = set()
    preferred_nums = generate_preferred_numbers()
    same_digit_nums = generate_same_digit_numbers()
    range_100_999 = generate_100_to_999_numbers()
    all_numbers = generate_extended_numbers() if include_extra_numbers else (
                preferred_nums + same_digit_nums + range_100_999)

    def add_candidate(c):
        if c not in seen:
            seen.add(c)
            passwords.append(c)
            if len(passwords) >= max_passwords:
                return True
        return False

    def apply_pattern_set(base, number_list):
        if add_candidate(base):
            return True
        for num in number_list:
            if add_candidate(base + num):
                return True
            if add_candidate(base + num + '!'):
                return True
            if add_candidate(base + '_' + num):
                return True
            if add_candidate(base + '_' + num + '!'):
                return True
            if add_candidate(base + '-' + num):
                return True
            if add_candidate(base + '-' + num + '!'):
                return True
            if add_candidate(base + '.' + num):
                return True
            if add_candidate(base + '.' + num + '!'):
                return True
            if add_candidate(base + '@' + num):
                return True
            if add_candidate(base + '@' + num + '!'):
                return True
        return False

    def should_skip_combination(token1, token2):
        return (token1 in name_tokens and token2 in name_tokens)

    print("Phase 1: Processing all tokens lowercase with 123, 321...")
    for token in tokens:
        lowercase = token.lower()
        if apply_pattern_set(lowercase, preferred_nums):
            return passwords

    if cap_mode == 'basic':
        print("Phase 2: Processing all tokens with capitalization (123, 321)...")
        for token in tokens:
            cap_variants = get_cap_variants(token)
            for variant in cap_variants:
                if apply_pattern_set(variant, preferred_nums):
                    return passwords

    print("Phase 3: Processing all tokens lowercase with same-digit numbers...")
    for token in tokens:
        lowercase = token.lower()
        if apply_pattern_set(lowercase, same_digit_nums):
            return passwords

    if cap_mode == 'basic':
        print("Phase 4: Processing all tokens with caps + same-digit numbers...")
        for token in tokens:
            cap_variants = get_cap_variants(token)
            for variant in cap_variants:
                if apply_pattern_set(variant, same_digit_nums):
                    return passwords

    print("Phase 5: Processing all tokens lowercase with 100-999...")
    for token in tokens:
        lowercase = token.lower()
        if apply_pattern_set(lowercase, range_100_999):
            return passwords

    if cap_mode == 'basic':
        print("Phase 6: Processing all tokens with caps + 100-999...")
        for token in tokens:
            cap_variants = get_cap_variants(token)
            for variant in cap_variants:
                if apply_pattern_set(variant, range_100_999):
                    return passwords

    if birth_year:
        print("Phase 7: Processing birth year combinations...")
        for token in tokens:
            lowercase = token.lower()
            if add_candidate(lowercase + birth_year):
                return passwords
            if add_candidate(lowercase + birth_year + '!'):
                return passwords
            if add_candidate(lowercase + '_' + birth_year):
                return passwords
            if add_candidate(lowercase + '_' + birth_year + '!'):
                return passwords
            if add_candidate(lowercase + '.' + birth_year):
                return passwords
            if add_candidate(lowercase + '.' + birth_year + '!'):
                return passwords
            if add_candidate(lowercase + '-' + birth_year):
                return passwords
            if add_candidate(lowercase + '-' + birth_year + '!'):
                return passwords
            if add_candidate(lowercase + '@' + birth_year):
                return passwords
            if add_candidate(lowercase + '@' + birth_year + '!'):
                return passwords
            if cap_mode == 'basic':
                cap_variants = get_cap_variants(token)
                for variant in cap_variants:
                    if add_candidate(variant + birth_year):
                        return passwords
                    if add_candidate(variant + birth_year + '!'):
                        return passwords
                    if add_candidate(variant + '_' + birth_year):
                        return passwords
                    if add_candidate(variant + '_' + birth_year + '!'):
                        return passwords
                    if add_candidate(variant + '.' + birth_year):
                        return passwords
                    if add_candidate(variant + '.' + birth_year + '!'):
                        return passwords
                    if add_candidate(variant + '-' + birth_year):
                        return passwords
                    if add_candidate(variant + '-' + birth_year + '!'):
                        return passwords

    if len(tokens) >= 2:
        print("Phase 8: Processing two-word combinations...")
        for combo in itertools.permutations(tokens, 2):
            if should_skip_combination(combo[0], combo[1]):
                continue
            for sep in ['', '.', '-', '_']:
                lowercase_combo = sep.join([t.lower() for t in combo])
                if apply_pattern_set(lowercase_combo, all_numbers):
                    return passwords
                if cap_mode == 'basic':
                    cap_combo = sep.join([t[0].upper() + t[1:].lower() if len(t) > 0 else t for t in combo])
                    if apply_pattern_set(cap_combo, all_numbers):
                        return passwords

    if len(tokens) >= 3:
        print("Phase 9: Processing three-word combinations...")
        for combo in itertools.permutations(tokens, 3):
            if all(t in name_tokens for t in combo):
                continue
            for sep in ['', '.', '-', '_']:
                lowercase_combo = sep.join([t.lower() for t in combo])
                if apply_pattern_set(lowercase_combo, all_numbers):
                    return passwords

    if include_extra_numbers and len(passwords) < max_passwords:
        print("Phase 10: Processing extended number range (1000+)...")
        extended_nums = generate_extended_numbers()
        for token in tokens:
            lowercase = token.lower()
            if apply_pattern_set(lowercase, extended_nums):
                return passwords
            if cap_mode == 'basic':
                cap_variants = get_cap_variants(token)
                for variant in cap_variants:
                    if apply_pattern_set(variant, extended_nums):
                        return passwords

    return passwords


def main():
    print("Educational Password Pattern Generator — AUTHORIZED USE ONLY")
    print("Type exactly this phrase to confirm you have written authorization to test: ")
    print(f"  {CONSENT_PHRASE}")
    consent = input("Enter consent phrase (or Ctrl-C to quit): ").strip()
    if consent != CONSENT_PHRASE:
        print("Consent phrase not provided. Exiting.")
        sys.exit(1)

    print("\n" + "=" * 60)
    print("PERSONAL INFORMATION GATHERING (for authorized testing only)")
    print("=" * 60)
    print("Provide information about the target account/user.")
    print("Leave blank and press Enter to skip any field.\n")

    all_tokens = []
    name_tokens = []

    first_name = input("First name: ").strip()
    if first_name:
        all_tokens.append(first_name)
        name_tokens.append(first_name)

    last_name = input("Last name / Family name: ").strip()
    if last_name:
        all_tokens.append(last_name)
        name_tokens.append(last_name)

    nickname = input("Nickname (e.g., Fred for Frederic): ").strip()
    if nickname:
        all_tokens.append(nickname)
        name_tokens.append(nickname)

    birth_year = input("Birth year (if known): ").strip()

    city = input("City they live in: ").strip()
    if city:
        all_tokens.append(city)

    country = input("Country they live in: ").strip()
    if country:
        all_tokens.append(country)

    pet_names = input("Pet names (comma-separated): ").strip()
    if pet_names:
        all_tokens.extend(normalize_tokens(pet_names))

    old_password = input("Known old password or favorite word: ").strip()
    if old_password:
        all_tokens.append(old_password)

    if not all_tokens:
        print("\nNo information provided. Exiting.")
        sys.exit(1)

    print(f"\nCollected {len(all_tokens)} token(s): {', '.join(all_tokens)}")
    if birth_year:
        print(f"Birth year: {birth_year}")

    print("\n" + "=" * 60)
    print("NUMBER RANGE OPTIONS")
    print("=" * 60)
    print("By default: 123, 321, then 111-999, 000, then 100-999")
    include_extra = input("\nInclude extended numbers (1000-9999 full range)? (y/N): ").strip().lower()
    include_extra_numbers = include_extra in ("y", "yes")

    print("\nCapitalization options:")
    print("  none - lowercase only")
    print("  basic - Xaax, xaaX, XaaX variants")
    cap_choice = input("Capitalization mode (none/basic) [basic]: ").strip().lower()
    if cap_choice not in ('none', 'basic'):
        cap_choice = 'basic'

    max_input = input(f"\nMax passwords to generate [{MAX_DEFAULT}]: ").strip()
    try:
        max_passwords = int(max_input) if max_input else MAX_DEFAULT
    except ValueError:
        max_passwords = MAX_DEFAULT

    print("\n" + "=" * 60)
    print("GENERATING PASSWORDS")
    print("=" * 60)
    print("Priority order:")
    print("1. ALL tokens lowercase + 123, 321")
    print("2. ALL tokens with caps + 123, 321")
    print("3. ALL tokens lowercase + 111-999, 000")
    print("4. ALL tokens with caps + 111-999, 000")
    print("5. ALL tokens lowercase + 100-999")
    print("6. ALL tokens with caps + 100-999")
    print("7. Birth year combinations")
    print("8. Multi-word combinations (skips name+nickname combos)")
    print("9. Extended numbers 1000-9999 (if requested)")
    print(f"\nGenerating up to {max_passwords:,} passwords...\n")

    passwords = generate_patterns(all_tokens, name_tokens, birth_year, include_extra_numbers, cap_choice, max_passwords)

    filename = input("\nOutput filename (default passwords.txt): ").strip() or "passwords.txt"

    print(f"\nWriting {len(passwords):,} passwords to {filename}...")
    with open(filename, "w", encoding="utf-8") as f:
        for p in passwords:
            f.write(p + "\n")

    print(f"\nDone! Wrote {len(passwords):,} passwords to {filename}.")
    print("Remember: use these only for authorized testing, training, or lab exercises.")


if __name__ == "__main__":
    main()
