from gameObject import GameObject


class Entity(GameObject):
    health: int
    maxHealth: int
    speed: int

    def __init__(
        self,
        x,
        y,
        sprite,
        state,
        animation,
        animatedTime,
        animationFrame,
        health,
        maxHealth,
        attack,
        defense,
        speed,
        level,
        experience,
        nextLevelExp,
    ):
        super().__init__(x, y, sprite, state, animation, animatedTime, animationFrame)
        self.health = health
        self.maxHealth = maxHealth
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.level = level
        self.experience = experience
        self.nextLevelExp = nextLevelExp

    @classmethod
    def from_json(filePath: str):
        data = None
        with open(filePath, "r") as file:
            data = json.load(file)
        return Entity(
            float(data["x"]),
            float(data["y"]),
            pygame.image.load(data["sprite"]),
            "",
            data["animation"],
            pygame.time.get_ticks(),
            0,
            data["health"],
            data["maxHealth"],
            data["attack"],
            data["defense"],
            data["speed"],
            data["level"],
            data["experience"],
            data["nextLevelExp"],
        )
