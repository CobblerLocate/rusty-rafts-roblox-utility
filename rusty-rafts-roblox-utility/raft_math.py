"""
Mathematical utilities for raft physics calculations.
"""
import math

def calculate_buoyancy(submerged_volume: float, water_density: float = 1000.0, gravity: float = 9.81) -> float:
    """Calculate buoyant force (Newtons) based on submerged volume (m^3)."""
    return submerged_volume * water_density * gravity

def calculate_raft_speed(wind_force: float, mass: float, drag_coefficient: float = 0.47) -> float:
    """Estimate raft speed (m/s) given wind force (N), mass (kg), and drag."""
    if mass <= 0:
        return 0.0
    net_force = wind_force - (drag_coefficient * mass * 9.81 * 0.02)
    if net_force <= 0:
        return 0.0
    return math.sqrt((2 * net_force) / (mass * 1.225 * 0.5))

def clamp_rotation(angle: float, limit: float = 30.0) -> float:
    """Clamp rotation angle (degrees) to prevent raft tipping beyond limit."""
    return max(-limit, min(limit, angle))