import random

username = "userplayer"
pw = "passplayer"
player_score = 0
enemy_score = 0

print("Game Gunting kertas Batu")
print("sebelum memainkan game harap login terlebih dahulu !")

while True:
    userin = str(input("Masukan Username : "))
    pwin = str(input("masukan password : "))
    if userin != username or pwin != pw:
        print("Username/Password Salah, Coba lagi")
    else:
        break

print("==================================")
print("    GAME GUNTING KERTAS BATU   ")
print("==================================")

while player_score != 3 or enemy_score != 3:
    print("Skor Kamu : ", player_score, " Skor musuh : ", enemy_score)
    player = input("Masukan Pilihan (g/k/b) : ")
    enemy_choice = random.randint(1, 30)

    if enemy_choice <= 10:
        print("Musuh memilih gunting !")
        match player:
            case "g":
                print("seri")
            case "k":
                print("kamu kalah !")
                enemy_score += 1
            case "b":
                print("kamu menang !")
                player_score += 1

    elif enemy_choice <= 20:
        print("Musuh memilih Batu !")
        match player:
            case "g":
                print("kamu kalah !")
                enemy_score += 1
            case "k":
                print("kamu menang !")
                player_score += 1
            case "b":
                print("seri")

    else:
        print("Musuh memilih kertas !")
        match player:
            case "g":
                print("kamu menang !")
                player_score += 1
            case "k":
                print("seri")
            case "b":
                print("kamu kalah !")
                enemy_score += 1
   
if player_score == 3:
    print("==================================")
    print("      Kamu memenangkan game  ")
    print("==================================")
else:
    print("==================================")
    print("      Kamu KALAH SAMA BOT :v    ")
    print("==================================")