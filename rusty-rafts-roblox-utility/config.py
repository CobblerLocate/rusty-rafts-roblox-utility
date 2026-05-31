"""
Configuration defaults for Rusty Rafts Roblox game mechanics.
"""
from dataclasses import dataclass

@dataclass
class RaftConfig:
    max_raft_parts: int = 12
    max_inventory_slots: int = 20
    water_density: float = 1000.0
    gravity: float = 9.81
    base_sail_force: float = 150.0
    repair_cost_wood: int = 3
    repair_cost_metal: int = 1

    @classmethod
    def default(cls) -> "RaftConfig":
        return cls()

    def __post_init__(self):
        assert self.max_raft_parts > 0, "max_raft_parts must be positive"
        assert self.water_density > 0, "water_density must be positive"