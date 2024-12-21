from fetch_data import fetch_data
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta
import locale

def process(apiKey: str, apiUrl: str) -> str:
    try:
        locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
    except locale.Error:
        print("La locale 'fr_FR.UTF-8' n'est pas disponible sur ce système. Assurez-vous qu'elle est installée.")
        return "Erreur de configuration de la langue."

    responses = fetch_data(apiKey, apiUrl)

    if responses.status_code == 200:
        data = responses.json().get('response', {})

        matchs_wins = [
            match for match in data
            if (match['teams']['away']['name'] == 'Lens' and match['teams']['away']['winner']) or
               (match['teams']['home']['name'] == 'Lens' and match['teams']['home']['winner'])
        ]

        last_win = max(
            datetime.fromisoformat(match['fixture']['date'].replace("Z", "+00:00"))
            for match in matchs_wins
        )

        now = datetime.now(timezone.utc)
        difference = relativedelta(now, last_win)

        return (
            f"Lens n'a pas gagné de match contre Lille depuis le {last_win.strftime('%d %B %Y')}, "
            f"soit {difference.years} années, {difference.months} mois et {difference.days} jours."
        )
    else:
        print(f"Error: {responses.status_code}")
        return "Error"
