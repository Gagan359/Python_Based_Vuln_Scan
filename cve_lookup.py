import requests


def lookup_cves(product, version):

    if not product:
        return []

    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"

    params = {
        "keywordSearch": f"{product} {version}",
        "resultsPerPage": 10
    }

    try:

        response = requests.get(url, params=params, timeout=15)

        if response.status_code != 200:
            return []

        data = response.json()

    except requests.RequestException:
        return []

    results = []

    vulnerabilities = data.get("vulnerabilities", [])

    for vulnerability in vulnerabilities:

        cve = vulnerability.get("cve", {})

        cve_id = cve.get("id", "Unknown")

        description = "No description available"

        descriptions = cve.get("descriptions", [])

        for desc in descriptions:
            if desc.get("lang") == "en":
                description = desc.get("value")
                break

        severity = "Unknown"

        metrics = cve.get("metrics", {})

        if "cvssMetricV31" in metrics:
            severity = metrics["cvssMetricV31"][0]["cvssData"]["baseSeverity"]

        elif "cvssMetricV30" in metrics:
            severity = metrics["cvssMetricV30"][0]["cvssData"]["baseSeverity"]

        elif "cvssMetricV2" in metrics:
            severity = metrics["cvssMetricV2"][0]["baseSeverity"]

        results.append(
            {
                "id": cve_id,
                "severity": severity,
                "description": description
            }
        )

    return results


if __name__ == "__main__":

    product = input("Product: ")
    version = input("Version: ")

    results = lookup_cves(product, version)

    print(f"\nFound {len(results)} CVEs\n")

    for cve in results:

        print("-" * 60)
        print(f"CVE: {cve['id']}")
        print(f"Severity: {cve['severity']}")
        print(f"Description: {cve['description']}")