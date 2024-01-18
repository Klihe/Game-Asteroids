def check_collision(self, other_spirit, time) -> None:
        if self.hit_detection_cooldown < time - self.last_hit:
            if self.rect.colliderect(other_spirit.rect):
                self.last_hit = time
                self.health -= other_spirit.damage
                other_spirit.health -= self.body_damage
                self.image = pygame.image.load("source/playing/rocket_hit.png")
            else:
                self.image = pygame.image.load("source/playing/rocket.png")