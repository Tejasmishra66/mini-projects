import streamlit as st
import pandas as pd
import os
import io
from datetime import datetime
from auth import authenticate_gmail
from email_sender import send_emails_with_attachments
from logger import log_status

# Page config
st.set_page_config(page_title="Bulk Email Sender", page_icon="📧", layout="centered")

# Sidebar instructions
with st.sidebar:
    st.header("📌 Instructions")
    st.markdown("""
    1. Upload an Excel file with columns: `Email`, `Subject`, `Body`
    2. Attachments are fixed for now (form_1.docx, form_2.docx)
    3. Click **Send Emails** to begin
    4. Status will be logged and downloadable
    """)

# Main title
st.title("📧 TPC Bulk Email Automation Tool")
st.caption(f"🕒 Last run: {datetime.now().strftime('%d %b %Y, %I:%M %p')}")

# Upload Excel file
uploaded_file = st.file_uploader("📂 Upload Excel File", type=["xlsx"])

# Static attachment paths
attachment_paths = [
    "C:/TPC_forms/form_1.docx",
    "C:/TPC_forms/form_2.docx"
]

# Process uploaded file
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.success("✅ File uploaded successfully!")
    st.write("📄 Preview of Uploaded Data:")
    st.dataframe(df)

    total = len(df)
    st.metric(label="📊 Total Emails to Send", value=total)

    if st.button("🚀 Send Emails"):
        try:
            st.info("🔐 Authenticating Gmail...")
            service = authenticate_gmail()

            with st.spinner("📤 Sending emails... Please wait ⏳"):
                send_emails_with_attachments(service, uploaded_file, attachment_paths, log_status)

            st.success("✅ All emails processed successfully!")
            st.balloons()

            # Reload updated DataFrame with status
            df_updated = pd.read_excel("status_log.xlsx")

            # Delivery summary
            st.markdown("### 📈 Delivery Summary")
            sent_count = df_updated['Status'].str.contains("Sent").sum()
            failed_count = df_updated['Status'].str.contains("Failed").sum()
            skipped_count = df_updated['Status'].str.contains("Skipped").sum()

            st.write(f"✅ Sent: {sent_count}")
            st.write(f"❌ Failed: {failed_count}")
            st.write(f"⚠️ Skipped: {skipped_count}")

            # Download button
            output = io.BytesIO()
            df_updated.to_excel(output, index=False)
            st.download_button("📥 Download Status Log", data=output.getvalue(), file_name="status_log.xlsx")

        except Exception as e:
            st.error(f"❌ Error: {e}")
else:
    st.warning("Please upload an Excel file to begin.")