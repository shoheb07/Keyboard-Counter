import keyboard

count = 0

print("Press any key... Press 'esc' to stop.")

while True:
    event = keyboard.read_event()
    
    if event.event_type == keyboard.KEY_DOWN:
        count += 1
        print(f"Key pressed: {event.name} | Total count: {count}")
    
    if event.name == 'esc':
        print("\nStopped!")
        print(f"Total key presses: {count}")
        break
