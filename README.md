# bhsc-invoice-pkg

This repository contains the PL/SQL package `bhsc_import_invoice_pkg` for invoice import, check creation and GL interfacing used in Oracle E-Business Suite / Oracle DB.

Files:
- src/plsql/bhsc_import_invoice_pkg.pck — package spec and body (combined .pks/.pkb in single .pck file).

Deployment:
1. Review and (optionally) split the package into spec (.pks) and body (.pkb).
2. Connect to the target database as a user with privileges to create packages:
   sqlplus apps/<password>@DB
3. Run:
   @src/plsql/bhsc_import_invoice_pkg.pck

Notes:
- This package interacts with Oracle EBS tables/APIs (AP, AR, GL, FND modules). Deploy only in a compatible EBS environment.
- Run in a test environment first.
- Update sequence names, user ids, and other environment-specific references as needed.

License: MIT
