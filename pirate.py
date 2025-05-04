"""
Detect pirate !
===============================

Author: Chyngyz Mirzamatov
Created on: Sunday, May 5 2025
Last updated on: Sunday, May 5 2025

Program that  ask user for password. If it's pirate go away if now greet him
"""
greeting = input("Hello, possible pirate! What's the password?")
                      
if greeting in ("Arrr!"):
	print("Go away, pirate.")
else:
	print("Greetings, hater of pirates!")
