# scanner.py - AuditChain Prototype
# Simple static analysis for smart contract vulnerabilities

dangerous_patterns = [
    "delegatecall",
    "call.value",
    "tx.origin",
    "unchecked",
    "reentrancy",
    "selfdestruct",
    "block.timestamp"
]

def scan_contract(code):
    found = []
    for pattern in dangerous_patterns:
        if pattern in code:
            found.append(pattern)
    return found

if __name__ == "__main__":
    print("📄 Paste your smart contract code below (type END to finish):")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    contract_code = "\n".join(lines)
    results = scan_contract(contract_code)

    print("\n🔍 Audit Results:")
    if results:
        print("⚠️ Vulnerabilities found:")
        for r in results:
            print(f" - {r}")
    else:
        print("✅ No known dangerous patterns found.")
