# 🔐 Wi-Fi Password Strength Visualizer

A Python-based tool to analyze and visualize the strength of Wi-Fi passwords. This project educates users on password security by calculating entropy and offering actionable tips to improve their password hygiene.

---

## 🚩 Objective

Many Wi-Fi networks use short or predictable passwords, making them vulnerable to attacks. This tool:
- Evaluates password strength based on entropy
- Classifies passwords as Weak / Moderate / Strong
- Visualizes the result using a bar chart
- Provides security improvement tips

---

## 🛠️ Technologies Used

- **Python 3**
- `matplotlib` – for bar chart visualization
- `math`, `string` – for entropy and pattern logic

---

## 📦 Project Structure

 How It Works
User is prompted to enter a Wi-Fi password.

The app calculates its entropy based on character sets used.

A bar graph shows whether the password is:

🔴 Weak (Entropy < 30)

🟠 Moderate (Entropy 30–50)

🟢 Strong (Entropy > 50)

The app displays smart tips to make the password stronger.

🔒 Security Note
The tool does not fetch or store real Wi-Fi passwords.

Passwords are input manually and used only in memory.

No credentials are saved, logged, or transmitted.

❌ Out of Scope: This tool doesn’t fetch saved Wi-Fi passwords automatically or test brute-force times in real time. It’s an educational and visual analyzer only.

## 🔐 Cybersecurity Best Practices Followed

- No sensitive information is stored or transmitted
- Passwords are not logged or hardcoded
- Breach detection included using offline password list
- Tool educates users on password complexity and safety

