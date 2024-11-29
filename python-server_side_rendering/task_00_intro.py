import os

def generate_invitations(template, attendees):
    """
    Generate personalized invitations from a template and a list of attendees.

    Args:
        template (str): The template with placeholders.
        attendees (list): List of dictionaries containing attendee data.

    Returns:
        None
    """
    # Vérification des types d'entrée
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    # Gérer le cas du modèle vide
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Gérer le cas où la liste est vide
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Traiter chaque participant
    for index, attendee in enumerate(attendees, start=1):
        # Remplacement des balises avec les valeurs fournies
        filled_template = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A")
            filled_template = filled_template.replace(f"{{{key}}}", value if value else "N/A")

        # Générer le fichier de sortie
        output_filename = f"output_{index}.txt"
        with open(output_filename, "w") as output_file:
            output_file.write(filled_template)
        print(f"Generated: {output_filename}")
