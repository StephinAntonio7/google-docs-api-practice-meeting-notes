import time
from google.colab import auth
from googleapiclient.discovery import build
from google.auth import default

# Authenticate and create the service
auth.authenticate_user()
creds, _ = default()
service = build("docs", "v1", credentials=creds)

# Properly ordered meeting notes (from top to bottom)
meeting_notes = [
    {"text": "Product Team Sync - May 15, 2023", "style": "HEADING_1"},
    {"text": "Attendees", "style": "HEADING_2"},
    {"text": "- Sarah Chen (Product Lead)\n- Mike Johnson (Engineering)\n- 
Anna Smith (Design)\n- David Park (QA)", "style": "NORMAL_TEXT"},
    {"text": "Agenda", "style": "HEADING_2"},
    
    # Sprint Review
    {"text": "1. Sprint Review", "style": "HEADING_3"},
    {"text": "* Completed Features\n  * User authentication flow\n  * 
Dashboard redesign\n  * Performance optimization\n    * Reduced load time 
by 40%\n    * Implemented caching solution", "style": "NORMAL_TEXT"},
    {"text": "* Pending Items\n  * Mobile responsive fixes\n  * Beta 
testing feedback integration", "style": "NORMAL_TEXT"},
    
    # Current Challenges
    {"text": "2. Current Challenges", "style": "HEADING_3"},
    {"text": "* Resource constraints in QA team\n* Third-party API 
integration delays\n* User feedback on new UI\n  * Navigation confusion\n  
* Color contrast issues", "style": "NORMAL_TEXT"},
    
    # Next Sprint Planning
    {"text": "3. Next Sprint Planning", "style": "HEADING_3"},
    {"text": "* Priority Features\n  * Payment gateway integration\n  * 
User profile enhancement\n  * Analytics dashboard", "style": 
"NORMAL_TEXT"},
    {"text": "* Technical Debt\n  * Code refactoring\n  * Documentation 
updates", "style": "NORMAL_TEXT"},
    
    # Notes Section
    {"text": "Notes", "style": "HEADING_2"},
    {"text": "* Next sync scheduled for May 22, 2023\n* Platform demo for 
stakeholders on May 25\n* Remember to update JIRA tickets", "style": 
"NORMAL_TEXT"},
    
    # Next Steps Section
    {"text": "Next Steps", "style": "HEADING_2"},
    {"text": "* Schedule individual team reviews\n* Update sprint board\n* 
Share meeting summary with stakeholders", "style": "NORMAL_TEXT"},
    
    # Action Items (Checklists with proper formatting)
    {"text": "Action Items", "style": "HEADING_2"},
    {"text": "☐ @david: Prepare QA resource allocation proposal", 
"style": "CHECKBOX", "color": "blue"},
    {"text": "☐ @anna: Share updated design system documentation", 
"style": "CHECKBOX", "color": "blue"},
    {"text": "☐ @mike: Schedule technical review for payment 
integration", "style": "CHECKBOX", "color": "blue"},
    {"text": "☐ @sarah: Finalize Q3 roadmap by Friday", "style": 
"CHECKBOX", "color": "blue"},

    # Footer Info (Bold)
    {"text": "Meeting recorded by: Sarah Chen\nDuration: 45 minutes", 
"style": "BOLD_TEXT", "color": "green"},
]

# Create a new Google Doc
try:
    document = service.documents().create(body={"title": "Product Team 
Sync - May 15, 2023"}).execute()
    doc_id = document["documentId"]
except Exception as e:
    print(f"Error creating document: {e}")
    exit()

def get_document_length(service, doc_id):
    """ Fetches the current length of the document. """
    try:
        doc = service.documents().get(documentId=doc_id).execute()
        return doc["body"]["content"][-1]["endIndex"]
    except Exception as e:
        print(f"Error fetching document length: {e}")
        return None

def insert_text_with_formatting(service, doc_id, content_list):
    """ Inserts text into Google Docs while maintaining order and applying 
styles. """
    try:
        requests = []

        # Reverse the list to insert from bottom to top
        for item in reversed(content_list):
            index = 1  # Always insert at the top

            if item["style"] == "CHECKBOX":
                requests.append({
                    "insertText": {"location": {"index": index}, "text": 
item["text"] + "\n"}
                })
                if "color" in item:
                    color_rgb = {"red": 1.0, "green": 0.0, "blue": 0.0}
                    requests.append({
                        "updateTextStyle": {
                            "range": {"startIndex": index, "endIndex": 
index + len(item["text"]) + 1},
                            "textStyle": {"foregroundColor": {"color": 
{"rgbColor": {"red": 0.1, "green": 0.3, "blue": 1.0}}}},
                            "fields": "foregroundColor"
                        }
                    })
            elif item["style"] == "BOLD_TEXT":
                requests.append({
                    "insertText": {"location": {"index": index}, "text": 
item["text"] + "\n"}
                })
                requests.append({
                    "updateTextStyle": {
                        "range": {"startIndex": index, "endIndex": index + 
len(item["text"]) + 1},
                        "textStyle": {"bold": True},
                        "fields": "bold"
                    }
                })
            else:
                requests.append({
                    "insertText": {"location": {"index": index}, "text": 
item["text"] + "\n"}
                })

                if item["style"].startswith("HEADING_"):
                    requests.append({
                        "updateParagraphStyle": {
                            "range": {"startIndex": index, "endIndex": 
index + len(item["text"]) + 1},
                            "paragraphStyle": {"namedStyleType": 
item["style"]},
                            "fields": "namedStyleType"
                        }
                    })

        service.documents().batchUpdate(documentId=doc_id, 
body={"requests": requests}).execute()
        time.sleep(5)
    except Exception as e:
        print(f"Error during text insertion: {e}")

print(f"Google Doc successfully created! View it here: 
https://docs.google.com/document/d/{doc_id}")

# Insert the meeting notes with proper formatting
insert_text_with_formatting(service, doc_id, meeting_notes)


