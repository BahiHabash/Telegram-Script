import os
import sys
from dotenv import load_dotenv
from rich.console import Console
from rich.theme import Theme

# Setup Rich Console with custom theme
custom_theme = Theme({
    "info": "cyan",
    "success": "bold green",
    "warning": "yellow",
    "error": "bold red",
    "highlight": "magenta"
})
console = Console(theme=custom_theme)

def load_config():
    # Loads environment variables and selects the user profile.
    load_dotenv()
    
    console.print("[bold]🔐 TELEGRAM AUTHENTICATION[/bold]", style="highlight")
    profile = input("👤 Enter Profile Name (e.g., BAHI, MO): ").strip().upper()
    
    api_id = os.getenv(f"{profile}_API_ID")
    api_hash = os.getenv(f"{profile}_API_HASH")
    phone = '+' + os.getenv(f"{profile}_PHONE")
    default_bot = os.getenv("DEFAULT_BOT_USERNAME", "x6AzkarBOT")

    if not api_id or not api_hash:
        console.print(f"❌ Error: Missing credentials for [bold]{profile}[/bold] in .env file.", style="error")
        sys.exit(1)
        
    return {
        "api_id": int(api_id),
        "api_hash": api_hash,
        "phone": phone,
        "session_name": f"session_{profile.lower()}-{phone.replace('+', '')}",
        "default_bot": default_bot
    }