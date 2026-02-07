import time
import random
from telethon import functions, types, utils
from telethon.errors import FloodWaitError, PeerFloodError
from config import console

def process_group(client, title, prefs, targets):
    # Handles Create, Invite, Mute, Archive, Message for one group.
    try:
        # 1. CREATE
        result = client(functions.channels.CreateChannelRequest(
            title=title,
            about="Archive",
            megagroup=True
        ))
        chat = result.chats[0]
        peer = utils.get_input_peer(chat)
        console.print(f"   ✅ Created (ID: {chat.id})", style="success")
        
        time.sleep(random.uniform(1.5, 2.5))

        # 2. MUTE
        if prefs['mute']:
            client(functions.account.UpdateNotifySettingsRequest(
                peer=peer,
                settings=types.InputPeerNotifySettings(mute_until=2147483647, silent=True)
            ))
            console.print("   🔕 Muted", style="warning")

        time.sleep(random.uniform(1.5, 2.5))

        # 3. INVITE
        if targets:
            try:
                client(functions.channels.InviteToChannelRequest(peer, targets))
                console.print(f"   👤 Invited {len(targets)} users", style="success")
            except Exception as e:
                console.print(f"   ⚠️ Invite Error: {str(e)[:30]}", style="warning")

        time.sleep(random.uniform(1.5, 2.5))

        # 5. MESSAGE
        if prefs['message']:
            text = prefs['message'] if prefs['message'] else title
            client.send_message(peer, text)
            console.print("   💬 Message Sent", style="success")

        time.sleep(random.uniform(1.5, 2.5))

        # 4. ARCHIVE
        if prefs['archive']:
            client(functions.folders.EditPeerFoldersRequest(
                folder_peers=[types.InputFolderPeer(peer=peer, folder_id=1)]
            ))
            console.print("   📂 Archived", style="warning")

        return True

    except FloodWaitError as e:
        console.print(f"\n🛑 FLOOD WAIT: Sleeping {e.seconds}s", style="error")
        time.sleep(e.seconds)
        return False
    except PeerFloodError:
        console.print("\n💀 CRITICAL: Account Limited (PeerFlood)", style="error")
        raise
    except Exception as e:
        console.print(f"   ❌ Unexpected Error: {e}", style="error")
        return False
    