import time
import random
from config import console

def get_bool(prompt):
    # Asks a Yes/No question using Rich.
    response = console.input(f"[yellow]❓ {prompt} (y/n): [/yellow]").strip().lower()
    return response.startswith('y')

def smart_sleep(start_time, min_s=10, max_s=20):
    # Calculates remaining time to ensure safety buffer.
    elapsed = time.time() - start_time
    target_wait = random.uniform(min_s, max_s)
    remaining = target_wait - elapsed
    
    if remaining > 0:
        console.print(f"   ⏳ Safety Buffer: Waiting [cyan]{remaining:.1f}s[/cyan]...", style="dim")
        time.sleep(remaining)
    else:
        console.print(f"   ⚡ Ready (Took {elapsed:.1f}s)", style="dim")

def resolve_entities(client, usernames):
    # Resolves a list of usernames to InputEntities.
    if not usernames:
        return []
    
    console.print(f"\n🔎 Resolving {len(usernames)} users...", style="info")
    entities = []
    for user in usernames:
        try:
            entity = client.get_input_entity(user)
            entities.append(entity)
            console.print(f"   ✅ Found: [bold]{user}[/bold]", style="success")
        except Exception:
            console.print(f"   ❌ Not Found: [bold]{user}[/bold]", style="error")
            
    return entities