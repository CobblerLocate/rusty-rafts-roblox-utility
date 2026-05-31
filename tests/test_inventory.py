"""
Unit tests for inventory management.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from rusty_rafts_roblox_utility.inventory import Inventory

def test_add_item():
    inv = Inventory(max_slots=5)
    assert inv.add_item("wood", 10) == True
    assert inv.get_item_count("wood") == 10

def test_remove_item():
    inv = Inventory()
    inv.add_item("metal", 5)
    assert inv.remove_item("metal", 2) == True
    assert inv.get_item_count("metal") == 3

def test_remove_insufficient():
    inv = Inventory()
    inv.add_item("rope", 1)
    assert inv.remove_item("rope", 5) == False

def test_inventory_full():
    inv = Inventory(max_slots=1)
    inv.add_item("wood")
    assert inv.add_item("metal") == False

def test_list_items():
    inv = Inventory()
    inv.add_item("plank", 4)
    inv.add_item("nail", 20)
    items = inv.list_items()
    assert items == {"plank": 4, "nail": 20}