---
# Diffie-Hellman Key Exchange Calculator

## Header Information

- **Program Name:** Diffie-Hellman Key Exchange Calculator
- **Author:** Haro, Leander Grant L. & Gragasin, Nathaniel
- **Date:**
  - **Creation Date:** 2024-09-25
  - **Last Modification Date:** 2024-09-27
- **Version:** 1.0
- **Purpose:**  
  This program implements the Diffie-Hellman key exchange protocol, allowing users to securely exchange cryptographic keys over a public channel. It provides a web-based calculator where users can input parameters to generate private keys, public keys, and compute the shared secret. The application is hosted on a local Flask server and is designed for demonstration purposes.

## System Requirements

### Hardware

- **CPU:** Minimum dual-core processor.
- **RAM:** At least 4 GB.
- **Storage:** Minimum of 100 MB free disk space.

### Software

- **Operating System:**  
  Windows 10 or higher, macOS Mojave or higher, or a compatible Linux distribution.
- **Python Version:**  
  Python 3.7 or higher.
- **Libraries:**  
  Flask (install via `pip install Flask`)

## Functional Description

### Input

- **Prime Number (P):** An integer greater than or equal to 3.
- **Base (G):** An integer greater than or equal to 2.
- **Alice's Private Key (a):** An optional integer greater than or equal to 2.
- **Bob's Private Key (b):** An optional integer greater than or equal to 2.  
  *If the private keys are not provided, they are generated randomly.*

### Processing

#### Form Submission

Users input or accept default values for **P**, **G**, **a**, and **b** via an HTML form.

#### Input Validation

- The application checks that **P ≥ 3** and **G ≥ 2**.
- Optional private keys are validated to be integers **≥ 2**.

#### Key Generation

- **Private Keys:**  
  If not provided, **a** and **b** are generated randomly within the range `[2, P−2]`.
  
- **Public Keys:**  
  - **A = Gᵃ mod P** *(Alice's public key)*
  - **B = Gᵇ mod P** *(Bob's public key)*

#### Shared Secret Calculation

- **S_A = Bᵃ mod P** *(Alice's computation)*
- **S_B = Aᵇ mod P** *(Bob's computation)*

*Both **S_A** and **S_B** should be equal, forming the shared secret **S**.*

#### Result Rendering

The application displays **a**, **A**, **b**, **B**, and **S** on the web page.

### Output

- **Displayed Data:**
  - Alice's Private Key (**a**)
  - Alice's Public Key (**A**)
  - Bob's Private Key (**b**)
  - Bob's Public Key (**B**)
  - Shared Secret (**S**)

- **Formats:**  
  The results are displayed in a styled HTML format for readability.

## Security Considerations

### Vulnerability Assessment

- **Key Interception:**  
  Public keys can be intercepted during transmission, potentially enabling man-in-the-middle attacks.
  
- **Weak Keys:**  
  Using small primes and bases can make the key exchange susceptible to attacks.
  
- **Predictable Private Keys:**  
  If private keys are not securely generated, they can be predicted by attackers.

### Mitigation Strategies

- **Use Secure Channels:**  
  In real-world applications, ensure that public keys are transmitted over secure channels (e.g., HTTPS).
  
- **Large Primes and Bases:**  
  Utilize large prime numbers and appropriate primitive roots to enhance security.
  
- **Secure Random Number Generation:**  
  Use cryptographically secure random number generators for private key generation (e.g., `secrets` module in Python).

## Testing

- **Unit Testing:**  
  Verify that for various inputs, the shared secret is correctly computed and consistent between Alice and Bob.
  
- **Edge Case Testing:**  
  Test with minimal and maximal acceptable values for inputs.
  
- **Security Testing:**  
  Simulate interception of public keys to ensure that shared secrets remain secure.

## Usage Instructions

### Installation

1. **Clone the Repository or Set Up the Project Directory:**  
   Ensure that the project directory is structured correctly with all necessary files.

2. **Navigate to the Project Directory:**

   ```bash
   cd C:\Users\NR\Desktop\pythonProject1> 

3. **Set Up a Virtual Environment (optional but recommended):**

   ```bash
   python -m venv .venv

4. **Activate the Virtual Environment:**

   ```bash
   .\.venv\Scripts\activate

5. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

### Configuration

- **Prime Number (P) and Base (G):**
  Users can input their own values via the web form.
Defaults:
- P = 23
- G = 5

### Execution

1. **Run the Flask Application:**
   ```bash
   python flask_app.py

2. **Access the Application:**
Open a web browser and navigate to:
   ```bash
   http://127.0.0.1:5000

3. **Perform Calculations:**
   - Fill in the form with desired values or use the defaults.
   - Click "Calculate Shared Secret" to view the results.

### Error Handling
#### Error Codes
- ValueError:
  Raised when inputs do not meet validation criteria (e.g., P < 3, G < 2).

**Recovery Procedures**
- Invalid Input Handling:
  Users are informed of input errors via error messages displayed on the webpage.

- Exception Logging:
  All exceptions are caught and displayed as error messages to the user.

## Maintenance Log
|Date           |Changes Description                                             |Author          |
|---------------|----------------------------------------------------------------|----------------|
|2024-09-25     |Initial creation of the Diffie-Hellman Key Exchange Calculator. |Haro & Gragasin |
|2024-09-27     |Added input validation and enhanced error handling.             |Haro & Gragasin |