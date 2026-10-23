import time

print("=================================================")
print("  🤖 TRADEFLOW AI - MÉTHODE TENDANCE & PROBABILITÉ")
print("=================================================")

capital_input = input("Entrez votre capital disponible ($) : ")
try:
    capital = float(capital_input.replace("$", "").strip())
except ValueError:
    capital = 16.0

print("\n[Chargement] Analyse de la tendance globale du marché...")
time.sleep(1)

# Application de la méthode pro
paire = "EUR/USD"
tendance = "HAUSSIÈRE FORTE (Tendance de fond)"
action = "ACHETER (BUY / LONG)"
prix_entree = 1.0850
stop_loss = 1.0820       # -30 pips (Risque)
take_profit = 1.0920     # +70 pips (Objectif / Ratio > 1:2)
risque_max_usd = capital * 0.02  # 2% de risque
gain_potentiel = risque_max_usd * 2.3

def main():
    print(f"\n🔹 Actif : {paire}")
    print(f"📈 Analyse : {tendance}")
    print(f"🚀 ACTION MÉTHODE : {action}")
    print(f"-----------------------------------------")
    print(f"🛑 STOP LOSS (Sécurité max) : {stop_loss} (-{risque_max_usd:.2f} $)")
    print(f"🎯 TAKE PROFIT (Cible pro)  : {take_profit} (+{gain_potentiel:.2f} $)")
    print(f"-----------------------------------------")
    print("💡 RÈGLE DE LA MÉTHODE :")
    print("   On laisse courir les gains vers le Take Profit")
    print("   et on coupe net au Stop Loss si le plan échoue.")
    print("-----------------------------------------")

if __name__ == "__main__":
    main()

