import pygame # type: ignore
import sys
import webbrowser
import os
import time


def show_version_info():
    # Create a new "About" surface
    DISTRO_NAME = "disto_name" # Replace With Disto Name
    about_width, about_height = 400, 200
    about_screen = pygame.Surface((about_width, about_height))
    about_screen.fill((255, 255, 255))  # Set white background

    # Add text
    font = pygame.font.Font(None, 36)
    title = font.render("About TS-DESKTOP and Distro", True, (0, 0, 0))  # Black text
    version = font.render(f"TS-DESKTOP: 1.0.0 TS-DISTRO: {DISTRO_NAME}", True, (0, 0, 0))

    # Draw text onto the About screen
    about_screen.blit(title, (50, 50))
    about_screen.blit(version, (50, 100))
    font = pygame.font.Font(None, 36)
    test_text_version = font.render("version_number", True, (0, 0, 0))  # Replace "version_name" With Version number
    about_screen.blit(test_text_version, (50, 150))  # Correct placement

    # Display the About screen over the main GUI
    running_about = True
    while running_about:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
                running_about = False  # Exit when the user presses ENTER or closes the window
        pygame.display.set_caption("About TS-DOS/TS-GUI")  # Change the window caption

        # Render the "About" window as an overlay
        screen = pygame.display.get_surface()  # Get the existing main screen
        screen.blit(about_screen, (200, 150))  # Center the "About" window on the screen
        pygame.display.flip()  # Update the display
        if not running_about:
            pygame.display.set_caption("TS-GUI TEST 1.0.0 LANPACK ENG")  # Reset the window caption




print("If You're In The \"About TS-DESKTOP/TS-DISTO Distro\" Tab Click The Windows Key and Clcik The Python Icon And Click The x And You Be Back to The Desktop!")
time.sleep(1)

pygame.init()

# Screen setup
screen_width, screen_height = 1920, 1080  # Example resolution for TS-DESKTOP
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TS-DESKTOP 1.0.0 For TS-KERNEL 1.0.1pa2")

# Define colors
WHITE = (255, 255, 255)
BLUE = (70, 130, 180)
DARK_BLUE = (0, 102, 153)
BLACK = (0, 0, 0)

# Button dimensions and positions
button_width, button_height = 150, 40
taskbar_height = 50
start_button_x = 10
start_button_y = screen_height - taskbar_height + 5  # Positioned on taskbar

# Font setup
font = pygame.font.Font(None, 32)

# Start button text
start_button_text = font.render("Start", True, WHITE)

# Example App Buttons
app_button_width, app_button_height = 500, 60
app_buttons = [
    {"label": "Browser", "x": 190, "y": 100},
    {"label": "File Manager", "x": 190, "y": 180},
    {"label": "Settings", "x": 190, "y": 260},
    {"label": "About TS-DESKTOP/TS-DISTRO Distro", "x": 190, "y": 340},
    {"label": "Exit TS-DESKTOP", "x": 190, "y": 420}
]

# Draw buttons helper
def draw_button(label, x, y, is_hovered):
    color = DARK_BLUE if is_hovered else BLUE
    pygame.draw.rect(screen, color, (x, y, app_button_width, app_button_height))
    text = font.render(label, True, WHITE)
    screen.blit(text, (x + (app_button_width - text.get_width()) // 2, y + (app_button_height - text.get_height()) // 2))

# Main loop
running = True
while running:
    screen.fill(WHITE)  # Clear the screen with white background
    pygame.draw.rect(screen, BLACK, (0, screen_height - taskbar_height, screen_width, taskbar_height))  # Taskbar background
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit the desktop environment
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Handle clicks
            # Check for Start button clicks
            if start_button_x <= mouse_x <= start_button_x + button_width and start_button_y <= mouse_y <= start_button_y + button_height:
                print("Start Menu Opened!")
                print("Available Apps:")
                for app in app_buttons:
                    print(f"- {app['label']}")

            # Check for clicks on app buttons
            for app in app_buttons:
                if app["x"] <= mouse_x <= app["x"] + app_button_width and app["y"] <= mouse_y <= app["y"] + app_button_height:
                    print(f"{app['label']} Button Clicked!")
                    if app["label"] == "Exit TS-DESKTOP":
                        print("Exiting TS-DESKTOP...")
                        pygame.quit()
                        sys.exit()
                    elif app["label"] == "Browser":
                        print("Opening Browser...")
                        webbrowser.open("https://www.google.com")
                    elif app["label"] == "File Manager":
                        print("Launching File Manager...")
                        os.system("start explorer.exe")
                    elif app["label"] == "Settings":
                        print("Opening Settings...")
                        os.system("cd C:\\Windows\\ImmersiveControlPanel")
                        os.system("SystemSettings.exe")

                    elif app["label"] == "About TS-DESKTOP/TS-DISTRO Distro":
                        show_version_info()

    # Draw the Start button with hover effect
    if start_button_x <= mouse_x <= start_button_x + button_width and start_button_y <= mouse_y <= start_button_y + button_height:
        pygame.draw.rect(screen, DARK_BLUE, (start_button_x, start_button_y, button_width, button_height))
    else:
        pygame.draw.rect(screen, BLUE, (start_button_x, start_button_y, button_width, button_height))
    screen.blit(start_button_text, (start_button_x + (button_width - start_button_text.get_width()) // 2,
                                    start_button_y + (button_height - start_button_text.get_height()) // 2))

    # Draw app buttons
    for app in app_buttons:
        is_hovered = app["x"] <= mouse_x <= app["x"] + app_button_width and app["y"] <= mouse_y <= app["y"] + app_button_height
        draw_button(app["label"], app["x"], app["y"], is_hovered)

    # Update display
    pygame.display.flip()

# Quit Pygame when the main loop ends
pygame.quit()
sys.exit()
