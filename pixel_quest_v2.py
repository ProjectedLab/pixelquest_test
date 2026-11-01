import random
import sys
import time

# --- Color Constants (ANSI Codes) ---
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"

def clear_screen():
    """Clears the terminal screen for a clean UI transition."""
    print("\033[H\033[J", end="")

def print_banner():
    """Displays a large game title logo."""
    banner = f"""{CYAN}{BOLD}
  ██████╗ ██╗██╗  ██╗███████╗██╗     ██████╗  ██████╗ ██╗███████╗████████╗
  ██╔══██╗██║██║  ██║██╔════╝██║    ██╔═══██╗██╔═══██╗██║██╔════╝╚══██╔══╝
  ██████╔╝██║███████║█████╗  ██║    ██║   ██║██║   ██║██║█████╗     ██║   
  ██╔═══╝ ██║██╔══██║██╔══╝  ██║    ██║   ██║██║   ██║██║██╔══╝     ██║   
  ██║     ██║██║  ██║███████╗███████╗╚██████╔╝╚██████╔╝██║███████╗   ██║   
  ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚══════╝   ╚═╝   
{RESET}"""
    print(banner)

def slow_print(text, delay=0.015, color=WHITE):
    """Prints text with a smooth typewriter animation."""
    print(color, end="")
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print(RESET)

def draw_hud(player_name, health, max_health, gold, level, xp, xp_to_level, inventory):
    """Draws a spacious, formatted head-up display box."""
    print(f"{YELLOW}╔═════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{YELLOW}║{RESET}  {BOLD}Hero:{RESET} {player_name:<12} | {GREEN}{BOLD}HP:{RESET} {health}/{max_health:<3} | {YELLOW}{BOLD}Gold:{RESET} {gold:<3} | {MAGENTA}{BOLD}Lvl:{RESET} {level} ({xp}/{xp_to_level}) {YELLOW}║{RESET}")
    print(f"{YELLOW}╚═════════════════════════════════════════════════════════════════════╝{RESET}\n")

def check_level_up(level, xp, xp_to_level, max_health):
    """Handles leveling up logic."""
    if xp >= xp_to_level:
        level += 1
        xp -= xp_to_level
        xp_to_level = int(xp_to_level * 1.5)
        max_health += 25
        slow_print(f"\n✨ LEVEL UP! You reached Level {level}! Max HP increased to {max_health}!", color=YELLOW)
        time.sleep(1.5)
        return level, xp, xp_to_level, max_health
    return level, xp, xp_to_level, max_health

