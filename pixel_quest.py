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
    """Displays a large, bold game title logo."""
    banner = f"""{CYAN}{BOLD}
  ██████╗ ██╗██╗  ██╗███████╗██╗     ██████╗  ██████╗ ██╗███████╗████████╗
  ██╔══██╗██║██║  ██║██╔════╝██║    ██╔═══██╗██╔═══██╗██║██╔════╝╚══██╔══╝
  ██████╔╝██║███████║█████╗  ██║    ██║   ██║██║   ██║██║█████╗     ██║   
  ██╔═══╝ ██║██╔══██║██╔══╝  ██║    ██║   ██║██║   ██║██║██╔══╝     ██║   
  ██║     ██║██║  ██║███████╗███████╗╚██████╔╝╚██████╔╝██║███████╗   ██║   
  ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚══════╝   ╚═╝   
{RESET}"""
    print(banner)

def slow_print(text, delay=0.02, color=WHITE):
    """Prints text with a smooth typewriter animation."""
    print(color, end="")
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print(RESET)

def draw_hud(player_name, health, gold, inventory):
    """Draws a spacious, formatted head-up display box."""
    print(f"{YELLOW}╔═════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{YELLOW}║{RESET}  {BOLD}Hero:{RESET} {player_name:<16} | {GREEN}{BOLD}HP:{RESET} {health:<3}/100 | {YELLOW}{BOLD}Gold:{RESET} {gold:<4} | {MAGENTA}{BOLD}Items:{RESET} {len(inventory):<2} {YELLOW}║{RESET}")
    print(f"{YELLOW}╚═════════════════════════════════════════════════════════════════════╝{RESET}\n")

def start_game():
    clear_screen()
    print_banner()
    
    player_name = input(f"{BOLD}Enter your hero's name adventurer:{RESET} ").strip()
    if not player_name:
        player_name = "Valiant Hero"
        
    slow_print(f"\nGreetings, {player_name}! The Kingdom of Bitania needs your courage.", color=CYAN)
    time.sleep(1)

    health = 100
    gold = 10
    inventory = []

    while health > 0:
        clear_screen()
        print_banner()
        draw_hud(player_name, health, gold, inventory)

        print(f"{BOLD}Choose your next move:{RESET}\n")
        print(f"  {GREEN}[1]{RESET} Explore the Whispering Forest")
        print(f"  {YELLOW}[2]{RESET} Visit the Town Merchant")
        print(f"  {MAGENTA}[3]{RESET} View Inventory & Rest")
        print(f"  {RED}[4]{RESET} Abandon Quest (Quit)")
        
        choice = input(f"\n{BOLD}Select an action (1-4):{RESET} ").strip()

        if choice == '1':
            clear_screen()
            print_banner()
            draw_hud(player_name, health, gold, inventory)
            slow_print("You venture deep into the dark, towering woods...\n", color=GREEN)
            time.sleep(1)

            event = random.choice(["monster", "treasure", "mystery"])

            if event == "monster":
                monster_name = random.choice(["Giga Glitch", "Shadow Syntax", "Byte Basilisk"])
                monster_hp = random.randint(40, 70)
                slow_print(f"⚠️  AN ENEMY APPEARS! A wild {RED}{monster_name}{RESET} blocks your path!", color=RED)
                
                while monster_hp > 0 and health > 0:
                    print(f"\n{RED}{monster_name} HP:{RESET} {monster_hp} | {GREEN}Your HP:{RESET} {health}")
                    action = input(f"Will you {BOLD}[f]ight{RESET} or {BOLD}[r]un{RESET}? ").lower().strip()
                    
                    if action == 'f':
                        damage_dealt = random.randint(15, 30)
                        if "Iron Sword" in inventory:
                            damage_dealt += 10
                        
                        monster_hp -= damage_dealt
                        slow_print(f"⚔️  You strike the {monster_name} for {damage_dealt} damage!", color=GREEN)
                        
                        if monster_hp > 0:
                            damage_taken = random.randint(10, 25)
                            health -= damage_taken
                            slow_print(f"💥 The enemy strikes back! You lose {damage_taken} HP.", color=RED)
                    else:
                        slow_print("🏃 You retreat safely back to camp!", color=YELLOW)
                        break

                if monster_hp <= 0:
                    reward = random.randint(20, 50)
                    gold += reward
                    slow_print(f"\n🎉 VICTORY! You defeated the {monster_name} and claimed {reward} gold!", color=YELLOW)
                    
            elif event == "treasure":
                found_gold = random.randint(30, 70)
                gold += found_gold
                slow_print(f"💎 TREASURE! You discovered a chest filled with {found_gold} sparkling gold coins!", color=YELLOW)
            
            else:
                slow_print("🍃 The woods are quiet. You rest near a stream and regain 10 HP.", color=CYAN)
                health = min(100, health + 10)

            input(f"\n{BOLD}Press Enter to continue...{RESET}")

        elif choice == '2':
            clear_screen()
            print_banner()
            draw_hud(player_name, health, gold, inventory)
            print(f"{YELLOW}--- TOWN MARKETPLACE ---{RESET}\n")
            print(f"1. Health Potion (+40 HP) - {CYAN}30 Gold{RESET}")
            print(f"2. Iron Sword (+10 Attack) - {CYAN}60 Gold{RESET}")
            print("3. Leave shop")

            buy = input(f"\n{BOLD}What would you like to buy? (1-3):{RESET} ").strip()
            if buy == '1':
                if gold >= 30:
                    gold -= 30
                    health = min(100, health + 40)
                    slow_print("🧪 You drank the Potion. Health restored!", color=GREEN)
                else:
                    slow_print("❌ Not enough gold!", color=RED)
            elif buy == '2':
                if gold >= 60:
                    if "Iron Sword" not in inventory:
                        gold -= 60
                        inventory.append("Iron Sword")
                        slow_print("⚔️ You equipped the Iron Sword!", color=GREEN)
                    else:
                        slow_print("You already own an Iron Sword!", color=YELLOW)
                else:
                    slow_print("❌ Not enough gold!", color=RED)
            
            input(f"\n{BOLD}Press Enter to return...{RESET}")

        elif choice == '3':
            clear_screen()
            print_banner()
            draw_hud(player_name, health, gold, inventory)
            print(f"{MAGENTA}--- INVENTORY ---{RESET}")
            if inventory:
                for item in inventory:
                    print(f"• {item}")
            else:
                print("Your bag is empty.")
            input(f"\n{BOLD}Press Enter to continue...{RESET}")

        elif choice == '4':
            slow_print(f"\nFarewell, {player_name}! Your legend remains written in code.", color=CYAN)
            break

        if health <= 0:
            clear_screen()
            print_banner()
            slow_print(f"\n☠️ GAME OVER! {player_name} has fallen in battle...", color=RED)
            break

if __name__ == "__main__":
    start_game()
