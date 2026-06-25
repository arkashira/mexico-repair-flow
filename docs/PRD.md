# Product Requirements Document (PRD)  
## Mexico Repair Flow – Customer Information Management System  
**Version:** 1.0 – 2026‑06‑25  
**Author:** Senior Product/Engineering Lead – Axentx  
**Repository:** `mexico-repair-flow` (GitHub: `arkashira/mexico-repair-flow`)  

---

## 1. Problem Statement  
Repair shops in Mexico face fragmented customer data spread across spreadsheets, paper records, and disparate tools. This leads to:

- **Duplicate entries** – multiple records for the same customer, causing billing errors.  
- **Data loss** – manual entry mistakes or accidental deletions.  
- **Inefficient workflows** – time spent searching for customer history instead of focusing on repairs.  

The current market lacks a lightweight, open‑source solution that is **easy to deploy**, **secure**, and **integrated** with existing repair‑shop software stacks.

---

## 2. Target Users  

| Persona | Role | Pain Points | Desired Outcomes |
|---------|------|-------------|------------------|
| **Shop Owner** | Oversees daily operations | • Time wasted on paperwork<br>• Inaccurate customer records | • Quick access to customer history<br>• Reduce duplicate entries |
| **Repair Technician** | Performs repairs | • Needs to verify customer details before work<br>• Lacks a unified view of past repairs | • One‑click lookup of customer data |
| **Front‑Desk Clerk** | Handles appointments | • Manual data entry errors<br>• Difficulty finding customers | • Simple UI for creating/updating/searching customers |
| **IT Admin** | Maintains shop software | • Needs a lightweight, self‑hosted solution<br>• Security compliance | • Easy deployment, JSON backup, minimal dependencies |

---

## 3. Goals & Success Metrics  

| Goal | Success Metric | Target |
|------|----------------|--------|
| **Reduce duplicate customer records** | % of duplicate entries detected | < 2% |
| **Improve data retrieval time** | Avg. search latency | < 200 ms |
| **Increase user satisfaction** | NPS (Net Promoter Score) | ≥ 70 |
| **Ensure data integrity** | % of successful backups | 100% (daily JSON export) |
| **Facilitate adoption** | Number of installations in pilot shops | ≥ 20 shops in 3 months |

---

## 4. Key Features (Prioritized)

| Rank | Feature | Description | Dependencies | Acceptance Criteria |
|------|---------|-------------|--------------|---------------------|
| 1 | **Create Customer** | Add a new customer with name, email, phone, and optional notes. | None | • Customer ID auto‑generated<br>• Validation of email format |
| 2 | **Retrieve Customer** | Fetch customer by ID or unique email. | None | • Returns full customer record<br>• 404 if not found |
| 3 | **Update Customer** | Modify any field of an existing customer. | None | • Partial updates allowed<br>• Audit trail of changes |
| 4 | **Search Customers** | Query by name, email, phone, or notes (case‑insensitive, partial match). | None | • Returns list of matching IDs<br>• Supports pagination |
| 5 | **JSON Persistence** | Export all customers to a JSON file; import from JSON. | None | • Export includes all fields<br>• Import merges without duplicates |
| 6 | **Duplicate Detection** | Flag potential duplicates during create/update. | None | • Suggest existing record(s) with similarity score |
| 7 | **CLI Interface** | Simple command‑line tool for quick operations. | None | • Supports all CRUD operations |
| 8 | **REST API** | Expose CRUD endpoints for integration with shop software. | Flask/FastAPI | • Standard HTTP status codes<br>• Authentication token |
| 9 | **Docker Container** | Pre‑built image for easy deployment. | Docker | • Runs on Linux, macOS, Windows |
| 10 | **Unit & Integration Tests** | 90% code coverage. | pytest | • CI pipeline passes on every commit |

---

## 5. Scope (In‑Scope)

- Core CRUD operations for customer data.  
- JSON import/export functionality.  
- Duplicate detection logic.  
- Basic CLI for manual use.  
- Docker image for deployment.  
- Unit tests and CI pipeline.  

## 6. Out‑of‑Scope

- Graphical user interface (web or desktop).  
- Advanced analytics or reporting dashboards.  
- Integration with payment gateways or inventory systems.  
- Multi‑tenant architecture or cloud hosting.  

---

## 7. Technical Constraints & Assumptions

| Constraint | Rationale | Impact |
|------------|-----------|--------|
| **Python 3.11+** | Modern language features, type hints. | Requires Python runtime on host. |
| **No external database** | Keeps deployment lightweight. | Data stored in memory + JSON files. |
| **No external authentication** | Simplifies CLI usage. | REST API will use simple token auth. |
| **Open‑source license (MIT)** | Encourages adoption in small shops. | No commercial restrictions. |

---

## 8. Roadmap (High‑Level)

| Sprint | Deliverable | Notes |
|--------|-------------|-------|
| 1 | Core CRUD + JSON persistence | MVP release |
| 2 | Duplicate detection + CLI | Add user feedback |
| 3 | REST API + Docker image | Enable integration |
| 4 | Unit tests + CI | Ensure quality |
| 5 | Pilot deployment & feedback | Iterate on UX |

---

## 9. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Data loss during import/export | Medium | High | Validate JSON schema, backup before import |
| Duplicate detection false positives | Low | Medium | Tune similarity threshold, allow manual override |
| Performance degradation with >10k customers | Medium | Medium | Profile and optimize search algorithm |
| Adoption barrier due to lack of UI | Medium | Medium | Provide clear CLI docs, plan future web UI |

---

## 10. Stakeholder Sign‑Off

| Stakeholder | Role | Signature |
|-------------|------|-----------|
| Alex Rivera | Shop Owner (Pilot) |  |
| Maria Gonzales | Repair Technician |  |
| Carlos Méndez | IT Admin |  |

--- 

*Prepared by: Senior Product/Engineering Lead – Axentx*
