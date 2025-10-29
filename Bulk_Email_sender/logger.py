def log_status(df, index, status):
    df.at[index, 'Status'] = status
    df.to_excel("email_status_log.xlsx", index=False)