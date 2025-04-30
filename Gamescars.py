import pygame
import random
import time

# Inisialisasi Pygame
pygame.init()

# Warna
HITAM = (0, 0, 0)
PUTIH = (255, 255, 255)
HIJAU = (0, 255, 0)
MERAH = (255, 0, 0)
BIRU = (0, 0, 255)

# Ukuran layar
LEBAR = 800
TINGGI = 600
ukuran_layar = (LEBAR, TINGGI)
layar = pygame.display.set_mode(ukuran_layar)
pygame.display.set_caption("Game Balapan")

# Clock untuk mengatur FPS
clock = pygame.time.Clock()

# Gambar latar belakang (bisa diganti dengan gambar jalan)
background = pygame.Surface(layar.get_size())
background.fill(HIJAU)
# Gambar garis jalan
pygame.draw.rect(background, HITAM, (LEBAR//2 - 100, 0, 200, TINGGI))
pygame.draw.rect(background, PUTIH, (LEBAR//2 - 95, 0, 190, TINGGI))
for i in range(0, TINGGI, 40):
    pygame.draw.rect(background, HITAM, (LEBAR//2 - 5, i, 10, 20))

class Mobil(pygame.sprite.Sprite):
    def __init__(self, warna, x, y):
        super().__init__()
        self.image = pygame.Surface([50, 80])
        self.image.fill(warna)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 0
        
    def update(self):
        self.rect.y += self.speed
        # Batasi mobil tidak keluar layar
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > TINGGI - 80:
            self.rect.y = TINGGI - 80

class Musuh(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 80])
        self.image.fill(MERAH)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(LEBAR//2 - 80, LEBAR//2 + 30)
        self.rect.y = -100
        self.speed = random.randrange(3, 8)
        
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > TINGGI:
            self.rect.y = -100
            self.rect.x = random.randrange(LEBAR//2 - 80, LEBAR//2 + 30)
            self.speed = random.randrange(3, 8)

# Buat grup sprite
semua_sprite = pygame.sprite.Group()
musuh_group = pygame.sprite.Group()

# Buat mobil pemain
mobil_pemain = Mobil(BIRU, LEBAR//2 - 25, TINGGI - 100)
semua_sprite.add(mobil_pemain)

# Buat musuh
for i in range(5):
    m = Musuh()
    semua_sprite.add(m)
    musuh_group.add(m)

# Variabel game
skor = 0
game_over = False
font = pygame.font.SysFont('Arial', 30)

# Loop game
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    mobil_pemain.speed = -5
                if event.key == pygame.K_DOWN:
                    mobil_pemain.speed = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    mobil_pemain.speed = 0
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Reset game
                    game_over = False
                    skor = 0
                    mobil_pemain.rect.y = TINGGI - 100
                    for m in musuh_group:
                        m.rect.y = -100
                        m.rect.x = random.randrange(LEBAR//2 - 80, LEBAR//2 + 30)
    
    if not game_over:
        # Update
        semua_sprite.update()
        
        # Cek tabrakan
        if pygame.sprite.spritecollide(mobil_pemain, musuh_group, False):
            game_over = True
        
        # Tambah skor
        skor += 0.1
    
    # Render
    layar.blit(background, (0, 0))
    semua_sprite.draw(layar)
    
    # Tampilkan skor
    text = font.render(f"Skor: {int(skor)}", True, PUTIH)
    layar.blit(text, (10, 10))
    
    if game_over:
        text = font.render("GAME OVER! Tekan R untuk restart", True, PUTIH)
        layar.blit(text, (LEBAR//2 - 180, TINGGI//2))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
