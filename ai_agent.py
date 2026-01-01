"""
AI Agent for Email Reply Assistant
Handles email intent analysis, tone detection, and response generation
"""

import requests
import json
from config import OPENROUTER_API_KEY, OPENROUTER_MODEL, OPENROUTER_URL


class EmailReplyAgent:
    def __init__(self):
        self.api_key = OPENROUTER_API_KEY
        self.model = OPENROUTER_MODEL
        self.url = OPENROUTER_URL

    def analyze_email_intent(self, email_text):
        """
        Analyze the intent of the incoming email
        """
        prompt = f"""
        Analyze the following email and identify the main intent/purpose:
        
        Email: {email_text}
        
        Identify the intent in 1-2 sentences. Examples of intents: 
        - Request for information
        - Meeting scheduling
        - Complaint or issue reporting
        - Thank you or appreciation
        - Business proposal
        - Follow-up inquiry
        - Other
        """
        
        response = self._call_llm(prompt)
        return response

    def detect_tone(self, email_text, selected_tone=None):
        """
        Detect appropriate tone for the response if not provided by user
        """
        if selected_tone and selected_tone.lower() != "auto":
            return selected_tone
            
        prompt = f"""
        Analyze the tone of the following email and suggest an appropriate response tone:
        
        Email: {email_text}
        
        Available tones: Formal, Casual, Friendly
        
        Respond with just the appropriate tone based on the email's context and formality level.
        """
        
        response = self._call_llm(prompt)
        return response.strip()

    def generate_reply(self, email_text, tone="Auto"):
        """
        Generate a professional reply based on the email content and desired tone
        """
        # Determine the appropriate tone
        response_tone = self.detect_tone(email_text, tone)
        
        # Analyze the intent of the email
        intent = self.analyze_email_intent(email_text)
        
        prompt = f"""
        You are an email assistant. Generate a professional reply to the following email:
        
        Original Email: {email_text}
        
        Email Intent: {intent}
        Desired Response Tone: {response_tone}
        
        Generate a context-aware, grammatically correct, polite and professional reply.
        The reply should address the main points of the original email appropriately.
        Keep the response concise but complete.
        """
        
        response = self._call_llm(prompt)
        return response.strip()

    def _call_llm(self, prompt):
        """
        Internal method to call the LLM API
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:8501",  # For local Streamlit app
            "X-Title": "Email Reply Assistant Agent", 
        }

        data = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        try:
            response = requests.post(
                url=self.url,
                headers=headers,
                data=json.dumps(data)
            )
            
            if response.status_code == 200:
                result = response.json()
                return result['choices'][0]['message']['content']
            else:
                raise Exception(f"API request failed with status {response.status_code}: {response.text}")
                
        except Exception as e:
            return f"Error generating response: {str(e)}"


# Example usage
if __name__ == "__main__":
    agent = EmailReplyAgent()
    
    # Example email
    email = "Hi, I hope you're doing well. Just wanted to follow up on the proposal we discussed last week. When would be a good time to schedule a meeting to review it?"
    
    reply = agent.generate_reply(email, "Friendly")
    print("Generated Reply:")
    print(reply)