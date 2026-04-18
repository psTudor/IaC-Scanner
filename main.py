import glob
import logging
import os
from parsers.terraform import parse_terraform
from scanner.rules import scan_resources

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("security_scan.log"),
        logging.StreamHandler()                 
    ]
)


def main():
    logging.info("---- IaC Security Scanner ----")
    
    files_to_scan = glob.glob("samples/*.tf")
    resources = []
    
    for file in files_to_scan:
        logging.info(f"Parsing file: {os.path.basename(file)}")
        resources.extend(parse_terraform(file))

    alerts = scan_resources(resources)

    if not alerts:
        logging.info("Scan complete. No security issues found.")
    else:
        logging.warning(f"Scan complete. Found {len(alerts)} vulnerabilities!")
        for alert in alerts:
            logging.warning(alert)

if __name__ == "__main__":
    main()