# Azure Terraform Security Scanner

## English

### Description
A lightweight Static Analysis Security Testing (SAST) tool designed to detect common security misconfigurations in Azure Terraform scripts. The scanner matches Terraform resources against a customizable set of security rules defined in YAML.

#### 📂 Files
* `main.py`: Startup code.
* `scanner/`: Logic for parsing HCL and rule matching.
* `rules.yaml`: Dictionary of security rules (Description, Expected Value, Remediation).
* `samples/`: Directory containing `.tf` files for testing.
* `requirements.txt`: List of Python dependencies.
* `scan_results.log`: Output file where vulnerabilities are recorded.

#### Installation
1.  **Prerequisites**: Python 3.11.6
2.  **Clone/Copy the project** to your local machine.
    ```
    git clone https://github.com/psTudor/IaC-Scanner.git
    ```
3.  **Install Dependencies**:
   Create a virtual enviroment and activate it
    ```bash
    python -m venv venv
    ```
    Windows powershell
    ```bash
    venv\Scripts\Activate.ps1
    ```
    Linux bash/zsh
    ```bash
    source venv/bin/activate
    ```
    Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

#### How to run
Run the scanner from the terminal:
```bash
python main.py
```

#### Output
```
2026-04-18 12:29:57,840 - WARNING - 
[!] VULNERABILITY: AZU-APP-002
 -> Location: TG_app_service.tf -> app-service1
 -> Issue: has weak or missing TLS version. (Got: 1.1)
 -> Why: Old TLS versions (1.0/1.1) are vulnerable to known cryptographic attacks.
 -> Fix: Set 'min_tls_version = "1.2"'.

 2026-04-18 12:29:57,840 - WARNING - 
[!] VULNERABILITY: AZU-NET-001
 -> Location: TG_networking.tf -> bad_sg
 -> Issue: allows inbound traffic from anywhere (Internet). (Got: *)
 -> Why: Allowing any IP (*) opens the network to public brute-force and scanning attacks.
 -> Fix: Restrict 'source_address_prefix' to specific trusted IPs.
```



## Romana

### Descriere
Un script de tip Static Analysis Security Testing (SAST) conceput pentru a detecta configurări gresite de securitate în scripturile Azure Terraform. Scannerul verifica resursele Terraform pe baza unui set de reguli definit în fiierul YAML.

#### 📂 Fisiere
* `main.py`: Rularea scriptului.
* `scanner/`: Directorul care contine logica de parsare HCL si comparare a regulilor.
* `rules.yaml`: Dictionarul cu reguli de securitate (Descriere, Valoare Asteptata, Remediere).
* `samples/`: Directorul cu fisiere .tf folosite pentru testare.
* `requirements.txt`: Lista versiunilor exacte ale dependentelor python (Lark, PyYAML, etc.).
* `scan_results.log`: Fisierul unde sunt salvate vulnerabilitatile detectate.

#### Instalare
1.  **Cerinte**: Python 3.11.6
2.  **Copiati proiectul** pe masina voastra.
    ```
    git clone https://github.com/psTudor/IaC-Scanner.git
    ```
3.  **Instalare Dependinte**:
   Creati un virtual enviroment pe care apoi il activati
    ```bash
    python -m venv venv
    ```
    Windows powershell
    ```bash
    venv\Scripts\Activate.ps1
    ```
    Linux bash/zsh
    ```bash
    source venv/bin/activate
    ```
    Instalarea Dependintelor
    ```bash
    pip install -r requirements.txt
    ```

#### Utilizare
Rulati scriptul din terminal:
```bash
python main.py
```

#### Rezultat
```
2026-04-18 12:29:57,840 - WARNING - 
[!] VULNERABILITY: AZU-APP-002
 -> Location: TG_app_service.tf -> app-service1
 -> Issue: has weak or missing TLS version. (Got: 1.1)
 -> Why: Old TLS versions (1.0/1.1) are vulnerable to known cryptographic attacks.
 -> Fix: Set 'min_tls_version = "1.2"'.

 2026-04-18 12:29:57,840 - WARNING - 
[!] VULNERABILITY: AZU-NET-001
 -> Location: TG_networking.tf -> bad_sg
 -> Issue: allows inbound traffic from anywhere (Internet). (Got: *)
 -> Why: Allowing any IP (*) opens the network to public brute-force and scanning attacks.
 -> Fix: Restrict 'source_address_prefix' to specific trusted IPs.
```
