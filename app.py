"""
Streamlit UI for Email Reply Assistant Agent
Provides a user interface for inputting emails and generating replies
"""

import streamlit as st
from ai_agent import EmailReplyAgent


def main():
    # Set up the Streamlit page
    st.set_page_config(
        page_title="Email Reply Assistant Agent",
        page_icon="📧",
        layout="wide"
    )
    
    # Header
    st.title("📧 Email Reply Assistant Agent")
    st.markdown("AI-powered assistant to generate professional email replies")
    
    # Create two columns for layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("Input Email")
        
        # Text area for incoming email
        incoming_email = st.text_area(
            "Enter the incoming email text:",
            height=300,
            placeholder="Paste the email you received here..."
        )
        
        # Tone selection
        tone_options = ["Auto", "Formal", "Casual", "Friendly"]
        selected_tone = st.selectbox(
            "Select response tone (or let AI auto-detect):",
            tone_options,
            index=0
        )
        
        # Generate button
        generate_clicked = st.button("Generate Reply", type="primary")
    
    with col2:
        st.header("Generated Reply")
        
        # Display area for generated reply
        if generate_clicked:
            if incoming_email.strip() == "":
                st.warning("Please enter an email to generate a reply.")
            else:
                with st.spinner("Generating your email reply..."):
                    try:
                        agent = EmailReplyAgent()
                        generated_reply = agent.generate_reply(incoming_email, selected_tone)
                        
                        # Display the generated reply
                        st.text_area(
                            "Your AI-generated reply:",
                            value=generated_reply,
                            height=300,
                            key="reply_output"
                        )
                        
                        # Copy to clipboard button
                        st.code(generated_reply, language="text")
                        st.download_button(
                            label="📋 Copy to Clipboard",
                            data=generated_reply,
                            file_name="email_reply.txt",
                            mime="text/plain"
                        )
                        
                        # Show additional information
                        st.success("Reply generated successfully!")
                        
                    except Exception as e:
                        st.error(f"Error generating reply: {str(e)}")
        else:
            st.info("Enter an email and click 'Generate Reply' to get started.")
    
    # Additional information section
    with st.expander("How it works"):
        st.markdown("""
        - **Intent Analysis**: The AI analyzes the incoming email to understand its purpose
        - **Tone Detection**: Automatically detects appropriate response tone or uses your selection
        - **Reply Generation**: Creates a context-aware, professional reply
        - **Copy Feature**: Use the clipboard button to copy the generated reply
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("*Email Reply Assistant Agent - Powered by AI*")


if __name__ == "__main__":
    main()