def start_game():
    clear_screen()
    print_banner()
    
    player_name = input(f"{BOLD}Enter your hero's name adventurer:{RESET} ").strip()
    if not player_name:
        player_name = "Valiant Hero"
        
    slow_print(f"\nGreetings, {player_name}! The Kingdom of Bitania is under threat from the corrupt Lord Null.", color=CYAN)
    slow_print("Grow strong, gather gear, and defeat Lord Null in his Spire to save the realm!", color=CYAN)
    time.sleep(2)

    # Player Stats
    max_health = 100
    health = 100
    gold = 20
    level = 1
    xp = 0
    xp_to_level = 50
    inventory = []

    while health > 0:
        clear_screen()
        print_banner()
        draw_hud(player_name, health, max_health, gold, level, xp, xp_to_level, inventory)

        print(f"{BOLD}Choose where to travel:{RESET}\n")
        print(f"  {GREEN}[1]{RESET} Explore the Whispering Forest (Level 1+)")
        print(f"  {MAGENTA}[2]{RESET} Venture into the Cursed Crypt (Level 2+)")
        print(f"  {RED}[3]{RESET} Assault Lord Null's Spire (Final Boss - Level 3+)")
        print(f"  {YELLOW}[4]{RESET} Visit Town Marketplace")
        print(f"  {CYAN}[5]{RESET} Check Inventory & Status")
        print(f"  {WHITE}[6]{RESET} Quit Game")
        
        choice = input(f"\n{BOLD}Select an action (1-6):{RESET} ").strip()

        # --- 1. WHISPERING FOREST ---
        if choice == '1':
            clear_screen()
            print_banner()
            draw_hud(player_name, health, max_health, gold, level, xp, xp_to_level, inventory)
            slow_print("You walk among the tall, humming trees of the Whispering Forest...\n", color=GREEN)
            time.sleep(1)

            event = random.choice(["monster", "treasure", "fountain"])

            if event == "monster":
                monster_name = random.choice(["Glitch Goblin", "Byte Bandit", "Syntax Spider"])
                monster_hp = random.randint(30, 50)
                monster_max_hp = monster_hp
                monster_attack = random.randint(8, 15)
                
                slow_print(f"⚠️ A wild {RED}{monster_name}{RESET} ambushes you!", color=RED)
                
                while monster_hp > 0 and health > 0:
                    print(f"\n{RED}{monster_name} HP:{RESET} {monster_hp}/{monster_max_hp} | {GREEN}Your HP:{RESET} {health}/{max_health}")
                    action = input(f"Will you {BOLD}[f]ight{RESET} or {BOLD}[r]un{RESET}? ").lower().strip()
                    
                    if action == 'f':
                        damage_dealt = random.randint(12, 22) + (level * 3)
                        if "Iron Sword" in inventory:
                            damage_dealt += 8
                        if "Flame Blade" in inventory:
                            damage_dealt += 18
                        
                        monster_hp -= damage_dealt
                        slow_print(f"⚔️ You strike the {monster_name} for {damage_dealt} damage!", color=GREEN)
                        
                        if monster_hp > 0:
                            health -= monster_attack
                            slow_print(f"💥 The {monster_name} hits you back for {monster_attack} damage!", color=RED)
                    else:
                        slow_print("🏃 You successfully escaped back to safety!", color=YELLOW)
                        break

                if monster_hp <= 0:
                    reward_gold = random.randint(15, 30)
                    reward_xp = 25
                    gold += reward_gold
                    xp += reward_xp
                    slow_print(f"\n🎉 VICTORY! Gained {reward_gold} gold and {reward_xp} XP!", color=YELLOW)
                    level, xp, xp_to_level, max_health = check_level_up(level, xp, xp_to_level, max_health)
                    
            elif event == "treasure":
                found_gold = random.randint(20, 45)
                gold += found_gold
                slow_print(f"💎 You discovered a hidden stash with {found_gold} gold coins!", color=YELLOW)
            
            else:
                slow_print("⛲ You find a glowing mystic spring. Your health is fully refreshed!", color=CYAN)
                health = max_health

            input(f"\n{BOLD}Press Enter to continue...{RESET}")

        # --- 2. CURSED CRYPT ---
        elif choice == '2':
            if level < 2:
                slow_print("⚠️ You are too inexperienced! Reach Level 2 before entering the Cursed Crypt.", color=RED)
                input(f"\n{BOLD}Press Enter to continue...{RESET}")
                continue

            clear_screen()
            print_banner()
            draw_hud(player_name, health, max_health, gold, level, xp, xp_to_level, inventory)
            slow_print("Cold stone walls echo with ghostly whispers as you enter the Crypt...\n", color=MAGENTA)
            time.sleep(1)

            event = random.choice(["monster", "treasure", "trap"])

            if event == "monster":
                monster_name = random.choice(["Skeleton Knight", "Crypt Wraith", "Zombie Coder"])
                monster_hp = random.randint(60, 90)
                monster_max_hp = monster_hp
                monster_attack = random.randint(15, 25)
                
                slow_print(f"⚠️ A terrifying {RED}{monster_name}{RESET} rises from the tombs!", color=RED)
                
                while monster_hp > 0 and health > 0:
                    print(f"\n{RED}{monster_name} HP:{RESET} {monster_hp}/{monster_max_hp} | {GREEN}Your HP:{RESET} {health}/{max_health}")
                    action = input(f"Will you {BOLD}[f]ight{RESET} or {BOLD}[r]un{RESET}? ").lower().strip()
                    
                    if action == 'f':
                        damage_dealt = random.randint(18, 30) + (level * 4)
                        if "Iron Sword" in inventory:
                            damage_dealt += 8
                        if "Flame Blade" in inventory:
                            damage_dealt += 18
                        
                        monster_hp -= damage_dealt
                        slow_print(f"⚔️ You slice through the {monster_name} for {damage_dealt} damage!", color=GREEN)
                        
                        if monster_hp > 0:
                            health -= monster_attack
                            slow_print(f"💥 The undead foe strikes for {monster_attack} damage!", color=RED)
                    else:
                        slow_print("🏃 You retreat from the crypt!", color=YELLOW)
                        break

                if monster_hp <= 0:
                    reward_gold = random.randint(40, 70)
                    reward_xp = 50
                    gold += reward_gold
                    xp += reward_xp
                    slow_print(f"\n🎉 VICTORY! Gained {reward_gold} gold and {reward_xp} XP!", color=YELLOW)
                    level, xp, xp_to_level, max_health = check_level_up(level, xp, xp_to_level, max_health)

            elif event == "treasure":
                found_gold = random.randint(50, 100)
                gold += found_gold
                slow_print(f"💰 You loot an ancient sarcophagus containing {found_gold} gold coins!", color=YELLOW)
            
            else:
                trap_damage = 20
                health -= trap_damage
                slow_print(f"⚡ Watch out! You triggered a pressure plate trap and took {trap_damage} damage.", color=RED)

            input(f"\n{BOLD}Press Enter to continue...{RESET}")

        # --- 3. LORD NULL'S SPIRE (BOSS) ---
        elif choice == '3':
            if level < 3:
                slow_print("⚠️ Lord Null's barrier is too strong! You must reach Level 3 first.", color=RED)
                input(f"\n{BOLD}Press Enter to continue...{RESET}")
                continue

            clear_screen()
            print_banner()
            slow_print("You climb the spiraling obsidian steps of Lord Null's citadel...", color=RED)
            time.sleep(1)
            slow_print("Lord Null turns around, eyes glowing with corrupted data streams!\n", color=RED)
            
            boss_hp = 180
            boss_max_hp = 180
            
            while boss_hp > 0 and health > 0:
                print(f"\n{RED}LORD NULL HP:{RESET} {boss_hp}/{boss_max_hp} | {GREEN}Your HP:{RESET} {health}/{max_health}")
                action = input(f"Will you {BOLD}[f]ight{RESET} or {BOLD}[r]un{RESET}? ").lower().strip()
                
                if action == 'f':
                    damage_dealt = random.randint(25, 40) + (level * 5)
                    if "Flame Blade" in inventory:
                        damage_dealt += 20
                    elif "Iron Sword" in inventory:
                        damage_dealt += 10
                        
                    boss_hp -= damage_dealt
                    slow_print(f"🔥 You land a massive blow on Lord Null for {damage_dealt} damage!", color=GREEN)
                    
                    if boss_hp > 0:
                        boss_damage = random.randint(20, 35)
                        health -= boss_damage
                        slow_print(f"⚡ Lord Null unleashes a dark firewall pulse for {boss_damage} damage!", color=RED)
                else:
                    slow_print("You cannot run from the final battle!", color=YELLOW)
            
            if boss_hp <= 0:
                clear_screen()
                print_banner()
                slow_print(f"\n🏆 LEGENDARY VICTORY! {player_name} has defeated Lord Null and saved Bitania!", color=YELLOW)
                slow_print("Thank you for playing Pixel Quest!", color=CYAN)
                break
            
            input(f"\n{BOLD}Press Enter to continue...{RESET}")

        # --- 4. MARKETPLACE ---
        elif choice == '4':
            clear_screen()
            print_banner()
            draw_hud(player_name, health, max_health, gold, level, xp, xp_to_level, inventory)
            print(f"{YELLOW}--- TOWN MARKETPLACE ---{RESET}\n")
            print(f"1. Health Potion (+50 HP) - {CYAN}35 Gold{RESET}")
            print(f"2. Iron Sword (+8 Attack) - {CYAN}70 Gold{RESET}")
            print(f"3. Flame Blade (+18 Attack) - {CYAN}150 Gold{RESET}")
            print("4. Leave shop")

            buy = input(f"\n{BOLD}What would you like to buy? (1-4):{RESET} ").strip()
            if buy == '1':
                if gold >= 35:
                    gold -= 35
                    health = min(max_health, health + 50)
                    slow_print("🧪 You drank the Potion. Health restored!", color=GREEN)
                else:
                    slow_print("❌ Not enough gold!", color=RED)
            elif buy == '2':
                if gold >= 70:
                    if "Iron Sword" not in inventory and "Flame Blade" not in inventory:
                        gold -= 70
                        inventory.append("Iron Sword")
                        slow_print("⚔️ You equipped the Iron Sword!", color=GREEN)
                    else:
                        slow_print("You already own a better or equal weapon!", color=YELLOW)
                else:
                    slow_print("❌ Not enough gold!", color=RED)
            elif buy == '3':
                if gold >= 150:
                    if "Flame Blade" not in inventory:
                        gold -= 150
                        if "Iron Sword" in inventory:
                            inventory.remove("Iron Sword")
                        inventory.append("Flame Blade")
                        slow_print("🔥 You equipped the legendary Flame Blade!", color=GREEN)
                    else:
                        slow_print("You already own the Flame Blade!", color=YELLOW)
                else:
                    slow_print("❌ Not enough gold!", color=RED)
            
            input(f"\n{BOLD}Press Return to town...{RESET}")

        # --- 5. INVENTORY ---
        elif choice == '5':
            clear_screen()
            print_banner()
            draw_hud(player_name, health, max_health, gold, level, xp, xp_to_level, inventory)
            print(f"{MAGENTA}--- INVENTORY & STATUS ---{RESET}")
            print(f"Hero Name: {player_name}")
            print(f"Level: {level} (XP: {xp}/{xp_to_level})")
            print(f"Gold: {gold}")
            print("\nEquipped Items:")
            if inventory:
                for item in inventory:
                    print(f"• {item}")
            else:
                print("• None")
            input(f"\n{BOLD}Press Enter to continue...{RESET}")

        # --- 6. QUIT ---
        elif choice == '6':
            slow_print(f"\nFarewell, {player_name}! Your adventure pauses here.", color=CYAN)
            break

        if health <= 0:
            clear_screen()
            print_banner()
            slow_print(f"\n☠️ GAME OVER! {player_name} has fallen in battle...", color=RED)
            break

if __name__ == "__main__":
    start_game()
