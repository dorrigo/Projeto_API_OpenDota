import requests
import pandas as pd

url = "https://api.opendota.com/api/heroStats?patch=7.39"
heroes_data = requests.get(url).json()

# Calcula o win rate para cada herói no patch 7.39
for hero in heroes_data:
    id = hero["id"]
    picks = hero.get("pro_pick", 0)
    wins = hero.get("pro_win", 0)
    roles = hero.get("roles", [])
    hero["win_rate"] = (wins / picks * 100) if picks > 0 else 0

# Função para obter o win rate de um herói
def get_win_rate(hero):
    return hero["win_rate"]

# Ordena os heróis pelo win rate
sorted_heroes = sorted(heroes_data, key=get_win_rate, reverse=True)

# Cria um DataFrame para melhor visualização dos 10 melhores
heroes_df = pd.DataFrame(sorted_heroes, columns=["localized_name", "win_rate", "roles"])

# Renomeia as colunas para algo mais amigável
heroes_df.columns = ["Hero", "Win Rate","Roles"]

# Formata o win rate para duas casas decimais
heroes_df["Win Rate"] = heroes_df["Win Rate"].apply(lambda x: float(f"{x:.2f}"))

# Define o DataFrame
heroes_win_rate = heroes_df

########################################################################################

# Calcula a quantidade vezes banido para cada herói no patch 7.39
for hero in heroes_data:
    hero_name = hero.get("localized_name")
    bans = hero.get("pro_ban", 0)
    roles = hero.get("roles", [])
    hero["ban_count"] = bans

# Cria um DataFrame para os heróis banidos      
ban_heroes_df = pd.DataFrame(heroes_data, columns=["localized_name", "ban_count","roles"])

# Renomeia as colunas para algo mais amigável   
ban_heroes_df.columns = ["Hero", "Ban Count", "Roles"]

# Ordena os heróis pelo número de bans
ban_heroes_df = ban_heroes_df.sort_values(by="Ban Count", ascending=False)

# Exibe o DataFrame
heroes_ban_count = ban_heroes_df

########################################################################################

# Calcula a quantidade de vezes que cada herói foi escolhido no patch 7.39
for hero in heroes_data:
    hero_name = hero.get("localized_name")
    picks = hero.get("pro_pick", 0)
    roles = hero.get("roles", [])
    hero["pick_count"] = picks

# Cria um DataFrame para os heróis escolhidos
pick_heroes_df = pd.DataFrame(heroes_data, columns=["localized_name", "pick_count", "roles"])

# Renomeia as colunas para algo mais amigável  
pick_heroes_df.columns = ["Hero", "Pick Count", "Roles"]

# Ordena os heróis pelo número de picks
pick_heroes_df = pick_heroes_df.sort_values(by="Pick Count", ascending=False)

# Exibe o DataFrame 
heroes_pick_count = pick_heroes_df

########################################################################################

url = "https://api.opendota.com/api/proMatches"

# Obtém os dados das partidas profissionais
pro_data = requests.get(url).json()

# Cria um DataFrame para os dados dos jogos profissionais
pro_df = pd.DataFrame(pro_data)

# Corrigir a duração para minutos e arredondar para 2 casas decimais
pro_df["duration"] = pro_df["duration"].apply(lambda x: round(x / 60, 2) if x is not None else 0)

# Exibe as primeiras linhas do DataFrame
print(pro_df)

pro_matches = pro_df

#########################################################################################

url = "https://api.opendota.com/api/publicMatches"

# Obtém os dados das partidas profissionais
public_data = requests.get(url).json()

# Cria um DataFrame para os dados dos jogos profissionais
public_df = pd.DataFrame(public_data)

# Corrigir a duração para minutos e arredondar para 2 casas decimais
public_df["duration"] = public_df["duration"].apply(lambda x: round(x / 60, 2) if x is not None else 0)

public_matches = public_df

##########################################################################################

dataset_heroes_ban_count = heroes_ban_count
dataset_heroes_pick_count = heroes_pick_count
dataset_heroes_win_rate = heroes_win_rate
dataset_pro_matches = pro_matches
dataset_public_matches = public_matches
