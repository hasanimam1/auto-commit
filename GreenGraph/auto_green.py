import os
import datetime

# Configuration: Kab se kab tak ka graph green karna hai
# Hum poora 2025 cover kar rahe hain
start_date = datetime.date(2026, 1, 1)
end_date = datetime.date(2026, 3, 31)

current_date = start_date

print(f"🚀 Starting the Green Mission from {start_date} to {end_date}...")

while current_date <= end_date:
    # Ek din mein 2-4 random commits taaki graph natural lage (ekdum same na dikhe)
    # Aap is range ko badha bhi sakte ho (e.g., range(2, 5))
    for i in range(2): 
        # Date format for Git
        d = current_date.strftime('%Y-%m-%d 12:00:00')
        
        # Dummy file update
        with open('data.txt', 'a') as f:
            f.write(f'Contribution on {d}\n')
        
        # Git Commands for Windows PowerShell
        # Hum Environment variables set kar rahe hain taaki Git purani date register kare
        os.system(f'git add data.txt')
        os.system(f'set GIT_AUTHOR_DATE="{d}" && set GIT_COMMITTER_DATE="{d}" && git commit -m "Data Science Activity {d}"')

    current_date += datetime.timedelta(days=1)

print("✅ Done! Sabhi dates commit ho gayi hain. Ab bas 'git push' karo.")