import sys
import time
from telethon.sync import TelegramClient
from config import load_config, console
from utils import get_bool, smart_sleep, resolve_entities
from core import process_group

def main():
    # 1. Setup
    cfg = load_config()
    console.print(f"\n[bold green]Loaded Profile:[/bold green] {cfg['session_name']}")
    console.print(f"[bold cyan]Default Bot:[/bold cyan] {cfg['default_bot']}\n")
    console.print(f"[bold cyan]__________________________________________[/bold cyan]\n")


    # 2. User Inputs
    try:
        start_r = int(console.input("[bold]Groups Name Start Range: [/bold]"))
        end_r = int(console.input("[bold]Groups Name End Range:   [/bold]"))
    except ValueError:
        console.print("❌ Invalid numbers.", style="error")
        sys.exit()

    prefs = {
        'mute': get_bool("Mute groups?"),
        'archive': get_bool("Archive groups?"),
        'message': None
    }

    # User List Building
    users_to_add = []
    if get_bool("Add custom users?"):
        raw = console.input("   [dim]Enter usernames (comma sep): [/dim]")
        users_to_add = [u.strip() for u in raw.replace(" ", "").split(",") if u.strip()]

    if get_bool(f"Add default bot ({cfg['default_bot']})?"):
        users_to_add.append(cfg['default_bot'])

    if get_bool("Send a message?"):
        prefs['message'] = console.input("   [dim]Message text (Empty=Title): [/dim]")

    # 3. Execution
    console.print("\n[bold]____________ STARTING ENGINE... ____________[/bold]")
    
    with TelegramClient(cfg['session_name'], cfg['api_id'], cfg['api_hash']) as client:
        if not client.is_user_authorized():
            console.print("⚠️ Auth Required. Sending code...", style="warning")
            client.start(phone=cfg['phone'])

        # Resolve Users ONCE
        target_entities = resolve_entities(client, users_to_add)
        
        total = end_r - start_r + 1
        count = 0

        console.print(f"\n[bold]Processing {total} Groups[/bold]")
        console.rule()

        for i in range(start_r, end_r + 1):
            count += 1
            t_start = time.time()
            title = str(i)
            
            console.print(f"\n[bold cyan][{count}/{total}][/bold cyan] Group: [bold white]{title}[/bold white]")
            
            try:
                process_group(client, title, prefs, target_entities)
                smart_sleep(t_start, 10, 20)
                
            except KeyboardInterrupt:
                console.print("\n👋 Stopped by user.", style="warning")
                break
            except Exception:
                break

    console.print("\n[bold green]✨ JOB COMPLETE ✨[/bold green]")

if __name__ == "__main__":
    main()