# educational-targeted-pwgen
Educational password pattern generator for authorized security testing and penetration testing engagements

## ⚠️ DISCLAIMER

**FOR EDUCATIONAL AND AUTHORIZED SECURITY TESTING ONLY**

This tool is designed exclusively for:
- Authorized penetration testing
- Security research and education
- Password security assessments with written permission
- Training purposes in controlled environments

**UNAUTHORIZED USE IS ILLEGAL.** Using this tool to access systems without explicit written authorization is a crime under computer fraud and abuse laws in most jurisdictions.

**THE AUTHOR ASSUMES NO LIABILITY FOR MISUSE OF THIS TOOL.** By using this software, you agree that you have proper authorization and accept full responsibility for your actions.

---

## 📖 Overview

This Python-based password pattern generator creates wordlists for authorized security testing. It generates password variations based on personal information patterns that people commonly use, helping security professionals:

- Test password strength in authorized environments
- Conduct approved penetration testing engagements
- Educate users about weak password patterns
- Perform security audits with proper authorization

---

## 🚀 How It Works

### Input Collection
The tool collects various pieces of information:
- **Name information**: First name, last name, nickname
- **Personal details**: Birth year, city, country
- **Other tokens**: Pet names, known passwords, favorite words

### Pattern Generation Priority

The generator follows a strict priority system to create realistic password patterns:

1. **Phase 1-2**: All tokens + common numbers (123, 321)
   - `password123`, `Password123`, `password123!`
   
2. **Phase 3-4**: All tokens + same-digit patterns (111-999, 000)
   - `password111`, `Password_999!`, `password-666`
   
3. **Phase 5-6**: All tokens + number range (100-999)
   - `password552`, `Password.427!`, `password_815`
   
4. **Phase 7**: Birth year combinations
   - `password1990`, `Password_1990!`
   
5. **Phase 8-9**: Multi-word combinations
   - `john.montreal123` (but NOT `john.johnny123` - avoids name+nickname)
   
6. **Phase 10**: Extended numbers (1000-9999) - optional

### Pattern Formats

For each token and number combination, the tool generates:
- `word123`
- `word123!`
- `word_123`
- `word_123!`
- `word-123`
- `word-123!`
- `word.123`
- `word.123!`
- `word@123`
- `word@123!`

### Capitalization Variants

When capitalization is enabled, generates:
- `password` (lowercase)
- `Password` (first letter capitalized)
- `passworD` (last letter capitalized)
- `PassworD` (first and last capitalized)

---

## 🛠️ Usage

### Requirements
- Python 3.6 or higher
- No external dependencies (uses only standard library)

### Running the Tool

```bash
python pwgen_lab.py
```

### Consent Requirement

Before the tool runs, you must enter the exact phrase:
```
I HAVE AUTHORIZATION
```

This serves as a reminder that you must have written permission to use this tool.

### Example Session

```
First name: John
Last name / Family name: Smith
Nickname (e.g., Fred for Frederic): Johnny
Birth year (if known): 1990
City they live in: Montreal
Country they live in: Canada
Pet names (comma-separated): Fluffy
Known old password or favorite word: 

Include number combinations (123, 321, 111-999, up to 9999)? (y/N): y
Capitalization mode (none/basic) [basic]: basic
Max passwords to generate [1500000]: 

Output filename (default passwords.txt): john_wordlist.txt
```

### Output

The tool generates a text file with one password per line:
```
john
john!
john123
john123!
john_123
john_123!
...
```

---

## ⚙️ Configuration Options

### Number Ranges
- **Default**: 123, 321, 111-999, 000, 100-999
- **Extended**: Full range 1000-9999 (optional)

### Capitalization
- **none**: Lowercase only
- **basic**: Multiple capitalization variants (default)

### Maximum Passwords
- Default: 1,500,000
- Customizable at runtime

---

## 🎓 Educational Use Cases

### Security Training
- Demonstrate common password patterns
- Show why personal information shouldn't be used in passwords
- Teach password complexity requirements

### Penetration Testing Labs
- Practice credential testing in controlled environments
- Learn about wordlist generation techniques
- Understand attack vectors for social engineering

### Password Policy Development
- Test password strength rules
- Identify weak patterns to block
- Develop better security policies

---

## 🔒 Security & Ethics

### Legal Requirements
✅ **DO:**
- Obtain written authorization before testing
- Use only in authorized environments
- Follow responsible disclosure practices
- Respect all applicable laws and regulations

❌ **DO NOT:**
- Test systems without explicit permission
- Use for unauthorized access attempts
- Share generated lists publicly
- Apply to production systems without approval

### Best Practices
1. **Document authorization** before each engagement
2. **Secure generated wordlists** and delete after use
3. **Report findings** responsibly to authorized parties
4. **Respect scope limitations** of your authorization

---

## 📋 Features

- ✅ Consent phrase requirement
- ✅ Intelligent pattern prioritization
- ✅ Avoids unrealistic combinations (e.g., name+nickname)
- ✅ Customizable number ranges
- ✅ Multiple capitalization variants
- ✅ Up to 1.5 million password generation
- ✅ Clean, readable code
- ✅ No external dependencies

---

## 🤝 Contributing

Contributions for educational improvements are welcome! Please:
1. Maintain the security warnings and consent mechanisms
2. Add clear documentation for any new features
3. Follow responsible disclosure practices
4. Test thoroughly before submitting

---

## 📄 License

MIT License - See LICENSE file for details

---

## 📞 Support

For questions about legitimate security research use cases, please open an issue on GitHub.

**Remember**: Always obtain proper authorization before conducting any security testing.

---

## 🙏 Acknowledgments

Created for educational purposes and authorized security testing engagements.

**Use responsibly. Test ethically. Stay legal.**
