import csv
import sys
import os
from datetime import datetime, timedelta
from jira import JIRA

class JiraStatusAnalyzer:
    """
    Refactored for testability - separated concerns
    """
    
    def __init__(self, jira_url, api_token):
        self.jira_url = jira_url
        self.api_token = api_token
        self.jira = None
    
    def connect_to_jira(self):
        """
        Establish connection to Jira using Personal Access Token
        """
        headers = JIRA.DEFAULT_OPTIONS["headers"].copy()
        headers["Authorization"] = f"Bearer {self.api_token}"
        
        try:
            self.jira = JIRA(server=self.jira_url, options={"headers": headers})
            return True
        except Exception as e:
            print(f"❌ Failed to connect to Jira: {e}")
            return False
    
    def get_issue_transitions(self, issue_key):
        """
        Get issue transitions - now returns structured data
        """
        if not self.jira:
            raise ConnectionError("Not connected to Jira")
        
        try:
            issue = self.jira.issue(issue_key, expand='changelog')
            transitions = []
            
            if hasattr(issue, 'changelog') and issue.changelog:
                for history in issue.changelog.histories:
                    for item in history.items:
                        if item.field == 'status':
                            transitions.append({
                                'date': datetime.strptime(history.created.split('T')[0], '%Y-%m-%d'),
                                'from_status': item.fromString,
                                'to_status': item.toString,
                                'created': history.created
                            })
            
            return transitions
            
        except Exception as e:
            raise Exception(f"Error fetching transitions for {issue_key}: {e}")
    
    def find_status_transitions(self, transitions):
        """
        Find first 'In Progress' and last 'Done' transitions
        """
        first_in_progress = None
        last_done = None
        
        for transition in transitions:
            # Find first transition TO "In Progress"
            if transition['to_status'] and 'progress' in transition['to_status'].lower():
                if first_in_progress is None:
                    first_in_progress = transition
            
            # Find last transition TO "Done"
            if transition['to_status'] and 'done' in transition['to_status'].lower():
                last_done = transition
        
        return first_in_progress, last_done
    
    def calculate_days_difference(self, start_date, end_date):
        """
        Calculate difference in days between two dates
        """
        if start_date and end_date:
            return (end_date - start_date).days
        return None
    
    def parse_csv_row(self, row, row_number):
        """
        Parse a single CSV row and extract issue key
        """
        if not row:
            return None, f"Row {row_number}: Empty row"
        
        issue_key = row[0].strip() if row else ""
        if not issue_key:
            return None, f"Row {row_number}: Empty issue key"
        
        return issue_key, None
    
    def process_issue(self, issue_key):
        """
        Process a single issue and return transition data
        """
        transitions = self.get_issue_transitions(issue_key)
        first_in_progress, last_done = self.find_status_transitions(transitions)
        
        result = {
            'issue_key': issue_key,
            'first_in_progress_date': '',
            'last_done_date': '',
            'days_difference': ''
        }
        
        if first_in_progress:
            result['first_in_progress_date'] = first_in_progress['date'].strftime('%Y-%m-%d')
            
        if last_done:
            result['last_done_date'] = last_done['date'].strftime('%Y-%m-%d')
        
        if first_in_progress and last_done:
            days_diff = self.calculate_days_difference(
                first_in_progress['date'], 
                last_done['date']
            )
            result['days_difference'] = str(days_diff) if days_diff is not None else ''
        
        return result

def main():
    """
    Main function - CLI interface
    """
    print("🚀 Jira Status Transition Analyzer")
    
    # Configuration
    JIRA_URL = "https://jira.worldline-solutions.com/"
    API_TOKEN = "INSERT CODE"
    
    analyzer = JiraStatusAnalyzer(JIRA_URL, API_TOKEN)
    
    # Get file paths
    if len(sys.argv) != 3:
        input_file = input("Enter input CSV file path: ").strip()
        output_file = input("Enter output CSV file path: ").strip()
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    
    # Connect and process
    if analyzer.connect_to_jira():
        process_csv_file(analyzer, input_file, output_file)

def process_csv_file(analyzer, input_file, output_file):
    """
    Process entire CSV file - separated for testing
    """
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        csv_reader = csv.reader(infile)
        rows = list(csv_reader)
    
    if not rows:
        raise ValueError("Input file is empty")
    
    output_rows = []
    header_row = rows[0]
    new_headers = header_row + [
        'First_In_Progress_Date', 
        'Last_Done_Date', 
        'Days_In_Progress_To_Done'
    ]
    output_rows.append(new_headers)
    
    # Process data rows
    for i, row in enumerate(rows[1:], 1):
        issue_key, error = analyzer.parse_csv_row(row, i)
        
        if error:
            print(f"⚠️ {error}")
            output_rows.append(row + ["", "", ""])
            continue
        
        try:
            result = analyzer.process_issue(issue_key)
            output_row = row + [
                result['first_in_progress_date'],
                result['last_done_date'],
                result['days_difference']
            ]
            output_rows.append(output_row)
            print(f"✅ Processed {issue_key}")
            
        except Exception as e:
            print(f"❌ Error processing {issue_key}: {e}")
            output_rows.append(row + ["ERROR", "ERROR", "ERROR"])
    
    # Write output
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        csv_writer = csv.writer(outfile)
        csv_writer.writerows(output_rows)

if __name__ == "__main__":
    main()