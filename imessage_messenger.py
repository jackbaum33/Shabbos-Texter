import subprocess
import re
import time

class ImessageSender:
    def send_text(self, phone_number, message):
        """Send message via iMessage or SMS"""
        phone_number = self.format_phone_number(phone_number)
        message = message.replace('\\', '\\\\').replace('"', '\\"')
        
        # This script tries to send via any available service
        applescript = f'''
        tell application "Messages"
            set targetService to 1st account whose service type = iMessage
            set targetBuddy to participant "{phone_number}" of targetService
            send "{message}" to targetBuddy
        end tell
        '''
        
        try:
            result = subprocess.run(['osascript', '-e', applescript], 
                                capture_output=True, 
                                text=True, 
                                check=True,
                                timeout=10)
            return True
        except subprocess.CalledProcessError as e:
            return False

    def format_phone_number(self, phone_number):
        """Format phone number to include country code"""
        # Remove all non-digit characters
        clean_number = re.sub(r'\D', '', phone_number.strip())
        
        # Check if it starts with 972 (Israel)
        if clean_number.startswith('972'):
            # Israeli number - add + prefix
            return '+' + clean_number
        
        # Check if it starts with 1 and has 11 digits (US/Canada with country code)
        elif clean_number.startswith('1') and len(clean_number) == 11:
            return '+' + clean_number
        
        # If it's 10 digits, assume US number and add +1
        elif len(clean_number) == 10:
            return '+1' + clean_number
        
        # Otherwise return with + prefix
        else:
            return '+' + clean_number