AuditChain  Qubic Track

>Track: Qubic Track  
>Team: AuditChain Qubic Track  
>Role: Research & Technical Writing (Iniubong Ebong)  

 🧠 Project Overview

AuditChain is a decentralized smart contract auditing tool built on the Qubic testnet. It allows developers to scan, verify, and log audits of smart contracts in a transparent and secure way. The tool performs static analysis on contracts and stores proof of audits on the Qubic blockchain, ensuring verifiable audit history.


🎯 Problem Statement

With the rise of Web3 and smart contracts, security vulnerabilities like reentrancy attacks, integer overflows, and logic flaws are common. Many developers lack tools to quickly audit their contracts before deployment.


 🚀 Solution

AuditChain provides:

- ✅ Upload or paste smart contract code  
- ✅ Runs static analysis for known vulnerabilities  
- ✅ Generates an audit report with severity levels  
- ✅ Commits audit result hash to Qubic testnet  
- ✅ Optional: View previous audits via contract ID


 ⚙️ Architecture

```txt
[User] 
   ↓
[Frontend/CLI Upload]
   ↓
[Audit Engine (local scan)]
   ↓
[Report Generator] → [IPFS or Local]
   ↓
[Hash Submitted to Qubic Testnet via Smart Contract]



🛠️ Tech Stack

| Component        | Tech/Tool Used                     |
|------------------|------------------------------------|
| Audit Engine     | Python / Node.js static analysis   |
| Smart Contract   | Qubic Testnet                      |
| Frontend (opt)   | HTML / React (if applicable)       |
| Storage (opt)    | IPFS or Local                      |
| Deployment       | Qubic CLI or API                   |



 👤 Team Members

Iniubong Ebong Research, Technical Writing, Documentation  
Hammad Hassan  Developer, Smart Contract Integration


🎬 Demo Video

Coming soon  A short walkthrough showing how a contract is uploaded, scanned, and the result is verified on the Qubic testnet.


📈 Future Plans

- Add dynamic vulnerability pattern support  
- Deploy public version with web interface  
- Add Slither/MythX integration  
- Support for other testnets beyond Qubic  
- Real-time reporting and audit explorer



 📍 How to Run

1. Clone the repository  
2. Install dependencies (Python/Node.js based)  
3. Upload or paste contract code  
4. Run audit using provided script  
5. Generate report  
6. Submit report hash to Qubic Testnet



 💡 Why Qubic?

Qubic provides a high-speed, decentralized compute environment perfect for verifiable auditing. Its testnet supports submitting and querying smart contract data in a trustless way ideal for security-focused tools like AuditChain.


📜 License

MIT License  free for public use and contribution.

Solo Submission Note

This project was created by a solo participant, Iniubong Ebong, as part of the Qubic Track at RAISE Your Hack. While I faced team challenges, I remained committed to researching, documenting, and building a clear blueprint and prototype for a functional tool. AuditChain is my solo contribution to the hackathon and my proof of determination to grow in Web3.
