import pytest
import pygame
from project import move_player, update_score, check_collision, reset_game

def test_move_player():
    # Inicjalizacja obiektów
    player = pygame.Rect(100, 100, 50, 50)
    keys = {pygame.K_LEFT: True, pygame.K_RIGHT: False}
    level = 1  # Dodajemy level jako argument
    move_player(player, keys, level)  # Przekazujemy level
    assert player.x < 100  # Sprawdzamy, czy gracz przesunął się w lewo

def test_update_score():
    # Inicjalizacja zmiennych
    score = 14  # Zaczynamy od 14, aby po jednej aktualizacji poziom wzrósł
    level = 1
    obstacle_speed = 5
    spawn_rate = 30

    # Zaktualizowanie wyniku
    score, level, obstacle_speed, spawn_rate = update_score(score, level, obstacle_speed, spawn_rate)

    # Sprawdzamy, czy wynik wzrósł
    assert score > 0
    assert level > 1  # Po zaktualizowaniu poziomu

def test_check_collision():
    # Sprawdzamy, czy wykrywa kolizję
    player = pygame.Rect(100, 100, 50, 50)
    obstacle = pygame.Rect(100, 100, 50, 50)
    assert check_collision(player, [obstacle]) == True
