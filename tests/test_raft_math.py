"""
Unit tests for raft math utilities.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from rusty_rafts_roblox_utility.raft_math import (
    calculate_buoyancy,
    calculate_raft_speed,
    clamp_rotation
)

def test_calculate_buoyancy():
    # 1 cubic meter submerged in water -> ~9810 N
    result = calculate_buoyancy(1.0)
    assert abs(result - 9810.0) < 0.1, f"Expected ~9810, got {result}"

def test_calculate_raft_speed_no_wind():
    speed = calculate_raft_speed(0.0, 100.0)
    assert speed == 0.0, "No wind should give zero speed"

def test_calculate_raft_speed_positive():
    speed = calculate_raft_speed(500.0, 100.0)
    assert speed > 0.0, "Wind should produce positive speed"

def test_clamp_rotation_within_limit():
    assert clamp_rotation(15.0) == 15.0

def test_clamp_rotation_exceeds_limit():
    assert clamp_rotation(45.0) == 30.0
    assert clamp_rotation(-45.0) == -30.0

def test_clamp_rotation_zero():
    assert clamp_rotation(0.0) == 0.0