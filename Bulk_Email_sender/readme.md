 **Project Title**
**Bulk Email Sender using Gmail API & Excel**

---

**Project Description**
The Bulk Email Sender is a Python-based automation tool designed to streamline mass communication using Gmail and Excel. It allows users to send personalized emails with optional attachments to multiple recipients listed in an Excel sheet, making it ideal for institutional outreach, placement coordination, or event announcements.


 **Features**
- Gmail API authentication via OAuth2
- Excel-based bulk email dispatch
- Optional file attachments (e.g., PDFs, forms)
- Tkinter GUI for ease of use
- Real-time delivery status logging to Excel
- Modular and scalable codebase


**Tech Stack**
- **Language:** Python 3.x  
- **Email API:** Gmail API (`google-api-python-client`)  
- **GUI:** Tkinter  
- **Data Handling:** Pandas, openpyxl  
- **File Format:** `.xlsx` for input/output  


 **Input Format**
Prepare an Excel file with the following columns:

| Email             | Subject           | Body                         |
|------------------|-------------------|------------------------------|
| user@example.com | Welcome to TPC!   | Please find attached forms. |



 **Use Cases**
- Faculty outreach for Training & Placement Cell (TPC)
- Sending forms, notices, or reminders in bulk
- Event invitations and follow-ups
- Institutional announcements


**Scalability & Future Enhancements**
- Works with any Gmail account
- Easily extendable to other APIs (Outlook, SMTP)
- Can be containerized for deployment
- Future plans:
  - Email scheduling
  - Dynamic attachment selection
  - AI-powered personalization

