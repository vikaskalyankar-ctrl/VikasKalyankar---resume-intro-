import time

name = "Vikas Kalyankar"

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


print("\n" + "=" * 50)
print(" " * 14 + "WELCOME")
print("=" * 50)

slow_print("\nHello! My name is...")
time.sleep(0.5)

print()
print("╔" + "═" * 48 + "╗")
print("║" + " " * 12 + "VIKAS KALYANKAR" + " " * 21 + "║")
print("╚" + "═" * 48 + "╝")

print()
slow_print("Learning Python • DSA • Git & GitHub")
slow_print("Building something better every day.")

print("\n" + "=" * 50)
print("              KEEP CODING!")
print("=" * 50)