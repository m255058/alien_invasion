WIDTH = 500
HEIGHT = 300
ship_speed = 4

ship = Actor('ship')
ship.pos = 0,HEIGHT/2
bullet_timer_limit = 0.5
bullet_radius = 5
bullets = []
bullet_timer = bullet_timer_limit

def draw():
    screen.fill((150,0,255))
    ship.draw()
    for bullet in bullets:
                screen.draw.filled_circle((bullet['x'] + offset_x, bullet['y'] + offset_y), bullet_radius, color=(0, 0, 0))

def update():
    check_events()
    update_bullets()

def check_events():
    '''checks for the specific keyboard events'''
    if keyboard.UP and ship.top > 0:
        ship.y -= int(ship_speed)
    if keyboard.DOWN and ship.bottom < HEIGHT:
        ship.y += int(ship_speed)
    if keyboard.SPACE:
        if bullet_timer >= bullet_timer_limit:
            bullet_timer = 0
            bullets.append({
                'x': ship_x + math.cos(ship_angle) * ship_radius,
                'y': ship_y + math.sin(ship_angle) * ship_radius,
                'angle': ship_angle,
                'time_left': 4,})

def update_bullets():
    global bullet_timer
    for bullet in bullets.copy():
        bullet['time_left'] -= dt

        if bullet['time_left'] <= 0:
            bullets.remove(bullet)
            continue
        bullet_speed = 500
        bullet['x'] += math.cos(bullet['angle']) * bullet_speed * dt
        bullet['y'] += math.sin(bullet['angle']) * bullet_speed * dt
        bullet['x'] %= arena_width
        bullet['y'] %= arena_height
    bullet_timer += dt
